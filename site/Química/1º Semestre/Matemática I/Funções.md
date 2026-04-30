---
title: Funções
description: Definição formal de função, domínio, imagem, classificação (injetora/sobrejetora/bijetora),
  composição e função inversa — a linguagem central de todo o cálculo.
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: matematica
semestre: 1
---

# Funções

> Definição formal de função, domínio, imagem, classificação (injetora/sobrejetora/bijetora), composição e função inversa — a linguagem central de todo o cálculo.

---

## Definição

Uma **função** $f$ de $A$ em $B$ é uma **regra que associa a cada elemento $x \in A$ um único elemento $y \in B$**, denotado $f(x)$. A unicidade é fundamental: cada entrada tem **exatamente uma** saída.

Notação padrão:

$$f: A \to B, \quad x \mapsto f(x)$$

Lê-se: "$f$ é uma função de $A$ em $B$ que leva $x$ em $f(x)$". $A$ é o **domínio**, $B$ é o **contradomínio** e $x$ é a **variável independente**; $y = f(x)$ é a **variável dependente**.

## Teoria & Fundamentos

### Domínio, contradomínio e imagem

| Conceito | Notação | Definição |
| -------- | ------- | --------- |
| Domínio | $D(f)$ ou $\operatorname{Dom}(f)$ | Conjunto de partida $A$ — onde $f$ está definida |
| Contradomínio | $CD(f)$ | Conjunto de chegada $B$ — todas as saídas **possíveis** |
| Imagem | $\operatorname{Im}(f)$ | Subconjunto de $B$ formado pelos $y$ que **efetivamente** ocorrem: $\operatorname{Im}(f) = \{f(x) \mid x \in A\}$ |

> **Importante:** $\operatorname{Im}(f) \subseteq CD(f)$, mas em geral $\operatorname{Im}(f) \neq CD(f)$. A igualdade só ocorre quando $f$ é sobrejetora.

### Função vs. relação

Nem toda relação entre conjuntos é função. A condição de função exige:

1. **Existência:** todo $x \in A$ tem pelo menos um associado em $B$
2. **Unicidade:** todo $x \in A$ tem **no máximo um** associado em $B$

Teste prático (reta vertical): no plano $xy$, uma curva representa uma função se e somente se toda reta vertical a intercepta **em no máximo um ponto**.

### Domínio máximo (natural)

Quando $f$ é definida apenas por uma fórmula (sem especificar $D(f)$ explicitamente), o **domínio máximo** é o maior subconjunto de $\mathbb{R}$ em que a fórmula está bem definida. As restrições típicas são:

| Situação | Restrição | Motivo |
| -------- | --------- | ------ |
| Denominador | $\text{denominador} \neq 0$ | Divisão por zero é indefinida |
| Raiz de índice par | radicando $\geq 0$ | Raiz par de número negativo não é real |
| Logaritmo | argumento $> 0$ | $\log$ só definido para positivos |

Quando há **mais de uma restrição**, o domínio máximo é a **interseção** de todos os conjuntos que satisfazem cada condição individualmente.

### Igualdade de funções

Duas funções $f$ e $g$ são **iguais** ($f = g$) se, e somente se:
1. Têm o mesmo domínio: $D(f) = D(g)$
2. Têm o mesmo contradomínio: $CD(f) = CD(g)$
3. $f(x) = g(x)$ para todo $x$ no domínio comum

### Funções especiais

**Função identidade:** $\operatorname{id}_A: A \to A$, definida por $\operatorname{id}_A(x) = x$. Cada elemento vai para si mesmo.

**Função constante:** $f: A \to B$, $f(x) = c$ para todo $x \in A$, onde $c \in B$ é fixo. Imagem $= \{c\}$.

**Função restrita:** dada $f: A \to B$, a restrição de $f$ a $C \subseteq A$ é $f|_C: C \to B$, $f|_C(x) = f(x)$. Útil para "consertar" injetividade.

### Classificação de funções

**Injetora (ou injetiva, 1-1):**

$$x_1 \neq x_2 \implies f(x_1) \neq f(x_2) \quad \text{(equivalentemente: } f(x_1) = f(x_2) \implies x_1 = x_2\text{)}$$

Cada elemento do contradomínio é atingido por **no máximo um** elemento do domínio. No gráfico: toda reta horizontal intercepta a curva em no máximo um ponto.

**Sobrejetora (ou sobrejetiva, sobre):**

