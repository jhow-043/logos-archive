---
title: FunÃ§Ãµes e GrÃ¡ficos
description: RepresentaÃ§Ã£o visual de funÃ§Ãµes no plano cartesiano, propriedades
  geomÃ©tricas (paridade, monotonicidade, limitaÃ§Ã£o), funÃ§Ãµes elementares e transformaÃ§…
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: matematica
semestre: 1
---
# FunÃ§Ãµes e GrÃ¡ficos

> RepresentaÃ§Ã£o visual de funÃ§Ãµes no plano cartesiano, propriedades geomÃ©tricas (paridade, monotonicidade, limitaÃ§Ã£o), funÃ§Ãµes elementares e transformaÃ§Ãµes de grÃ¡ficos.

---

## DefiniÃ§Ã£o

O **grÃ¡fico** de uma funÃ§Ã£o $f: A \to B$ Ã© o conjunto de todos os pares ordenados $(x, f(x))$:

$$G(f) = \{(x, f(x)) \mid x \in A\} \subset A \times B$$

No plano cartesiano ($A \subseteq \mathbb{R}$, $B \subseteq \mathbb{R}$), cada elemento $x$ do domÃ­nio gera um ponto $(x, y)$ com $y = f(x)$. A curva formada por todos esses pontos Ã© o grÃ¡fico de $f$ â€” uma ferramenta visual que revela propriedades (domÃ­nio, imagem, zeros, monotonicidade, paridade) de forma imediata.

## Teoria & Fundamentos

### Leitura do grÃ¡fico

A partir do grÃ¡fico de $f$ no plano $xy$, Ã© possÃ­vel extrair:

| InformaÃ§Ã£o | Como ler no grÃ¡fico |
| ---------- | ------------------- |
| DomÃ­nio $D(f)$ | ProjeÃ§Ã£o da curva sobre o eixo $x$ (extensÃ£o horizontal) |
| Imagem $\operatorname{Im}(f)$ | ProjeÃ§Ã£o da curva sobre o eixo $y$ (extensÃ£o vertical) |
| Zeros/raÃ­zes | Pontos onde a curva cruza o eixo $x$ (i.e., $f(x) = 0$) |
| Valor inicial | Ponto onde a curva cruza o eixo $y$ (i.e., $f(0)$, se $0 \in D(f)$) |
| Sinal de $f$ | PorÃ§Ãµes acima do eixo $x$: $f(x) > 0$; abaixo: $f(x) < 0$ |

### Teste da reta vertical

Uma curva no plano cartesiano Ã© grÃ¡fico de **alguma funÃ§Ã£o** se e somente se **toda reta vertical a intercepta em no mÃ¡ximo um ponto**. Se alguma reta vertical corta a curva em dois ou mais pontos, entÃ£o hÃ¡ dois $y$ para o mesmo $x$, violando a unicidade.

> **NÃ£o confundir** com o **teste da reta horizontal** (que testa injetividade): toda reta horizontal corta o grÃ¡fico em no mÃ¡ximo 1 ponto $\iff$ $f$ Ã© injetora.

### FunÃ§Ãµes elementares

#### FunÃ§Ã£o constante â€” $f(x) = c$

- **DomÃ­nio:** $\mathbb{R}$ | **Imagem:** $\{c\}$
- **GrÃ¡fico:** reta horizontal na altura $y = c$
- **Propriedades:** par (se o domÃ­nio for simÃ©trico); nem crescente nem decrescente

#### FunÃ§Ã£o identidade â€” $f(x) = x$

- **DomÃ­nio:** $\mathbb{R}$ | **Imagem:** $\mathbb{R}$
- **GrÃ¡fico:** reta que passa pela origem com inclinaÃ§Ã£o 45Â°
- **Propriedades:** Ã­mpar; estritamente crescente em $\mathbb{R}$

#### FunÃ§Ã£o afim (linear) â€” $f(x) = ax + b$

