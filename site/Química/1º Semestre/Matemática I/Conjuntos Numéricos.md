---
title: Conjuntos Numéricos
description: Hierarquia $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset
  \mathbb{R}$, propriedades dos números reais, intervalos e módulo — base de todo
  o cálculo.
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: matematica
semestre: 1
---

# Conjuntos Numéricos

> Hierarquia $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$, propriedades dos números reais, intervalos e módulo — base de todo o cálculo.

---

## Definição

Os **conjuntos numéricos** formam uma hierarquia de extensões sucessivas, em que cada novo conjunto é construído para resolver uma limitação do anterior — tipicamente, o **fechamento** (ou não) sob uma operação. Por exemplo, $\mathbb{N}$ não é fechado sob subtração ($3 - 5 \notin \mathbb{N}$), o que motiva a criação de $\mathbb{Z}$; $\mathbb{Z}$ não é fechado sob divisão, motivando $\mathbb{Q}$; e $\mathbb{Q}$ tem "buracos" na reta (como $\sqrt{2}$), motivando $\mathbb{R}$.

Essa cadeia é a base sobre a qual se constroem domínios e imagens de funções, sequências, limites e toda a análise real.

## Teoria & Fundamentos

### Naturais ($\mathbb{N}$)

$$\mathbb{N} = \{0, 1, 2, 3, 4, \ldots\}$$

> **Convenção:** na tradição brasileira (e no Iezzi/Guidorizzi), o $0$ é incluído em $\mathbb{N}$. $\mathbb{N}^* = \mathbb{N} \setminus \{0\} = \{1, 2, 3, \ldots\}$ exclui o zero.

Fechado sob soma e multiplicação; **não** fechado sob subtração nem divisão.

### Inteiros ($\mathbb{Z}$)

$$\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}$$

Estende $\mathbb{N}$ para fechar a subtração. Subconjuntos úteis:

| Notação | Significado |
| ------- | ----------- |
| $\mathbb{Z}^*$ | $\mathbb{Z} \setminus \{0\}$ |
| $\mathbb{Z}_+$ | inteiros não-negativos $= \mathbb{N}$ |
| $\mathbb{Z}_-$ | inteiros não-positivos |
| $\mathbb{Z}_+^*$ | inteiros estritamente positivos |
| $\mathbb{Z}_-^*$ | inteiros estritamente negativos |

### Racionais ($\mathbb{Q}$)

$$\mathbb{Q} = \left\{\frac{a}{b} \;\middle|\; a \in \mathbb{Z},\; b \in \mathbb{Z}^*\right\}$$

Estende $\mathbb{Z}$ para fechar a divisão (por elementos não-nulos).

**Caracterização decimal:** um número é racional se, e somente se, sua representação decimal é **finita** ou uma **dízima periódica**.

| Tipo | Exemplo | Forma fracionária |
| ---- | ------- | ----------------- |
| Decimal finita | $0{,}25$ | $\dfrac{1}{4}$ |
| Dízima periódica simples | $0{,}\overline{3}$ | $\dfrac{1}{3}$ |
| Dízima periódica composta | $0{,}1\overline{6}$ | $\dfrac{1}{6}$ |

### Irracionais ($\mathbb{I}$)

Números cuja representação decimal é **infinita e não-periódica**. Não podem ser escritos como $\dfrac{a}{b}$ com $a, b \in \mathbb{Z}$.

Exemplos clássicos: $\sqrt{2}, \sqrt{3}, \sqrt{5}, \pi, e$.

> [!info]- Esboço: por que $\sqrt{2}$ é irracional (redução ao absurdo)
> Suponha, por absurdo, que $\sqrt{2} = \dfrac{a}{b}$ com $a, b \in \mathbb{Z}$, $b \neq 0$, e a fração **irredutível** ($\operatorname{mdc}(a,b) = 1$).
> Elevando ao quadrado: $2 = \dfrac{a^2}{b^2} \implies a^2 = 2b^2$. Logo $a^2$ é par, então $a$ é par; escreve-se $a = 2k$.
> Substituindo: $(2k)^2 = 2b^2 \implies 4k^2 = 2b^2 \implies b^2 = 2k^2$. Logo $b$ também é par.
> Mas se $a$ e $b$ são ambos pares, $\operatorname{mdc}(a,b) \geq 2$, contradizendo a hipótese de fração irredutível. ∎

### Reais ($\mathbb{R}$)

$$\mathbb{R} = \mathbb{Q} \cup \mathbb{I}$$

Existe uma **correspondência biunívoca** entre $\mathbb{R}$ e os pontos da reta orientada (reta real) — cada real corresponde a um único ponto, e vice-versa. Essa é a base geométrica de todo o cálculo.

### Cadeia de inclusões

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

