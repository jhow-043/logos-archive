---
title: Conjuntos
description: 'Teoria básica de conjuntos: linguagem, notação, operações e cardinalidade
  — fundamento comum a toda a matemática do semestre.'
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: matematica
semestre: 1
---

# Conjuntos

> Teoria básica de conjuntos: linguagem, notação, operações e cardinalidade — fundamento comum a toda a matemática do semestre.

---

## Definição

Um **conjunto** é uma coleção bem-definida de objetos chamados **elementos** (ou membros). "Bem-definida" significa que, dado qualquer objeto, é possível determinar sem ambiguidade se ele pertence ou não ao conjunto. Os conjuntos são representados por letras maiúsculas ($A$, $B$, $C$, …) e seus elementos por letras minúsculas ($a$, $b$, $c$, …).

A teoria de conjuntos é a linguagem base de toda a matemática moderna: domínio, contradomínio e imagem de funções são conjuntos; os conjuntos numéricos ($\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$) são conjuntos; soluções de equações são conjuntos.

## Teoria & Fundamentos

### Pertinência

A relação fundamental entre elemento e conjunto é a **pertinência**:

$$a \in A \quad \text{($a$ pertence a $A$)}$$

$$a \notin A \quad \text{($a$ não pertence a $A$)}$$

> **Atenção:** pertinência ($\in$) é relação entre **elemento** e conjunto. Não confundir com inclusão ($\subseteq$), que é relação entre dois conjuntos.

### Formas de representar conjuntos

| Forma | Como escrever | Exemplo |
| ----- | ------------- | ------- |
| **Extensão** (listagem) | Listar todos os elementos entre chaves | $A = \{1, 2, 3, 4\}$ |
| **Compreensão** (propriedade) | Descrever a propriedade que define os elementos | $A = \{x \in \mathbb{N} \mid x < 5\}$ |
| **Diagrama de Venn** | Representação geométrica com elipses/círculos | *(desenho)* |

Na forma por extensão, a ordem dos elementos e repetições não importam: $\{1, 2, 3\} = \{3, 1, 2\} = \{1, 1, 2, 3\}$.

### Conjunto vazio e conjunto universo

**Conjunto vazio** ($\emptyset$ ou $\{\}$): conjunto sem nenhum elemento. É **único** e é subconjunto de qualquer conjunto.

> $\emptyset \neq \{\emptyset\}$ — o primeiro tem 0 elementos; o segundo tem 1 elemento (o próprio $\emptyset$).

**Conjunto universo** ($U$): conjunto de referência que contém todos os elementos relevantes no contexto do problema. Varia conforme o enunciado.

### Igualdade de conjuntos

Dois conjuntos $A$ e $B$ são **iguais** se e somente se possuem exatamente os mesmos elementos:

$$A = B \iff (A \subseteq B \text{ e } B \subseteq A)$$

### Subconjuntos e inclusão

$A$ é **subconjunto** de $B$ ($A \subseteq B$) quando todo elemento de $A$ também pertence a $B$:

$$A \subseteq B \iff \forall\, x,\; x \in A \implies x \in B$$

| Notação | Leitura | Observação |
| ------- | ------- | ---------- |
| $A \subseteq B$ | $A$ está contido em $B$ | inclui o caso $A = B$ |
| $A \subsetneq B$ | $A$ é subconjunto próprio de $B$ | $A \subseteq B$ e $A \neq B$ |
| $A \not\subseteq B$ | $A$ não está contido em $B$ | existe pelo menos um $x \in A$ com $x \notin B$ |

**Propriedades da inclusão:**
- Todo conjunto é subconjunto de si mesmo: $A \subseteq A$
- O conjunto vazio é subconjunto de qualquer conjunto: $\emptyset \subseteq A$
- Se $A \subseteq B$ e $B \subseteq C$, então $A \subseteq C$ (transitividade)

**Número de subconjuntos de um conjunto finito:** se $n(A) = n$, então $A$ possui $2^n$ subconjuntos distintos (incluindo $\emptyset$ e o próprio $A$).

### Operações com conjuntos

**União ($A \cup B$):** conjunto de todos os elementos que pertencem a $A$ **ou** a $B$ (ou a ambos).

$$A \cup B = \{x \mid x \in A \text{ ou } x \in B\}$$

**Interseção ($A \cap B$):** conjunto de todos os elementos que pertencem a $A$ **e** a $B$ simultaneamente.

$$A \cap B = \{x \mid x \in A \text{ e } x \in B\}$$

Se $A \cap B = \emptyset$, diz-se que $A$ e $B$ são **disjuntos**.

**Diferença ($A \setminus B$):** conjunto dos elementos de $A$ que **não** pertencem a $B$.

$$A \setminus B = \{x \mid x \in A \text{ e } x \notin B\}$$

> A diferença **não é comutativa**: em geral $A \setminus B \neq B \setminus A$.

**Complementar ($A^c$ ou $\overline{A}$):** conjunto dos elementos do universo $U$ que não pertencem a $A$. Equivale à diferença $U \setminus A$.

$$A^c = \{x \in U \mid x \notin A\}$$

