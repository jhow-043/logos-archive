---
title: Funções Trigonométricas
description: As funções trigonométricas ($\operatorname{sen}$, $\operatorname{cos}$,
  $\operatorname{tg}$ e suas recíprocas) são funções reais definidas a partir do ciclo
  tri
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: matematica
semestre: 1
---

# Funções Trigonométricas

> As funções trigonométricas ($\operatorname{sen}$, $\operatorname{cos}$, $\operatorname{tg}$ e suas recíprocas) são funções reais definidas a partir do ciclo trigonométrico, com periodicidade, simetria e comportamento gráfico característicos — base para o estudo de oscilações, ondas e Cálculo I.

---

## Definição

A partir do ciclo trigonométrico unitário (raio $= 1$, centro na origem), associa-se a cada número real $x$ (comprimento de arco orientado) um ponto $P = (\operatorname{cos} x,\, \operatorname{sen} x)$ na circunferência. Isso define:

$$\operatorname{sen}: \mathbb{R} \to [-1, 1] \qquad \operatorname{cos}: \mathbb{R} \to [-1, 1] \qquad \operatorname{tg}: \mathbb{R} \setminus \left\{\frac{\pi}{2} + k\pi,\, k \in \mathbb{Z}\right\} \to \mathbb{R}$$

A relação fundamental:

$$\operatorname{sen}^2 x + \operatorname{cos}^2 x = 1 \quad \text{para todo } x \in \mathbb{R}$$

## Teoria & Fundamentos

### Função seno — $f(x) = \operatorname{sen} x$

| Propriedade | Valor |
| ----------- | ----- |
| Domínio | $\mathbb{R}$ |
| Imagem | $[-1, 1]$ |
| Período | $T = 2\pi$ |
| Paridade | **Ímpar** — $\operatorname{sen}(-x) = -\operatorname{sen} x$ |
| Máximo | $\operatorname{sen} x = 1$ em $x = \dfrac{\pi}{2} + 2k\pi$ |
| Mínimo | $\operatorname{sen} x = -1$ em $x = -\dfrac{\pi}{2} + 2k\pi$ |
| Zeros | $x = k\pi$, $k \in \mathbb{Z}$ |
| Limitada | Sim: $|\operatorname{sen} x| \leq 1$ para todo $x \in \mathbb{R}$ |

**Monotonicidade em $[0, 2\pi]$:**

| Intervalo | Comportamento |
| --------- | ------------- |
| $\left[0, \dfrac{\pi}{2}\right]$ | Crescente ($0 \to 1$) |
| $\left[\dfrac{\pi}{2}, \dfrac{3\pi}{2}\right]$ | Decrescente ($1 \to -1$) |
| $\left[\dfrac{3\pi}{2}, 2\pi\right]$ | Crescente ($-1 \to 0$) |

**Valores notáveis (primeiro ciclo positivo):**

| $x$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\operatorname{sen} x$ | $0$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $1$ | $0$ | $-1$ | $0$ |

### Função cosseno — $f(x) = \operatorname{cos} x$

| Propriedade | Valor |
| ----------- | ----- |
| Domínio | $\mathbb{R}$ |
| Imagem | $[-1, 1]$ |
| Período | $T = 2\pi$ |
| Paridade | **Par** — $\operatorname{cos}(-x) = \operatorname{cos} x$ |
| Máximo | $\operatorname{cos} x = 1$ em $x = 2k\pi$ |
| Mínimo | $\operatorname{cos} x = -1$ em $x = \pi + 2k\pi$ |
| Zeros | $x = \dfrac{\pi}{2} + k\pi$, $k \in \mathbb{Z}$ |
| Limitada | Sim: $|\operatorname{cos} x| \leq 1$ para todo $x \in \mathbb{R}$ |

**Relação com o seno:** $\operatorname{cos} x = \operatorname{sen}\!\left(x + \dfrac{\pi}{2}\right)$  — o gráfico de $\operatorname{cos}$ é o de $\operatorname{sen}$ deslocado $\dfrac{\pi}{2}$ unidades **para a esquerda**.

**Valores notáveis:**

