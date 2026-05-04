# Pipeline de Sync — `tools/sync_from_source.py`

Documento de referência do script que extrai conteúdo do vault privado e o
transforma para o padrão do site público.

---

## Visão geral

```
O Grafo de Alexandria/          logos-archive/site/
01 - Roadmaps/                  Química/
  Graduação em Química/   ─→      1º Semestre/
    1º Semestre/                    Fundamentos de Química I/
      Fundamentos de Química I/         Fundamentos de Química I.md
      ...                              O que é Química.md
```

O script percorre recursivamente a pasta fonte, avalia cada arquivo pelas
**regras de inclusão** e, se aprovado, aplica as **transformações** antes de gravar
no destino.

**Princípio fundamental:** o vault nunca é modificado. O script é somente-leitura
em relação ao Grafo.

---

## Configuração (topo do script)

```python
SOURCE_ROOT = Path(r"d:\Projetos\Vault\O Grafo de Alexandria\01 - Roadmaps\Graduação em Química")
DEST_ROOT   = Path(r"d:\Projetos\Vault\logos-archive\site\Química")

# Arquivos excluídos por nome
EXCLUDE_ROOT_FILES = {"Graduação em Química.md"}   # raiz da pasta fonte
EXCLUDE_FILES      = {"1º Semestre.md"}            # qualquer nível

# Seções de MOC removidas durante o sync (nunca devem aparecer no site)
MOC_SECTIONS_TO_STRIP = {
    "Notas da Disciplina",
    "Notas do semestre",
    "Material da Disciplina",
    "PDFs dos Textos",
}
```

Para adicionar uma nova seção a remover, basta incluir o nome exato do heading
`## ` em `MOC_SECTIONS_TO_STRIP`.

---

## Regras de inclusão (`should_sync`)

Um arquivo é sincronizado se satisfazer **qualquer** das condições abaixo:

| Condição | Campo avaliado |
|---|---|
| `tipo: moc` (ou tag `tipo/moc`) | MOCs de disciplina/semestre — sempre publicados |
| `status: done` (ou tag `status/done`) | Notas de estudo concluídas |

Arquivos sem frontmatter ou com outros valores de status são ignorados silenciosamente.

---

## Transformação de frontmatter (`transform_frontmatter`)

O frontmatter do vault tem campos específicos do Obsidian que não fazem sentido no
Quartz. O script normaliza esses campos durante o sync.

### Vault → Site

| Campo no vault | Campo no site | Observação |
|---|---|---|
| `aliases: [Nome]` | — | Removido |
| `tags: [tipo/moc, trilha/quimica]` | `tags: [quimica]` | Extrai apenas os valores de `trilha/` |
| `tags: [tipo/estudo, ...]` | — | Trilha vira `tags`; `tipo` vira campo separado |
| `tipo: moc` / tag `tipo/moc` | `tipo: moc` | Campo direto no frontmatter do site |
| `created: 2026-04-24` | `date: 2026-04-24` | Renomeado |
| `date: ...` | `date: ...` | Preservado se já existir |
| `cssclasses: [nota-estudo]` | — | Removido |
| `status: done` | — | Removido |
| H1 do corpo | `title: Nome da Nota` | Extraído automaticamente |
| Primeiro `> blockquote` do corpo | `description: "..."` | Truncado a 160 chars |
| `disciplina: quimica-geral` | `disciplina: quimica-geral` | Preservado |
| `semestre: 1` | `semestre: 1` | Preservado |

### Exemplo

**Vault (entrada):**
```yaml
aliases: [Fundamentos de Química I]
tags: [tipo/moc, trilha/quimica]
created: 2026-04-24
```

**Site (saída):**
```yaml
title: Fundamentos de Química I
description: 'MOC da disciplina...'
tags:
- quimica
date: 2026-04-24
tipo: moc
```

---

## Remoção de seções vault-only (`strip_moc_sections`)

Aplicado **apenas em MOCs** (`tipo == "moc"`), antes de gravar o arquivo.

O algoritmo bufferiza cada separador `---` junto com as linhas em branco seguintes
e só os emite após confirmar que o próximo heading `## ` não está em
`MOC_SECTIONS_TO_STRIP`. Isso garante que dois blocos removidos consecutivos não
deixem `---` duplicados no output.

**Seções removidas atualmente:**

| Seção no vault | Motivo |
|---|---|
| `## Notas da Disciplina` | Sempre vazia no vault (bloco de anotações pessoais) |
| `## Notas do semestre` | Idem |
| `## Material da Disciplina` | Caminhos de PDF locais — inválidos fora do vault |
| `## PDFs dos Textos` | Idem |

---

## Exclusões de arquivo

| Arquivo | Motivo |
|---|---|
| `Graduação em Química.md` | Roadmap geral — não publicado |
| `1º Semestre.md` | Índice de semestre — substituído por `index.md` gerado pelo Quartz |

---

## Flags de linha de comando

```bash
python tools/sync_from_source.py              # sync normal
python tools/sync_from_source.py --dry-run    # simula sem gravar
python tools/sync_from_source.py --validate-stubs           # valida links internos
python tools/sync_from_source.py --validate-stubs --report-only  # só reporta, sem modificar
```

---

## Fluxo completo de um arquivo MOC

```
1. parse_file(src)              → frontmatter dict + corpo string
2. should_sync(fm)              → True se tipo==moc ou status==done
3. transform_frontmatter(...)   → frontmatter normalizado para o site
4. strip_moc_sections(body)     → corpo sem seções vault-only  ← só para MOCs
5. montar: "---\n{fm}---\n{body}"
6. dest.write_bytes(...)        → grava UTF-8 com LF no site/
```