### Cardinalidade

A **cardinalidade** de um conjunto finito $A$, denotada $n(A)$ ou $|A|$, é o número de elementos distintos de $A$.

**Fórmula de inclusão-exclusão para 2 conjuntos:**

$$n(A \cup B) = n(A) + n(B) - n(A \cap B)$$

> O termo $n(A \cap B)$ é subtraído porque os elementos da interseção foram contados duas vezes (uma em $n(A)$ e outra em $n(B)$).

**Fórmula de inclusão-exclusão para 3 conjuntos:**

$$n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(A \cap C) - n(B \cap C) + n(A \cap B \cap C)$$

### Propriedades das operações

| Propriedade | União | Interseção |
| ----------- | ----- | ---------- |
| Comutativa | $A \cup B = B \cup A$ | $A \cap B = B \cap A$ |
| Associativa | $(A \cup B) \cup C = A \cup (B \cup C)$ | $(A \cap B) \cap C = A \cap (B \cap C)$ |
| Distributiva | $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ |
| Identidade | $A \cup \emptyset = A$ | $A \cap U = A$ |
| Complementar | $A \cup A^c = U$ | $A \cap A^c = \emptyset$ |

**Leis de De Morgan:**

$$\overline{A \cup B} = \overline{A} \cap \overline{B} \qquad \overline{A \cap B} = \overline{A} \cup \overline{B}$$

## Fórmulas & Equações

### Símbolos fundamentais

| Símbolo | Significado |
| ------- | ----------- |
| $\in$ | pertence (elemento → conjunto) |
| $\notin$ | não pertence |
| $\subseteq$ | está contido (conjunto → conjunto) |
| $\subsetneq$ | está contido próprio |
| $\cup$ | união |
| $\cap$ | interseção |
| $\setminus$ | diferença |
| $\emptyset$ | conjunto vazio |
| $U$ | conjunto universo |
| $A^c$ ou $\overline{A}$ | complementar de $A$ |
| $n(A)$ ou $\|A\|$ | cardinalidade de $A$ |
| $2^n$ | número de subconjuntos de um conjunto com $n$ elementos |

### Cardinalidade

$$n(A \cup B) = n(A) + n(B) - n(A \cap B)$$

$$n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(A \cap C) - n(B \cap C) + n(A \cap B \cap C)$$

$$\text{Número de subconjuntos de } A = 2^{n(A)}$$

## Exemplos Resolvidos

**Exemplo 1 — Básico: operações entre dois conjuntos**

> **Enunciado:** Dados $A = \{1, 2, 3, 4\}$ e $B = \{3, 4, 5, 6\}$, determine $A \cup B$, $A \cap B$, $A \setminus B$ e $B \setminus A$.

**Passo 1 — União ($A \cup B$): reunir todos os elementos de ambos os conjuntos, sem repetir.**

Listar os elementos de $A$: $1, 2, 3, 4$.
Acrescentar os elementos de $B$ que ainda não aparecem: $5, 6$ (os elementos $3$ e $4$ já estão).

$$A \cup B = \{1, 2, 3, 4, 5, 6\}$$

**Passo 2 — Interseção ($A \cap B$): identificar os elementos comuns aos dois conjuntos.**

Percorrer os elementos de $A$ e verificar quais também estão em $B$:
- $1 \in A$, $1 \notin B$ → não entra
- $2 \in A$, $2 \notin B$ → não entra
- $3 \in A$, $3 \in B$ → **entra**
- $4 \in A$, $4 \in B$ → **entra**

$$A \cap B = \{3, 4\}$$

**Passo 3 — Diferença $A \setminus B$: elementos de $A$ que não estão em $B$.**

Percorrer os elementos de $A$ e excluir os que pertencem a $B$:
- $1$: não está em $B$ → **entra**
- $2$: não está em $B$ → **entra**
- $3$: está em $B$ → excluído
- $4$: está em $B$ → excluído

$$A \setminus B = \{1, 2\}$$

**Passo 4 — Diferença $B \setminus A$: elementos de $B$ que não estão em $A$.**

Percorrer os elementos de $B$ e excluir os que pertencem a $A$:
- $3$: está em $A$ → excluído
- $4$: está em $A$ → excluído
- $5$: não está em $A$ → **entra**
- $6$: não está em $A$ → **entra**

$$B \setminus A = \{5, 6\}$$

> **Observação:** Note que $A \setminus B = \{1, 2\} \neq \{5, 6\} = B \setminus A$, confirmando que a diferença **não é comutativa**.

---

**Exemplo 2 — Intermediário: subconjuntos de um conjunto**

> **Enunciado:** Liste todos os subconjuntos de $A = \{a, b, c\}$ e verifique o total com a fórmula $2^n$.

**Passo 1 — Identificar a cardinalidade de $A$.**

$A$ tem 3 elementos, logo $n(A) = 3$. Pelo fórmula, o número de subconjuntos esperado é $2^3 = 8$.

**Passo 2 — Listar os subconjuntos organizados por número de elementos.**

Organizar por **quantidade de elementos** (cardinalidade 0, 1, 2, 3) facilita não esquecer nenhum:

