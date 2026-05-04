---
title: FunÃ§Ãµes
description: DefiniÃ§Ã£o formal de funÃ§Ã£o, domÃ­nio, imagem, classificaÃ§Ã£o (injetora/sobrejetora/bijetora),
  composiÃ§Ã£o e funÃ§Ã£o inversa â€” a linguagem central de to…
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: matematica
semestre: 1
---
# FunÃ§Ãµes

> DefiniÃ§Ã£o formal de funÃ§Ã£o, domÃ­nio, imagem, classificaÃ§Ã£o (injetora/sobrejetora/bijetora), composiÃ§Ã£o e funÃ§Ã£o inversa â€” a linguagem central de todo o cÃ¡lculo.

---

## DefiniÃ§Ã£o

Uma **funÃ§Ã£o** $f$ de $A$ em $B$ Ã© uma **regra que associa a cada elemento $x \in A$ um Ãºnico elemento $y \in B$**, denotado $f(x)$. A unicidade Ã© fundamental: cada entrada tem **exatamente uma** saÃ­da.

NotaÃ§Ã£o padrÃ£o:

$$f: A \to B, \quad x \mapsto f(x)$$

LÃª-se: "$f$ Ã© uma funÃ§Ã£o de $A$ em $B$ que leva $x$ em $f(x)$". $A$ Ã© o **domÃ­nio**, $B$ Ã© o **contradomÃ­nio** e $x$ Ã© a **variÃ¡vel independente**; $y = f(x)$ Ã© a **variÃ¡vel dependente**.

## Teoria & Fundamentos

### DomÃ­nio, contradomÃ­nio e imagem

| Conceito | NotaÃ§Ã£o | DefiniÃ§Ã£o |
| -------- | ------- | --------- |
| DomÃ­nio | $D(f)$ ou $\operatorname{Dom}(f)$ | Conjunto de partida $A$ â€” onde $f$ estÃ¡ definida |
| ContradomÃ­nio | $CD(f)$ | Conjunto de chegada $B$ â€” todas as saÃ­das **possÃ­veis** |
| Imagem | $\operatorname{Im}(f)$ | Subconjunto de $B$ formado pelos $y$ que **efetivamente** ocorrem: $\operatorname{Im}(f) = \{f(x) \mid x \in A\}$ |

> **Importante:** $\operatorname{Im}(f) \subseteq CD(f)$, mas em geral $\operatorname{Im}(f) \neq CD(f)$. A igualdade sÃ³ ocorre quando $f$ Ã© sobrejetora.

### FunÃ§Ã£o vs. relaÃ§Ã£o

Nem toda relaÃ§Ã£o entre conjuntos Ã© funÃ§Ã£o. A condiÃ§Ã£o de funÃ§Ã£o exige:

1. **ExistÃªncia:** todo $x \in A$ tem pelo menos um associado em $B$
2. **Unicidade:** todo $x \in A$ tem **no mÃ¡ximo um** associado em $B$

Teste prÃ¡tico (reta vertical): no plano $xy$, uma curva representa uma funÃ§Ã£o se e somente se toda reta vertical a intercepta **em no mÃ¡ximo um ponto**.

### DomÃ­nio mÃ¡ximo (natural)

Quando $f$ Ã© definida apenas por uma fÃ³rmula (sem especificar $D(f)$ explicitamente), o **domÃ­nio mÃ¡ximo** Ã© o maior subconjunto de $\mathbb{R}$ em que a fÃ³rmula estÃ¡ bem definida. As restriÃ§Ãµes tÃ­picas sÃ£o:

| SituaÃ§Ã£o | RestriÃ§Ã£o | Motivo |
| -------- | --------- | ------ |
| Denominador | $\text{denominador} \neq 0$ | DivisÃ£o por zero Ã© indefinida |
| Raiz de Ã­ndice par | radicando $\geq 0$ | Raiz par de nÃºmero negativo nÃ£o Ã© real |
| Logaritmo | argumento $> 0$ | $\log$ sÃ³ definido para positivos |

Quando hÃ¡ **mais de uma restriÃ§Ã£o**, o domÃ­nio mÃ¡ximo Ã© a **interseÃ§Ã£o** de todos os conjuntos que satisfazem cada condiÃ§Ã£o individualmente.

### Igualdade de funÃ§Ãµes

