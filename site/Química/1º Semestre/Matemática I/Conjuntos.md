---
title: Conjuntos
description: 'Teoria bÃ¡sica de conjuntos: linguagem, notaÃ§Ã£o, operaÃ§Ãµes e cardinalidade
  â€” fundamento comum a toda a matemÃ¡tica do semestre.'
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: matematica
semestre: 1
---
# Conjuntos

> Teoria bÃ¡sica de conjuntos: linguagem, notaÃ§Ã£o, operaÃ§Ãµes e cardinalidade â€” fundamento comum a toda a matemÃ¡tica do semestre.

---

## DefiniÃ§Ã£o

Um **conjunto** Ã© uma coleÃ§Ã£o bem-definida de objetos chamados **elementos** (ou membros). "Bem-definida" significa que, dado qualquer objeto, Ã© possÃ­vel determinar sem ambiguidade se ele pertence ou nÃ£o ao conjunto. Os conjuntos sÃ£o representados por letras maiÃºsculas ($A$, $B$, $C$, â€¦) e seus elementos por letras minÃºsculas ($a$, $b$, $c$, â€¦).

A teoria de conjuntos Ã© a linguagem base de toda a matemÃ¡tica moderna: domÃ­nio, contradomÃ­nio e imagem de funÃ§Ãµes sÃ£o conjuntos; os conjuntos numÃ©ricos ($\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$) sÃ£o conjuntos; soluÃ§Ãµes de equaÃ§Ãµes sÃ£o conjuntos.

## Teoria & Fundamentos

### PertinÃªncia

A relaÃ§Ã£o fundamental entre elemento e conjunto Ã© a **pertinÃªncia**:

$$a \in A \quad \text{($a$ pertence a $A$)}$$

$$a \notin A \quad \text{($a$ nÃ£o pertence a $A$)}$$

> **AtenÃ§Ã£o:** pertinÃªncia ($\in$) Ã© relaÃ§Ã£o entre **elemento** e conjunto. NÃ£o confundir com inclusÃ£o ($\subseteq$), que Ã© relaÃ§Ã£o entre dois conjuntos.

### Formas de representar conjuntos

| Forma | Como escrever | Exemplo |
| ----- | ------------- | ------- |
| **ExtensÃ£o** (listagem) | Listar todos os elementos entre chaves | $A = \{1, 2, 3, 4\}$ |
| **CompreensÃ£o** (propriedade) | Descrever a propriedade que define os elementos | $A = \{x \in \mathbb{N} \mid x < 5\}$ |
| **Diagrama de Venn** | RepresentaÃ§Ã£o geomÃ©trica com elipses/cÃ­rculos | *(desenho)* |

Na forma por extensÃ£o, a ordem dos elementos e repetiÃ§Ãµes nÃ£o importam: $\{1, 2, 3\} = \{3, 1, 2\} = \{1, 1, 2, 3\}$.

### Conjunto vazio e conjunto universo

**Conjunto vazio** ($\emptyset$ ou $\{\}$): conjunto sem nenhum elemento. Ã‰ **Ãºnico** e Ã© subconjunto de qualquer conjunto.

> $\emptyset \neq \{\emptyset\}$ â€” o primeiro tem 0 elementos; o segundo tem 1 elemento (o prÃ³prio $\emptyset$).

**Conjunto universo** ($U$): conjunto de referÃªncia que contÃ©m todos os elementos relevantes no contexto do problema. Varia conforme o enunciado.

### Igualdade de conjuntos

Dois conjuntos $A$ e $B$ sÃ£o **iguais** se e somente se possuem exatamente os mesmos elementos:

$$A = B \iff (A \subseteq B \text{ e } B \subseteq A)$$

### Subconjuntos e inclusÃ£o

$A$ Ã© **subconjunto** de $B$ ($A \subseteq B$) quando todo elemento de $A$ tambÃ©m pertence a $B$:

$$A \subseteq B \iff \forall\, x,\; x \in A \implies x \in B$$

| NotaÃ§Ã£o | Leitura | ObservaÃ§Ã£o |
| ------- | ------- | ---------- |
| $A \subseteq B$ | $A$ estÃ¡ contido em $B$ | inclui o caso $A = B$ |
| $A \subsetneq B$ | $A$ Ã© subconjunto prÃ³prio de $B$ | $A \subseteq B$ e $A \neq B$ |
| $A \not\subseteq B$ | $A$ nÃ£o estÃ¡ contido em $B$ | existe pelo menos um $x \in A$ com $x \notin B$ |

**Propriedades da inclusÃ£o:**
- Todo conjunto Ã© subconjunto de si mesmo: $A \subseteq A$
- O conjunto vazio Ã© subconjunto de qualquer conjunto: $\emptyset \subseteq A$
- Se $A \subseteq B$ e $B \subseteq C$, entÃ£o $A \subseteq C$ (transitividade)

