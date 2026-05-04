---
title: FunÃ§Ãµes TrigonomÃ©tricas
description: As funÃ§Ãµes trigonomÃ©tricas ($\operatorname{sen}$, $\operatorname{cos}$,
  $\operatorname{tg}$ e suas recÃ­procas) sÃ£o funÃ§Ãµes reais definidas a partir
  do ci…
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: matematica
semestre: 1
---
# FunÃ§Ãµes TrigonomÃ©tricas

> As funÃ§Ãµes trigonomÃ©tricas ($\operatorname{sen}$, $\operatorname{cos}$, $\operatorname{tg}$ e suas recÃ­procas) sÃ£o funÃ§Ãµes reais definidas a partir do ciclo trigonomÃ©trico, com periodicidade, simetria e comportamento grÃ¡fico caracterÃ­sticos â€” base para o estudo de oscilaÃ§Ãµes, ondas e CÃ¡lculo I.

---

## DefiniÃ§Ã£o

A partir do ciclo trigonomÃ©trico unitÃ¡rio (raio $= 1$, centro na origem), associa-se a cada nÃºmero real $x$ (comprimento de arco orientado) um ponto $P = (\operatorname{cos} x,\, \operatorname{sen} x)$ na circunferÃªncia. Isso define:

$$\operatorname{sen}: \mathbb{R} \to [-1, 1] \qquad \operatorname{cos}: \mathbb{R} \to [-1, 1] \qquad \operatorname{tg}: \mathbb{R} \setminus \left\{\frac{\pi}{2} + k\pi,\, k \in \mathbb{Z}\right\} \to \mathbb{R}$$

A relaÃ§Ã£o fundamental:

$$\operatorname{sen}^2 x + \operatorname{cos}^2 x = 1 \quad \text{para todo } x \in \mathbb{R}$$

## Teoria & Fundamentos

### FunÃ§Ã£o seno â€” $f(x) = \operatorname{sen} x$

| Propriedade | Valor |
| ----------- | ----- |
| DomÃ­nio | $\mathbb{R}$ |
| Imagem | $[-1, 1]$ |
| PerÃ­odo | $T = 2\pi$ |
| Paridade | **Ãmpar** â€” $\operatorname{sen}(-x) = -\operatorname{sen} x$ |
| MÃ¡ximo | $\operatorname{sen} x = 1$ em $x = \dfrac{\pi}{2} + 2k\pi$ |
| MÃ­nimo | $\operatorname{sen} x = -1$ em $x = -\dfrac{\pi}{2} + 2k\pi$ |
| Zeros | $x = k\pi$, $k \in \mathbb{Z}$ |
| Limitada | Sim: $|\operatorname{sen} x| \leq 1$ para todo $x \in \mathbb{R}$ |

**Monotonicidade em $[0, 2\pi]$:**

| Intervalo | Comportamento |
| --------- | ------------- |
| $\left[0, \dfrac{\pi}{2}\right]$ | Crescente ($0 \to 1$) |
| $\left[\dfrac{\pi}{2}, \dfrac{3\pi}{2}\right]$ | Decrescente ($1 \to -1$) |
| $\left[\dfrac{3\pi}{2}, 2\pi\right]$ | Crescente ($-1 \to 0$) |

**Valores notÃ¡veis (primeiro ciclo positivo):**

| $x$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\operatorname{sen} x$ | $0$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $1$ | $0$ | $-1$ | $0$ |

### FunÃ§Ã£o cosseno â€” $f(x) = \operatorname{cos} x$

| Propriedade | Valor |
| ----------- | ----- |
| DomÃ­nio | $\mathbb{R}$ |
| Imagem | $[-1, 1]$ |
| PerÃ­odo | $T = 2\pi$ |
| Paridade | **Par** â€” $\operatorname{cos}(-x) = \operatorname{cos} x$ |
| MÃ¡ximo | $\operatorname{cos} x = 1$ em $x = 2k\pi$ |
| MÃ­nimo | $\operatorname{cos} x = -1$ em $x = \pi + 2k\pi$ |
| Zeros | $x = \dfrac{\pi}{2} + k\pi$, $k \in \mathbb{Z}$ |
| Limitada | Sim: $|\operatorname{cos} x| \leq 1$ para todo $x \in \mathbb{R}$ |