Duas funÃ§Ãµes $f$ e $g$ sÃ£o **iguais** ($f = g$) se, e somente se:
1. TÃªm o mesmo domÃ­nio: $D(f) = D(g)$
2. TÃªm o mesmo contradomÃ­nio: $CD(f) = CD(g)$
3. $f(x) = g(x)$ para todo $x$ no domÃ­nio comum

### FunÃ§Ãµes especiais

**FunÃ§Ã£o identidade:** $\operatorname{id}_A: A \to A$, definida por $\operatorname{id}_A(x) = x$. Cada elemento vai para si mesmo.

**FunÃ§Ã£o constante:** $f: A \to B$, $f(x) = c$ para todo $x \in A$, onde $c \in B$ Ã© fixo. Imagem $= \{c\}$.

**FunÃ§Ã£o restrita:** dada $f: A \to B$, a restriÃ§Ã£o de $f$ a $C \subseteq A$ Ã© $f|_C: C \to B$, $f|_C(x) = f(x)$. Ãštil para "consertar" injetividade.

### ClassificaÃ§Ã£o de funÃ§Ãµes

**Injetora (ou injetiva, 1-1):**

$$x_1 \neq x_2 \implies f(x_1) \neq f(x_2) \quad \text{(equivalentemente: } f(x_1) = f(x_2) \implies x_1 = x_2\text{)}$$

Cada elemento do contradomÃ­nio Ã© atingido por **no mÃ¡ximo um** elemento do domÃ­nio. No grÃ¡fico: toda reta horizontal intercepta a curva em no mÃ¡ximo um ponto.

**Sobrejetora (ou sobrejetiva, sobre):**

$$\operatorname{Im}(f) = CD(f) \quad \text{(todo elemento de $B$ Ã© atingido por algum $x \in A$)}$$

Para todo $y \in B$, existe (pelo menos) um $x \in A$ com $f(x) = y$.

**Bijetora:** injetora **e** sobrejetora simultaneamente. Cada elemento de $B$ Ã© atingido por **exatamente um** elemento de $A$ â€” existe correspondÃªncia biunÃ­voca entre $A$ e $B$.

### FunÃ§Ã£o composta

Dadas $f: A \to B$ e $g: B \to C$ (com $\operatorname{Im}(f) \subseteq D(g)$), a **composiÃ§Ã£o** $g \circ f$ Ã© a funÃ§Ã£o:

$$(g \circ f): A \to C, \quad (g \circ f)(x) = g(f(x))$$

LÃª-se "g composta com f" ou "g apÃ³s f". A ordem importa: primeiro aplica-se $f$, depois $g$.

**Propriedades da composiÃ§Ã£o:**

| Propriedade | Enunciado |
| ----------- | --------- |
| Associatividade | $(h \circ g) \circ f = h \circ (g \circ f)$ |
| Identidade Ã  direita | $f \circ \operatorname{id}_A = f$ |
| Identidade Ã  esquerda | $\operatorname{id}_B \circ f = f$ |
| **NÃ£o-comutatividade** | Em geral, $g \circ f \neq f \circ g$ |

> A condiÃ§Ã£o $\operatorname{Im}(f) \subseteq D(g)$ deve ser verificada antes de compor. Se $\operatorname{Im}(f) \not\subseteq D(g)$, Ã© preciso restringir o domÃ­nio.

### FunÃ§Ã£o inversa

A funÃ§Ã£o inversa $f^{-1}: B \to A$ existe **se e somente se $f$ Ã© bijetora**. Ela satisfaz:

$$f^{-1}(f(x)) = x \quad \text{para todo } x \in A$$

$$f(f^{-1}(y)) = y \quad \text{para todo } y \in B$$

Equivalentemente: $f^{-1} \circ f = \operatorname{id}_A$ e $f \circ f^{-1} = \operatorname{id}_B$.

**Como calcular $f^{-1}$:**
1. Escrever $y = f(x)$
2. Trocar $x \leftrightarrow y$: obter $x = f(y)$
3. Isolar $y$ em funÃ§Ã£o de $x$ â†’ o resultado Ã© $f^{-1}(x)$

**Propriedades da inversa:**
- $(f^{-1})^{-1} = f$
- $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$ (a ordem inverte na inversÃ£o de compostas)

## FÃ³rmulas & EquaÃ§Ãµes

### NotaÃ§Ãµes principais

