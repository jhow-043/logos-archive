"""Audita encoding, frontmatter e links internos nos arquivos do site.

Modos:
  (padrão) — Verifica vault + site (encoding only)
  --ci      — Verifica apenas site/ (encoding + frontmatter + wikilinks)
              Exit code 1 se qualquer problema for encontrado (para CI/CD)
"""
import argparse
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


def _load_config():
    config_path = Path(__file__).parent / "sync.config.yaml"
    if not config_path.exists():
        return None, None
    with config_path.open(encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    return Path(cfg["source"]), Path(cfg["dest"])


ARTIFACTS = ["â\x80\x94", "â\x80\x99", "â\x80\x9c", "â\x80\x9d",
             "Ã§", "Ã£", "Ã©", "Ã³", "Ãµ", "Ã\xaa", "cdotp"]

REQUIRED_FIELDS = ("title", "tipo", "date")
FRONTMATTER_RE  = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
WIKILINK_RE     = re.compile(r"\[\[([^\]|#]+)")


def check_encoding(root: Path, label: str) -> int:
    """Verifica BOM e artifacts de double-encoding. Retorna número de problemas."""
    print(f"\n=== {label} (encoding) ===")
    issues = 0
    for md in sorted(root.rglob("*.md")):
        raw = md.read_bytes()
        if raw[:3] == b"\xef\xbb\xbf":
            print(f"  BOM: {md.name}")
            issues += 1
            continue
        try:
            text = raw.decode("utf-8")
        except Exception as e:
            print(f"  ERRO UTF-8: {md.name}: {e}")
            issues += 1
            continue
        found = [a for a in ARTIFACTS if a in text]
        if found:
            for i, line in enumerate(text.splitlines(), 1):
                if any(a in line for a in found):
                    print(f"  [{md.name}] linha {i}: {line[:100]}")
                    break
            issues += 1
    if issues == 0:
        print("  Nenhum problema de encoding.")
    return issues


def check_frontmatter(site: Path) -> int:
    """Verifica campos obrigatórios (title, tipo, date) em todos os .md do site."""
    print(f"\n=== SITE (frontmatter) ===")
    issues = 0
    for md in sorted(site.rglob("*.md")):
        text = md.read_text(encoding="utf-8", errors="replace")
        m = FRONTMATTER_RE.match(text)
        if not m:
            print(f"  SEM FRONTMATTER: {md.relative_to(site)}")
            issues += 1
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as exc:
            print(f"  YAML INVÁLIDO: {md.relative_to(site)}: {exc}")
            issues += 1
            continue
        missing = [f for f in REQUIRED_FIELDS if not fm.get(f)]
        if missing:
            print(f"  CAMPOS FALTANDO {missing}: {md.relative_to(site)}")
            issues += 1
    if issues == 0:
        print("  Todos os frontmatters válidos.")
    return issues


def check_wikilinks(site: Path) -> None:
    """Verifica wikilinks [[...]] cujo destino não existe em site/.

    Ignora links em linhas de blockquote (>) e na seção ## Conexões —
    são referências intencionais ao vault não publicadas no site.
    Reporta como warnings mas não bloqueia o CI.
    """
    print(f"\n=== SITE (wikilinks — somente aviso) ===")
    warnings = 0
    all_stems = {md.stem for md in site.rglob("*.md")}
    for md in sorted(site.rglob("*.md")):
        text = md.read_text(encoding="utf-8", errors="replace")
        in_conexoes = False
        for line in text.splitlines():
            if line.strip().startswith("## "):
                in_conexoes = line.strip().lower() == "## conexões"
            if in_conexoes or line.lstrip().startswith(">"):
                continue  # conexões e breadcrumbs são intencionais
            for match in WIKILINK_RE.finditer(line):
                target = match.group(1).strip()
                stem = Path(target).stem if "/" in target else target
                if stem not in all_stems:
                    print(f"  AVISO [{md.relative_to(site)}]: [[{target}]]")
                    warnings += 1
    if warnings == 0:
        print("  Todos os wikilinks resolvidos.")
    else:
        print(f"  {warnings} link(s) sem destino (não bloqueia deploy).")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audita arquivos do site logos-archive")
    parser.add_argument("--ci", action="store_true",
                        help="Modo CI: verifica apenas site/ com todas as validações; exit 1 se erro")
    args = parser.parse_args()

    vault, site = _load_config()

    total = 0

    if args.ci:
        if site is None:
            print("Erro: sync.config.yaml não encontrado.", file=sys.stderr)
            sys.exit(1)
        total += check_encoding(site, "SITE")
        total += check_frontmatter(site)
        check_wikilinks(site)  # warning only — não soma ao total bloqueante
    else:
        if vault:
            total += check_encoding(vault, "VAULT FONTE")
        else:
            print("⚠ sync.config.yaml não encontrado; pulando verificação do vault.")
        if site:
            total += check_encoding(site, "SITE PUBLICADO")
        else:
            print("⚠ sync.config.yaml não encontrado; pulando verificação do site.")

    print(f"\nTotal de problemas: {total}")
    if total > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
