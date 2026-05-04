---
title: Conjuntos NumÃ©ricos
description: Hierarquia $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset
  \mathbb{R}$, propriedades dos nÃºmeros reais, intervalos e mÃ³dulo â€” base de todo
  o cÃ¡lc…
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: matematica
semestre: 1
---
# Conjuntos NumÃ©ricos

> Hierarquia $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$, propriedades dos nÃºmeros reais, intervalos e mÃ³dulo â€” base de todo o cÃ¡lculo.

---

## DefiniÃ§Ã£o

Os **conjuntos numÃ©ricos** formam uma hierarquia de extensÃµes sucessivas, em que cada novo conjunto Ã© construÃ­do para resolver uma limitaÃ§Ã£o do anterior â€” tipicamente, o **fechamento** (ou nÃ£o) sob uma operaÃ§Ã£o. Por exemplo, $\mathbb{N}$ nÃ£o Ã© fechado sob subtraÃ§Ã£o ($3 - 5 \notin \mathbb{N}$), o que motiva a criaÃ§Ã£o de $\mathbb{Z}$; $\mathbb{Z}$ nÃ£o Ã© fechado sob divisÃ£o, motivando $\mathbb{Q}$; e $\mathbb{Q}$ tem "buracos" na reta (como $\sqrt{2}$), motivando $\mathbb{R}$.

Essa cadeia Ã© a base sobre a qual se constroem domÃ­nios e imagens de funÃ§Ãµes, sequÃªncias, limites e toda a anÃ¡lise real.

## Teoria & Fundamentos

### Naturais ($\mathbb{N}$)

$$\mathbb{N} = \{0, 1, 2, 3, 4, \ldots\}$$

> **ConvenÃ§Ã£o:** na tradiÃ§Ã£o brasileira (e no Iezzi/Guidorizzi), o $0$ Ã© incluÃ­do em $\mathbb{N}$. $\mathbb{N}^* = \mathbb{N} \setminus \{0\} = \{1, 2, 3, \ldots\}$ exclui o zero.

Fechado sob soma e multiplicaÃ§Ã£o; **nÃ£o** fechado sob subtraÃ§Ã£o nem divisÃ£o.

### Inteiros ($\mathbb{Z}$)

$$\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}$$

Estende $\mathbb{N}$ para fechar a subtraÃ§Ã£o. Subconjuntos Ãºteis:

| NotaÃ§Ã£o | Significado |
| ------- | ----------- |
| $\mathbb{Z}^*$ | $\mathbb{Z} \setminus \{0\}$ |
| $\mathbb{Z}_+$ | inteiros nÃ£o-negativos $= \mathbb{N}$ |
| $\mathbb{Z}_-$ | inteiros nÃ£o-positivos |
| $\mathbb{Z}_+^*$ | inteiros estritamente positivos |
| $\mathbb{Z}_-^*$ | inteiros estritamente negativos |

### Racionais ($\mathbb{Q}$)

$$\mathbb{Q} = \left\{\frac{a}{b} \;\middle|\; a \in \mathbb{Z},\; b \in \mathbb{Z}^*\right\}$$

Estende $\mathbb{Z}$ para fechar a divisÃ£o (por elementos nÃ£o-nulos).

**CaracterizaÃ§Ã£o decimal:** um nÃºmero Ã© racional se, e somente se, sua representaÃ§Ã£o decimal Ã© **finita** ou uma **dÃ­zima periÃ³dica**.

| Tipo | Exemplo | Forma fracionÃ¡ria |
| ---- | ------- | ----------------- |
| Decimal finita | $0{,}25$ | $\dfrac{1}{4}$ |
| DÃ­zima periÃ³dica simples | $0{,}\overline{3}$ | $\dfrac{1}{3}$ |
| DÃ­zima periÃ³dica composta | $0{,}1\overline{6}$ | $\dfrac{1}{6}$ |

### Irracionais ($\mathbb{I}$)

NÃºmeros cuja representaÃ§Ã£o decimal Ã© **infinita e nÃ£o-periÃ³dica**. NÃ£o podem ser escritos como $\dfrac{a}{b}$ com $a, b \in \mathbb{Z}$.

Exemplos clÃ¡ssicos: $\sqrt{2}, \sqrt{3}, \sqrt{5}, \pi, e$.