**RelaÃ§Ã£o com o seno:** $\operatorname{cos} x = \operatorname{sen}\!\left(x + \dfrac{\pi}{2}\right)$  â€” o grÃ¡fico de $\operatorname{cos}$ Ã© o de $\operatorname{sen}$ deslocado $\dfrac{\pi}{2}$ unidades **para a esquerda**.

**Valores notÃ¡veis:**

| $x$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\operatorname{cos} x$ | $1$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{1}{2}$ | $0$ | $-1$ | $0$ | $1$ |

### FunÃ§Ã£o tangente â€” $f(x) = \operatorname{tg} x$

$$\operatorname{tg} x = \frac{\operatorname{sen} x}{\operatorname{cos} x}$$

| Propriedade | Valor |
| ----------- | ----- |
| DomÃ­nio | $\mathbb{R} \setminus \left\{\dfrac{\pi}{2} + k\pi,\, k \in \mathbb{Z}\right\}$ |
| Imagem | $\mathbb{R}$ |
| PerÃ­odo | $T = \pi$ (metade do perÃ­odo de sen e cos) |
| Paridade | **Ãmpar** â€” $\operatorname{tg}(-x) = -\operatorname{tg} x$ |
| Zeros | $x = k\pi$, $k \in \mathbb{Z}$ |
| AssÃ­ntotas verticais | $x = \dfrac{\pi}{2} + k\pi$ (onde $\operatorname{cos} x = 0$) |
| Limitada | **NÃ£o** â€” imagem Ã© $\mathbb{R}$ inteiro |

**Monotonicidade:** $\operatorname{tg} x$ Ã© **estritamente crescente** em cada intervalo $\left(-\dfrac{\pi}{2} + k\pi,\, \dfrac{\pi}{2} + k\pi\right)$.

**Valores notÃ¡veis (em $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$):**

| $x$ | $-\dfrac{\pi}{3}$ | $-\dfrac{\pi}{4}$ | $-\dfrac{\pi}{6}$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $\operatorname{tg} x$ | $-\sqrt{3}$ | $-1$ | $-\dfrac{\sqrt{3}}{3}$ | $0$ | $\dfrac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ |

### FunÃ§Ãµes recÃ­procas

| FunÃ§Ã£o | FÃ³rmula | DomÃ­nio | Imagem | PerÃ­odo |
| ------ | ------- | ------- | ------ | ------- |
| Cotangente | $\operatorname{cotg} x = \dfrac{\operatorname{cos} x}{\operatorname{sen} x}$ | $\mathbb{R} \setminus \{k\pi\}$ | $\mathbb{R}$ | $\pi$ |
| Secante | $\sec x = \dfrac{1}{\operatorname{cos} x}$ | $\mathbb{R} \setminus \left\{\dfrac{\pi}{2} + k\pi\right\}$ | $(-\infty, -1] \cup [1, +\infty)$ | $2\pi$ |
| Cossecante | $\csc x = \dfrac{1}{\operatorname{sen} x}$ | $\mathbb{R} \setminus \{k\pi\}$ | $(-\infty, -1] \cup [1, +\infty)$ | $2\pi$ |

### FunÃ§Ã£o sinusoidal geral

A forma geral de uma senÃ³ide Ã©:

$$f(x) = A\operatorname{sen}(Bx + C) + D \qquad \text{ou} \qquad f(x) = A\operatorname{cos}(Bx + C) + D$$