- **DomÃ­nio:** $\mathbb{R}$ | **Imagem:** $\mathbb{R}$ (se $a \neq 0$)
- **GrÃ¡fico:** reta com **coeficiente angular** $a$ e **coeficiente linear** $b$
- $a > 0$: crescente | $a < 0$: decrescente | $a = 0$: constante
- **Zero (raiz):** $x = -\dfrac{b}{a}$ (ponto onde cruza o eixo $x$)
- **Intercepto $y$:** $f(0) = b$

| ParÃ¢metro | Significado geomÃ©trico |
| --------- | ---------------------- |
| $a > 0$ | Reta sobe da esquerda para a direita |
| $a < 0$ | Reta desce da esquerda para a direita |
| $b > 0$ | Reta cruza o eixo $y$ acima da origem |
| $b < 0$ | Reta cruza o eixo $y$ abaixo da origem |
| $b = 0$ | Reta passa pela origem (funÃ§Ã£o linear pura) |

#### FunÃ§Ã£o quadrÃ¡tica â€” $f(x) = ax^2 + bx + c$, $a \neq 0$

- **DomÃ­nio:** $\mathbb{R}$ | **Imagem:** $\left[-\dfrac{\Delta}{4a}, +\infty\right)$ se $a > 0$; $\left(-\infty, -\dfrac{\Delta}{4a}\right]$ se $a < 0$
- **GrÃ¡fico:** parÃ¡bola com eixo de simetria vertical
- **Discriminante:** $\Delta = b^2 - 4ac$
- **VÃ©rtice:** $V = \left(-\dfrac{b}{2a},\; -\dfrac{\Delta}{4a}\right)$
- **Concavidade:** $a > 0$ â†’ abre para cima (mÃ­nimo no vÃ©rtice); $a < 0$ â†’ abre para baixo (mÃ¡ximo no vÃ©rtice)
- **RaÃ­zes:** $x = \dfrac{-b \pm \sqrt{\Delta}}{2a}$ (existem em $\mathbb{R}$ quando $\Delta \geq 0$)

| $\Delta$ | NÃºmero de raÃ­zes reais | PosiÃ§Ã£o da parÃ¡bola |
| -------- | ---------------------- | ------------------- |
| $\Delta > 0$ | 2 raÃ­zes distintas | Corta o eixo $x$ em 2 pontos |
| $\Delta = 0$ | 1 raiz dupla | Tangencia o eixo $x$ no vÃ©rtice |
| $\Delta < 0$ | 0 raÃ­zes reais | NÃ£o toca o eixo $x$ |

#### FunÃ§Ã£o mÃ³dulo â€” $f(x) = |x|$

- **DomÃ­nio:** $\mathbb{R}$ | **Imagem:** $[0, +\infty)$
- **GrÃ¡fico:** formato de "V" com vÃ©rtice na origem; $f(x) = x$ para $x \geq 0$ e $f(x) = -x$ para $x < 0$
- **Propriedades:** par; decrescente em $(-\infty, 0]$, crescente em $[0, +\infty)$

#### FunÃ§Ã£o raiz quadrada â€” $f(x) = \sqrt{x}$

- **DomÃ­nio:** $[0, +\infty)$ | **Imagem:** $[0, +\infty)$
- **GrÃ¡fico:** metade direita de uma parÃ¡bola deitada, partindo da origem
- **Propriedades:** estritamente crescente; Ã© a inversa de $f(x) = x^2$ restrita a $[0, +\infty)$

#### FunÃ§Ã£o recÃ­proca (hiperbÃ³lica) â€” $f(x) = \dfrac{1}{x}$

- **DomÃ­nio:** $\mathbb{R}^* = (-\infty, 0) \cup (0, +\infty)$ | **Imagem:** $\mathbb{R}^*$
- **GrÃ¡fico:** hipÃ©rbole equilÃ¡tera com assÃ­ntotas nos eixos coordenados (eixo $x$: assÃ­ntota horizontal; eixo $y$: assÃ­ntota vertical)
- **Propriedades:** Ã­mpar; decrescente em cada ramo (em $(-\infty,0)$ e em $(0,+\infty)$ separadamente)