> [!info]- EsboÃ§o: por que $\sqrt{2}$ Ã© irracional (reduÃ§Ã£o ao absurdo)
> Suponha, por absurdo, que $\sqrt{2} = \dfrac{a}{b}$ com $a, b \in \mathbb{Z}$, $b \neq 0$, e a fraÃ§Ã£o **irredutÃ­vel** ($\operatorname{mdc}(a,b) = 1$).
> Elevando ao quadrado: $2 = \dfrac{a^2}{b^2} \implies a^2 = 2b^2$. Logo $a^2$ Ã© par, entÃ£o $a$ Ã© par; escreve-se $a = 2k$.
> Substituindo: $(2k)^2 = 2b^2 \implies 4k^2 = 2b^2 \implies b^2 = 2k^2$. Logo $b$ tambÃ©m Ã© par.
> Mas se $a$ e $b$ sÃ£o ambos pares, $\operatorname{mdc}(a,b) \geq 2$, contradizendo a hipÃ³tese de fraÃ§Ã£o irredutÃ­vel. âˆŽ

### Reais ($\mathbb{R}$)

$$\mathbb{R} = \mathbb{Q} \cup \mathbb{I}$$

Existe uma **correspondÃªncia biunÃ­voca** entre $\mathbb{R}$ e os pontos da reta orientada (reta real) â€” cada real corresponde a um Ãºnico ponto, e vice-versa. Essa Ã© a base geomÃ©trica de todo o cÃ¡lculo.

### Cadeia de inclusÃµes

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

> Note que $\mathbb{I}$ **nÃ£o estÃ¡** nessa cadeia: $\mathbb{I}$ Ã© disjunto de $\mathbb{Q}$ e $\mathbb{I} \subset \mathbb{R}$.

### Propriedades algÃ©bricas dos reais

Para todos $a, b, c \in \mathbb{R}$:

| Propriedade | Soma | MultiplicaÃ§Ã£o |
| ----------- | ---- | ------------- |
| Fechamento | $a + b \in \mathbb{R}$ | $a \cdot b \in \mathbb{R}$ |
| Comutativa | $a + b = b + a$ | $a \cdot b = b \cdot a$ |
| Associativa | $(a + b) + c = a + (b + c)$ | $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ |
| Elemento neutro | $a + 0 = a$ | $a \cdot 1 = a$ |
| Inverso | $a + (-a) = 0$ | $a \cdot \dfrac{1}{a} = 1$ ($a \neq 0$) |
| Distributiva | $a \cdot (b + c) = a \cdot b + a \cdot c$ | |

### Propriedades de ordem

Para todos $a, b, c \in \mathbb{R}$:

- **Tricotomia:** vale exatamente uma das trÃªs relaÃ§Ãµes: $a < b$, $a = b$ ou $a > b$
- **Transitividade:** se $a < b$ e $b < c$, entÃ£o $a < c$
- **Compatibilidade com soma:** se $a < b$, entÃ£o $a + c < b + c$
- **Compatibilidade com produto:**
    - se $a < b$ e $c > 0$, entÃ£o $a \cdot c < b \cdot c$
    - se $a < b$ e $c < 0$, entÃ£o $a \cdot c > b \cdot c$ (desigualdade **inverte**)

### Intervalos reais

Subconjuntos especiais de $\mathbb{R}$ definidos por desigualdades. Sejam $a, b \in \mathbb{R}$ com $a < b$:

| Tipo | NotaÃ§Ã£o | Desigualdade | Reta |
| ---- | ------- | ------------ | ---- |
| Fechado | $[a, b]$ | $a \leq x \leq b$ | $\bullet\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\!\bullet$ |
| Aberto | $(a, b)$ | $a < x < b$ | $\circ\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\!\circ$ |
| Semiaberto Ã  direita | $[a, b)$ | $a \leq x < b$ | $\bullet\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\!\circ$ |
| Semiaberto Ã  esquerda | $(a, b]$ | $a < x \leq b$ | $\circ\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\!\bullet$ |
| Infinito Ã  direita | $[a, +\infty)$ | $x \geq a$ | $\bullet\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\to$ |
| Infinito Ã  direita (aberto) | $(a, +\infty)$ | $x > a$ | $\circ\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\to$ |
| Infinito Ã  esquerda | $(-\infty, b]$ | $x \leq b$ | $\leftarrow\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\!\bullet$ |
| Infinito Ã  esquerda (aberto) | $(-\infty, b)$ | $x < b$ | $\leftarrow\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\!\circ$ |
| Toda a reta | $(-\infty, +\infty)$ | $x \in \mathbb{R}$ | $\leftarrow\!\!\rule[0.5ex]{1.5em}{0.4pt}\!\to$ |