| SÃ­mbolo | Significado |
| ------- | ----------- |
| $f: A \to B$ | $f$ Ã© funÃ§Ã£o de $A$ em $B$ |
| $x \mapsto f(x)$ | $x$ Ã© levado a $f(x)$ |
| $D(f)$ | domÃ­nio de $f$ |
| $CD(f)$ | contradomÃ­nio de $f$ |
| $\operatorname{Im}(f)$ | imagem de $f$ |
| $f^{-1}$ | funÃ§Ã£o inversa de $f$ (quando $f$ Ã© bijetora) |
| $g \circ f$ | composiÃ§Ã£o: $(g \circ f)(x) = g(f(x))$ |
| $f\|_C$ | restriÃ§Ã£o de $f$ ao subconjunto $C \subseteq D(f)$ |

### RestriÃ§Ãµes de domÃ­nio mÃ¡ximo

| ExpressÃ£o | CondiÃ§Ã£o a impor |
| --------- | ---------------- |
| $\dfrac{P(x)}{Q(x)}$ | $Q(x) \neq 0$ |
| $\sqrt{g(x)}$ (raiz par) | $g(x) \geq 0$ |
| $\sqrt[2n]{g(x)}$ (raiz par geral) | $g(x) \geq 0$ |
| $\log_a g(x)$ | $g(x) > 0$ (e $a > 0$, $a \neq 1$) |
| CombinaÃ§Ã£o | interseÃ§Ã£o de todas as condiÃ§Ãµes |

## Exemplos Resolvidos

**Exemplo 1 â€” BÃ¡sico: calcular imagem de uma funÃ§Ã£o num domÃ­nio finito**

> **Enunciado:** Dada $f(x) = 2x + 3$ com $D(f) = \{0, 1, 2, 3\}$, calcule $f(0)$, $f(1)$, $f(2)$, $f(3)$ e determine $\operatorname{Im}(f)$.

**Passo 1 â€” Substituir cada elemento do domÃ­nio na fÃ³rmula.**

A funÃ§Ã£o $f(x) = 2x + 3$ Ã© avaliada ponto a ponto. Para cada $x \in D(f)$, multiplica-se por 2 e soma-se 3:

$$f(0) = 2 \cdot 0 + 3 = 0 + 3 = 3$$

$$f(1) = 2 \cdot 1 + 3 = 2 + 3 = 5$$

$$f(2) = 2 \cdot 2 + 3 = 4 + 3 = 7$$

$$f(3) = 2 \cdot 3 + 3 = 6 + 3 = 9$$

**Passo 2 â€” Construir a imagem.**

A imagem Ã© o conjunto de **todos os valores obtidos** â€” sem repetiÃ§Ã£o:

$$\operatorname{Im}(f) = \{3, 5, 7, 9\}$$

**Passo 3 â€” Verificar se $f$ Ã© injetora neste domÃ­nio.**

Valores distintos de $x$ deram valores distintos de $f(x)$: $0 \neq 1 \neq 2 \neq 3$ e $3 \neq 5 \neq 7 \neq 9$. Logo $f$ Ã© **injetora** em $D(f)$.

> **ObservaÃ§Ã£o:** $\operatorname{Im}(f) = \{3, 5, 7, 9\} \subsetneq \mathbb{R}$ â€” a imagem Ã© subconjunto prÃ³prio de qualquer contradomÃ­nio mais amplo (ex: $\mathbb{R}$). $f$ nÃ£o seria sobrejetora sobre $\mathbb{R}$.

---

**Exemplo 2 â€” IntermediÃ¡rio: determinar o domÃ­nio mÃ¡ximo**

> **Enunciado:** Determine o domÃ­nio mÃ¡ximo de $f(x) = \dfrac{\sqrt{x - 2}}{x - 5}$.

**Passo 1 â€” Identificar as restriÃ§Ãµes da fÃ³rmula.**

A expressÃ£o envolve dois elementos que impÃµem condiÃ§Ãµes:

- **Raiz quadrada** no numerador: o radicando deve ser nÃ£o-negativo
- **Denominador:** nÃ£o pode ser zero

Logo hÃ¡ **duas condiÃ§Ãµes a impor simultaneamente**.

**Passo 2 â€” Resolver a condiÃ§Ã£o da raiz.**

$$x - 2 \geq 0 \implies x \geq 2$$

Em notaÃ§Ã£o de intervalo: $x \in [2, +\infty)$.

**Passo 3 â€” Resolver a condiÃ§Ã£o do denominador.**

$$x - 5 \neq 0 \implies x \neq 5$$

Ou seja, excluir o ponto $x = 5$.

**Passo 4 â€” Interseccionar as duas condiÃ§Ãµes.**