| Cardinalidade | Subconjuntos |
| ------------- | ------------ |
| 0 elemento | $\emptyset$ |
| 1 elemento | $\{a\}$, $\{b\}$, $\{c\}$ |
| 2 elementos | $\{a, b\}$, $\{a, c\}$, $\{b, c\}$ |
| 3 elementos | $\{a, b, c\}$ |

**Passo 3 — Contar e verificar com a fórmula.**

Total listado: $1 + 3 + 3 + 1 = 8$ subconjuntos.

Fórmula: $2^{n(A)} = 2^3 = 8$ ✓

> **Observação:** O subconjunto com todos os elementos ($\{a, b, c\} = A$) é chamado **subconjunto impróprio**; todos os outros são **subconjuntos próprios**. O $\emptyset$ também é subconjunto de $A$.

---

**Exemplo 3 — Avançado: cardinalidade com 3 conjuntos**

> **Enunciado:** Em uma turma de 40 alunos, sabe-se que:
> - 20 estudam Química ($Q$)
> - 18 estudam Física ($F$)
> - 12 estudam Matemática ($M$)
> - 8 estudam Química e Física ($Q \cap F$)
> - 6 estudam Química e Matemática ($Q \cap M$)
> - 5 estudam Física e Matemática ($F \cap M$)
> - 3 estudam as três disciplinas ($Q \cap F \cap M$)
>
> Quantos alunos estudam **pelo menos uma** das três disciplinas? Quantos **não estudam nenhuma**?

**Passo 1 — Identificar os dados e a fórmula a usar.**

Queremos $n(Q \cup F \cup M)$. A fórmula de inclusão-exclusão para 3 conjuntos é:

$$n(Q \cup F \cup M) = n(Q) + n(F) + n(M) - n(Q \cap F) - n(Q \cap M) - n(F \cap M) + n(Q \cap F \cap M)$$

**Passo 2 — Substituir os valores dados.**

$$n(Q \cup F \cup M) = 20 + 18 + 12 - 8 - 6 - 5 + 3$$

**Passo 3 — Calcular da esquerda para a direita.**

Soma dos individuais:

$$20 + 18 + 12 = 50$$

Subtrair as interseções duplas:

$$50 - 8 - 6 - 5 = 31$$

Somar a interseção tripla (que foi subtraída três vezes a mais):

$$31 + 3 = 34$$

$$n(Q \cup F \cup M) = 34$$

**Passo 4 — Encontrar os que não estudam nenhuma das três.**

O total da turma é 40. Os que não estudam nenhuma das três disciplinas são os que **não** pertencem a $Q \cup F \cup M$, ou seja, pertencem ao complementar:

$$n\!\left((Q \cup F \cup M)^c\right) = n(U) - n(Q \cup F \cup M) = 40 - 34 = 6$$

> **Resultado:** **34 alunos** estudam pelo menos uma disciplina; **6 alunos** não estudam nenhuma.

**Verificação da lógica:** Se somássemos 20 + 18 + 12 = 50 sem descontar interseções, estaríamos contando duas vezes os alunos que estudam duas disciplinas e três vezes os que estudam as três. A fórmula corrige esse excesso de contagem.

## Armadilhas & Edge Cases

- **Confundir pertinência com inclusão** — $2 \in \{1, 2, 3\}$ (elemento no conjunto), mas $\{2\} \subseteq \{1, 2, 3\}$ (conjunto contido em conjunto); nunca escrever $2 \subseteq \{1, 2, 3\}$
- **Confundir $\emptyset$ com $\{\emptyset\}$** — $\emptyset$ tem $n = 0$ elementos; $\{\emptyset\}$ tem $n = 1$ elemento (que é o próprio $\emptyset$); portanto $\emptyset \in \{\emptyset\}$ mas $\emptyset \neq \{\emptyset\}$
- **Achar que a diferença é comutativa** — $A \setminus B \neq B \setminus A$ em geral; verificar sempre qual conjunto é o "minuendo"
- **Esquecer de subtrair a interseção na fórmula de cardinalidade** — o erro mais frequente é usar $n(A \cup B) = n(A) + n(B)$ sem descontar $n(A \cap B)$, resultando em dupla contagem
- **Confundir "pelo menos um" com "exatamente um"** em enunciados — "pelo menos um" é $n(A \cup B \cup C)$; "exatamente um" exige calcular apenas as regiões exclusivas de cada conjunto (sem interseção)
- **Usar $\subseteq$ onde deveria ser $\subsetneq$** — se o enunciado pede subconjunto **próprio**, o próprio conjunto não conta; o total passa a ser $2^n - 1$

## Conexões

- [[Matemática]] — MOC da área
- [[Graduação em Química]] — Roadmap da graduação
- [[Conjuntos Numéricos]] — extensão direta: $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ são conjuntos com inclusão encadeada (próximo tópico)
- Funções — domínio, contradomínio e imagem são conjuntos; a definição formal de função depende desta linguagem

## Fontes

- IEZZI, Gelson et al. *Fundamentos de Matemática Elementar* — Vol. 1: Conjuntos e Funções. pg. 19. Atual Editora.