| $x$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\operatorname{cos} x$ | $1$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{1}{2}$ | $0$ | $-1$ | $0$ | $1$ |

### Função tangente — $f(x) = \operatorname{tg} x$

$$\operatorname{tg} x = \frac{\operatorname{sen} x}{\operatorname{cos} x}$$

| Propriedade | Valor |
| ----------- | ----- |
| Domínio | $\mathbb{R} \setminus \left\{\dfrac{\pi}{2} + k\pi,\, k \in \mathbb{Z}\right\}$ |
| Imagem | $\mathbb{R}$ |
| Período | $T = \pi$ (metade do período de sen e cos) |
| Paridade | **Ímpar** — $\operatorname{tg}(-x) = -\operatorname{tg} x$ |
| Zeros | $x = k\pi$, $k \in \mathbb{Z}$ |
| Assíntotas verticais | $x = \dfrac{\pi}{2} + k\pi$ (onde $\operatorname{cos} x = 0$) |
| Limitada | **Não** — imagem é $\mathbb{R}$ inteiro |

**Monotonicidade:** $\operatorname{tg} x$ é **estritamente crescente** em cada intervalo $\left(-\dfrac{\pi}{2} + k\pi,\, \dfrac{\pi}{2} + k\pi\right)$.

**Valores notáveis (em $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$):**

| $x$ | $-\dfrac{\pi}{3}$ | $-\dfrac{\pi}{4}$ | $-\dfrac{\pi}{6}$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $\operatorname{tg} x$ | $-\sqrt{3}$ | $-1$ | $-\dfrac{\sqrt{3}}{3}$ | $0$ | $\dfrac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ |

### Funções recíprocas

| Função | Fórmula | Domínio | Imagem | Período |
| ------ | ------- | ------- | ------ | ------- |
| Cotangente | $\operatorname{cotg} x = \dfrac{\operatorname{cos} x}{\operatorname{sen} x}$ | $\mathbb{R} \setminus \{k\pi\}$ | $\mathbb{R}$ | $\pi$ |
| Secante | $\sec x = \dfrac{1}{\operatorname{cos} x}$ | $\mathbb{R} \setminus \left\{\dfrac{\pi}{2} + k\pi\right\}$ | $(-\infty, -1] \cup [1, +\infty)$ | $2\pi$ |
| Cossecante | $\csc x = \dfrac{1}{\operatorname{sen} x}$ | $\mathbb{R} \setminus \{k\pi\}$ | $(-\infty, -1] \cup [1, +\infty)$ | $2\pi$ |

### Função sinusoidal geral

A forma geral de uma senóide é:

$$f(x) = A\operatorname{sen}(Bx + C) + D \qquad \text{ou} \qquad f(x) = A\operatorname{cos}(Bx + C) + D$$

| Parâmetro | Nome | Efeito no gráfico |
| --------- | ---- | ----------------- |
| $A$ | **Amplitude** | Escala vertical; imagem $= [D - |A|,\, D + |A|]$; se $A < 0$, reflexão em relação ao eixo central |
| $B$ | **Frequência angular** | Período $T = \dfrac{2\pi}{|B|}$; $|B| > 1$ comprime, $0 < |B| < 1$ dilata horizontalmente |
| $C$ | **Fase inicial** | Deslocamento horizontal de $-\dfrac{C}{B}$ unidades ($C > 0$: desloca para a esquerda) |
| $D$ | **Deslocamento vertical** | Move o eixo central para $y = D$; imagem deslocada de $[-1,1]$ para $[D-|A|, D+|A|]$ |

> **Eixo central:** a reta $y = D$ em torno da qual a senóide oscila (substitui o eixo $x$).

### Comparativo: seno × cosseno × tangente