#### FunÃ§Ã£o exponencial â€” $f(x) = a^x$, $a > 0$, $a \neq 1$

- **DomÃ­nio:** $\mathbb{R}$ | **Imagem:** $(0, +\infty)$
- **GrÃ¡fico:** passa sempre por $(0, 1)$ (pois $a^0 = 1$)
- $a > 1$: crescente (cresce Ã  direita, se aproxima de 0 Ã  esquerda)
- $0 < a < 1$: decrescente (decresce Ã  direita, se aproxima de 0 Ã  direita)
- **AssÃ­ntota horizontal:** eixo $x$ (o grÃ¡fico nunca toca $y = 0$)
- **NÃ£o tem raiz real** (imagem Ã© $(0, +\infty)$, nunca atinge $y = 0$)

#### FunÃ§Ã£o logarÃ­tmica â€” $f(x) = \log_a x$, $a > 0$, $a \neq 1$

- **DomÃ­nio:** $(0, +\infty)$ | **Imagem:** $\mathbb{R}$
- **GrÃ¡fico:** inversa da exponencial; simÃ©trica a $a^x$ em relaÃ§Ã£o Ã  reta $y = x$; passa por $(1, 0)$
- $a > 1$: crescente | $0 < a < 1$: decrescente
- **AssÃ­ntota vertical:** eixo $y$ ($x = 0$)
- **Zero:** $x = 1$ (pois $\log_a 1 = 0$)

### Paridade

A paridade Ã© uma propriedade **algÃ©brica** com reflexo **geomÃ©trico**. Exige que o domÃ­nio seja **simÃ©trico em relaÃ§Ã£o Ã  origem**.

**FunÃ§Ã£o par:** $f(-x) = f(x)$ para todo $x \in D(f)$
- GrÃ¡fico: **simÃ©trico ao eixo $y$** (reflexÃ£o vertical)
- Exemplos: $x^2$, $x^4$, $|x|$, $\operatorname{cos} x$

**FunÃ§Ã£o Ã­mpar:** $f(-x) = -f(x)$ para todo $x \in D(f)$
- GrÃ¡fico: **simÃ©trico Ã  origem** (rotaÃ§Ã£o de 180Â° em torno da origem)
- Exemplos: $x$, $x^3$, $\dfrac{1}{x}$, $\operatorname{sen} x$

**Nem par nem Ã­mpar:** a condiÃ§Ã£o nÃ£o Ã© satisfeita.

> **MÃ©todo de teste:** calcular $f(-x)$, simplificar e comparar com $f(x)$ e com $-f(x)$.

### Monotonicidade

Seja $I \subseteq D(f)$ um intervalo:

**Estritamente crescente em $I$:** $x_1 < x_2 \implies f(x_1) < f(x_2)$

**Estritamente decrescente em $I$:** $x_1 < x_2 \implies f(x_1) > f(x_2)$

> Uma funÃ§Ã£o pode ser crescente em um intervalo e decrescente em outro. Por exemplo, $f(x) = x^2$ Ã© decrescente em $(-\infty, 0]$ e crescente em $[0, +\infty)$.

**ConexÃ£o com injetividade:** toda funÃ§Ã£o estritamente monÃ³tona em um intervalo Ã© injetora nesse intervalo.

### LimitaÃ§Ã£o

- **Limitada superiormente em $I$:** existe $M \in \mathbb{R}$ tal que $f(x) \leq M$ para todo $x \in I$
- **Limitada inferiormente em $I$:** existe $m \in \mathbb{R}$ tal que $f(x) \geq m$ para todo $x \in I$
- **Limitada em $I$:** limitada superior e inferiormente

### TransformaÃ§Ãµes de grÃ¡ficos

Dada a curva de $y = f(x)$, as transformaÃ§Ãµes a seguir produzem novos grÃ¡ficos:

