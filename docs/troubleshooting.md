# Troubleshooting

Problemas comuns e como resolvê-los.

---

## `sync.config.yaml` não encontrado

**Sintoma:**
```
Erro: .../tools/sync.config.yaml não encontrado.
Copie .../sync.config.example.yaml para sync.config.yaml e ajuste os caminhos.
```

**Causa:** O arquivo de configuração local não existe — ele está no `.gitignore` e precisa ser criado manualmente em cada máquina.

**Solução:**
```bash
cp tools/sync.config.example.yaml tools/sync.config.yaml
# Edite sync.config.yaml com os caminhos reais do seu sistema
```

---

## `source` ou `dest` não encontrado

**Sintoma:**
```
Erro: source não encontrado:
  /caminho/para/vault
Verifique o campo 'source' em tools/sync.config.yaml
```

**Causa:** O caminho configurado em `sync.config.yaml` não existe no sistema atual.

**Solução:** Abra `tools/sync.config.yaml` e corrija os campos `source` e `dest` com os caminhos absolutos corretos para sua máquina. Use `python -c "from pathlib import Path; print(Path('~/seu/caminho').expanduser())"` para confirmar o path.

---

## YAML inválido em X.md

**Sintoma:**
```
⚠ YAML inválido em NomeDaNota.md: ...
```

**Causa:** O frontmatter do arquivo possui algum erro de sintaxe YAML (aspas não fechadas, tabs em vez de espaços, caracteres especiais não escapados).

**Diagnóstico:**
1. Abra o arquivo no Obsidian ou em um editor de texto
2. Inspecione o bloco entre os `---` iniciais
3. Problemas comuns: `:` sem espaço após, aspas simples/duplas misturadas, bullets com indentação incorreta

**Solução:** Corrija o frontmatter seguindo o padrão em [docs/patterns.md](patterns.md).

---

## Stats da homepage desatualizadas

**Sintoma:** O site mostra "47 notas" mas você sabe que há mais notas publicadas.

**Causa:** As stats em `site/index.md` são atualizadas automaticamente ao final do `make sync`. Se o sync não foi executado recentemente, os números ficam defasados.

**Solução:**
```bash
make sync        # Sincroniza e atualiza stats
# ou, para apenas recalcular sem re-sincronizar:
python tools/sync_from_source.py --report-only  # não atualiza stats
make sync        # necessário para gravar
```

---

## Encoding / BOM detectado

**Sintoma:**
```
BOM: NomeDaNota.md
```
ou
```
[NomeDaNota.md] linha 3: â€"  (exemplo de double-encoding)
```

**Causa:** O arquivo foi salvo com BOM (Byte Order Mark) ou houve uma conversão de encoding errada (Latin-1 → UTF-8 dupla).

**Solução:**
```bash
python tools/_fix_encoding.py  # remove BOM e corrige artifacts conhecidos
python tools/_audit.py         # confirma que os problemas foram resolvidos
```

---

## Link morto no audit (`[[Nota]]` sem destino)

**Sintoma:**
```
AVISO [Disciplina/Nota.md]: [[Outra Nota]]
```

**Causas possíveis:**

1. **Link intencional ao vault privado** — Links na seção `## Conexões` são ignorados automaticamente; links em blockquotes (`>`) também. Se o link está fora dessas seções, mova-o para `## Conexões`.

2. **Nota ainda não publicada** — A nota alvo existe no vault mas não tem `status: done` nem `tipo: moc`. Quando publicar a nota, o link será resolvido automaticamente no próximo sync.

3. **Typo no nome do arquivo** — Verifique se o nome no wikilink corresponde exatamente ao nome do arquivo (case-sensitive no Linux/CI).

---

## Sync parece travado / sem output

**Sintoma:** `make sync` não imprime nada por muito tempo.

**Causa:** O vault de origem tem muitos arquivos e o script está processando sem emitir output para os arquivos ignorados (comportamento padrão).

**Solução:** Use a flag `--verbose` para ver todos os arquivos sendo processados:
```bash
python tools/sync_from_source.py --verbose
```

---

## Deploy falhou no GitHub Actions

**Diagnóstico:**
1. Acesse a aba **Actions** no repositório GitHub
2. Clique no workflow com falha
3. Expanda o step com erro

**Causas comuns:**

| Erro no log | Causa | Solução |
|---|---|---|
| `CAMPOS FALTANDO ['title']` | Frontmatter incompleto no site/ | Execute `make audit` localmente e corrija |
| `BOM: arquivo.md` | Encoding inválido | Execute `python tools/_fix_encoding.py` e faça novo commit |
| `npm ERR!` | Problema de build no Quartz | Verifique `quartz/quartz.config.ts` por erros de sintaxe |