**NÃºmero de subconjuntos de um conjunto finito:** se $n(A) = n$, entÃ£o $A$ possui $2^n$ subconjuntos distintos (incluindo $\emptyset$ e o prÃ³prio $A$).

### OperaÃ§Ãµes com conjuntos

**UniÃ£o ($A \cup B$):** conjunto de todos os elementos que pertencem a $A$ **ou** a $B$ (ou a ambos).

$$A \cup B = \{x \mid x \in A \text{ ou } x \in B\}$$

**InterseÃ§Ã£o ($A \cap B$):** conjunto de todos os elementos que pertencem a $A$ **e** a $B$ simultaneamente.

$$A \cap B = \{x \mid x \in A \text{ e } x \in B\}$$

Se $A \cap B = \emptyset$, diz-se que $A$ e $B$ sÃ£o **disjuntos**.

**DiferenÃ§a ($A \setminus B$):** conjunto dos elementos de $A$ que **nÃ£o** pertencem a $B$.

$$A \setminus B = \{x \mid x \in A \text{ e } x \notin B\}$$

> A diferenÃ§a **nÃ£o Ã© comutativa**: em geral $A \setminus B \neq B \setminus A$.

**Complementar ($A^c$ ou $\overline{A}$):** conjunto dos elementos do universo $U$ que nÃ£o pertencem a $A$. Equivale Ã  diferenÃ§a $U \setminus A$.

$$A^c = \{x \in U \mid x \notin A\}$$

### Cardinalidade

A **cardinalidade** de um conjunto finito $A$, denotada $n(A)$ ou $|A|$, Ã© o nÃºmero de elementos distintos de $A$.

**FÃ³rmula de inclusÃ£o-exclusÃ£o para 2 conjuntos:**

$$n(A \cup B) = n(A) + n(B) - n(A \cap B)$$

> O termo $n(A \cap B)$ Ã© subtraÃ­do porque os elementos da interseÃ§Ã£o foram contados duas vezes (uma em $n(A)$ e outra em $n(B)$).

**FÃ³rmula de inclusÃ£o-exclusÃ£o para 3 conjuntos:**

$$n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(A \cap C) - n(B \cap C) + n(A \cap B \cap C)$$

### Propriedades das operaÃ§Ãµes

| Propriedade | UniÃ£o | InterseÃ§Ã£o |
| ----------- | ----- | ---------- |
| Comutativa | $A \cup B = B \cup A$ | $A \cap B = B \cap A$ |
| Associativa | $(A \cup B) \cup C = A \cup (B \cup C)$ | $(A \cap B) \cap C = A \cap (B \cap C)$ |
| Distributiva | $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ |
| Identidade | $A \cup \emptyset = A$ | $A \cap U = A$ |
| Complementar | $A \cup A^c = U$ | $A \cap A^c = \emptyset$ |

**Leis de De Morgan:**

$$\overline{A \cup B} = \overline{A} \cap \overline{B} \qquad \overline{A \cap B} = \overline{A} \cup \overline{B}$$

## FÃ³rmulas & EquaÃ§Ãµes

### SÃ­mbolos fundamentais

| SÃ­mbolo | Significado |
| ------- | ----------- |
| $\in$ | pertence (elemento â†’ conjunto) |
| $\notin$ | nÃ£o pertence |
| $\subseteq$ | estÃ¡ contido (conjunto â†’ conjunto) |
| $\subsetneq$ | estÃ¡ contido prÃ³prio |
| $\cup$ | uniÃ£o |
| $\cap$ | interseÃ§Ã£o |
| $\setminus$ | diferenÃ§a |
| $\emptyset$ | conjunto vazio |
| $U$ | conjunto universo |
| $A^c$ ou $\overline{A}$ | complementar de $A$ |
| $n(A)$ ou $\|A\|$ | cardinalidade de $A$ |
| $2^n$ | nÃºmero de subconjuntos de um conjunto com $n$ elementos |

### Cardinalidade

$$n(A \cup B) = n(A) + n(B) - n(A \cap B)$$

$$n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(A \cap C) - n(B \cap C) + n(A \cap B \cap C)$$

$$\text{NÃºmero de subconjuntos de } A = 2^{n(A)}$$

## Exemplos Resolvidos

**Exemplo 1 â€” BÃ¡sico: operaÃ§Ãµes entre dois conjuntos**

> **Enunciado:** Dados $A = \{1, 2, 3, 4\}$ e $B = \{3, 4, 5, 6\}$, determine $A \cup B$, $A \cap B$, $A \setminus B$ e $B \setminus A$.