| ParÃ¢metro | Nome | Efeito no grÃ¡fico |
| --------- | ---- | ----------------- |
| $A$ | **Amplitude** | Escala vertical; imagem $= [D - |A|,\, D + |A|]$; se $A < 0$, reflexÃ£o em relaÃ§Ã£o ao eixo central |
| $B$ | **FrequÃªncia angular** | PerÃ­odo $T = \dfrac{2\pi}{|B|}$; $|B| > 1$ comprime, $0 < |B| < 1$ dilata horizontalmente |
| $C$ | **Fase inicial** | Deslocamento horizontal de $-\dfrac{C}{B}$ unidades ($C > 0$: desloca para a esquerda) |
| $D$ | **Deslocamento vertical** | Move o eixo central para $y = D$; imagem deslocada de $[-1,1]$ para $[D-|A|, D+|A|]$ |

> **Eixo central:** a reta $y = D$ em torno da qual a senÃ³ide oscila (substitui o eixo $x$).

### Comparativo: seno Ã— cosseno Ã— tangente

| Propriedade | $\operatorname{sen} x$ | $\operatorname{cos} x$ | $\operatorname{tg} x$ |
| ----------- | ---------------------- | --------- | ---------------------- |
| DomÃ­nio | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R} \setminus \left\{\frac{\pi}{2}+k\pi\right\}$ |
| Imagem | $[-1, 1]$ | $[-1, 1]$ | $\mathbb{R}$ |
| PerÃ­odo | $2\pi$ | $2\pi$ | $\pi$ |
| Paridade | Ãmpar | Par | Ãmpar |
| Limitada | Sim | Sim | NÃ£o |
| AssÃ­ntotas | Nenhuma | Nenhuma | $x = \frac{\pi}{2}+k\pi$ |
| Zero em $x=0$ | $\operatorname{sen}(0)=0$ | $\operatorname{cos}(0)=1$ | $\operatorname{tg}(0)=0$ |

## FÃ³rmulas & EquaÃ§Ãµes

### RelaÃ§Ãµes fundamentais

$$\operatorname{sen}^2 x + \operatorname{cos}^2 x = 1 \qquad 1 + \operatorname{tg}^2 x = \sec^2 x \qquad 1 + \operatorname{cotg}^2 x = \csc^2 x$$

### PerÃ­odo e amplitude (senÃ³ide geral)

$$T = \frac{2\pi}{|B|} \qquad \text{Amplitude} = |A| \qquad \text{Imagem} = [D - |A|,\; D + |A|]$$

$$\text{Deslocamento horizontal} = -\frac{C}{B} \qquad \text{Eixo central} = y = D$$

### Paridade das funÃ§Ãµes trigonomÃ©tricas

$$\operatorname{sen}(-x) = -\operatorname{sen} x \qquad \operatorname{cos}(-x) = \operatorname{cos} x \qquad \operatorname{tg}(-x) = -\operatorname{tg} x$$

### Valores notÃ¡veis â€” quadro completo

| $x$ (rad) | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ |
| --- | --- | --- | --- | --- | --- |
| $\operatorname{sen}$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ |
| $\operatorname{cos}$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ |
| $\operatorname{tg}$ | $0$ | $\frac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ | indefinido |

## Exemplos Resolvidos

**Exemplo 1 â€” BÃ¡sico: traÃ§ar $f(x) = \operatorname{sen} x$ em $[-2\pi, 2\pi]$**

> **Enunciado:** Use os valores notÃ¡veis para esboÃ§ar o grÃ¡fico de $f(x) = \operatorname{sen} x$ no intervalo $[-2\pi, 2\pi]$.

**Passo 1 â€” Identificar os parÃ¢metros da senÃ³ide.**

Comparar com a forma $A\operatorname{sen}(Bx + C) + D$:

$$A = 1, \quad B = 1, \quad C = 0, \quad D = 0$$

Portanto: **amplitude** $= 1$, **perÃ­odo** $T = \dfrac{2\pi}{1} = 2\pi$, **eixo central** $= y = 0$, **sem deslocamento**.

**Passo 2 â€” Identificar os pontos-chave em $[0, 2\pi]$.**

Um ciclo completo tem 5 pontos-chave (inÃ­cio, mÃ¡ximo, meio, mÃ­nimo, fim), espaÃ§ados de $T/4 = \pi/2$:

| $x$ | $\operatorname{sen} x$ | DescriÃ§Ã£o |
| --- | --------- | --------- |
| $0$ | $0$ | InÃ­cio (zero ascendente) |
| $\dfrac{\pi}{2}$ | $1$ | MÃ¡ximo |
| $\pi$ | $0$ | Zero descendente |
| $\dfrac{3\pi}{2}$ | $-1$ | MÃ­nimo |
| $2\pi$ | $0$ | Fim (zero ascendente) |

**Passo 3 â€” Usar a paridade para obter $[-2\pi, 0]$.**

Como $\operatorname{sen}$ Ã© **Ã­mpar**, $\operatorname{sen}(-x) = -\operatorname{sen} x$: o grÃ¡fico em $[-2\pi, 0]$ Ã© o reflexo em relaÃ§Ã£o Ã  origem do trecho em $[0, 2\pi]$.

| $x$ | $\operatorname{sen} x$ |
| --- | --------- |
| $-2\pi$ | $0$ |
| $-\dfrac{3\pi}{2}$ | $1$ |
| $-\pi$ | $0$ |
| $-\dfrac{\pi}{2}$ | $-1$ |
| $0$ | $0$ |

**Passo 4 â€” EsboÃ§o (ASCII).**

```
  1 |    *           *           *
    |   * *         * *         * *
    |  *   *       *   *       *   *
    | *     *     *     *     *     *
  0 |*       *   *       *   *       *
    |         * *         * * 
 -1 |          *           *
    +---+---+---+---+---+---+---+---+--
      -2Ï€  -Ï€   0   Ï€/2  Ï€  3Ï€/2  2Ï€
```

> A curva Ã© suave, contÃ­nua, Ã­mpar (simÃ©trica Ã  origem), oscila entre $-1$ e $1$, cruzando o eixo $x$ em cada mÃºltiplo inteiro de $\pi$.

---

**Exemplo 2 â€” IntermediÃ¡rio: amplitude e perÃ­odo de $f(x) = 3\operatorname{sen}(2x)$**

> **Enunciado:** Para $f(x) = 3\operatorname{sen}(2x)$, determine: amplitude, perÃ­odo, imagem, zeros e pontos de mÃ¡ximo e mÃ­nimo no intervalo $[0, 2\pi]$.

**Passo 1 â€” Identificar os parÃ¢metros.**

Comparar com $A\operatorname{sen}(Bx + C) + D$:

$$A = 3, \quad B = 2, \quad C = 0, \quad D = 0$$

**Passo 2 â€” Calcular a amplitude.**

$$\text{Amplitude} = |A| = |3| = 3$$

O grÃ¡fico oscila entre $-3$ e $3$ (a altura mÃ¡xima e mÃ­nima sÃ£o triplicadas em relaÃ§Ã£o ao $\operatorname{sen}$ bÃ¡sico).

**Passo 3 â€” Calcular o perÃ­odo.**

$$T = \frac{2\pi}{|B|} = \frac{2\pi}{2} = \pi$$

O perÃ­odo Ã© **$\pi$** (metade do perÃ­odo de $\operatorname{sen} x$). Em $[0, 2\pi]$, o grÃ¡fico completa **dois ciclos**.

**Passo 4 â€” Determinar a imagem.**

$$\text{Imagem} = [D - |A|,\; D + |A|] = [0 - 3,\; 0 + 3] = [-3, 3]$$

**Passo 5 â€” Calcular os zeros.**

Os zeros ocorrem quando $\operatorname{sen}(2x) = 0$, ou seja, quando o argumento $2x$ Ã© mÃºltiplo de $\pi$:

$$2x = k\pi \implies x = \frac{k\pi}{2}, \quad k \in \mathbb{Z}$$

Em $[0, 2\pi]$: $x = 0,\; \dfrac{\pi}{2},\; \pi,\; \dfrac{3\pi}{2},\; 2\pi$.

**Passo 6 â€” Calcular mÃ¡ximos e mÃ­nimos.**