| TransformaÃ§Ã£o na fÃ³rmula | Efeito no grÃ¡fico |
| ------------------------ | ----------------- |
| $f(x) + k$, $k > 0$ | TranslaÃ§Ã£o vertical **para cima** de $k$ unidades |
| $f(x) - k$, $k > 0$ | TranslaÃ§Ã£o vertical **para baixo** de $k$ unidades |
| $f(x - h)$, $h > 0$ | TranslaÃ§Ã£o horizontal **para a direita** de $h$ unidades |
| $f(x + h)$, $h > 0$ | TranslaÃ§Ã£o horizontal **para a esquerda** de $h$ unidades |
| $-f(x)$ | ReflexÃ£o em relaÃ§Ã£o ao **eixo $x$** |
| $f(-x)$ | ReflexÃ£o em relaÃ§Ã£o ao **eixo $y$** |
| $a \cdot f(x)$, $a > 1$ | DilataÃ§Ã£o vertical (estica verticalmente) |
| $a \cdot f(x)$, $0 < a < 1$ | CompressÃ£o vertical |
| $f(ax)$, $a > 1$ | CompressÃ£o horizontal |
| $f(ax)$, $0 < a < 1$ | DilataÃ§Ã£o horizontal |

### GrÃ¡fico da funÃ§Ã£o inversa

Se $f$ Ã© bijetora, o grÃ¡fico de $f^{-1}$ Ã© a **reflexÃ£o do grÃ¡fico de $f$ em relaÃ§Ã£o Ã  reta $y = x$**. Em termos de pontos: se $(a, b) \in G(f)$, entÃ£o $(b, a) \in G(f^{-1})$.

## FÃ³rmulas & EquaÃ§Ãµes

### Resumo das funÃ§Ãµes elementares

| FunÃ§Ã£o | FÃ³rmula | DomÃ­nio | Imagem | GrÃ¡fico |
| ------ | ------- | ------- | ------ | ------- |
| Constante | $c$ | $\mathbb{R}$ | $\{c\}$ | Reta horizontal |
| Identidade | $x$ | $\mathbb{R}$ | $\mathbb{R}$ | Reta diagonal (45Â°) |
| Afim | $ax + b$ | $\mathbb{R}$ | $\mathbb{R}$ | Reta inclinada |
| QuadrÃ¡tica | $ax^2 + bx + c$ | $\mathbb{R}$ | Depende de $a$ e $\Delta$ | ParÃ¡bola |
| MÃ³dulo | $\|x\|$ | $\mathbb{R}$ | $[0,+\infty)$ | Forma de V |
| Raiz quadrada | $\sqrt{x}$ | $[0,+\infty)$ | $[0,+\infty)$ | Meia parÃ¡bola deitada |
| RecÃ­proca | $1/x$ | $\mathbb{R}^*$ | $\mathbb{R}^*$ | HipÃ©rbole |
| Exponencial | $a^x$ | $\mathbb{R}$ | $(0,+\infty)$ | Curva exponencial |
| LogarÃ­tmica | $\log_a x$ | $(0,+\infty)$ | $\mathbb{R}$ | Curva logarÃ­tmica |

### FÃ³rmulas da quadrÃ¡tica

$$V_x = -\frac{b}{2a} \qquad V_y = -\frac{\Delta}{4a} \qquad \Delta = b^2 - 4ac \qquad x = \frac{-b \pm \sqrt{\Delta}}{2a}$$

## Exemplos Resolvidos

**Exemplo 1 â€” BÃ¡sico: anÃ¡lise completa de uma funÃ§Ã£o afim**

> **Enunciado:** Para $f(x) = -2x + 4$, determine: coeficiente angular, coeficiente linear, raiz, intercepto com eixo $y$, sinal e esboÃ§o.

**Passo 1 â€” Identificar os parÃ¢metros $a$ e $b$.**

Comparar $f(x) = -2x + 4$ com a forma $ax + b$:

$$a = -2 \quad \text{(coeficiente angular)} \qquad b = 4 \quad \text{(coeficiente linear)}$$

**Passo 2 â€” Determinar o comportamento da reta.**

Como $a = -2 < 0$, a funÃ§Ã£o Ã© **estritamente decrescente** â€” a reta desce da esquerda para a direita.