O domÃ­nio mÃ¡ximo exige que **ambas** as condiÃ§Ãµes sejam satisfeitas ao mesmo tempo:

$$D(f) = [2, +\infty) \cap \{x \mid x \neq 5\}$$

O ponto $x = 5$ pertencia a $[2, +\infty)$, pois $5 \geq 2$. Portanto deve ser **excluÃ­do** de $[2, +\infty)$. Isso divide o intervalo em dois:

$$D(f) = [2, 5) \cup (5, +\infty)$$

**VerificaÃ§Ã£o com pontos de teste:**

- $x = 2$: $f(2) = \dfrac{\sqrt{0}}{-3} = 0$ âœ“ (estÃ¡ definida)
- $x = 5$: $f(5) = \dfrac{\sqrt{3}}{0}$ â†’ **indefinida** âœ“ (corretamente excluÃ­do)
- $x = 9$: $f(9) = \dfrac{\sqrt{7}}{4}$ âœ“ (estÃ¡ definida)

> **Resultado:** $D(f) = [2, 5) \cup (5, +\infty)$.

---

**Exemplo 3 â€” AvanÃ§ado: composiÃ§Ã£o e funÃ§Ã£o inversa**

> **Enunciado:** Dadas $f(x) = 3x - 1$ e $g(x) = x^2 + 2$ (ambas com $D = \mathbb{R}$):
> a) Calcule $(f \circ g)(x)$ e $(g \circ f)(x)$ e mostre que sÃ£o diferentes.
> b) Encontre $f^{-1}(x)$ e verifique que $f$ Ã© de fato invertÃ­vel.

**â€” Parte a: composiÃ§Ã£o â€”**

**Passo 1 â€” Calcular $(f \circ g)(x) = f(g(x))$.**

Substituir a expressÃ£o inteira de $g(x)$ no lugar de $x$ em $f$:

$$f(g(x)) = f(x^2 + 2)$$

Agora aplicar $f$: onde $f$ tem "$x$", colocar "$x^2 + 2$":

$$f(x^2 + 2) = 3(x^2 + 2) - 1$$

Distribuir o 3 e simplificar:

$$= 3x^2 + 6 - 1 = 3x^2 + 5$$

$$\boxed{(f \circ g)(x) = 3x^2 + 5}$$

**Passo 2 â€” Calcular $(g \circ f)(x) = g(f(x))$.**

Substituir a expressÃ£o de $f(x)$ no lugar de $x$ em $g$:

$$g(f(x)) = g(3x - 1)$$

Aplicar $g$: onde $g$ tem "$x$", colocar "$3x - 1$":

$$g(3x - 1) = (3x - 1)^2 + 2$$

Expandir o quadrado $(a - b)^2 = a^2 - 2ab + b^2$ com $a = 3x$ e $b = 1$:

$$(3x - 1)^2 = 9x^2 - 6x + 1$$

Somar 2:

$$= 9x^2 - 6x + 1 + 2 = 9x^2 - 6x + 3$$

$$\boxed{(g \circ f)(x) = 9x^2 - 6x + 3}$$

**Passo 3 â€” Verificar que sÃ£o diferentes.**

$(f \circ g)(x) = 3x^2 + 5$ e $(g \circ f)(x) = 9x^2 - 6x + 3$ sÃ£o polinÃ´mios distintos (coeficientes diferentes). Por exemplo, em $x = 1$:

$$(f \circ g)(1) = 3 + 5 = 8 \qquad (g \circ f)(1) = 9 - 6 + 3 = 6$$

$8 \neq 6$, confirmando $f \circ g \neq g \circ f$. âœ“

**â€” Parte b: funÃ§Ã£o inversa de $f$ â€”**

**Passo 4 â€” Verificar que $f(x) = 3x - 1$ Ã© bijetora (condiÃ§Ã£o para existÃªncia da inversa).**

- **Injetora:** $f$ Ã© polinÃ´mio de grau 1 com coeficiente $3 > 0$ (funÃ§Ã£o estritamente crescente). FunÃ§Ãµes estritamente monÃ³tonas sÃ£o sempre injetoras.
- **Sobrejetora sobre $\mathbb{R}$:** funÃ§Ã£o afim com domÃ­nio $\mathbb{R}$ atinge todos os reais (imagem $= \mathbb{R} = CD(f)$).

Logo $f$ Ã© **bijetora** â†’ a inversa existe. âœ“

**Passo 5 â€” Escrever $y = f(x)$ e trocar $x \leftrightarrow y$.**