| Propriedade | $\operatorname{sen} x$ | $\operatorname{cos} x$ | $\operatorname{tg} x$ |
| ----------- | ---------------------- | --------- | ---------------------- |
| Domínio | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R} \setminus \left\{\frac{\pi}{2}+k\pi\right\}$ |
| Imagem | $[-1, 1]$ | $[-1, 1]$ | $\mathbb{R}$ |
| Período | $2\pi$ | $2\pi$ | $\pi$ |
| Paridade | Ímpar | Par | Ímpar |
| Limitada | Sim | Sim | Não |
| Assíntotas | Nenhuma | Nenhuma | $x = \frac{\pi}{2}+k\pi$ |
| Zero em $x=0$ | $\operatorname{sen}(0)=0$ | $\operatorname{cos}(0)=1$ | $\operatorname{tg}(0)=0$ |

## Fórmulas & Equações

### Relações fundamentais

$$\operatorname{sen}^2 x + \operatorname{cos}^2 x = 1 \qquad 1 + \operatorname{tg}^2 x = \sec^2 x \qquad 1 + \operatorname{cotg}^2 x = \csc^2 x$$

### Período e amplitude (senóide geral)

$$T = \frac{2\pi}{|B|} \qquad \text{Amplitude} = |A| \qquad \text{Imagem} = [D - |A|,\; D + |A|]$$

$$\text{Deslocamento horizontal} = -\frac{C}{B} \qquad \text{Eixo central} = y = D$$

### Paridade das funções trigonométricas

$$\operatorname{sen}(-x) = -\operatorname{sen} x \qquad \operatorname{cos}(-x) = \operatorname{cos} x \qquad \operatorname{tg}(-x) = -\operatorname{tg} x$$

### Valores notáveis — quadro completo

| $x$ (rad) | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ |
| --- | --- | --- | --- | --- | --- |
| $\operatorname{sen}$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ |
| $\operatorname{cos}$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ |
| $\operatorname{tg}$ | $0$ | $\frac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ | indefinido |

## Exemplos Resolvidos

**Exemplo 1 — Básico: traçar $f(x) = \operatorname{sen} x$ em $[-2\pi, 2\pi]$**

> **Enunciado:** Use os valores notáveis para esboçar o gráfico de $f(x) = \operatorname{sen} x$ no intervalo $[-2\pi, 2\pi]$.

**Passo 1 — Identificar os parâmetros da senóide.**

Comparar com a forma $A\operatorname{sen}(Bx + C) + D$:

$$A = 1, \quad B = 1, \quad C = 0, \quad D = 0$$

Portanto: **amplitude** $= 1$, **período** $T = \dfrac{2\pi}{1} = 2\pi$, **eixo central** $= y = 0$, **sem deslocamento**.

**Passo 2 — Identificar os pontos-chave em $[0, 2\pi]$.**

Um ciclo completo tem 5 pontos-chave (início, máximo, meio, mínimo, fim), espaçados de $T/4 = \pi/2$:

| $x$ | $\operatorname{sen} x$ | Descrição |
| --- | --------- | --------- |
| $0$ | $0$ | Início (zero ascendente) |
| $\dfrac{\pi}{2}$ | $1$ | Máximo |
| $\pi$ | $0$ | Zero descendente |
| $\dfrac{3\pi}{2}$ | $-1$ | Mínimo |
| $2\pi$ | $0$ | Fim (zero ascendente) |

**Passo 3 — Usar a paridade para obter $[-2\pi, 0]$.**

Como $\operatorname{sen}$ é **ímpar**, $\operatorname{sen}(-x) = -\operatorname{sen} x$: o gráfico em $[-2\pi, 0]$ é o reflexo em relação à origem do trecho em $[0, 2\pi]$.

| $x$ | $\operatorname{sen} x$ |
| --- | --------- |
| $-2\pi$ | $0$ |
| $-\dfrac{3\pi}{2}$ | $1$ |
| $-\pi$ | $0$ |
| $-\dfrac{\pi}{2}$ | $-1$ |
| $0$ | $0$ |

**Passo 4 — Esboço (ASCII).**

```
  1 |    *           *           *
    |   * *         * *         * *
    |  *   *       *   *       *   *
    | *     *     *     *     *     *
  0 |*       *   *       *   *       *
    |         * *         * * 
 -1 |          *           *
    +---+---+---+---+---+---+---+---+--
      -2π  -π   0   π/2  π  3π/2  2π
```

