"""Audita e corrige encoding nos arquivos fonte do vault + site."""
from pathlib import Path

VAULT = Path(r"d:\Projetos\Vault\O Grafo de Alexandria\01 - Roadmaps\Graduação em Química")
SITE  = Path(r"d:\Projetos\Vault\logos-archive\site\Química")

ARTIFACTS = ["â\x80\x94", "â\x80\x99", "â\x80\x9c", "â\x80\x9d",
             "Ã§", "Ã£", "Ã©", "Ã³", "Ãµ", "Ã\xaa", "cdotp"]


def check_dir(root: Path, label: str):
    print(f"\n=== {label} ===")
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
            # mostra linhas problemáticas
            for i, line in enumerate(text.splitlines(), 1):
                if any(a in line for a in found):
                    print(f"  [{md.name}] linha {i}: {line[:100]}")
                    break
            issues += 1

    if issues == 0:
        print("  Nenhum problema encontrado.")
    else:
        print(f"\n  {issues} arquivo(s) com problema.")


check_dir(VAULT, "VAULT FONTE")
check_dir(SITE, "SITE PUBLICADO")