> **Importante:** $\infty$ **nunca** Ã© incluÃ­do em intervalo (nunca hÃ¡ colchete em $\infty$); $\infty$ Ã© sÃ­mbolo de "sem limite", nÃ£o um nÃºmero real.

### Valor absoluto (mÃ³dulo)

$$|x| = \begin{cases} x, & \text{se } x \geq 0 \\ -x, & \text{se } x < 0 \end{cases}$$

**InterpretaÃ§Ã£o geomÃ©trica:** $|x|$ Ã© a **distÃ¢ncia** de $x$ atÃ© a origem na reta real. Generalizando, $|x - a|$ Ã© a distÃ¢ncia entre $x$ e $a$.

**Propriedades** (para todo $x, y \in \mathbb{R}$):

| Propriedade | FÃ³rmula |
| ----------- | ------- |
| NÃ£o-negatividade | $\|x\| \geq 0$, e $\|x\| = 0 \iff x = 0$ |
| Simetria | $\|-x\| = \|x\|$ |
| Multiplicativa | $\|x \cdot y\| = \|x\| \cdot \|y\|$ |
| Quociente | $\left\|\dfrac{x}{y}\right\| = \dfrac{\|x\|}{\|y\|}$, $y \neq 0$ |
| Desigualdade triangular | $\|x + y\| \leq \|x\| + \|y\|$ |
| Raiz quadrada | $\sqrt{x^2} = \|x\|$ |
| EquaÃ§Ã£o modular | $\|x\| = a \;(a \geq 0) \iff x = a$ ou $x = -a$ |
| InequaÃ§Ã£o modular | $\|x\| \leq a \;(a > 0) \iff -a \leq x \leq a$ |
| InequaÃ§Ã£o modular | $\|x\| \geq a \;(a > 0) \iff x \leq -a$ ou $x \geq a$ |

## FÃ³rmulas & EquaÃ§Ãµes

### NotaÃ§Ã£o dos conjuntos

| SÃ­mbolo | Significado |
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

### ConversÃ£o dÃ­zima periÃ³dica â†’ fraÃ§Ã£o

Para $0,\overline{a_1 a_2 \ldots a_n}$ (perÃ­odo de $n$ dÃ­gitos), a fraÃ§Ã£o geratriz Ã©:

$$\frac{\text{perÃ­odo}}{\underbrace{99\ldots9}_{n \text{ noves}}}$$

## Exemplos Resolvidos

**Exemplo 1 â€” BÃ¡sico: classificar nÃºmeros nos conjuntos**

> **Enunciado:** Classifique cada nÃºmero abaixo indicando a quais dos conjuntos $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{I}, \mathbb{R}$ ele pertence: $-3$, $0$, $\dfrac{2}{5}$, $\sqrt{2}$, $\pi$, $0{,}\overline{3}$, $\sqrt{4}$.

**Passo 1 â€” Lembrar a hierarquia.**

Como $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ e $\mathbb{I} \subset \mathbb{R}$ (com $\mathbb{I} \cap \mathbb{Q} = \emptyset$), basta identificar o "menor" conjunto que contÃ©m o nÃºmero â€” ele estarÃ¡ em todos os conjuntos acima desse na hierarquia.

**Passo 2 â€” Analisar cada nÃºmero individualmente.**

- $-3$: inteiro negativo â†’ $\mathbb{Z}, \mathbb{Q}, \mathbb{R}$ (nÃ£o Ã© natural)
- $0$: natural â†’ $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$
- $\dfrac{2}{5}$: fraÃ§Ã£o nÃ£o-inteira (decimal finito $0{,}4$) â†’ $\mathbb{Q}, \mathbb{R}$
- $\sqrt{2}$: irracional clÃ¡ssico (decimal infinita nÃ£o-periÃ³dica) â†’ $\mathbb{I}, \mathbb{R}$
- $\pi$: irracional clÃ¡ssico â†’ $\mathbb{I}, \mathbb{R}$
- $0{,}\overline{3}$: dÃ­zima periÃ³dica â†’ racional ($= \dfrac{1}{3}$) â†’ $\mathbb{Q}, \mathbb{R}$
- $\sqrt{4}$: **calcular antes de classificar!** $\sqrt{4} = 2$, que Ã© natural â†’ $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$