> Note que $\mathbb{I}$ **não está** nessa cadeia: $\mathbb{I}$ é disjunto de $\mathbb{Q}$ e $\mathbb{I} \subset \mathbb{R}$.

### Propriedades algébricas dos reais

Para todos $a, b, c \in \mathbb{R}$:

| Propriedade | Soma | Multiplicação |
| ----------- | ---- | ------------- |
| Fechamento | $a + b \in \mathbb{R}$ | $a \cdot b \in \mathbb{R}$ |
| Comutativa | $a + b = b + a$ | $a \cdot b = b \cdot a$ |
| Associativa | $(a + b) + c = a + (b + c)$ | $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ |
| Elemento neutro | $a + 0 = a$ | $a \cdot 1 = a$ |
| Inverso | $a + (-a) = 0$ | $a \cdot \dfrac{1}{a} = 1$ ($a \neq 0$) |
| Distributiva | $a \cdot (b + c) = a \cdot b + a \cdot c$ | |

### Propriedades de ordem

Para todos $a, b, c \in \mathbb{R}$:

- **Tricotomia:** vale exatamente uma das três relações: $a < b$, $a = b$ ou $a > b$
- **Transitividade:** se $a < b$ e $b < c$, então $a < c$
- **Compatibilidade com soma:** se $a < b$, então $a + c < b + c$
- **Compatibilidade com produto:**
    - se $a < b$ e $c > 0$, então $a \cdot c < b \cdot c$
    - se $a < b$ e $c < 0$, então $a \cdot c > b \cdot c$ (desigualdade **inverte**)

### Intervalos reais

Subconjuntos especiais de $\mathbb{R}$ definidos por desigualdades. Sejam $a, b \in \mathbb{R}$ com $a < b$:

| Tipo | Notação | Desigualdade | Reta |
| ---- | ------- | ------------ | ---- |
| Fechado | $[a, b]$ | $a \leq x \leq b$ | $\bullet\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\!\bullet$ |
| Aberto | $(a, b)$ | $a < x < b$ | $\circ\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\!\circ$ |
| Semiaberto à direita | $[a, b)$ | $a \leq x < b$ | $\bullet\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\!\circ$ |
| Semiaberto à esquerda | $(a, b]$ | $a < x \leq b$ | $\circ\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\!\bullet$ |
| Infinito à direita | $[a, +\infty)$ | $x \geq a$ | $\bullet\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\to$ |
| Infinito à direita (aberto) | $(a, +\infty)$ | $x > a$ | $\circ\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\to$ |
| Infinito à esquerda | $(-\infty, b]$ | $x \leq b$ | $\leftarrow\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\!\bullet$ |
| Infinito à esquerda (aberto) | $(-\infty, b)$ | $x < b$ | $\leftarrow\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\!\circ$ |
| Toda a reta | $(-\infty, +\infty)$ | $x \in \mathbb{R}$ | $\leftarrow\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\to$ |

> **Importante:** $\infty$ **nunca** é incluído em intervalo (nunca há colchete em $\infty$); $\infty$ é símbolo de "sem limite", não um número real.

### Valor absoluto (módulo)

$$|x| = \begin{cases} x, & \text{se } x \geq 0 \\ -x, & \text{se } x < 0 \end{cases}$$

**Interpretação geométrica:** $|x|$ é a **distância** de $x$ até a origem na reta real. Generalizando, $|x - a|$ é a distância entre $x$ e $a$.

**Propriedades** (para todo $x, y \in \mathbb{R}$):

| Propriedade | Fórmula |
| ----------- | ------- |
| Não-negatividade | $\|x\| \geq 0$, e $\|x\| = 0 \iff x = 0$ |
| Simetria | $\|-x\| = \|x\|$ |
| Multiplicativa | $\|x \cdot y\| = \|x\| \cdot \|y\|$ |
| Quociente | $\left\|\dfrac{x}{y}\right\| = \dfrac{\|x\|}{\|y\|}$, $y \neq 0$ |
| Desigualdade triangular | $\|x + y\| \leq \|x\| + \|y\|$ |
| Raiz quadrada | $\sqrt{x^2} = \|x\|$ |
| Equação modular | $\|x\| = a \;(a \geq 0) \iff x = a$ ou $x = -a$ |
| Inequação modular | $\|x\| \leq a \;(a > 0) \iff -a \leq x \leq a$ |
| Inequação modular | $\|x\| \geq a \;(a > 0) \iff x \leq -a$ ou $x \geq a$ |

## Fórmulas & Equações

### Notação dos conjuntos