**Passo 1 â€” UniÃ£o ($A \cup B$): reunir todos os elementos de ambos os conjuntos, sem repetir.**

Listar os elementos de $A$: $1, 2, 3, 4$.
Acrescentar os elementos de $B$ que ainda nÃ£o aparecem: $5, 6$ (os elementos $3$ e $4$ jÃ¡ estÃ£o).

$$A \cup B = \{1, 2, 3, 4, 5, 6\}$$

**Passo 2 â€” InterseÃ§Ã£o ($A \cap B$): identificar os elementos comuns aos dois conjuntos.**

Percorrer os elementos de $A$ e verificar quais tambÃ©m estÃ£o em $B$:
- $1 \in A$, $1 \notin B$ â†’ nÃ£o entra
- $2 \in A$, $2 \notin B$ â†’ nÃ£o entra
- $3 \in A$, $3 \in B$ â†’ **entra**
- $4 \in A$, $4 \in B$ â†’ **entra**

$$A \cap B = \{3, 4\}$$

**Passo 3 â€” DiferenÃ§a $A \setminus B$: elementos de $A$ que nÃ£o estÃ£o em $B$.**

Percorrer os elementos de $A$ e excluir os que pertencem a $B$:
- $1$: nÃ£o estÃ¡ em $B$ â†’ **entra**
- $2$: nÃ£o estÃ¡ em $B$ â†’ **entra**
- $3$: estÃ¡ em $B$ â†’ excluÃ­do
- $4$: estÃ¡ em $B$ â†’ excluÃ­do

$$A \setminus B = \{1, 2\}$$

**Passo 4 â€” DiferenÃ§a $B \setminus A$: elementos de $B$ que nÃ£o estÃ£o em $A$.**

Percorrer os elementos de $B$ e excluir os que pertencem a $A$:
- $3$: estÃ¡ em $A$ â†’ excluÃ­do
- $4$: estÃ¡ em $A$ â†’ excluÃ­do
- $5$: nÃ£o estÃ¡ em $A$ â†’ **entra**
- $6$: nÃ£o estÃ¡ em $A$ â†’ **entra**

$$B \setminus A = \{5, 6\}$$

> **ObservaÃ§Ã£o:** Note que $A \setminus B = \{1, 2\} \neq \{5, 6\} = B \setminus A$, confirmando que a diferenÃ§a **nÃ£o Ã© comutativa**.

---

**Exemplo 2 â€” IntermediÃ¡rio: subconjuntos de um conjunto**

> **Enunciado:** Liste todos os subconjuntos de $A = \{a, b, c\}$ e verifique o total com a fÃ³rmula $2^n$.

**Passo 1 â€” Identificar a cardinalidade de $A$.**

$A$ tem 3 elementos, logo $n(A) = 3$. Pelo fÃ³rmula, o nÃºmero de subconjuntos esperado Ã© $2^3 = 8$.

**Passo 2 â€” Listar os subconjuntos organizados por nÃºmero de elementos.**

Organizar por **quantidade de elementos** (cardinalidade 0, 1, 2, 3) facilita nÃ£o esquecer nenhum:

| Cardinalidade | Subconjuntos |
| ------------- | ------------ |
| 0 elemento | $\emptyset$ |
| 1 elemento | $\{a\}$, $\{b\}$, $\{c\}$ |
| 2 elementos | $\{a, b\}$, $\{a, c\}$, $\{b, c\}$ |
| 3 elementos | $\{a, b, c\}$ |

**Passo 3 â€” Contar e verificar com a fÃ³rmula.**

Total listado: $1 + 3 + 3 + 1 = 8$ subconjuntos.

FÃ³rmula: $2^{n(A)} = 2^3 = 8$ âœ“

> **ObservaÃ§Ã£o:** O subconjunto com todos os elementos ($\{a, b, c\} = A$) Ã© chamado **subconjunto imprÃ³prio**; todos os outros sÃ£o **subconjuntos prÃ³prios**. O $\emptyset$ tambÃ©m Ã© subconjunto de $A$.

---

**Exemplo 3 â€” AvanÃ§ado: cardinalidade com 3 conjuntos**

> **Enunciado:** Em uma turma de 40 alunos, sabe-se que:
> - 20 estudam QuÃ­mica ($Q$)
> - 18 estudam FÃ­sica ($F$)
> - 12 estudam MatemÃ¡tica ($M$)
> - 8 estudam QuÃ­mica e FÃ­sica ($Q \cap F$)
> - 6 estudam QuÃ­mica e MatemÃ¡tica ($Q \cap M$)
> - 5 estudam FÃ­sica e MatemÃ¡tica ($F \cap M$)
> - 3 estudam as trÃªs disciplinas ($Q \cap F \cap M$)
>
> Quantos alunos estudam **pelo menos uma** das trÃªs disciplinas? Quantos **nÃ£o estudam nenhuma**?