$$\operatorname{Im}(f) = CD(f) \quad \text{(todo elemento de $B$ é atingido por algum $x \in A$)}$$

Para todo $y \in B$, existe (pelo menos) um $x \in A$ com $f(x) = y$.

**Bijetora:** injetora **e** sobrejetora simultaneamente. Cada elemento de $B$ é atingido por **exatamente um** elemento de $A$ — existe correspondência biunívoca entre $A$ e $B$.

### Função composta

Dadas $f: A \to B$ e $g: B \to C$ (com $\operatorname{Im}(f) \subseteq D(g)$), a **composição** $g \circ f$ é a função:

$$(g \circ f): A \to C, \quad (g \circ f)(x) = g(f(x))$$

Lê-se "g composta com f" ou "g após f". A ordem importa: primeiro aplica-se $f$, depois $g$.

**Propriedades da composição:**

| Propriedade | Enunciado |
| ----------- | --------- |
| Associatividade | $(h \circ g) \circ f = h \circ (g \circ f)$ |
| Identidade à direita | $f \circ \operatorname{id}_A = f$ |
| Identidade à esquerda | $\operatorname{id}_B \circ f = f$ |
| **Não-comutatividade** | Em geral, $g \circ f \neq f \circ g$ |

> A condição $\operatorname{Im}(f) \subseteq D(g)$ deve ser verificada antes de compor. Se $\operatorname{Im}(f) \not\subseteq D(g)$, é preciso restringir o domínio.

### Função inversa

A função inversa $f^{-1}: B \to A$ existe **se e somente se $f$ é bijetora**. Ela satisfaz:

$$f^{-1}(f(x)) = x \quad \text{para todo } x \in A$$

$$f(f^{-1}(y)) = y \quad \text{para todo } y \in B$$

Equivalentemente: $f^{-1} \circ f = \operatorname{id}_A$ e $f \circ f^{-1} = \operatorname{id}_B$.

**Como calcular $f^{-1}$:**
1. Escrever $y = f(x)$
2. Trocar $x \leftrightarrow y$: obter $x = f(y)$
3. Isolar $y$ em função de $x$ → o resultado é $f^{-1}(x)$

**Propriedades da inversa:**
- $(f^{-1})^{-1} = f$
- $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$ (a ordem inverte na inversão de compostas)

## Fórmulas & Equações

### Notações principais

| Símbolo | Significado |
| ------- | ----------- |
| $f: A \to B$ | $f$ é função de $A$ em $B$ |
| $x \mapsto f(x)$ | $x$ é levado a $f(x)$ |
| $D(f)$ | domínio de $f$ |
| $CD(f)$ | contradomínio de $f$ |
| $\operatorname{Im}(f)$ | imagem de $f$ |
| $f^{-1}$ | função inversa de $f$ (quando $f$ é bijetora) |
| $g \circ f$ | composição: $(g \circ f)(x) = g(f(x))$ |
| $f\|_C$ | restrição de $f$ ao subconjunto $C \subseteq D(f)$ |

### Restrições de domínio máximo

| Expressão | Condição a impor |
| --------- | ---------------- |
| $\dfrac{P(x)}{Q(x)}$ | $Q(x) \neq 0$ |
| $\sqrt{g(x)}$ (raiz par) | $g(x) \geq 0$ |
| $\sqrt[2n]{g(x)}$ (raiz par geral) | $g(x) \geq 0$ |
| $\log_a g(x)$ | $g(x) > 0$ (e $a > 0$, $a \neq 1$) |
| Combinação | interseção de todas as condições |

## Exemplos Resolvidos

**Exemplo 1 — Básico: calcular imagem de uma função num domínio finito**

> **Enunciado:** Dada $f(x) = 2x + 3$ com $D(f) = \{0, 1, 2, 3\}$, calcule $f(0)$, $f(1)$, $f(2)$, $f(3)$ e determine $\operatorname{Im}(f)$.

**Passo 1 — Substituir cada elemento do domínio na fórmula.**

A função $f(x) = 2x + 3$ é avaliada ponto a ponto. Para cada $x \in D(f)$, multiplica-se por 2 e soma-se 3:

$$f(0) = 2 \cdot 0 + 3 = 0 + 3 = 3$$

$$f(1) = 2 \cdot 1 + 3 = 2 + 3 = 5$$

$$f(2) = 2 \cdot 2 + 3 = 4 + 3 = 7$$