| Símbolo | Significado |
| ------- | ----------- |
| $\mathbb{N}$ | naturais $\{0, 1, 2, \ldots\}$ |
| $\mathbb{N}^*$ | naturais sem zero |
| $\mathbb{Z}$ | inteiros |
| $\mathbb{Z}^*, \mathbb{Z}_+, \mathbb{Z}_-, \mathbb{Z}_+^*, \mathbb{Z}_-^*$ | variantes de $\mathbb{Z}$ |
| $\mathbb{Q}$ | racionais |
| $\mathbb{Q}^*, \mathbb{Q}_+, \mathbb{Q}_-$ | variantes de $\mathbb{Q}$ |
| $\mathbb{I}$ ou $\mathbb{R} \setminus \mathbb{Q}$ | irracionais |
| $\mathbb{R}$ | reais |
| $\mathbb{R}^*, \mathbb{R}_+, \mathbb{R}_-, \mathbb{R}_+^*, \mathbb{R}_-^*$ | variantes de $\mathbb{R}$ |

### Conversão dízima periódica → fração

Para $0,\overline{a_1 a_2 \ldots a_n}$ (período de $n$ dígitos), a fração geratriz é:

$$\frac{\text{período}}{\underbrace{99\ldots9}_{n \text{ noves}}}$$

## Exemplos Resolvidos

**Exemplo 1 — Básico: classificar números nos conjuntos**

> **Enunciado:** Classifique cada número abaixo indicando a quais dos conjuntos $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{I}, \mathbb{R}$ ele pertence: $-3$, $0$, $\dfrac{2}{5}$, $\sqrt{2}$, $\pi$, $0{,}\overline{3}$, $\sqrt{4}$.

**Passo 1 — Lembrar a hierarquia.**

Como $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ e $\mathbb{I} \subset \mathbb{R}$ (com $\mathbb{I} \cap \mathbb{Q} = \emptyset$), basta identificar o "menor" conjunto que contém o número — ele estará em todos os conjuntos acima desse na hierarquia.

**Passo 2 — Analisar cada número individualmente.**

- $-3$: inteiro negativo → $\mathbb{Z}, \mathbb{Q}, \mathbb{R}$ (não é natural)
- $0$: natural → $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$
- $\dfrac{2}{5}$: fração não-inteira (decimal finito $0{,}4$) → $\mathbb{Q}, \mathbb{R}$
- $\sqrt{2}$: irracional clássico (decimal infinita não-periódica) → $\mathbb{I}, \mathbb{R}$
- $\pi$: irracional clássico → $\mathbb{I}, \mathbb{R}$
- $0{,}\overline{3}$: dízima periódica → racional ($= \dfrac{1}{3}$) → $\mathbb{Q}, \mathbb{R}$
- $\sqrt{4}$: **calcular antes de classificar!** $\sqrt{4} = 2$, que é natural → $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$

**Passo 3 — Resumir em tabela.**

| Número | $\mathbb{N}$ | $\mathbb{Z}$ | $\mathbb{Q}$ | $\mathbb{I}$ | $\mathbb{R}$ |
| ------ | --- | --- | --- | --- | --- |
| $-3$ | ✗ | ✓ | ✓ | ✗ | ✓ |
| $0$ | ✓ | ✓ | ✓ | ✗ | ✓ |
| $\dfrac{2}{5}$ | ✗ | ✗ | ✓ | ✗ | ✓ |
| $\sqrt{2}$ | ✗ | ✗ | ✗ | ✓ | ✓ |
| $\pi$ | ✗ | ✗ | ✗ | ✓ | ✓ |
| $0{,}\overline{3}$ | ✗ | ✗ | ✓ | ✗ | ✓ |
| $\sqrt{4}$ | ✓ | ✓ | ✓ | ✗ | ✓ |

> **Observação:** Note que $\sqrt{4}$ é racional/natural; não confundir "raiz quadrada" com "irracional automático".

---

**Exemplo 2 — Intermediário: dízima periódica em fração**

> **Enunciado:** Escreva $0{,}\overline{27}$ na forma de fração irredutível.

**Passo 1 — Nomear o número.**

Chamar $x = 0{,}\overline{27} = 0{,}272727\ldots$. Esse é o passo crucial: dar nome ao número permite manipular algebricamente.

**Passo 2 — Determinar quantos dígitos formam o período e multiplicar por $10^n$.**

O período tem **2 dígitos** (o "27"), então multiplica-se ambos os lados por $10^2 = 100$ para "deslocar" o período para a parte inteira:

$$100x = 27{,}272727\ldots$$

**Passo 3 — Subtrair as duas equações para eliminar a parte decimal infinita.**

$$\begin{aligned}
100x &= 27{,}272727\ldots \\
\;\;-\;\; x &= \;\;0{,}272727\ldots \\
\hline
99x &= 27
\end{aligned}$$

A subtração funciona porque a parte decimal de ambos os números é **idêntica** (mesma cauda infinita), então ela se cancela.

**Passo 4 — Isolar $x$.**

$$x = \frac{27}{99}$$

**Passo 5 — Simplificar a fração.**