MÃ¡ximo: $\operatorname{sen}(2x) = 1 \implies 2x = \dfrac{\pi}{2} + 2k\pi \implies x = \dfrac{\pi}{4} + k\pi$

Em $[0, 2\pi]$: mÃ¡ximos em $x = \dfrac{\pi}{4}$ (com $f = 3$) e $x = \dfrac{5\pi}{4}$ (com $f = 3$).

MÃ­nimo: $\operatorname{sen}(2x) = -1 \implies 2x = \dfrac{3\pi}{2} + 2k\pi \implies x = \dfrac{3\pi}{4} + k\pi$

Em $[0, 2\pi]$: mÃ­nimos em $x = \dfrac{3\pi}{4}$ (com $f = -3$) e $x = \dfrac{7\pi}{4}$ (com $f = -3$).

**VerificaÃ§Ã£o:** o ciclo de pontos-chave (espaÃ§ados de $T/4 = \pi/4$) no primeiro ciclo $[0, \pi]$:

| $x$ | $0$ | $\frac{\pi}{4}$ | $\frac{\pi}{2}$ | $\frac{3\pi}{4}$ | $\pi$ |
| --- | --- | --- | --- | --- | --- |
| $f(x)$ | $0$ | $3$ | $0$ | $-3$ | $0$ |

> **Resumo:** amplitude $= 3$, perÃ­odo $= \pi$, imagem $= [-3, 3]$, dois ciclos em $[0, 2\pi]$.

---

**Exemplo 3 â€” AvanÃ§ado: anÃ¡lise completa de $f(x) = 2\operatorname{cos}\!\left(x - \dfrac{\pi}{3}\right) + 1$**

> **Enunciado:** Para $f(x) = 2\operatorname{cos}\!\left(x - \dfrac{\pi}{3}\right) + 1$, determine: amplitude, perÃ­odo, deslocamentos, eixo central, imagem, zeros (se existirem em $[0, 2\pi]$), mÃ¡ximos e mÃ­nimos. EsboÃ§ar.

**Passo 1 â€” Identificar os parÃ¢metros.**

Comparar com $A\operatorname{cos}(Bx + C) + D$. Reescrever:

$$f(x) = 2\operatorname{cos}\!\left(1 \cdot x + \left(-\frac{\pi}{3}\right)\right) + 1$$

Portanto:

$$A = 2, \quad B = 1, \quad C = -\frac{\pi}{3}, \quad D = 1$$

**Passo 2 â€” Calcular a amplitude.**

$$\text{Amplitude} = |A| = |2| = 2$$

**Passo 3 â€” Calcular o perÃ­odo.**

$$T = \frac{2\pi}{|B|} = \frac{2\pi}{1} = 2\pi$$

**Passo 4 â€” Determinar o deslocamento horizontal (fase).**

$$\text{Deslocamento} = -\frac{C}{B} = -\frac{-\pi/3}{1} = +\frac{\pi}{3}$$

O grÃ¡fico de $\operatorname{cos} x$ Ã© deslocado $\dfrac{\pi}{3}$ unidades **para a direita**. O mÃ¡ximo, que em $\operatorname{cos} x$ ocorre em $x = 0$, agora ocorre em $x = \dfrac{\pi}{3}$.

**Passo 5 â€” Determinar o deslocamento vertical e o eixo central.**

$$D = 1 \implies \text{eixo central: } y = 1$$

O grÃ¡fico oscila em torno de $y = 1$ (e nÃ£o em torno de $y = 0$).

**Passo 6 â€” Calcular a imagem.**

$$\text{Imagem} = [D - |A|,\; D + |A|] = [1 - 2,\; 1 + 2] = [-1, 3]$$

**Passo 7 â€” Localizar os pontos-chave (um ciclo a partir de $x = \pi/3$).**

Os 5 pontos-chave estÃ£o espaÃ§ados de $T/4 = \pi/2$, comeÃ§ando no primeiro mÃ¡ximo ($x = \pi/3$):