> A curva é suave, contínua, ímpar (simétrica à origem), oscila entre $-1$ e $1$, cruzando o eixo $x$ em cada múltiplo inteiro de $\pi$.

---

**Exemplo 2 — Intermediário: amplitude e período de $f(x) = 3\operatorname{sen}(2x)$**

> **Enunciado:** Para $f(x) = 3\operatorname{sen}(2x)$, determine: amplitude, período, imagem, zeros e pontos de máximo e mínimo no intervalo $[0, 2\pi]$.

**Passo 1 — Identificar os parâmetros.**

Comparar com $A\operatorname{sen}(Bx + C) + D$:

$$A = 3, \quad B = 2, \quad C = 0, \quad D = 0$$

**Passo 2 — Calcular a amplitude.**

$$\text{Amplitude} = |A| = |3| = 3$$

O gráfico oscila entre $-3$ e $3$ (a altura máxima e mínima são triplicadas em relação ao $\operatorname{sen}$ básico).

**Passo 3 — Calcular o período.**

$$T = \frac{2\pi}{|B|} = \frac{2\pi}{2} = \pi$$

O período é **$\pi$** (metade do período de $\operatorname{sen} x$). Em $[0, 2\pi]$, o gráfico completa **dois ciclos**.

**Passo 4 — Determinar a imagem.**

$$\text{Imagem} = [D - |A|,\; D + |A|] = [0 - 3,\; 0 + 3] = [-3, 3]$$

**Passo 5 — Calcular os zeros.**

Os zeros ocorrem quando $\operatorname{sen}(2x) = 0$, ou seja, quando o argumento $2x$ é múltiplo de $\pi$:

$$2x = k\pi \implies x = \frac{k\pi}{2}, \quad k \in \mathbb{Z}$$

Em $[0, 2\pi]$: $x = 0,\; \dfrac{\pi}{2},\; \pi,\; \dfrac{3\pi}{2},\; 2\pi$.

**Passo 6 — Calcular máximos e mínimos.**

Máximo: $\operatorname{sen}(2x) = 1 \implies 2x = \dfrac{\pi}{2} + 2k\pi \implies x = \dfrac{\pi}{4} + k\pi$

Em $[0, 2\pi]$: máximos em $x = \dfrac{\pi}{4}$ (com $f = 3$) e $x = \dfrac{5\pi}{4}$ (com $f = 3$).

Mínimo: $\operatorname{sen}(2x) = -1 \implies 2x = \dfrac{3\pi}{2} + 2k\pi \implies x = \dfrac{3\pi}{4} + k\pi$

Em $[0, 2\pi]$: mínimos em $x = \dfrac{3\pi}{4}$ (com $f = -3$) e $x = \dfrac{7\pi}{4}$ (com $f = -3$).

**Verificação:** o ciclo de pontos-chave (espaçados de $T/4 = \pi/4$) no primeiro ciclo $[0, \pi]$:

| $x$ | $0$ | $\frac{\pi}{4}$ | $\frac{\pi}{2}$ | $\frac{3\pi}{4}$ | $\pi$ |
| --- | --- | --- | --- | --- | --- |
| $f(x)$ | $0$ | $3$ | $0$ | $-3$ | $0$ |

> **Resumo:** amplitude $= 3$, período $= \pi$, imagem $= [-3, 3]$, dois ciclos em $[0, 2\pi]$.

---

**Exemplo 3 — Avançado: análise completa de $f(x) = 2\operatorname{cos}\!\left(x - \dfrac{\pi}{3}\right) + 1$**

> **Enunciado:** Para $f(x) = 2\operatorname{cos}\!\left(x - \dfrac{\pi}{3}\right) + 1$, determine: amplitude, período, deslocamentos, eixo central, imagem, zeros (se existirem em $[0, 2\pi]$), máximos e mínimos. Esboçar.

**Passo 1 — Identificar os parâmetros.**

Comparar com $A\operatorname{cos}(Bx + C) + D$. Reescrever:

$$f(x) = 2\operatorname{cos}\!\left(1 \cdot x + \left(-\frac{\pi}{3}\right)\right) + 1$$

