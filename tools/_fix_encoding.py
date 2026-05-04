"""Repara arquivos corrompidos por double-encoding (PS 5.1 leu UTF-8 como cp1252)."""
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("Instale PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


def _load_source() -> Path:
    config_path = Path(__file__).parent / "sync.config.yaml"
    if not config_path.exists():
        print(f"Erro: {config_path} não encontrado.", file=sys.stderr)
        sys.exit(1)
    with config_path.open(encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    return Path(cfg["source"])


def recover_bytes(text: str) -> bytes:
    """Converte texto mojibake (cp1252→UTF-8→decodificado) de volta aos bytes UTF-8 originais.
    
    Usa cp1252 para o range definido (0x80-0x9F com mapeamentos cp1252) e
    fallback direto ao code point para posições indefinidas (0x8D, 0x8F, 0x90 etc.).
    """
    result = bytearray()
    for ch in text:
        try:
            result.extend(ch.encode('cp1252'))
        except UnicodeEncodeError:
            cp = ord(ch)
            if cp <= 0xFF:
                result.append(cp)   # byte de continuação UTF-8 indefinido no cp1252
            else:
                result.extend(ch.encode('utf-8'))  # fallback seguro
    return bytes(result)


ROOT = _load_source()
fixed = 0
errors = []

for md in ROOT.rglob("*.md"):
    raw = md.read_bytes()
    if raw[:3] != b'\xef\xbb\xbf':
        continue  # sem BOM = não foi tocado pelo PowerShell
    content_bytes = raw[3:]  # remove BOM
    try:
        text = content_bytes.decode('utf-8')
        original_bytes = recover_bytes(text)
        restored = original_bytes.decode('utf-8')
        bak = md.with_suffix('.md.bak')
        bak.write_bytes(raw)  # backup antes de modificar
        try:
            md.write_bytes(restored.encode('utf-8'))
            bak.unlink()  # remove backup se tudo OK
        except Exception:
            raise  # mantém o .bak para recuperação manual
        print(f"  ✓ {md.name}")
        fixed += 1
    except Exception as e:
        errors.append(f"  ✗ {md.name}: {e}")

print(f"\n{fixed} arquivo(s) reparado(s).")
if errors:
    print("Erros:")
    for e in errors:
        print(e)