Partir de:

$$y = 3x - 1$$

Trocar $x$ por $y$ e $y$ por $x$:

$$x = 3y - 1$$

**Passo 6 â€” Isolar $y$.**

Somar 1 nos dois lados:

$$x + 1 = 3y$$

Dividir por 3:

$$y = \frac{x + 1}{3}$$

$$\boxed{f^{-1}(x) = \frac{x + 1}{3}}$$

**Passo 7 â€” Verificar: $f^{-1}(f(x))$ deve ser $x$.**

$$f^{-1}(f(x)) = f^{-1}(3x - 1) = \frac{(3x - 1) + 1}{3} = \frac{3x}{3} = x \checkmark$$

Verificar tambÃ©m $f(f^{-1}(x)) = x$:

$$f(f^{-1}(x)) = f\!\left(\frac{x+1}{3}\right) = 3 \cdot \frac{x+1}{3} - 1 = (x + 1) - 1 = x \checkmark$$

## Armadilhas & Edge Cases

- **Confundir relaÃ§Ã£o com funÃ§Ã£o** â€” $y^2 = x$ nÃ£o Ã© funÃ§Ã£o: para $x = 4$, temos $y = 2$ e $y = -2$ (duas saÃ­das para uma entrada). Sempre verificar a unicidade da imagem
- **Imagem â‰  contradomÃ­nio** â€” $\operatorname{Im}(f) \subseteq CD(f)$ sempre, mas a igualdade sÃ³ ocorre se $f$ Ã© sobrejetora; nÃ£o confundir os dois conceitos
- **Esquecer de interseccionar restriÃ§Ãµes** â€” todas as condiÃ§Ãµes de domÃ­nio devem ser satisfeitas **ao mesmo tempo**; a interseÃ§Ã£o pode ser um conjunto menor do que cada condiÃ§Ã£o individualmente
- **$f^{-1}$ nÃ£o Ã© o recÃ­proco** â€” $f^{-1}(x)$ Ã© a **funÃ§Ã£o inversa**, nÃ£o $\dfrac{1}{f(x)}$; sÃ£o objetos completamente diferentes
- **ComposiÃ§Ã£o nÃ£o Ã© comutativa** â€” $g \circ f \neq f \circ g$ em geral; a ordem de aplicaÃ§Ã£o importa
- **Verificar $\operatorname{Im}(f) \subseteq D(g)$ antes de compor** â€” se a imagem de $f$ tiver pontos fora do domÃ­nio de $g$, a composiÃ§Ã£o nÃ£o estÃ¡ definida naqueles pontos
- **Inversa sem bijetividade** â€” tentar calcular $f^{-1}$ de uma funÃ§Ã£o nÃ£o-bijetora leva a inconsistÃªncias (a equaÃ§Ã£o $y = f(x)$ pode nÃ£o ter soluÃ§Ã£o ou ter mais de uma); soluÃ§Ã£o: restringir o domÃ­nio para tornar $f$ bijetora
- **Cuidado com $(g \circ f)^{-1}$** â€” a inversa da composiÃ§Ã£o **inverte a ordem**: $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$

## ConexÃµes

- [[MatemÃ¡tica]] â€” MOC da Ã¡rea
- [[GraduaÃ§Ã£o em QuÃ­mica]] â€” Roadmap da graduaÃ§Ã£o
- [[Conjuntos]] â€” prÃ©-requisito: domÃ­nio, contradomÃ­nio e imagem sÃ£o conjuntos; operaÃ§Ãµes de conjunto usadas em domÃ­nio mÃ¡ximo
- [[Conjuntos NumÃ©ricos]] â€” prÃ©-requisito: domÃ­nio e imagem tipicamente subconjuntos de $\mathbb{R}$; intervalos usados na notaÃ§Ã£o de domÃ­nio
- [[FunÃ§Ãµes e GrÃ¡ficos]] â€” representaÃ§Ã£o visual, paridade, monotonicidade, funÃ§Ãµes especÃ­ficas (afim, quadrÃ¡tica, exponencial, log)
- [[FÃ­sica]] â€” posiÃ§Ã£o, velocidade, forÃ§a como funÃ§Ãµes do tempo; composiÃ§Ã£o de grandezas

## Fontes

- GUIDORIZZI, Hamilton Luiz. *Um Curso de CÃ¡lculo* â€” Vol. 1, Cap. 1: FunÃ§Ãµes. pg. 37. LTC.