**Passo 3 â€” Resumir em tabela.**

| NÃºmero | $\mathbb{N}$ | $\mathbb{Z}$ | $\mathbb{Q}$ | $\mathbb{I}$ | $\mathbb{R}$ |
| ------ | --- | --- | --- | --- | --- |
| $-3$ | âœ— | âœ“ | âœ“ | âœ— | âœ“ |
| $0$ | âœ“ | âœ“ | âœ“ | âœ— | âœ“ |
| $\dfrac{2}{5}$ | âœ— | âœ— | âœ“ | âœ— | âœ“ |
| $\sqrt{2}$ | âœ— | âœ— | âœ— | âœ“ | âœ“ |
| $\pi$ | âœ— | âœ— | âœ— | âœ“ | âœ“ |
| $0{,}\overline{3}$ | âœ— | âœ— | âœ“ | âœ— | âœ“ |
| $\sqrt{4}$ | âœ“ | âœ“ | âœ“ | âœ— | âœ“ |

> **ObservaÃ§Ã£o:** Note que $\sqrt{4}$ Ã© racional/natural; nÃ£o confundir "raiz quadrada" com "irracional automÃ¡tico".

---

**Exemplo 2 â€” IntermediÃ¡rio: dÃ­zima periÃ³dica em fraÃ§Ã£o**

> **Enunciado:** Escreva $0{,}\overline{27}$ na forma de fraÃ§Ã£o irredutÃ­vel.

**Passo 1 â€” Nomear o nÃºmero.**

Chamar $x = 0{,}\overline{27} = 0{,}272727\ldots$. Esse Ã© o passo crucial: dar nome ao nÃºmero permite manipular algebricamente.

**Passo 2 â€” Determinar quantos dÃ­gitos formam o perÃ­odo e multiplicar por $10^n$.**

O perÃ­odo tem **2 dÃ­gitos** (o "27"), entÃ£o multiplica-se ambos os lados por $10^2 = 100$ para "deslocar" o perÃ­odo para a parte inteira:

$$100x = 27{,}272727\ldots$$

**Passo 3 â€” Subtrair as duas equaÃ§Ãµes para eliminar a parte decimal infinita.**

$$\begin{aligned}
100x &= 27{,}272727\ldots \\
\;\;-\;\; x &= \;\;0{,}272727\ldots \\
\hline
99x &= 27
\end{aligned}$$

A subtraÃ§Ã£o funciona porque a parte decimal de ambos os nÃºmeros Ã© **idÃªntica** (mesma cauda infinita), entÃ£o ela se cancela.

**Passo 4 â€” Isolar $x$.**

$$x = \frac{27}{99}$$

**Passo 5 â€” Simplificar a fraÃ§Ã£o.**

Calcular $\operatorname{mdc}(27, 99) = 9$. Dividir numerador e denominador por 9:

$$x = \frac{27 \div 9}{99 \div 9} = \frac{3}{11}$$

**VerificaÃ§Ã£o:** $3 \div 11 = 0{,}272727\ldots$ âœ“

> **Resultado:** $0{,}\overline{27} = \dfrac{3}{11}$.

---

**Exemplo 3 â€” AvanÃ§ado: inequaÃ§Ã£o modular**

> **Enunciado:** Resolva $|2x - 3| \leq 5$ em $\mathbb{R}$ e escreva a soluÃ§Ã£o como intervalo.

**Passo 1 â€” Aplicar a propriedade da inequaÃ§Ã£o modular.**

A propriedade-chave Ã©: $|y| \leq a \iff -a \leq y \leq a$ (para $a > 0$). Aqui $y = 2x - 3$ e $a = 5$:

$$|2x - 3| \leq 5 \iff -5 \leq 2x - 3 \leq 5$$

Essa Ã© uma **inequaÃ§Ã£o dupla** â€” trÃªs expressÃµes ligadas pela mesma variÃ¡vel.

**Passo 2 â€” Isolar o termo com $x$ somando 3 a todos os "lados" da desigualdade dupla.**

A regra de compatibilidade da ordem com a soma permite somar o mesmo nÃºmero aos trÃªs lados sem alterar as desigualdades:

$$-5 + 3 \leq 2x - 3 + 3 \leq 5 + 3$$

$$-2 \leq 2x \leq 8$$

**Passo 3 â€” Dividir todos os lados por 2 (positivo, entÃ£o as desigualdades se mantÃªm).**

