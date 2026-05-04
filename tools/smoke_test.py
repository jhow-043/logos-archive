"""Smoke tests para site/ — verifica integridade mínima antes de publicar.

Checks:
  1. site/ existe e contém pelo menos 1 arquivo .md
  2. Todo .md tem frontmatter com title, tipo e date
  3. Nenhum .md tem artifacts de double-encoding

Exit code 0 = OK | Exit code 1 = falha (compatível com make test e CI)
"""
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

try:
    import yaml
except ImportError:
    print("Instale PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


def _load_site() -> Path:
    config_path = Path(__file__).parent / "sync.config.yaml"
    if not config_path.exists():
        print(f"Erro: {config_path} não encontrado.", file=sys.stderr)
        sys.exit(1)
    with config_path.open(encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    return Path(cfg["dest"])


ARTIFACTS = ["â\x80\x94", "â\x80\x99", "â\x80\x9c", "â\x80\x9d",
             "Ã§", "Ã£", "Ã©", "Ã³", "Ãµ", "Ã\xaa", "cdotp"]

REQUIRED_FIELDS = ("title", "tipo", "date")
FRONTMATTER_RE  = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

failures: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)
    print(f"  FALHA: {msg}")


def test_site_has_files(site: Path) -> None:
    files = list(site.rglob("*.md"))
    if not files:
        fail(f"site/ não contém nenhum arquivo .md: {site}")
    else:
        print(f"  OK: {len(files)} arquivo(s) .md encontrado(s)")


def test_frontmatter(site: Path) -> None:
    for md in sorted(site.rglob("*.md")):
        text = md.read_text(encoding="utf-8", errors="replace")
        m = FRONTMATTER_RE.match(text)
        if not m:
            fail(f"sem frontmatter: {md.relative_to(site)}")
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as exc:
            fail(f"YAML inválido [{md.relative_to(site)}]: {exc}")
            continue
        missing = [f for f in REQUIRED_FIELDS if not fm.get(f)]
        if missing:
            fail(f"campos faltando {missing}: {md.relative_to(site)}")


def test_encoding(site: Path) -> None:
    for md in sorted(site.rglob("*.md")):
        raw = md.read_bytes()
        if raw[:3] == b"\xef\xbb\xbf":
            fail(f"BOM encontrado: {md.relative_to(site)}")
            continue
        try:
            text = raw.decode("utf-8")
        except Exception as e:
            fail(f"encoding inválido [{md.relative_to(site)}]: {e}")
            continue
        if any(a in text for a in ARTIFACTS):
            fail(f"double-encoding detectado: {md.relative_to(site)}")


def main() -> None:
    site = _load_site()

    print("Smoke tests — logos-archive/site/")
    print(f"Diretório: {site}\n")

    print("[1] Arquivos no site")
    test_site_has_files(site)

    print("\n[2] Frontmatter obrigatório")
    test_frontmatter(site)

    print("\n[3] Encoding")
    test_encoding(site)

    print()
    if failures:
        print(f"Resultado: {len(failures)} falha(s)")
        sys.exit(1)
    else:
        print("Resultado: todos os testes passaram ✓")


if __name__ == "__main__":
    main()