$$f(3) = 2 \cdot 3 + 3 = 6 + 3 = 9$$

**Passo 2 — Construir a imagem.**

A imagem é o conjunto de **todos os valores obtidos** — sem repetição:

$$\operatorname{Im}(f) = \{3, 5, 7, 9\}$$

**Passo 3 — Verificar se $f$ é injetora neste domínio.**

Valores distintos de $x$ deram valores distintos de $f(x)$: $0 \neq 1 \neq 2 \neq 3$ e $3 \neq 5 \neq 7 \neq 9$. Logo $f$ é **injetora** em $D(f)$.

> **Observação:** $\operatorname{Im}(f) = \{3, 5, 7, 9\} \subsetneq \mathbb{R}$ — a imagem é subconjunto próprio de qualquer contradomínio mais amplo (ex: $\mathbb{R}$). $f$ não seria sobrejetora sobre $\mathbb{R}$.

---

**Exemplo 2 — Intermediário: determinar o domínio máximo**

> **Enunciado:** Determine o domínio máximo de $f(x) = \dfrac{\sqrt{x - 2}}{x - 5}$.

**Passo 1 — Identificar as restrições da fórmula.**

A expressão envolve dois elementos que impõem condições:

- **Raiz quadrada** no numerador: o radicando deve ser não-negativo
- **Denominador:** não pode ser zero

Logo há **duas condições a impor simultaneamente**.

**Passo 2 — Resolver a condição da raiz.**

$$x - 2 \geq 0 \implies x \geq 2$$

Em notação de intervalo: $x \in [2, +\infty)$.

**Passo 3 — Resolver a condição do denominador.**

$$x - 5 \neq 0 \implies x \neq 5$$

Ou seja, excluir o ponto $x = 5$.

**Passo 4 — Interseccionar as duas condições.**

O domínio máximo exige que **ambas** as condições sejam satisfeitas ao mesmo tempo:

$$D(f) = [2, +\infty) \cap \{x \mid x \neq 5\}$$

O ponto $x = 5$ pertencia a $[2, +\infty)$, pois $5 \geq 2$. Portanto deve ser **excluído** de $[2, +\infty)$. Isso divide o intervalo em dois:

$$D(f) = [2, 5) \cup (5, +\infty)$$

**Verificação com pontos de teste:**

- $x = 2$: $f(2) = \dfrac{\sqrt{0}}{-3} = 0$ ✓ (está definida)
- $x = 5$: $f(5) = \dfrac{\sqrt{3}}{0}$ → **indefinida** ✓ (corretamente excluído)
- $x = 9$: $f(9) = \dfrac{\sqrt{7}}{4}$ ✓ (está definida)

> **Resultado:** $D(f) = [2, 5) \cup (5, +\infty)$.

---

**Exemplo 3 — Avançado: composição e função inversa**

> **Enunciado:** Dadas $f(x) = 3x - 1$ e $g(x) = x^2 + 2$ (ambas com $D = \mathbb{R}$):
> a) Calcule $(f \circ g)(x)$ e $(g \circ f)(x)$ e mostre que são diferentes.
> b) Encontre $f^{-1}(x)$ e verifique que $f$ é de fato invertível.

**— Parte a: composição —**

**Passo 1 — Calcular $(f \circ g)(x) = f(g(x))$.**

Substituir a expressão inteira de $g(x)$ no lugar de $x$ em $f$:

$$f(g(x)) = f(x^2 + 2)$$

Agora aplicar $f$: onde $f$ tem "$x$", colocar "$x^2 + 2$":

$$f(x^2 + 2) = 3(x^2 + 2) - 1$$

Distribuir o 3 e simplificar:

$$= 3x^2 + 6 - 1 = 3x^2 + 5$$

$$\boxed{(f \circ g)(x) = 3x^2 + 5}$$

**Passo 2 — Calcular $(g \circ f)(x) = g(f(x))$.**

Substituir a expressão de $f(x)$ no lugar de $x$ em $g$:

$$g(f(x)) = g(3x - 1)$$

Aplicar $g$: onde $g$ tem "$x$", colocar "$3x - 1$":

$$g(3x - 1) = (3x - 1)^2 + 2$$

Expandir o quadrado $(a - b)^2 = a^2 - 2ab + b^2$ com $a = 3x$ e $b = 1$:

$$(3x - 1)^2 = 9x^2 - 6x + 1$$

Somar 2:

