---
title: AGENTS
description: Este diretório contém todas as notas de estudo da trilha Graduação em
  Química.
---
# Trilha Química — Manual do Agente

Este diretório contém todas as notas de estudo da trilha **Graduação em Química**.

---

## Propósito

Trilha acadêmica com organização por semestre e disciplina. Cobre Química, Matemática, Física e Química Experimental. Segue padrão distinto da trilha IA & Dados — não misturar.

---

## Organização atual

```
Graduação em Química/
├── Graduação em Química.md   ← MOC hub
└── 1º Semestre/
    ├── 1º Semestre.md        ← MOC do semestre
    ├── Fundamentos de Química I/
    ├── Matemática I/
    ├── Física I/
    └── Introdução à Química Experimental I/
```

---

## Frontmatter obrigatório

```yaml
tags:
  - tipo/estudo
  - status/todo
  - trilha/quimica
created: YYYY-MM-DD
tipo: estudo
trilha: quimica
semestre: 1
disciplina: matematica   # quimica | matematica | fisica | quimica-experimental
status: todo
cssclasses:
  - nota-estudo
```

**Slugs de disciplina por pasta:**

| Pasta | `disciplina:` |
|---|---|
| `Fundamentos de Química I/` | `quimica` |
| `Matemática I/` | `matematica` |
| `Física I/` | `fisica` |
| `Introdução à Química Experimental I/` | `quimica-experimental` |

---

## Estrutura de uma nota de estudo (7 seções obrigatórias)

```markdown
# Título da Nota

> Resumo conciso (1-3 linhas) — o que é + por que importa.

---

## Definição

Definição rigorosa: enunciado formal + interpretação intuitiva. Citar livro + página.

## Teoria & Fundamentos

Subseções com `###`. Teoremas em blockquote:
> **Teorema:** enunciado

Tabelas para propriedades. Gráficos ASCII em pontos visuais-chave.

## Fórmulas & Equações

Tabelas resumo + display math KaTeX.

| Fórmula | Quando usar |
|---|---|
| $...$ | ... |

## Exemplos Resolvidos

**Exemplo 1 — Básico: <descrição curta>**

> **Enunciado:** ...

**Passo 1 — <ação>.**
<explicação>

$$<equação>$$

**Passo 2 — <ação>.**
...

$$\boxed{<resposta final>}$$

---

**Exemplo 2 — Intermediário: <descrição curta>**
...

**Exemplo 3 — Avançado: <descrição curta>**
...

## Armadilhas & Edge Cases

- **Palavra-chave** — descrição do erro comum
- ...

## Conexões

- [[Matemática]] — MOC da área (ou [[Química]], [[Física]])
- [[Graduação em Química]] — Roadmap
- [[Nota Pré-requisito]] — descrição
- (próxima nota) — próximo tópico

## Fontes

- SOBRENOME, Nome. *Título* — Vol. N, Cap. N (pg. N). Editora.
```

---

## Template a usar


---

## Notação matemática (KaTeX PT-BR) — OBRIGATÓRIO

| Função | CORRETO | ERRADO |
|---|---|---|
| Seno | `\operatorname{sen}` | `\sin` |
| Tangente | `\operatorname{tg}` | `\tan` |
| Cotangente | `\operatorname{cotg}` | `\cot` |
| Cossecante | `\csc` | — |
| Secante | `\sec` | — |

- Frações grandes: `\dfrac{}{}` (não `\frac{}{}`)
- Conjuntos: `\mathbb{R}`, `\mathbb{N}`, `\mathbb{Z}`, `\mathbb{Q}`
- **Resposta final de todo exemplo: `$$\boxed{...}$$`** — obrigatório

---

## Gráficos ASCII

Incluir quando o tópico tem componente visual (limites, gráficos de funções, geometria analítica):

````markdown
**Gráfico — <descrição>:**

```
  y
  |
  |    ...curva...
  +─────────────── x
```
_Legenda em itálico._
````

---

## Anti-patterns

- Usar `fase:` ou `domínio:` nesta trilha — campos da trilha IA & Dados
- Usar `\sin`, `\tan`, `\cot` — usar PT-BR obrigatoriamente
- Omitir `$$\boxed{...}$$` na resposta final dos exemplos
- Criar nota sem passo a passo detalhado nos exemplos (cada manipulação algébrica em passo separado e nomeado)
- Gráficos ASCII em conceitos sem componente visual claro

---

## Skills relevantes

| Ação | Arquivo |
|---|---|
| Criar nota de estudo | `.codex/skills/criar-nota-estudo/SKILL.md` |
| Validar nota | `.codex/skills/validar-nota/SKILL.md` |
| Corrigir nota | `.codex/skills/corrigir-nota/SKILL.md` |