| Ponto | $x$ | $f(x) = 2\operatorname{cos}\!\left(x - \frac{\pi}{3}\right) + 1$ | DescriÃ§Ã£o |
| ----- | --- | --- | --- |
| MÃ¡ximo | $\dfrac{\pi}{3}$ | $2\operatorname{cos}(0) + 1 = 2 \cdot 1 + 1 = 3$ | MÃ¡ximo |
| Zero descendente | $\dfrac{\pi}{3} + \dfrac{\pi}{2} = \dfrac{5\pi}{6}$ | $2\operatorname{cos}\!\left(\dfrac{\pi}{2}\right) + 1 = 0 + 1 = 1$ | Eixo central |
| MÃ­nimo | $\dfrac{\pi}{3} + \pi = \dfrac{4\pi}{3}$ | $2\operatorname{cos}(\pi) + 1 = -2 + 1 = -1$ | MÃ­nimo |
| Zero ascendente | $\dfrac{\pi}{3} + \dfrac{3\pi}{2} = \dfrac{11\pi}{6}$ | $2\operatorname{cos}\!\left(\dfrac{3\pi}{2}\right) + 1 = 0 + 1 = 1$ | Eixo central |
| MÃ¡ximo | $\dfrac{\pi}{3} + 2\pi = \dfrac{7\pi}{3}$ | $2\operatorname{cos}(2\pi) + 1 = 2 + 1 = 3$ | MÃ¡ximo (fim do ciclo) |

**Passo 8 â€” Determinar se $f$ tem zeros em $[0, 2\pi]$.**

Zeros ocorrem quando $f(x) = 0$:

$$2\operatorname{cos}\!\left(x - \frac{\pi}{3}\right) + 1 = 0 \implies \operatorname{cos}\!\left(x - \frac{\pi}{3}\right) = -\frac{1}{2}$$

O cosseno vale $-\dfrac{1}{2}$ em $\dfrac{2\pi}{3}$ e em $\dfrac{4\pi}{3}$ (dentro de $[0, 2\pi]$ para o argumento). Portanto:

$$x - \frac{\pi}{3} = \frac{2\pi}{3} \implies x = \pi \qquad \text{e} \qquad x - \frac{\pi}{3} = \frac{4\pi}{3} \implies x = \frac{5\pi}{3}$$

VerificaÃ§Ã£o: $f(\pi) = 2\operatorname{cos}\!\left(\pi - \dfrac{\pi}{3}\right) + 1 = 2\operatorname{cos}\!\left(\dfrac{2\pi}{3}\right) + 1 = 2\!\left(-\dfrac{1}{2}\right) + 1 = -1 + 1 = 0$ âœ“

Zeros em $[0, 2\pi]$: $x = \pi$ e $x = \dfrac{5\pi}{3}$.

**EsboÃ§o:**

```
  y
  3 |      *                      *
    |    *   *                  *   *
    |  *       *              *       *
  1 |*           *          *           *
    |              *      *
  0 |               *    *
    +--+----+----+---*--*---+----+------ x
       Ï€/3 5Ï€/6  Ï€  4Ï€/3  5Ï€/3 11Ï€/6
 -1 |              mÃ­nimo
```

> **Resumo:** amplitude $= 2$, perÃ­odo $= 2\pi$, deslocamento $\pi/3$ Ã  direita, eixo central $y = 1$, imagem $[-1, 3]$, mÃ¡ximo $3$ em $x = \pi/3$, mÃ­nimo $-1$ em $x = 4\pi/3$, zeros em $x = \pi$ e $x = 5\pi/3$.

## Armadilhas & Edge Cases