> AtenÃ§Ã£o: se o divisor fosse **negativo**, as desigualdades teriam que ser **invertidas**.

$$\frac{-2}{2} \leq \frac{2x}{2} \leq \frac{8}{2}$$

$$-1 \leq x \leq 4$$

**Passo 4 â€” Escrever a soluÃ§Ã£o em notaÃ§Ã£o de intervalo.**

Como ambas as desigualdades sÃ£o $\leq$ (nÃ£o-estritas), o intervalo Ã© **fechado** nas duas extremidades:

$$S = [-1, 4]$$

**VerificaÃ§Ã£o com extremos:**
- $x = -1$: $|2(-1) - 3| = |-5| = 5 \leq 5$ âœ“
- $x = 4$: $|2(4) - 3| = |5| = 5 \leq 5$ âœ“
- $x = 0$ (interior): $|2(0) - 3| = |-3| = 3 \leq 5$ âœ“

> **Resultado:** $S = [-1, 4] = \{x \in \mathbb{R} \mid -1 \leq x \leq 4\}$.

## Armadilhas & Edge Cases

- **ConvenÃ§Ã£o do zero em $\mathbb{N}$** â€” no Brasil/Iezzi/Guidorizzi, $0 \in \mathbb{N}$; em outros contextos (textos americanos antigos), $\mathbb{N}$ pode comeÃ§ar em 1; sempre verificar a convenÃ§Ã£o do livro
- **Achar que toda raiz Ã© irracional** â€” $\sqrt{4} = 2$, $\sqrt{9} = 3$, $\sqrt[3]{8} = 2$ sÃ£o naturais; sÃ³ raÃ­zes nÃ£o-exatas sÃ£o irracionais
- **Confundir dÃ­zima periÃ³dica com irracional** â€” toda dÃ­zima **periÃ³dica** Ã© racional; sÃ³ dÃ­zimas **infinitas e nÃ£o-periÃ³dicas** sÃ£o irracionais
- **$0{,}\overline{9} = 1$** â€” Ã© igualdade exata, nÃ£o aproximaÃ§Ã£o (verificÃ¡vel pela tÃ©cnica do Exemplo 2)
- **Confundir intervalos abertos e fechados** â€” $[a, b]$ inclui as extremidades (desigualdade $\leq$); $(a, b)$ exclui (desigualdade $<$); na reta, bola cheia $\bullet$ vs. bola vazia $\circ$
- **Colocar colchete em $\infty$** â€” sempre parÃªntese: $[a, +\infty)$, nunca $[a, +\infty]$, pois $\infty$ nÃ£o Ã© nÃºmero real
- **$\sqrt{x^2} = x$ Ã© falso em geral** â€” o correto Ã© $\sqrt{x^2} = |x|$; a igualdade sÃ³ vale se $x \geq 0$
- **Esquecer de inverter a desigualdade ao multiplicar/dividir por negativo** â€” erro clÃ¡ssico em inequaÃ§Ãµes
- **EquaÃ§Ã£o $|x| = a$ tem duas soluÃ§Ãµes para $a > 0$** â€” $x = a$ **ou** $x = -a$; esquecer da segunda Ã© erro frequente
- **InequaÃ§Ã£o modular: separaÃ§Ã£o errada** â€” $|y| \leq a$ vira $-a \leq y \leq a$ (forma dupla); $|y| \geq a$ vira $y \leq -a$ **ou** $y \geq a$ (uniÃ£o disjunta); nunca confundir as duas formas

## ConexÃµes

- [[MatemÃ¡tica]] â€” MOC da Ã¡rea
- [[GraduaÃ§Ã£o em QuÃ­mica]] â€” Roadmap da graduaÃ§Ã£o
- [[Conjuntos]] â€” prÃ©-requisito direto (linguagem, operaÃ§Ãµes, inclusÃ£o)
- [[FunÃ§Ãµes]] â€” domÃ­nio, contradomÃ­nio e imagem sÃ£o subconjuntos de $\mathbb{R}$ (prÃ³ximo tÃ³pico)
- [[FÃ­sica]] â€” grandezas fÃ­sicas medidas em $\mathbb{R}$; ordem de grandeza; mÃ³dulo de vetores

## Fontes

- GUIDORIZZI, Hamilton Luiz. *Um Curso de CÃ¡lculo* â€” Vol. 1, ApÃªndice 1: Propriedades dos nÃºmeros reais. pg. 1. LTC.