Portanto:

$$A = 2, \quad B = 1, \quad C = -\frac{\pi}{3}, \quad D = 1$$

**Passo 2 — Calcular a amplitude.**

$$\text{Amplitude} = |A| = |2| = 2$$

**Passo 3 — Calcular o período.**

$$T = \frac{2\pi}{|B|} = \frac{2\pi}{1} = 2\pi$$

**Passo 4 — Determinar o deslocamento horizontal (fase).**

$$\text{Deslocamento} = -\frac{C}{B} = -\frac{-\pi/3}{1} = +\frac{\pi}{3}$$

O gráfico de $\operatorname{cos} x$ é deslocado $\dfrac{\pi}{3}$ unidades **para a direita**. O máximo, que em $\operatorname{cos} x$ ocorre em $x = 0$, agora ocorre em $x = \dfrac{\pi}{3}$.

**Passo 5 — Determinar o deslocamento vertical e o eixo central.**

$$D = 1 \implies \text{eixo central: } y = 1$$

O gráfico oscila em torno de $y = 1$ (e não em torno de $y = 0$).

**Passo 6 — Calcular a imagem.**

$$\text{Imagem} = [D - |A|,\; D + |A|] = [1 - 2,\; 1 + 2] = [-1, 3]$$

**Passo 7 — Localizar os pontos-chave (um ciclo a partir de $x = \pi/3$).**

Os 5 pontos-chave estão espaçados de $T/4 = \pi/2$, começando no primeiro máximo ($x = \pi/3$):

| Ponto | $x$ | $f(x) = 2\operatorname{cos}\!\left(x - \frac{\pi}{3}\right) + 1$ | Descrição |
| ----- | --- | --- | --- |
| Máximo | $\dfrac{\pi}{3}$ | $2\operatorname{cos}(0) + 1 = 2 \cdot 1 + 1 = 3$ | Máximo |
| Zero descendente | $\dfrac{\pi}{3} + \dfrac{\pi}{2} = \dfrac{5\pi}{6}$ | $2\operatorname{cos}\!\left(\dfrac{\pi}{2}\right) + 1 = 0 + 1 = 1$ | Eixo central |
| Mínimo | $\dfrac{\pi}{3} + \pi = \dfrac{4\pi}{3}$ | $2\operatorname{cos}(\pi) + 1 = -2 + 1 = -1$ | Mínimo |
| Zero ascendente | $\dfrac{\pi}{3} + \dfrac{3\pi}{2} = \dfrac{11\pi}{6}$ | $2\operatorname{cos}\!\left(\dfrac{3\pi}{2}\right) + 1 = 0 + 1 = 1$ | Eixo central |
| Máximo | $\dfrac{\pi}{3} + 2\pi = \dfrac{7\pi}{3}$ | $2\operatorname{cos}(2\pi) + 1 = 2 + 1 = 3$ | Máximo (fim do ciclo) |

**Passo 8 — Determinar se $f$ tem zeros em $[0, 2\pi]$.**

Zeros ocorrem quando $f(x) = 0$:

$$2\operatorname{cos}\!\left(x - \frac{\pi}{3}\right) + 1 = 0 \implies \operatorname{cos}\!\left(x - \frac{\pi}{3}\right) = -\frac{1}{2}$$

O cosseno vale $-\dfrac{1}{2}$ em $\dfrac{2\pi}{3}$ e em $\dfrac{4\pi}{3}$ (dentro de $[0, 2\pi]$ para o argumento). Portanto:

$$x - \frac{\pi}{3} = \frac{2\pi}{3} \implies x = \pi \qquad \text{e} \qquad x - \frac{\pi}{3} = \frac{4\pi}{3} \implies x = \frac{5\pi}{3}$$

Verificação: $f(\pi) = 2\operatorname{cos}\!\left(\pi - \dfrac{\pi}{3}\right) + 1 = 2\operatorname{cos}\!\left(\dfrac{2\pi}{3}\right) + 1 = 2\!\left(-\dfrac{1}{2}\right) + 1 = -1 + 1 = 0$ ✓