- **Confundir o perÃ­odo de $\operatorname{tg}$ com o de $\operatorname{sen}$/$\operatorname{cos}$** â€” tangente tem perÃ­odo $\pi$, metade do perÃ­odo do seno e cosseno; um erro comum Ã© afirmar que tg tem perÃ­odo $2\pi$
- **Esquecer as assÃ­ntotas da tangente** â€” $\operatorname{tg} x$ nÃ£o estÃ¡ definida em $x = \pi/2 + k\pi$; o grÃ¡fico nÃ£o "atravessa" esses pontos â€” hÃ¡ uma descontinuidade essencial
- **Sinal errado na translaÃ§Ã£o horizontal** â€” em $\operatorname{sen}(x - C)$, o grÃ¡fico desloca $C$ unidades **para a direita** (nÃ£o para a esquerda); o sinal na fÃ³rmula Ã© oposto ao deslocamento geomÃ©trico
- **Amplitude Ã© $|A|$, nÃ£o $A$** â€” se $A = -3$, a amplitude ainda Ã© $3$; o sinal negativo causa reflexÃ£o vertical, mas nÃ£o reduz a amplitude
- **Confundir imagem das recÃ­procas com $[-1,1]$** â€” $\sec x$ e $\csc x$ tÃªm imagem $(-\infty,-1] \cup [1,+\infty)$, ou seja, **excluem** o intervalo $(-1, 1)$ (ao contrÃ¡rio de sen e cos)
- **Argumento sempre em radianos** â€” ao substituir valores, usar $x$ em radianos; $\operatorname{sen}(90) \neq 1$ (em radianos, $\operatorname{sen}(90) \approx 0{,}894$); o $1$ corresponde a $\operatorname{sen}(\pi/2)$
- **Periodicidade nÃ£o implica limitaÃ§Ã£o** â€” $\operatorname{tg} x$ Ã© periÃ³dica mas **nÃ£o Ã© limitada**; periÃ³dica e limitada sÃ£o propriedades independentes
- **$\operatorname{cos} x$ Ã© par, mas $\operatorname{sen} x$ e $\operatorname{tg} x$ sÃ£o Ã­mpares** â€” confundir a paridade leva a erros nos cÃ¡lculos de Ã¢ngulos negativos

## ConexÃµes

- [[MatemÃ¡tica]] â€” MOC da Ã¡rea
- [[GraduaÃ§Ã£o em QuÃ­mica]] â€” Roadmap da graduaÃ§Ã£o
- [[Trigonometria na CircunferÃªncia]] â€” prÃ©-requisito direto: definiÃ§Ã£o das funÃ§Ãµes via ciclo trigonomÃ©trico, quadrantes, valores notÃ¡veis, relaÃ§Ãµes fundamentais
- [[FunÃ§Ãµes e GrÃ¡ficos]] â€” prÃ©-requisito direto: framework de anÃ¡lise grÃ¡fica (leitura, paridade, monotonicidade, transformaÃ§Ãµes), aplicado aqui Ã s funÃ§Ãµes trigonomÃ©tricas
- [[FunÃ§Ãµes]] â€” prÃ©-requisito: conceito de funÃ§Ã£o, domÃ­nio mÃ¡ximo, periodicidade como propriedade geral
- [[Conjuntos NumÃ©ricos]] â€” domÃ­nio e imagem descritos em termos de intervalos reais ($[-1,1]$, $\mathbb{R}$, etc.)
- [[Limites]] â€” prÃ³ximo tÃ³pico: o limite fundamental $\displaystyle\lim_{x \to 0} \frac{\operatorname{sen} x}{x} = 1$ conecta diretamente funÃ§Ãµes trigonomÃ©tricas ao cÃ¡lculo
- [[FÃ­sica]] â€” oscilaÃ§Ãµes (MHS: $x(t) = A\operatorname{sen}(\omega t + \varphi)$), ondas mecÃ¢nicas e eletromagnÃ©ticas, circuitos AC

## Fontes

- GUIDORIZZI, Hamilton Luiz. *Um Curso de CÃ¡lculo* â€” Vol. 1, Cap. 1: FunÃ§Ãµes. LTC.
- IEZZI, Gelson; MURAKAMI, Carlos. *Fundamentos de MatemÃ¡tica Elementar* â€” Vol. 3: Trigonometria. Atual Editora. (referÃªncia cruzada para valores notÃ¡veis e identidades)