**Passo 3 â€” Calcular a raiz (zero da funÃ§Ã£o).**

Fazer $f(x) = 0$ e isolar $x$:

$$-2x + 4 = 0 \implies -2x = -4 \implies x = \frac{-4}{-2} = 2$$

A raiz Ã© $x = 2$: o grÃ¡fico corta o eixo $x$ no ponto $(2, 0)$.

**Passo 4 â€” Calcular o intercepto com o eixo $y$.**

Fazer $x = 0$:

$$f(0) = -2 \cdot 0 + 4 = 4$$

O grÃ¡fico corta o eixo $y$ no ponto $(0, 4)$.

**Passo 5 â€” Determinar o sinal de $f$.**

Com dois pontos-chave: $(0, 4)$ e $(2, 0)$, e reta decrescente:

- Para $x < 2$: $f(x) > 0$ (reta estÃ¡ acima do eixo $x$)
- Para $x = 2$: $f(x) = 0$ (raiz)
- Para $x > 2$: $f(x) < 0$ (reta estÃ¡ abaixo do eixo $x$)

**Passo 6 â€” EsboÃ§o do grÃ¡fico.**

Dois pontos determinam uma reta. Usar os dois interceptos:

```
  y
  |
4 â€¢  â† (0, 4)
  |  \
  |    \
--+-----â€¢------ x
  0     2 â† raiz
         \
          \
```

> **Resumo:** reta decrescente, zero em $x=2$, intercepto em $y=4$; $f(x) > 0$ para $x \in (-\infty, 2)$ e $f(x) < 0$ para $x \in (2, +\infty)$.

---

**Exemplo 2 â€” IntermediÃ¡rio: classificar paridade de trÃªs funÃ§Ãµes**

> **Enunciado:** Classifique quanto Ã  paridade: $f(x) = x^4 - 3x^2$, $g(x) = x^3 - x$, $h(x) = x^2 + x$.

**MÃ©todo geral:** calcular $f(-x)$, simplificar, e comparar com $f(x)$ e $-f(x)$.

**â€” Para $f(x) = x^4 - 3x^2$ â€”**

**Passo 1 â€” Verificar simetria do domÃ­nio.** DomÃ­nio $= \mathbb{R}$, que Ã© simÃ©trico em relaÃ§Ã£o Ã  origem. âœ“

**Passo 2 â€” Calcular $f(-x)$.**

Substituir $x$ por $(-x)$ na fÃ³rmula. Cada potÃªncia Ã© afetada:

$$f(-x) = (-x)^4 - 3(-x)^2$$

Aplicar as potÃªncias: $(-x)^4 = x^4$ (expoente par) e $(-x)^2 = x^2$ (expoente par):

$$f(-x) = x^4 - 3x^2$$

**Passo 3 â€” Comparar com $f(x)$ e $-f(x)$.**

$$f(-x) = x^4 - 3x^2 = f(x) \checkmark$$

Como $f(-x) = f(x)$, a funÃ§Ã£o Ã© **par**. GrÃ¡fico simÃ©trico ao eixo $y$.

---

**â€” Para $g(x) = x^3 - x$ â€”**

**Passo 1 â€” DomÃ­nio:** $\mathbb{R}$, simÃ©trico. âœ“

**Passo 2 â€” Calcular $g(-x)$.**

$$g(-x) = (-x)^3 - (-x)$$

Aplicar as potÃªncias: $(-x)^3 = -x^3$ (expoente Ã­mpar):

$$g(-x) = -x^3 - (-x) = -x^3 + x$$

**Passo 3 â€” Fatorar para reconhecer o padrÃ£o.**

$$g(-x) = -(x^3 - x) = -g(x) \checkmark$$

Como $g(-x) = -g(x)$, a funÃ§Ã£o Ã© **Ã­mpar**. GrÃ¡fico simÃ©trico Ã  origem.

---

**â€” Para $h(x) = x^2 + x$ â€”**

**Passo 1 â€” DomÃ­nio:** $\mathbb{R}$, simÃ©trico. âœ“

**Passo 2 â€” Calcular $h(-x)$.**