**Passo 1 â€” Identificar os dados e a fÃ³rmula a usar.**

Queremos $n(Q \cup F \cup M)$. A fÃ³rmula de inclusÃ£o-exclusÃ£o para 3 conjuntos Ã©:

$$n(Q \cup F \cup M) = n(Q) + n(F) + n(M) - n(Q \cap F) - n(Q \cap M) - n(F \cap M) + n(Q \cap F \cap M)$$

**Passo 2 â€” Substituir os valores dados.**

$$n(Q \cup F \cup M) = 20 + 18 + 12 - 8 - 6 - 5 + 3$$

**Passo 3 â€” Calcular da esquerda para a direita.**

Soma dos individuais:

$$20 + 18 + 12 = 50$$

Subtrair as interseÃ§Ãµes duplas:

$$50 - 8 - 6 - 5 = 31$$

Somar a interseÃ§Ã£o tripla (que foi subtraÃ­da trÃªs vezes a mais):

$$31 + 3 = 34$$

$$n(Q \cup F \cup M) = 34$$

**Passo 4 â€” Encontrar os que nÃ£o estudam nenhuma das trÃªs.**

O total da turma Ã© 40. Os que nÃ£o estudam nenhuma das trÃªs disciplinas sÃ£o os que **nÃ£o** pertencem a $Q \cup F \cup M$, ou seja, pertencem ao complementar:

$$n\!\left((Q \cup F \cup M)^c\right) = n(U) - n(Q \cup F \cup M) = 40 - 34 = 6$$

> **Resultado:** **34 alunos** estudam pelo menos uma disciplina; **6 alunos** nÃ£o estudam nenhuma.

**VerificaÃ§Ã£o da lÃ³gica:** Se somÃ¡ssemos 20 + 18 + 12 = 50 sem descontar interseÃ§Ãµes, estarÃ­amos contando duas vezes os alunos que estudam duas disciplinas e trÃªs vezes os que estudam as trÃªs. A fÃ³rmula corrige esse excesso de contagem.

## Armadilhas & Edge Cases

- **Confundir pertinÃªncia com inclusÃ£o** â€” $2 \in \{1, 2, 3\}$ (elemento no conjunto), mas $\{2\} \subseteq \{1, 2, 3\}$ (conjunto contido em conjunto); nunca escrever $2 \subseteq \{1, 2, 3\}$
- **Confundir $\emptyset$ com $\{\emptyset\}$** â€” $\emptyset$ tem $n = 0$ elementos; $\{\emptyset\}$ tem $n = 1$ elemento (que Ã© o prÃ³prio $\emptyset$); portanto $\emptyset \in \{\emptyset\}$ mas $\emptyset \neq \{\emptyset\}$
- **Achar que a diferenÃ§a Ã© comutativa** â€” $A \setminus B \neq B \setminus A$ em geral; verificar sempre qual conjunto Ã© o "minuendo"
- **Esquecer de subtrair a interseÃ§Ã£o na fÃ³rmula de cardinalidade** â€” o erro mais frequente Ã© usar $n(A \cup B) = n(A) + n(B)$ sem descontar $n(A \cap B)$, resultando em dupla contagem
- **Confundir "pelo menos um" com "exatamente um"** em enunciados â€” "pelo menos um" Ã© $n(A \cup B \cup C)$; "exatamente um" exige calcular apenas as regiÃµes exclusivas de cada conjunto (sem interseÃ§Ã£o)
- **Usar $\subseteq$ onde deveria ser $\subsetneq$** â€” se o enunciado pede subconjunto **prÃ³prio**, o prÃ³prio conjunto nÃ£o conta; o total passa a ser $2^n - 1$

## ConexÃµes

- [[MatemÃ¡tica]] â€” MOC da Ã¡rea
- [[GraduaÃ§Ã£o em QuÃ­mica]] â€” Roadmap da graduaÃ§Ã£o
- [[Conjuntos NumÃ©ricos]] â€” extensÃ£o direta: $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ sÃ£o conjuntos com inclusÃ£o encadeada (prÃ³ximo tÃ³pico)
- FunÃ§Ãµes â€” domÃ­nio, contradomÃ­nio e imagem sÃ£o conjuntos; a definiÃ§Ã£o formal de funÃ§Ã£o depende desta linguagem

## Fontes

- IEZZI, Gelson et al. *Fundamentos de MatemÃ¡tica Elementar* â€” Vol. 1: Conjuntos e FunÃ§Ãµes. pg. 19. Atual Editora.
