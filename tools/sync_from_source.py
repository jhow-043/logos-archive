#!/usr/bin/env python3
"""
sync_from_source.py — Sincroniza conteúdo do vault principal para logos-archive/site/.

Fonte:   d:\\Projetos\\Vault\\O Grafo de Alexandria\\01 - Roadmaps\\Graduação em Química
Destino: d:\\Projetos\\Vault\\logos-archive\\site\\Química

Regras de inclusão:
  - tipo: moc   → sempre sincroniza (índices de disciplina/semestre)
  - status: done → sincroniza notas de estudo concluídas

Transformação de frontmatter:
  - tags [tipo/X, status/done, trilha/quimica] → tipo: X, tags: [quimica]
  - created → date
  - remove: cssclasses, trilha, status, aliases
  - adiciona: title (do H1), description (do primeiro blockquote ~160 chars)
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Instale PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# ── Configuração ──────────────────────────────────────────────────────────────

SOURCE_ROOT = Path(r"d:\Projetos\Vault\O Grafo de Alexandria\01 - Roadmaps\Graduação em Química")
DEST_ROOT   = Path(r"d:\Projetos\Vault\logos-archive\site\Química")

# Arquivos que não devem ser publicados
EXCLUDE_ROOT_FILES = {"Graduação em Química.md"}
EXCLUDE_FILES = {"1º Semestre.md"}  # índice de semestre — substituído pelo index.md

# Seções de MOC do vault que não devem aparecer no site
MOC_SECTIONS_TO_STRIP = {
    "Notas da Disciplina",
    "Notas do semestre",
    "Material da Disciplina",
    "PDFs dos Textos",
}

# ── Helpers ───────────────────────────────────────────────────────────────────

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_file(path: Path) -> tuple[dict, str]:
    """Retorna (frontmatter_dict, corpo_sem_frontmatter)."""
    text = path.read_text(encoding="utf-8-sig")  # utf-8-sig remove BOM se presente
    text = text.replace("\r\n", "\n").replace("\r", "\n")  # normaliza para LF
    m = FRONTMATTER_RE.match(text)
    if m:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            fm = {}
        body = text[m.end():]
    else:
        fm = {}
        body = text
    return fm, body


def extract_title(body: str) -> str | None:
    """Extrai o texto do primeiro heading H1."""
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return None


def extract_description(body: str, max_len: int = 160) -> str | None:
    """Extrai o primeiro blockquote e trunca em max_len chars."""
    lines = body.splitlines()
    chunks: list[str] = []
    collecting = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("> "):
            collecting = True
            chunks.append(stripped[2:].strip())
        elif collecting:
            break

    if not chunks:
        # Fallback: primeiro parágrafo não-vazio e não-estrutural
        for line in lines:
            s = line.strip()
            if s and not s.startswith(("#", "```", "|", "---", ">")):
                chunks.append(s)
                break

    if not chunks:
        return None

    raw = " ".join(chunks)
    # Remove marcação markdown básica
    raw = re.sub(r"\*\*(.+?)\*\*", r"\1", raw)
    raw = re.sub(r"\*(.+?)\*", r"\1", raw)
    raw = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", raw)
    raw = re.sub(r"`(.+?)`", r"\1", raw)

    if len(raw) > max_len:
        raw = raw[:max_len].rstrip() + "…"
    return raw


def _get_tipo(fm: dict) -> str:
    """Extrai 'tipo' do campo direto ou de tags como tipo/X."""
    if "tipo" in fm:
        return str(fm["tipo"])
    for t in _iter_tags(fm):
        if t.startswith("tipo/"):
            return t.split("/", 1)[1]
    return ""


def _get_trilha(fm: dict) -> list[str]:
    """Extrai trilha do campo direto ou de tags como trilha/X."""
    if "trilha" in fm:
        v = fm["trilha"]
        return [str(v)] if v else []
    result = []
    for t in _iter_tags(fm):
        if t.startswith("trilha/"):
            result.append(t.split("/", 1)[1])
    return result


def _iter_tags(fm: dict):
    tags = fm.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    return [str(t) for t in tags]


def should_sync(fm: dict) -> bool:
    """Retorna True se o arquivo deve ser sincronizado."""
    tipo = _get_tipo(fm)
    if tipo == "moc":
        return True
    status = fm.get("status", "")
    if status == "done":
        return True
    if "status/done" in _iter_tags(fm):
        return True
    return False


def transform_frontmatter(fm: dict, body: str, stem: str) -> dict:
    """Transforma o frontmatter do vault para o formato do site."""
    out: dict = {}

    # title
    out["title"] = fm.get("title") or extract_title(body) or stem

    # description
    desc = fm.get("description") or extract_description(body)
    if desc:
        out["description"] = desc

    # tags (valores de trilha)
    trilha = _get_trilha(fm)
    if trilha:
        out["tags"] = trilha

    # date (de created ou date)
    date_val = fm.get("date") or fm.get("created")
    if date_val:
        out["date"] = date_val

    # tipo
    tipo = _get_tipo(fm)
    if tipo:
        out["tipo"] = tipo

    # campos extras preservados diretamente
    for field in ("disciplina", "semestre"):
        if field in fm:
            out[field] = fm[field]

    return out


def strip_moc_sections(body: str) -> str:
    """Remove seções de MOC que só fazem sentido no vault (ex.: Notas da Disciplina).

    Bufferiza cada separador `---` junto com as linhas em branco que o seguem e
    só os emite quando confirma que o próximo heading H2 não está em
    MOC_SECTIONS_TO_STRIP. Evita separadores duplicados quando duas seções
    consecutivas são removidas.
    """
    lines = body.splitlines(keepends=True)
    result: list[str] = []
    skip_section = False
    buffer: list[str] = []  # acumula `---` + linhas em branco até decisão
    H2_RE = re.compile(r"^##\s+(.+)")

    i = 0
    while i < len(lines):
        line = lines[i]

        # Separador `---`: inicia novo buffer
        if line.strip() == "---":
            buffer = [line]
            skip_section = False
            i += 1
            # Absorve linhas em branco imediatamente após o separador
            while i < len(lines) and not lines[i].strip():
                buffer.append(lines[i])
                i += 1
            continue

        # Heading H2: decide se emite ou descarta o buffer acumulado
        m = H2_RE.match(line)
        if m:
            heading = m.group(1).strip()
            if heading in MOC_SECTIONS_TO_STRIP:
                buffer = []            # descarta separador pendente
                skip_section = True
            else:
                result.extend(buffer)  # emite separador pendente
                buffer = []
                skip_section = False
                result.append(line)
            i += 1
            continue

        if skip_section:
            i += 1
            continue

        # Linha normal: emite buffer acumulado + a própria linha
        result.extend(buffer)
        buffer = []
        result.append(line)
        i += 1

    # Emite buffer restante se não estiver em seção removida
    if not skip_section:
        result.extend(buffer)

    return "".join(result)


def dump_frontmatter(fm: dict) -> str:
    return yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)


def sync_file(src: Path, dest: Path, dry_run: bool, stats: dict) -> None:
    fm, body = parse_file(src)

    if not should_sync(fm):
        stats["skipped"] += 1
        return

    new_fm = transform_frontmatter(fm, body, src.stem)
    if _get_tipo(fm) == "moc":
        body = strip_moc_sections(body)
    new_content = f"---\n{dump_frontmatter(new_fm)}---\n{body}"

    if dry_run:
        print(f"  [DRY] {src.relative_to(SOURCE_ROOT)}")
        stats["synced"] += 1
        return

    dest.parent.mkdir(parents=True, exist_ok=True)
    # Escreve em modo binário com LF explícito (evita CRLF no Windows)
    dest.write_bytes(new_content.encode("utf-8"))
    stats["synced"] += 1
    print(f"  ✓ {dest.relative_to(DEST_ROOT.parent)}")


def validate_stubs(report_only: bool) -> None:
    """Verifica links wiki em site/ que não têm destino."""
    link_re = re.compile(r"\[\[([^\]|#]+)")
    missing: list[tuple[str, str]] = []

    for md in DEST_ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for m in link_re.finditer(text):
            target = m.group(1).strip()
            if not list(DEST_ROOT.rglob(f"{target}.md")):
                missing.append((str(md.relative_to(DEST_ROOT)), target))

    if missing:
        print(f"\n⚠  Links sem destino ({len(missing)}):")
        for file, link in missing:
            print(f"   {file}: [[{link}]]")
        if not report_only:
            print("\nCrie os arquivos de stub ou corrija os links.")
    else:
        print("✓ Todos os links internos estão resolvidos.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync vault → logos-archive/site/")
    parser.add_argument("--dry-run", action="store_true", help="Simula sem copiar arquivos")
    parser.add_argument("--validate-stubs", action="store_true", help="Valida links internos")
    parser.add_argument("--report-only", action="store_true", help="Apenas reporta, sem modificar")
    args = parser.parse_args()

    if args.validate_stubs:
        validate_stubs(report_only=args.report_only)
        return

    if not SOURCE_ROOT.exists():
        print(f"Erro: source não encontrado:\n  {SOURCE_ROOT}", file=sys.stderr)
        sys.exit(1)

    stats = {"synced": 0, "skipped": 0}
    label = "[DRY-RUN] " if args.dry_run else ""
    print(f"{label}Sincronizando:\n  {SOURCE_ROOT}\n  → {DEST_ROOT}\n")

    for src in sorted(SOURCE_ROOT.rglob("*.md")):
        rel = src.relative_to(SOURCE_ROOT)
        # Exclui arquivos bloqueados
        if len(rel.parts) == 1 and rel.name in EXCLUDE_ROOT_FILES:
            continue
        if rel.name in EXCLUDE_FILES:
            continue
        dest = DEST_ROOT / rel
        sync_file(src, dest, dry_run=args.dry_run, stats=stats)

    verb = "Simulação" if args.dry_run else "Sync"
    print(f"\n{verb} concluído: {stats['synced']} sincronizado(s), {stats['skipped']} ignorado(s).")


if __name__ == "__main__":
    main()