$$= 9x^2 - 6x + 1 + 2 = 9x^2 - 6x + 3$$

$$\boxed{(g \circ f)(x) = 9x^2 - 6x + 3}$$

**Passo 3 — Verificar que são diferentes.**

$(f \circ g)(x) = 3x^2 + 5$ e $(g \circ f)(x) = 9x^2 - 6x + 3$ são polinômios distintos (coeficientes diferentes). Por exemplo, em $x = 1$:

$$(f \circ g)(1) = 3 + 5 = 8 \qquad (g \circ f)(1) = 9 - 6 + 3 = 6$$

$8 \neq 6$, confirmando $f \circ g \neq g \circ f$. ✓

**— Parte b: função inversa de $f$ —**

**Passo 4 — Verificar que $f(x) = 3x - 1$ é bijetora (condição para existência da inversa).**

- **Injetora:** $f$ é polinômio de grau 1 com coeficiente $3 > 0$ (função estritamente crescente). Funções estritamente monótonas são sempre injetoras.
- **Sobrejetora sobre $\mathbb{R}$:** função afim com domínio $\mathbb{R}$ atinge todos os reais (imagem $= \mathbb{R} = CD(f)$).

Logo $f$ é **bijetora** → a inversa existe. ✓

**Passo 5 — Escrever $y = f(x)$ e trocar $x \leftrightarrow y$.**

Partir de:

$$y = 3x - 1$$

Trocar $x$ por $y$ e $y$ por $x$:

$$x = 3y - 1$$

**Passo 6 — Isolar $y$.**

Somar 1 nos dois lados:

$$x + 1 = 3y$$

Dividir por 3:

$$y = \frac{x + 1}{3}$$

$$\boxed{f^{-1}(x) = \frac{x + 1}{3}}$$

**Passo 7 — Verificar: $f^{-1}(f(x))$ deve ser $x$.**

$$f^{-1}(f(x)) = f^{-1}(3x - 1) = \frac{(3x - 1) + 1}{3} = \frac{3x}{3} = x \checkmark$$

Verificar também $f(f^{-1}(x)) = x$:

$$f(f^{-1}(x)) = f\!\left(\frac{x+1}{3}\right) = 3 \cdot \frac{x+1}{3} - 1 = (x + 1) - 1 = x \checkmark$$

## Armadilhas & Edge Cases

- **Confundir relação com função** — $y^2 = x$ não é função: para $x = 4$, temos $y = 2$ e $y = -2$ (duas saídas para uma entrada). Sempre verificar a unicidade da imagem
- **Imagem ≠ contradomínio** — $\operatorname{Im}(f) \subseteq CD(f)$ sempre, mas a igualdade só ocorre se $f$ é sobrejetora; não confundir os dois conceitos
- **Esquecer de interseccionar restrições** — todas as condições de domínio devem ser satisfeitas **ao mesmo tempo**; a interseção pode ser um conjunto menor do que cada condição individualmente
- **$f^{-1}$ não é o recíproco** — $f^{-1}(x)$ é a **função inversa**, não $\dfrac{1}{f(x)}$; são objetos completamente diferentes
- **Composição não é comutativa** — $g \circ f \neq f \circ g$ em geral; a ordem de aplicação importa
- **Verificar $\operatorname{Im}(f) \subseteq D(g)$ antes de compor** — se a imagem de $f$ tiver pontos fora do domínio de $g$, a composição não está definida naqueles pontos
- **Inversa sem bijetividade** — tentar calcular $f^{-1}$ de uma função não-bijetora leva a inconsistências (a equação $y = f(x)$ pode não ter solução ou ter mais de uma); solução: restringir o domínio para tornar $f$ bijetora
- **Cuidado com $(g \circ f)^{-1}$** — a inversa da composição **inverte a ordem**: $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$

## Conexões

- [[Conjuntos]] — pré-requisito: domínio, contradomínio e imagem são conjuntos; operações de conjunto usadas em domínio máximo
- [[Conjuntos Numéricos]] — pré-requisito: domínio e imagem tipicamente subconjuntos de $\mathbb{R}$; intervalos usados na notação de domínio
- [[Funções e Gráficos]] — representação visual, paridade, monotonicidade, funções específicas (afim, quadrática, exponencial, log)

## Fontes

- GUIDORIZZI, Hamilton Luiz. *Um Curso de Cálculo* — Vol. 1, Cap. 1: Funções. pg. 37. LTC.