Calcular $\operatorname{mdc}(27, 99) = 9$. Dividir numerador e denominador por 9:

$$x = \frac{27 \div 9}{99 \div 9} = \frac{3}{11}$$

**Verificação:** $3 \div 11 = 0{,}272727\ldots$ ✓

> **Resultado:** $0{,}\overline{27} = \dfrac{3}{11}$.

---

**Exemplo 3 — Avançado: inequação modular**

> **Enunciado:** Resolva $|2x - 3| \leq 5$ em $\mathbb{R}$ e escreva a solução como intervalo.

**Passo 1 — Aplicar a propriedade da inequação modular.**

A propriedade-chave é: $|y| \leq a \iff -a \leq y \leq a$ (para $a > 0$). Aqui $y = 2x - 3$ e $a = 5$:

$$|2x - 3| \leq 5 \iff -5 \leq 2x - 3 \leq 5$$

Essa é uma **inequação dupla** — três expressões ligadas pela mesma variável.

**Passo 2 — Isolar o termo com $x$ somando 3 a todos os "lados" da desigualdade dupla.**

A regra de compatibilidade da ordem com a soma permite somar o mesmo número aos três lados sem alterar as desigualdades:

$$-5 + 3 \leq 2x - 3 + 3 \leq 5 + 3$$

$$-2 \leq 2x \leq 8$$

**Passo 3 — Dividir todos os lados por 2 (positivo, então as desigualdades se mantêm).**

> Atenção: se o divisor fosse **negativo**, as desigualdades teriam que ser **invertidas**.

$$\frac{-2}{2} \leq \frac{2x}{2} \leq \frac{8}{2}$$

$$-1 \leq x \leq 4$$

**Passo 4 — Escrever a solução em notação de intervalo.**

Como ambas as desigualdades são $\leq$ (não-estritas), o intervalo é **fechado** nas duas extremidades:

$$S = [-1, 4]$$

**Verificação com extremos:**
- $x = -1$: $|2(-1) - 3| = |-5| = 5 \leq 5$ ✓
- $x = 4$: $|2(4) - 3| = |5| = 5 \leq 5$ ✓
- $x = 0$ (interior): $|2(0) - 3| = |-3| = 3 \leq 5$ ✓

> **Resultado:** $S = [-1, 4] = \{x \in \mathbb{R} \mid -1 \leq x \leq 4\}$.

## Armadilhas & Edge Cases

- **Convenção do zero em $\mathbb{N}$** — no Brasil/Iezzi/Guidorizzi, $0 \in \mathbb{N}$; em outros contextos (textos americanos antigos), $\mathbb{N}$ pode começar em 1; sempre verificar a convenção do livro
- **Achar que toda raiz é irracional** — $\sqrt{4} = 2$, $\sqrt{9} = 3$, $\sqrt[3]{8} = 2$ são naturais; só raízes não-exatas são irracionais
- **Confundir dízima periódica com irracional** — toda dízima **periódica** é racional; só dízimas **infinitas e não-periódicas** são irracionais
- **$0{,}\overline{9} = 1$** — é igualdade exata, não aproximação (verificável pela técnica do Exemplo 2)
- **Confundir intervalos abertos e fechados** — $[a, b]$ inclui as extremidades (desigualdade $\leq$); $(a, b)$ exclui (desigualdade $<$); na reta, bola cheia $\bullet$ vs. bola vazia $\circ$
- **Colocar colchete em $\infty$** — sempre parêntese: $[a, +\infty)$, nunca $[a, +\infty]$, pois $\infty$ não é número real
- **$\sqrt{x^2} = x$ é falso em geral** — o correto é $\sqrt{x^2} = |x|$; a igualdade só vale se $x \geq 0$
- **Esquecer de inverter a desigualdade ao multiplicar/dividir por negativo** — erro clássico em inequações
- **Equação $|x| = a$ tem duas soluções para $a > 0$** — $x = a$ **ou** $x = -a$; esquecer da segunda é erro frequente
- **Inequação modular: separação errada** — $|y| \leq a$ vira $-a \leq y \leq a$ (forma dupla); $|y| \geq a$ vira $y \leq -a$ **ou** $y \geq a$ (união disjunta); nunca confundir as duas formas

## Conexões

- Matemática — MOC da área
- [[Química]] — Roadmap da graduação
- [[Conjuntos]] — pré-requisito direto (linguagem, operações, inclusão)
- [[Funções]] — domínio, contradomínio e imagem são subconjuntos de $\mathbb{R}$ (próximo tópico)
- Física — grandezas físicas medidas em $\mathbb{R}$; ordem de grandeza; módulo de vetores

## Fontes

- GUIDORIZZI, Hamilton Luiz. *Um Curso de Cálculo* — Vol. 1, Apêndice 1: Propriedades dos números reais. pg. 1. LTC.
