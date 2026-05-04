# Padrões de Conteúdo

Referência dos padrões esperados para cada tipo de arquivo, tanto no vault
(**O Grafo de Alexandria**) quanto no site (**logos-archive/site/**).

> **Regra geral:** edite sempre no vault. O sync transforma e copia para o site.
> Nunca edite `site/` diretamente — as mudanças serão sobrescritas no próximo sync.

---

## Templates do logos-archive

Localizados em **`logos-archive/templates/`**. Definem o formato canônico dos
arquivos no site — o que o sync deve produzir. Não são publicados (não estão
dentro de `site/`).

| Template | Arquivo | Tipo de conteúdo |
|---|---|---|
| MOC de Disciplina | [`templates/moc.md`](../templates/moc.md) | Índice de disciplina |
| Nota de Estudo — Química | [`templates/nota-estudo-quimica.md`](../templates/nota-estudo-quimica.md) | Notas de Química, Matemática, Física, Experimental |
| Nota de Estudo — IA & Dados | [`templates/nota-estudo-dados.md`](../templates/nota-estudo-dados.md) | Notas de Python, Engenharia, MLOps |

---

## Ícones de status

Usados nas tabelas de MOC para indicar o progresso de unidades e notas:

| Ícone | Significado |
|:---:|---|
| ✅ | Concluído (`status: done`) |
| 🟡 | Em progresso / revisão pendente |
| 🔲 | Não iniciado |

---

## MOC de Disciplina

### Estrutura no vault

```markdown
---
aliases: [Nome da Disciplina]
tags: [tipo/moc, trilha/quimica]
created: YYYY-MM-DD
---

# Nome da Disciplina

> Descrição em uma linha: o que a disciplina cobre.

---

## Unidades

| Unidade | Tema | Status |
| ------- | ---- | ------ |
| U1 | Tema da unidade | ✅ |

---

## U1 — Nome da Unidade

| # | Nota | Status |
|---|------|--------|
| 1 | [[Nome da Nota]] | ✅ |

---

## Notas da Disciplina          ← removido no sync
                                ← (seção de anotações pessoais, sempre vazia)
---

## Material da Disciplina       ← removido no sync
                                ← (caminhos de PDF locais, inválidos no site)
---

## Bibliografia

- AUTOR. *Título*. Edição. Local: Editora, ano.

---

## Conexões

- [[MOC da Área]] — descrição
- [[Roadmap]] — descrição
- [[Semestre]] — descrição

---

> [[Roadmap]] ← Roadmap | [[Semestre]] ← Semestre
```

**Regras:**
- `tags` obrigatoriamente `[tipo/moc, trilha/X]`
- `aliases` com o nome exato da disciplina
- Cada unidade tem sua própria seção `## UX — Nome`
- Seções `## Notas da Disciplina` e `## Material da Disciplina` podem existir no vault — serão removidas pelo sync
- Seção `## Conexões` conecta ao MOC de área, roadmap e semestre
- Última linha é sempre o breadcrumb `> [[Roadmap]] ← Roadmap | [[Semestre]] ← Semestre`

### Estrutura no site (após sync)

As mesmas seções, sem as vault-only, e com frontmatter transformado:

```yaml
title: Nome da Disciplina
description: 'Descrição truncada a 160 chars…'
tags:
- quimica
date: YYYY-MM-DD
tipo: moc
```

---

## Nota de Estudo — Trilha Química

### Frontmatter no vault

```yaml
tags: [tipo/estudo, status/todo, trilha/quimica]
created: YYYY-MM-DD
tipo: estudo
trilha: quimica
semestre: 1
disciplina: quimica-geral   # slug da disciplina
status: todo                # todo | done
cssclasses:
  - nota-estudo
```

Quando `status: done`, a nota é incluída no sync.

### Seções obrigatórias

```markdown
# Título da Nota

> Definição em uma linha — vira a `description` no site.

---

## Definição

## Teoria & Fundamentos

## Fórmulas & Equações

| Símbolo | Significado | Unidade |
| ------- | ----------- | ------- |

## Exemplos Resolvidos

## Armadilhas & Edge Cases

## Conexões

## Fontes
```

### Frontmatter no site (após sync)

```yaml
title: Título da Nota
description: 'Definição em uma linha…'
tags:
- quimica
date: YYYY-MM-DD
tipo: estudo
disciplina: quimica-geral
semestre: 1
```

---

## Nota de Estudo — Trilha IA & Dados

### Frontmatter no vault

```yaml
tags:
  - tipo/estudo
  - status/todo
created: YYYY-MM-DD
tipo: estudo
fase: Fase 0 - Python       # fase do roadmap
domínio: python             # domínio técnico
status: todo                # todo | done
cssclasses:
  - nota-estudo
```

### Seções obrigatórias

```markdown
# Título da Nota

> Definição em uma linha.

---

## Definição

## Motivação & Histórico

## Como funciona

## Sintaxe

## Armadilhas & Edge Cases

## Conexões

## Exemplos práticos

## Fontes
```

---

## O que NÃO fazer

| ❌ Errado | ✅ Correto |
|---|---|
| Editar arquivos em `site/` diretamente | Editar no vault, rodar `make sync` |
| Criar seções novas nos MOCs do site | Criar no vault; o sync reflete |
| Usar `status: done` num MOC | MOCs não têm campo `status` — são sempre sincronizados |
| Deixar `## Notas da Disciplina` com conteúdo | O bloco inteiro (com conteúdo) será removido pelo sync |
| Caminhos absolutos em `## Material da Disciplina` | A seção é removida; use links externos se necessário |