Zeros em $[0, 2\pi]$: $x = \pi$ e $x = \dfrac{5\pi}{3}$.

**Esboço:**

```
  y
  3 |      *                      *
    |    *   *                  *   *
    |  *       *              *       *
  1 |*           *          *           *
    |              *      *
  0 |               *    *
    +--+----+----+---*--*---+----+------ x
       π/3 5π/6  π  4π/3  5π/3 11π/6
 -1 |              mínimo
```

> **Resumo:** amplitude $= 2$, período $= 2\pi$, deslocamento $\pi/3$ à direita, eixo central $y = 1$, imagem $[-1, 3]$, máximo $3$ em $x = \pi/3$, mínimo $-1$ em $x = 4\pi/3$, zeros em $x = \pi$ e $x = 5\pi/3$.

## Armadilhas & Edge Cases

- **Confundir o período de $\operatorname{tg}$ com o de $\operatorname{sen}$/$\operatorname{cos}$** — tangente tem período $\pi$, metade do período do seno e cosseno; um erro comum é afirmar que tg tem período $2\pi$
- **Esquecer as assíntotas da tangente** — $\operatorname{tg} x$ não está definida em $x = \pi/2 + k\pi$; o gráfico não "atravessa" esses pontos — há uma descontinuidade essencial
- **Sinal errado na translação horizontal** — em $\operatorname{sen}(x - C)$, o gráfico desloca $C$ unidades **para a direita** (não para a esquerda); o sinal na fórmula é oposto ao deslocamento geométrico
- **Amplitude é $|A|$, não $A$** — se $A = -3$, a amplitude ainda é $3$; o sinal negativo causa reflexão vertical, mas não reduz a amplitude
- **Confundir imagem das recíprocas com $[-1,1]$** — $\sec x$ e $\csc x$ têm imagem $(-\infty,-1] \cup [1,+\infty)$, ou seja, **excluem** o intervalo $(-1, 1)$ (ao contrário de sen e cos)
- **Argumento sempre em radianos** — ao substituir valores, usar $x$ em radianos; $\operatorname{sen}(90) \neq 1$ (em radianos, $\operatorname{sen}(90) \approx 0{,}894$); o $1$ corresponde a $\operatorname{sen}(\pi/2)$
- **Periodicidade não implica limitação** — $\operatorname{tg} x$ é periódica mas **não é limitada**; periódica e limitada são propriedades independentes
- **$\operatorname{cos} x$ é par, mas $\operatorname{sen} x$ e $\operatorname{tg} x$ são ímpares** — confundir a paridade leva a erros nos cálculos de ângulos negativos

## Conexões

- [[Matemática]] — MOC da área
- [[Graduação em Química]] — Roadmap da graduação
- [[Trigonometria na Circunferência]] — pré-requisito direto: definição das funções via ciclo trigonométrico, quadrantes, valores notáveis, relações fundamentais
- [[Funções e Gráficos]] — pré-requisito direto: framework de análise gráfica (leitura, paridade, monotonicidade, transformações), aplicado aqui às funções trigonométricas
- [[Funções]] — pré-requisito: conceito de função, domínio máximo, periodicidade como propriedade geral
- [[Conjuntos Numéricos]] — domínio e imagem descritos em termos de intervalos reais ($[-1,1]$, $\mathbb{R}$, etc.)
- [[Limites]] — próximo tópico: o limite fundamental $\displaystyle\lim_{x \to 0} \frac{\operatorname{sen} x}{x} = 1$ conecta diretamente funções trigonométricas ao cálculo
- [[Física]] — oscilações (MHS: $x(t) = A\operatorname{sen}(\omega t + \varphi)$), ondas mecânicas e eletromagnéticas, circuitos AC

## Fontes

- GUIDORIZZI, Hamilton Luiz. *Um Curso de Cálculo* — Vol. 1, Cap. 1: Funções. LTC.
- IEZZI, Gelson; MURAKAMI, Carlos. *Fundamentos de Matemática Elementar* — Vol. 3: Trigonometria. Atual Editora. (referência cruzada para valores notáveis e identidades)