$$h(-x) = (-x)^2 + (-x) = x^2 - x$$

**Passo 3 â€” Comparar com $h(x)$ e $-h(x)$.**

$$h(x) = x^2 + x \qquad -h(x) = -x^2 - x$$

$h(-x) = x^2 - x \neq x^2 + x = h(x)$ â†’ **nÃ£o Ã© par**

$h(-x) = x^2 - x \neq -x^2 - x = -h(x)$ â†’ **nÃ£o Ã© Ã­mpar**

A funÃ§Ã£o $h$ **nÃ£o Ã© nem par nem Ã­mpar**.

> **Resumo:** $f$: par | $g$: Ã­mpar | $h$: nem par nem Ã­mpar.

---

**Exemplo 3 â€” AvanÃ§ado: anÃ¡lise completa de uma funÃ§Ã£o quadrÃ¡tica**

> **Enunciado:** Para $f(x) = x^2 - 4x + 3$, determine: vÃ©rtice, concavidade, raÃ­zes, intervalos de monotonicidade, imagem e esboÃ§o.

**Passo 1 â€” Identificar $a$, $b$, $c$.**

Comparar com $ax^2 + bx + c$:

$$a = 1, \quad b = -4, \quad c = 3$$

Como $a = 1 > 0$: **concavidade para cima** (parÃ¡bola abre para cima, vÃ©rtice Ã© mÃ­nimo).

**Passo 2 â€” Calcular o discriminante $\Delta$.**

$$\Delta = b^2 - 4ac = (-4)^2 - 4 \cdot 1 \cdot 3 = 16 - 12 = 4$$

$\Delta = 4 > 0$ â†’ **duas raÃ­zes reais distintas**.

**Passo 3 â€” Calcular as raÃ­zes pela fÃ³rmula de Bhaskara.**

$$x = \frac{-b \pm \sqrt{\Delta}}{2a} = \frac{-(-4) \pm \sqrt{4}}{2 \cdot 1} = \frac{4 \pm 2}{2}$$

Separar em dois casos:

$$x_1 = \frac{4 + 2}{2} = \frac{6}{2} = 3 \qquad x_2 = \frac{4 - 2}{2} = \frac{2}{2} = 1$$

RaÃ­zes: $x_1 = 1$ e $x_2 = 3$.

**Passo 4 â€” Calcular o vÃ©rtice.**

A abscissa do vÃ©rtice usa as duas raÃ­zes: $V_x = \dfrac{x_1 + x_2}{2}$ (ponto mÃ©dio das raÃ­zes), ou pela fÃ³rmula direta:

$$V_x = -\frac{b}{2a} = -\frac{-4}{2} = 2$$

A ordenada Ã© obtida substituindo $V_x$ em $f$:

$$V_y = f(2) = (2)^2 - 4(2) + 3 = 4 - 8 + 3 = -1$$

VÃ©rtice: $V = (2, -1)$.

VerificaÃ§Ã£o pela fÃ³rmula: $V_y = -\dfrac{\Delta}{4a} = -\dfrac{4}{4} = -1$ âœ“

**Passo 5 â€” Determinar os intervalos de monotonicidade.**

Como a parÃ¡bola abre para cima com vÃ©rtice em $x = 2$:

- **Decrescente:** $(-\infty, 2]$ (Ã  esquerda do vÃ©rtice, $f$ decresce)
- **Crescente:** $[2, +\infty)$ (Ã  direita do vÃ©rtice, $f$ cresce)

**Passo 6 â€” Determinar a imagem.**

O valor mÃ­nimo de $f$ Ã© $V_y = -1$ (atingido em $x = 2$). Como a parÃ¡bola abre para cima e nÃ£o tem mÃ¡ximo:

$$\operatorname{Im}(f) = [-1, +\infty)$$

**Passo 7 â€” Calcular o intercepto com o eixo $y$.**

$$f(0) = 0 - 0 + 3 = 3 \implies \text{ponto } (0, 3)$$

**EsboÃ§o do grÃ¡fico:**

