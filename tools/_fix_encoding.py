"""Repara arquivos corrompidos por double-encoding (PS 5.1 leu UTF-8 como cp1252)."""
from pathlib import Path


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


ROOT = Path(r"d:\Projetos\Vault\O Grafo de Alexandria\01 - Roadmaps\Graduação em Química")
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
        md.write_bytes(restored.encode('utf-8'))
        print(f"  ✓ {md.name}")
        fixed += 1
    except Exception as e:
        errors.append(f"  ✗ {md.name}: {e}")

print(f"\n{fixed} arquivo(s) reparado(s).")
if errors:
    print("Erros:")
    for e in errors:
        print(e)
