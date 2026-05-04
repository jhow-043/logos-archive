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

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

try:
    import yaml
except ImportError:
    print("Instale PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# ── Configuração ──────────────────────────────────────────────────────────────

def _load_config() -> tuple[Path, Path]:
    """Carrega SOURCE_ROOT e DEST_ROOT do sync.config.yaml na mesma pasta."""
    config_path = Path(__file__).parent / "sync.config.yaml"
    if not config_path.exists():
        example = Path(__file__).parent / "sync.config.example.yaml"
        print(
            f"Erro: {config_path} não encontrado.\n"
            f"Copie {example} para {config_path} e ajuste os caminhos.",
            file=sys.stderr,
        )
        sys.exit(1)
    with config_path.open(encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    source = Path(cfg["source"])
    dest   = Path(cfg["dest"])
    return source, dest

SOURCE_ROOT, DEST_ROOT = _load_config()

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
        except yaml.YAMLError as exc:
            print(f"  ⚠ YAML inválido em {path.name}: {exc}", file=sys.stderr)
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


EMOJI_RE = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # símbolos e pictogramas
    "\U0001F680-\U0001F6FF"  # transporte e mapa
    "\U0001F1E0-\U0001F1FF"  # bandeiras
    "\U00002700-\U000027BF"  # dingbats
    "\U000024C2-\U0001F251"  # símbolos variados
    "\uFE0F"                 # variation selector
    "\u200D"                 # zero-width joiner
    "]+",
    flags=re.UNICODE,
)


def strip_emojis(text: str) -> str:
    """Remove emojis e normaliza espaços extras resultantes."""
    return EMOJI_RE.sub("", text).strip()


# ── Terminal output (ANSI sem dependências externas) ──────────────────────────

_USE_COLOR = sys.stdout.isatty()


def _c(text: str, code: str) -> str:
    """Aplica código ANSI `code` apenas quando stdout é um terminal interativo."""
    return f"\033[{code}m{text}\033[0m" if _USE_COLOR else text


def _green(t: str)  -> str: return _c(t, "32")
def _yellow(t: str) -> str: return _c(t, "33")
def _red(t: str)    -> str: return _c(t, "31")
def _cyan(t: str)   -> str: return _c(t, "36")
def _bold(t: str)   -> str: return _c(t, "1")


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
    out["title"] = strip_emojis(fm.get("title") or extract_title(body) or stem)

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


def strip_h1(body: str) -> str:
    """Remove o primeiro heading H1 do corpo.

    O Quartz já renderiza o título via componente ArticleTitle (frontmatter
    `title`). Manter o H1 no corpo cria título duplicado na página.
    """
    lines = body.splitlines(keepends=True)
    H1_RE = re.compile(r"^#\s+.+")
    for i, line in enumerate(lines):
        if H1_RE.match(line):
            # Remove o H1 e a linha em branco imediatamente após (se houver)
            del lines[i]
            if i < len(lines) and not lines[i].strip():
                del lines[i]
            break
    return "".join(lines)


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
            if heading.lower() in {s.lower() for s in MOC_SECTIONS_TO_STRIP}:
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


def sync_file(src: Path, dest: Path, dry_run: bool, stats: dict, verbose: bool = False) -> None:
    fm, body = parse_file(src)

    if not should_sync(fm):
        stats["skipped"] += 1
        if verbose:
            tipo   = _get_tipo(fm) or "—"
            status = fm.get("status", "—")
            print(_yellow(f"  ~ {src.relative_to(SOURCE_ROOT)}  [tipo={tipo}, status={status}]"))
        return

    # Captura título bruto antes da transformação para detectar remoção de emoji
    _raw_title = fm.get("title") or extract_title(body) or src.stem
    new_fm = transform_frontmatter(fm, body, src.stem)
    if _raw_title and _raw_title != new_fm.get("title", ""):
        print(_yellow(f'  ⚠  Emoji removido do título: "{_raw_title}" → "{new_fm["title"]}"'))

    body = strip_h1(body)
    if _get_tipo(fm) == "moc":
        body = strip_moc_sections(body)
    new_content = f"---\n{dump_frontmatter(new_fm)}---\n{body}"

    if dry_run:
        print(_cyan(f"  [DRY] {src.relative_to(SOURCE_ROOT)}"))
        stats["synced"] += 1
        return

    dest.parent.mkdir(parents=True, exist_ok=True)
    # Escreve em modo binário com LF explícito (evita CRLF no Windows)
    dest.write_bytes(new_content.encode("utf-8"))
    stats["synced"] += 1
    if verbose:
        print(_green(f"  ✓ {src.relative_to(SOURCE_ROOT)}  →  {dest.relative_to(DEST_ROOT.parent)}"))
    else:
        print(_green(f"  ✓ {dest.relative_to(DEST_ROOT.parent)}"))


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
        print(_yellow(f"\n⚠  Links sem destino ({len(missing)}):"))
        for file, link in missing:
            print(f"   {file}: [[{link}]]")
        if not report_only:
            print("Crie os arquivos de stub ou corrija os links.")
    else:
        print(_green("✓ Todos os links internos estão resolvidos."))


def update_index_stats(dry_run: bool) -> None:
    """Conta notas/disciplinas/semestres no site/ e atualiza os stat-cards em index.md."""
    index_path = DEST_ROOT.parent / "index.md"
    if not index_path.exists():
        return

    notes = 0
    disciplinas: set = set()
    semestres: set = set()
    for md in DEST_ROOT.rglob("*.md"):
        notes += 1
        text = md.read_text(encoding="utf-8", errors="replace")
        m = FRONTMATTER_RE.match(text)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        if fm.get("disciplina"):
            disciplinas.add(str(fm["disciplina"]))
        if fm.get("semestre"):
            semestres.add(str(fm["semestre"]))

    n_notas = notes
    n_disc  = len(disciplinas)
    n_sem   = len(semestres)

    if dry_run:
        print(_cyan(f"  [DRY] Stats: {n_notas} notas, {n_disc} disciplina(s), {n_sem} semestre(s)"))
        return

    text = index_path.read_text(encoding="utf-8")
    replacements = [
        (r'(<span class="stat-num">)\d+(</span><span class="stat-label">notas</span>)',        rf'\g<1>{n_notas}\2'),
        (r'(<span class="stat-num">)\d+(</span><span class="stat-label">disciplinas</span>)', rf'\g<1>{n_disc}\2'),
        (r'(<span class="stat-num">)\d+(</span><span class="stat-label">semestre</span>)',    rf'\g<1>{n_sem}\2'),
    ]
    updated = text
    for pattern, repl in replacements:
        updated = re.sub(pattern, repl, updated)
    if updated != text:
        index_path.write_bytes(updated.encode("utf-8"))
        print(_green(f"  ✓ Stats atualizadas → {n_notas} notas, {n_disc} disciplina(s), {n_sem} semestre(s)"))
    else:
        print(f"  Stats inalteradas → {n_notas} notas, {n_disc} disciplina(s), {n_sem} semestre(s)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync vault → logos-archive/site/")
    parser.add_argument("--dry-run", action="store_true", help="Simula sem copiar arquivos")
    parser.add_argument("--validate-stubs", action="store_true", help="Valida links internos")
    parser.add_argument("--report-only", action="store_true", help="Apenas reporta, sem modificar")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Exibe arquivos ignorados com razão e paths de origem")
    args = parser.parse_args()

    if args.validate_stubs:
        validate_stubs(report_only=args.report_only)
        return

    if not SOURCE_ROOT.exists():
        print(_red(f"Erro: source não encontrado:\n  {SOURCE_ROOT}"), file=sys.stderr)
        print("Verifique o campo 'source' em tools/sync.config.yaml", file=sys.stderr)
        sys.exit(1)

    if not DEST_ROOT.parent.exists():
        print(_red(f"Erro: diretório pai do dest não encontrado:\n  {DEST_ROOT.parent}"), file=sys.stderr)
        print("Verifique o campo 'dest' em tools/sync.config.yaml", file=sys.stderr)
        sys.exit(1)

    stats = {"synced": 0, "skipped": 0}
    label = _cyan("[DRY-RUN] ") if args.dry_run else ""
    print(f"{label}{_bold('Sincronizando:')}\n  {SOURCE_ROOT}\n  -> {DEST_ROOT}\n")

    for src in sorted(SOURCE_ROOT.rglob("*.md")):
        rel = src.relative_to(SOURCE_ROOT)
        # Exclui arquivos bloqueados
        if len(rel.parts) == 1 and rel.name in EXCLUDE_ROOT_FILES:
            continue
        if rel.name in EXCLUDE_FILES:
            continue
        dest = DEST_ROOT / rel
        sync_file(src, dest, dry_run=args.dry_run, stats=stats, verbose=args.verbose)

    verb = "Simulação" if args.dry_run else "Sync"
    print(f"\n{_bold(verb + ' concluído:')} {stats['synced']} sincronizado(s), {stats['skipped']} ignorado(s).")

    if not args.report_only:
        print("\nAtualizando stats da homepage...")
        update_index_stats(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