```
  y
  |
3 â€¢  â† (0,3)
  |   \         /
  |    \       /
--+--â€¢---V---â€¢-- x
  0   1   2   3
       â†‘   â†‘
      raÃ­zes  V=(2,-1)
         â†“
        -1
```

> **Resumo:** concavidade para cima; vÃ©rtice $(2,-1)$ mÃ­nimo; raÃ­zes $x = 1$ e $x = 3$; intercepto $(0, 3)$; decrescente em $(-\infty, 2]$, crescente em $[2,+\infty)$; imagem $[-1,+\infty)$.

## Armadilhas & Edge Cases

- **Confundir teste da reta vertical com o da reta horizontal** â€” reta vertical testa se Ã© **funÃ§Ã£o**; reta horizontal testa **injetividade** (nÃ£o confundir os dois critÃ©rios)
- **Achar que toda funÃ§Ã£o Ã© par ou Ã­mpar** â€” a maioria das funÃ§Ãµes nÃ£o Ã© nenhuma das duas; Ã© preciso calcular $f(-x)$ e verificar explicitamente
- **Expoente par/Ã­mpar nÃ£o implica paridade automaticamente** â€” $f(x) = x^2 + 1$ Ã© par, mas $f(x) = x^2 + x$ nÃ£o Ã©; o teste deve ser feito na funÃ§Ã£o inteira, nÃ£o em cada termo isolado
- **Confundir crescente com positiva** â€” uma funÃ§Ã£o pode ser crescente em um intervalo onde seus valores sÃ£o negativos (ex: $x^2 - 4$ cresce em $[2,+\infty)$ mas tem valores negativos perto de $x=2$)
- **Erro de sinal no vÃ©rtice** â€” $V_x = -\dfrac{b}{2a}$, nÃ£o $\dfrac{b}{2a}$; o sinal negativo Ã© frequentemente esquecido
- **AssÃ­ntota vertical do logaritmo** â€” $\log_a x$ tem assÃ­ntota em $x = 0$ (o eixo $y$); o grÃ¡fico nunca cruza o eixo $y$
- **$f^{-1}$ â‰  reflexÃ£o de $\dfrac{1}{f}$** â€” o grÃ¡fico de $f^{-1}$ Ã© a reflexÃ£o de $f$ em relaÃ§Ã£o a $y = x$; nÃ£o tem nada a ver com $1/f(x)$
- **TranslaÃ§Ã£o horizontal: sinal contrÃ¡rio ao esperado** â€” $f(x - 2)$ desloca o grÃ¡fico 2 unidades **para a direita** (nÃ£o para a esquerda); o sinal na fÃ³rmula Ã© oposto ao deslocamento

## ConexÃµes

- [[MatemÃ¡tica]] â€” MOC da Ã¡rea
- [[GraduaÃ§Ã£o em QuÃ­mica]] â€” Roadmap da graduaÃ§Ã£o
- [[FunÃ§Ãµes]] â€” prÃ©-requisito direto (definiÃ§Ã£o formal, domÃ­nio/imagem, classificaÃ§Ã£o, inversa)
- [[Conjuntos NumÃ©ricos]] â€” eixos cartesianos baseados em $\mathbb{R}$; intervalos usados na descriÃ§Ã£o de monotonicidade e imagem
- [[FunÃ§Ãµes TrigonomÃ©tricas]] â€” aplicaÃ§Ã£o do estudo de grÃ¡ficos Ã s funÃ§Ãµes sen, cos, tg
- [[Trigonometria na CircunferÃªncia]] â€” fornece os valores que definem as funÃ§Ãµes trigonomÃ©tricas
- [[FÃ­sica]] â€” grÃ¡ficos de posiÃ§Ã£o Ã— tempo, velocidade Ã— tempo; funÃ§Ãµes afim e quadrÃ¡tica em cinemÃ¡tica

## Fontes

- GUIDORIZZI, Hamilton Luiz. *Um Curso de CÃ¡lculo* â€” Vol. 1, Cap. 1: FunÃ§Ãµes. LTC.
