---
title: Funções e Gráficos
description: Representação visual de funções no plano cartesiano, propriedades geométricas
  (paridade, monotonicidade, limitação), funções elementares e transformações de grá
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: matematica
semestre: 1
---

# Funções e Gráficos

> Representação visual de funções no plano cartesiano, propriedades geométricas (paridade, monotonicidade, limitação), funções elementares e transformações de gráficos.

---

## Definição

O **gráfico** de uma função $f: A \to B$ é o conjunto de todos os pares ordenados $(x, f(x))$:

$$G(f) = \{(x, f(x)) \mid x \in A\} \subset A \times B$$

No plano cartesiano ($A \subseteq \mathbb{R}$, $B \subseteq \mathbb{R}$), cada elemento $x$ do domínio gera um ponto $(x, y)$ com $y = f(x)$. A curva formada por todos esses pontos é o gráfico de $f$ — uma ferramenta visual que revela propriedades (domínio, imagem, zeros, monotonicidade, paridade) de forma imediata.

## Teoria & Fundamentos

### Leitura do gráfico

A partir do gráfico de $f$ no plano $xy$, é possível extrair:

| Informação | Como ler no gráfico |
| ---------- | ------------------- |
| Domínio $D(f)$ | Projeção da curva sobre o eixo $x$ (extensão horizontal) |
| Imagem $\operatorname{Im}(f)$ | Projeção da curva sobre o eixo $y$ (extensão vertical) |
| Zeros/raízes | Pontos onde a curva cruza o eixo $x$ (i.e., $f(x) = 0$) |
| Valor inicial | Ponto onde a curva cruza o eixo $y$ (i.e., $f(0)$, se $0 \in D(f)$) |
| Sinal de $f$ | Porções acima do eixo $x$: $f(x) > 0$; abaixo: $f(x) < 0$ |

### Teste da reta vertical

Uma curva no plano cartesiano é gráfico de **alguma função** se e somente se **toda reta vertical a intercepta em no máximo um ponto**. Se alguma reta vertical corta a curva em dois ou mais pontos, então há dois $y$ para o mesmo $x$, violando a unicidade.

> **Não confundir** com o **teste da reta horizontal** (que testa injetividade): toda reta horizontal corta o gráfico em no máximo 1 ponto $\iff$ $f$ é injetora.

### Funções elementares

#### Função constante — $f(x) = c$

- **Domínio:** $\mathbb{R}$ | **Imagem:** $\{c\}$
- **Gráfico:** reta horizontal na altura $y = c$
- **Propriedades:** par (se o domínio for simétrico); nem crescente nem decrescente

#### Função identidade — $f(x) = x$

- **Domínio:** $\mathbb{R}$ | **Imagem:** $\mathbb{R}$
- **Gráfico:** reta que passa pela origem com inclinação 45°
- **Propriedades:** ímpar; estritamente crescente em $\mathbb{R}$

#### Função afim (linear) — $f(x) = ax + b$

- **Domínio:** $\mathbb{R}$ | **Imagem:** $\mathbb{R}$ (se $a \neq 0$)
- **Gráfico:** reta com **coeficiente angular** $a$ e **coeficiente linear** $b$
- $a > 0$: crescente | $a < 0$: decrescente | $a = 0$: constante
- **Zero (raiz):** $x = -\dfrac{b}{a}$ (ponto onde cruza o eixo $x$)
- **Intercepto $y$:** $f(0) = b$

| Parâmetro | Significado geométrico |
| --------- | ---------------------- |
| $a > 0$ | Reta sobe da esquerda para a direita |
| $a < 0$ | Reta desce da esquerda para a direita |
| $b > 0$ | Reta cruza o eixo $y$ acima da origem |
| $b < 0$ | Reta cruza o eixo $y$ abaixo da origem |
| $b = 0$ | Reta passa pela origem (função linear pura) |

#### Função quadrática — $f(x) = ax^2 + bx + c$, $a \neq 0$

- **Domínio:** $\mathbb{R}$ | **Imagem:** $\left[-\dfrac{\Delta}{4a}, +\infty\right)$ se $a > 0$; $\left(-\infty, -\dfrac{\Delta}{4a}\right]$ se $a < 0$
- **Gráfico:** parábola com eixo de simetria vertical
- **Discriminante:** $\Delta = b^2 - 4ac$
- **Vértice:** $V = \left(-\dfrac{b}{2a},\; -\dfrac{\Delta}{4a}\right)$
- **Concavidade:** $a > 0$ → abre para cima (mínimo no vértice); $a < 0$ → abre para baixo (máximo no vértice)
- **Raízes:** $x = \dfrac{-b \pm \sqrt{\Delta}}{2a}$ (existem em $\mathbb{R}$ quando $\Delta \geq 0$)

| $\Delta$ | Número de raízes reais | Posição da parábola |
| -------- | ---------------------- | ------------------- |
| $\Delta > 0$ | 2 raízes distintas | Corta o eixo $x$ em 2 pontos |
| $\Delta = 0$ | 1 raiz dupla | Tangencia o eixo $x$ no vértice |
| $\Delta < 0$ | 0 raízes reais | Não toca o eixo $x$ |

#### Função módulo — $f(x) = |x|$

- **Domínio:** $\mathbb{R}$ | **Imagem:** $[0, +\infty)$
- **Gráfico:** formato de "V" com vértice na origem; $f(x) = x$ para $x \geq 0$ e $f(x) = -x$ para $x < 0$
- **Propriedades:** par; decrescente em $(-\infty, 0]$, crescente em $[0, +\infty)$

#### Função raiz quadrada — $f(x) = \sqrt{x}$

- **Domínio:** $[0, +\infty)$ | **Imagem:** $[0, +\infty)$
- **Gráfico:** metade direita de uma parábola deitada, partindo da origem
- **Propriedades:** estritamente crescente; é a inversa de $f(x) = x^2$ restrita a $[0, +\infty)$

#### Função recíproca (hiperbólica) — $f(x) = \dfrac{1}{x}$

- **Domínio:** $\mathbb{R}^* = (-\infty, 0) \cup (0, +\infty)$ | **Imagem:** $\mathbb{R}^*$
- **Gráfico:** hipérbole equilátera com assíntotas nos eixos coordenados (eixo $x$: assíntota horizontal; eixo $y$: assíntota vertical)
- **Propriedades:** ímpar; decrescente em cada ramo (em $(-\infty,0)$ e em $(0,+\infty)$ separadamente)

#### Função exponencial — $f(x) = a^x$, $a > 0$, $a \neq 1$

- **Domínio:** $\mathbb{R}$ | **Imagem:** $(0, +\infty)$
- **Gráfico:** passa sempre por $(0, 1)$ (pois $a^0 = 1$)
- $a > 1$: crescente (cresce à direita, se aproxima de 0 à esquerda)
- $0 < a < 1$: decrescente (decresce à direita, se aproxima de 0 à direita)
- **Assíntota horizontal:** eixo $x$ (o gráfico nunca toca $y = 0$)
- **Não tem raiz real** (imagem é $(0, +\infty)$, nunca atinge $y = 0$)

#### Função logarítmica — $f(x) = \log_a x$, $a > 0$, $a \neq 1$

- **Domínio:** $(0, +\infty)$ | **Imagem:** $\mathbb{R}$
- **Gráfico:** inversa da exponencial; simétrica a $a^x$ em relação à reta $y = x$; passa por $(1, 0)$
- $a > 1$: crescente | $0 < a < 1$: decrescente
- **Assíntota vertical:** eixo $y$ ($x = 0$)
- **Zero:** $x = 1$ (pois $\log_a 1 = 0$)

### Paridade

A paridade é uma propriedade **algébrica** com reflexo **geométrico**. Exige que o domínio seja **simétrico em relação à origem**.

**Função par:** $f(-x) = f(x)$ para todo $x \in D(f)$
- Gráfico: **simétrico ao eixo $y$** (reflexão vertical)
- Exemplos: $x^2$, $x^4$, $|x|$, $\operatorname{cos} x$

**Função ímpar:** $f(-x) = -f(x)$ para todo $x \in D(f)$
- Gráfico: **simétrico à origem** (rotação de 180° em torno da origem)
- Exemplos: $x$, $x^3$, $\dfrac{1}{x}$, $\operatorname{sen} x$

**Nem par nem ímpar:** a condição não é satisfeita.

> **Método de teste:** calcular $f(-x)$, simplificar e comparar com $f(x)$ e com $-f(x)$.

### Monotonicidade

Seja $I \subseteq D(f)$ um intervalo:

**Estritamente crescente em $I$:** $x_1 < x_2 \implies f(x_1) < f(x_2)$

**Estritamente decrescente em $I$:** $x_1 < x_2 \implies f(x_1) > f(x_2)$

> Uma função pode ser crescente em um intervalo e decrescente em outro. Por exemplo, $f(x) = x^2$ é decrescente em $(-\infty, 0]$ e crescente em $[0, +\infty)$.

**Conexão com injetividade:** toda função estritamente monótona em um intervalo é injetora nesse intervalo.

### Limitação

- **Limitada superiormente em $I$:** existe $M \in \mathbb{R}$ tal que $f(x) \leq M$ para todo $x \in I$
- **Limitada inferiormente em $I$:** existe $m \in \mathbb{R}$ tal que $f(x) \geq m$ para todo $x \in I$
- **Limitada em $I$:** limitada superior e inferiormente

### Transformações de gráficos

Dada a curva de $y = f(x)$, as transformações a seguir produzem novos gráficos:

| Transformação na fórmula | Efeito no gráfico |
| ------------------------ | ----------------- |
| $f(x) + k$, $k > 0$ | Translação vertical **para cima** de $k$ unidades |
| $f(x) - k$, $k > 0$ | Translação vertical **para baixo** de $k$ unidades |
| $f(x - h)$, $h > 0$ | Translação horizontal **para a direita** de $h$ unidades |
| $f(x + h)$, $h > 0$ | Translação horizontal **para a esquerda** de $h$ unidades |
| $-f(x)$ | Reflexão em relação ao **eixo $x$** |
| $f(-x)$ | Reflexão em relação ao **eixo $y$** |
| $a \cdot f(x)$, $a > 1$ | Dilatação vertical (estica verticalmente) |
| $a \cdot f(x)$, $0 < a < 1$ | Compressão vertical |
| $f(ax)$, $a > 1$ | Compressão horizontal |
| $f(ax)$, $0 < a < 1$ | Dilatação horizontal |

### Gráfico da função inversa

Se $f$ é bijetora, o gráfico de $f^{-1}$ é a **reflexão do gráfico de $f$ em relação à reta $y = x$**. Em termos de pontos: se $(a, b) \in G(f)$, então $(b, a) \in G(f^{-1})$.

## Fórmulas & Equações

### Resumo das funções elementares

| Função | Fórmula | Domínio | Imagem | Gráfico |
| ------ | ------- | ------- | ------ | ------- |
| Constante | $c$ | $\mathbb{R}$ | $\{c\}$ | Reta horizontal |
| Identidade | $x$ | $\mathbb{R}$ | $\mathbb{R}$ | Reta diagonal (45°) |
| Afim | $ax + b$ | $\mathbb{R}$ | $\mathbb{R}$ | Reta inclinada |
| Quadrática | $ax^2 + bx + c$ | $\mathbb{R}$ | Depende de $a$ e $\Delta$ | Parábola |
| Módulo | $\|x\|$ | $\mathbb{R}$ | $[0,+\infty)$ | Forma de V |
| Raiz quadrada | $\sqrt{x}$ | $[0,+\infty)$ | $[0,+\infty)$ | Meia parábola deitada |
| Recíproca | $1/x$ | $\mathbb{R}^*$ | $\mathbb{R}^*$ | Hipérbole |
| Exponencial | $a^x$ | $\mathbb{R}$ | $(0,+\infty)$ | Curva exponencial |
| Logarítmica | $\log_a x$ | $(0,+\infty)$ | $\mathbb{R}$ | Curva logarítmica |

### Fórmulas da quadrática

$$V_x = -\frac{b}{2a} \qquad V_y = -\frac{\Delta}{4a} \qquad \Delta = b^2 - 4ac \qquad x = \frac{-b \pm \sqrt{\Delta}}{2a}$$

## Exemplos Resolvidos

**Exemplo 1 — Básico: análise completa de uma função afim**

> **Enunciado:** Para $f(x) = -2x + 4$, determine: coeficiente angular, coeficiente linear, raiz, intercepto com eixo $y$, sinal e esboço.

**Passo 1 — Identificar os parâmetros $a$ e $b$.**

Comparar $f(x) = -2x + 4$ com a forma $ax + b$:

$$a = -2 \quad \text{(coeficiente angular)} \qquad b = 4 \quad \text{(coeficiente linear)}$$

**Passo 2 — Determinar o comportamento da reta.**

Como $a = -2 < 0$, a função é **estritamente decrescente** — a reta desce da esquerda para a direita.

**Passo 3 — Calcular a raiz (zero da função).**

Fazer $f(x) = 0$ e isolar $x$:

$$-2x + 4 = 0 \implies -2x = -4 \implies x = \frac{-4}{-2} = 2$$

A raiz é $x = 2$: o gráfico corta o eixo $x$ no ponto $(2, 0)$.

**Passo 4 — Calcular o intercepto com o eixo $y$.**

Fazer $x = 0$:

$$f(0) = -2 \cdot 0 + 4 = 4$$

O gráfico corta o eixo $y$ no ponto $(0, 4)$.

**Passo 5 — Determinar o sinal de $f$.**

Com dois pontos-chave: $(0, 4)$ e $(2, 0)$, e reta decrescente:

- Para $x < 2$: $f(x) > 0$ (reta está acima do eixo $x$)
- Para $x = 2$: $f(x) = 0$ (raiz)
- Para $x > 2$: $f(x) < 0$ (reta está abaixo do eixo $x$)

**Passo 6 — Esboço do gráfico.**

Dois pontos determinam uma reta. Usar os dois interceptos:

```
  y
  |
4 •  ← (0, 4)
  |  \
  |    \
--+-----•------ x
  0     2 ← raiz
         \
          \
```

> **Resumo:** reta decrescente, zero em $x=2$, intercepto em $y=4$; $f(x) > 0$ para $x \in (-\infty, 2)$ e $f(x) < 0$ para $x \in (2, +\infty)$.

---

**Exemplo 2 — Intermediário: classificar paridade de três funções**

> **Enunciado:** Classifique quanto à paridade: $f(x) = x^4 - 3x^2$, $g(x) = x^3 - x$, $h(x) = x^2 + x$.

**Método geral:** calcular $f(-x)$, simplificar, e comparar com $f(x)$ e $-f(x)$.

**— Para $f(x) = x^4 - 3x^2$ —**

**Passo 1 — Verificar simetria do domínio.** Domínio $= \mathbb{R}$, que é simétrico em relação à origem. ✓

**Passo 2 — Calcular $f(-x)$.**

Substituir $x$ por $(-x)$ na fórmula. Cada potência é afetada:

$$f(-x) = (-x)^4 - 3(-x)^2$$

Aplicar as potências: $(-x)^4 = x^4$ (expoente par) e $(-x)^2 = x^2$ (expoente par):

$$f(-x) = x^4 - 3x^2$$

**Passo 3 — Comparar com $f(x)$ e $-f(x)$.**

$$f(-x) = x^4 - 3x^2 = f(x) \checkmark$$

Como $f(-x) = f(x)$, a função é **par**. Gráfico simétrico ao eixo $y$.

---

**— Para $g(x) = x^3 - x$ —**

**Passo 1 — Domínio:** $\mathbb{R}$, simétrico. ✓

**Passo 2 — Calcular $g(-x)$.**

$$g(-x) = (-x)^3 - (-x)$$

Aplicar as potências: $(-x)^3 = -x^3$ (expoente ímpar):

$$g(-x) = -x^3 - (-x) = -x^3 + x$$

**Passo 3 — Fatorar para reconhecer o padrão.**

$$g(-x) = -(x^3 - x) = -g(x) \checkmark$$

Como $g(-x) = -g(x)$, a função é **ímpar**. Gráfico simétrico à origem.

---

**— Para $h(x) = x^2 + x$ —**

**Passo 1 — Domínio:** $\mathbb{R}$, simétrico. ✓

**Passo 2 — Calcular $h(-x)$.**

$$h(-x) = (-x)^2 + (-x) = x^2 - x$$

**Passo 3 — Comparar com $h(x)$ e $-h(x)$.**

$$h(x) = x^2 + x \qquad -h(x) = -x^2 - x$$

$h(-x) = x^2 - x \neq x^2 + x = h(x)$ → **não é par**

$h(-x) = x^2 - x \neq -x^2 - x = -h(x)$ → **não é ímpar**

A função $h$ **não é nem par nem ímpar**.

> **Resumo:** $f$: par | $g$: ímpar | $h$: nem par nem ímpar.

---

**Exemplo 3 — Avançado: análise completa de uma função quadrática**

> **Enunciado:** Para $f(x) = x^2 - 4x + 3$, determine: vértice, concavidade, raízes, intervalos de monotonicidade, imagem e esboço.

**Passo 1 — Identificar $a$, $b$, $c$.**

Comparar com $ax^2 + bx + c$:

$$a = 1, \quad b = -4, \quad c = 3$$

Como $a = 1 > 0$: **concavidade para cima** (parábola abre para cima, vértice é mínimo).

**Passo 2 — Calcular o discriminante $\Delta$.**

$$\Delta = b^2 - 4ac = (-4)^2 - 4 \cdot 1 \cdot 3 = 16 - 12 = 4$$

$\Delta = 4 > 0$ → **duas raízes reais distintas**.

**Passo 3 — Calcular as raízes pela fórmula de Bhaskara.**

$$x = \frac{-b \pm \sqrt{\Delta}}{2a} = \frac{-(-4) \pm \sqrt{4}}{2 \cdot 1} = \frac{4 \pm 2}{2}$$

Separar em dois casos:

$$x_1 = \frac{4 + 2}{2} = \frac{6}{2} = 3 \qquad x_2 = \frac{4 - 2}{2} = \frac{2}{2} = 1$$

Raízes: $x_1 = 1$ e $x_2 = 3$.

**Passo 4 — Calcular o vértice.**

A abscissa do vértice usa as duas raízes: $V_x = \dfrac{x_1 + x_2}{2}$ (ponto médio das raízes), ou pela fórmula direta:

$$V_x = -\frac{b}{2a} = -\frac{-4}{2} = 2$$

A ordenada é obtida substituindo $V_x$ em $f$:

$$V_y = f(2) = (2)^2 - 4(2) + 3 = 4 - 8 + 3 = -1$$

Vértice: $V = (2, -1)$.

Verificação pela fórmula: $V_y = -\dfrac{\Delta}{4a} = -\dfrac{4}{4} = -1$ ✓

**Passo 5 — Determinar os intervalos de monotonicidade.**

Como a parábola abre para cima com vértice em $x = 2$:

- **Decrescente:** $(-\infty, 2]$ (à esquerda do vértice, $f$ decresce)
- **Crescente:** $[2, +\infty)$ (à direita do vértice, $f$ cresce)

**Passo 6 — Determinar a imagem.**

O valor mínimo de $f$ é $V_y = -1$ (atingido em $x = 2$). Como a parábola abre para cima e não tem máximo:

$$\operatorname{Im}(f) = [-1, +\infty)$$

**Passo 7 — Calcular o intercepto com o eixo $y$.**

$$f(0) = 0 - 0 + 3 = 3 \implies \text{ponto } (0, 3)$$

**Esboço do gráfico:**

```
  y
  |
3 •  ← (0,3)
  |   \         /
  |    \       /
--+--•---V---•-- x
  0   1   2   3
       ↑   ↑
      raízes  V=(2,-1)
         ↓
        -1
```

> **Resumo:** concavidade para cima; vértice $(2,-1)$ mínimo; raízes $x = 1$ e $x = 3$; intercepto $(0, 3)$; decrescente em $(-\infty, 2]$, crescente em $[2,+\infty)$; imagem $[-1,+\infty)$.

## Armadilhas & Edge Cases

- **Confundir teste da reta vertical com o da reta horizontal** — reta vertical testa se é **função**; reta horizontal testa **injetividade** (não confundir os dois critérios)
- **Achar que toda função é par ou ímpar** — a maioria das funções não é nenhuma das duas; é preciso calcular $f(-x)$ e verificar explicitamente
- **Expoente par/ímpar não implica paridade automaticamente** — $f(x) = x^2 + 1$ é par, mas $f(x) = x^2 + x$ não é; o teste deve ser feito na função inteira, não em cada termo isolado
- **Confundir crescente com positiva** — uma função pode ser crescente em um intervalo onde seus valores são negativos (ex: $x^2 - 4$ cresce em $[2,+\infty)$ mas tem valores negativos perto de $x=2$)
- **Erro de sinal no vértice** — $V_x = -\dfrac{b}{2a}$, não $\dfrac{b}{2a}$; o sinal negativo é frequentemente esquecido
- **Assíntota vertical do logaritmo** — $\log_a x$ tem assíntota em $x = 0$ (o eixo $y$); o gráfico nunca cruza o eixo $y$
- **$f^{-1}$ ≠ reflexão de $\dfrac{1}{f}$** — o gráfico de $f^{-1}$ é a reflexão de $f$ em relação a $y = x$; não tem nada a ver com $1/f(x)$
- **Translação horizontal: sinal contrário ao esperado** — $f(x - 2)$ desloca o gráfico 2 unidades **para a direita** (não para a esquerda); o sinal na fórmula é oposto ao deslocamento

## Conexões

- Matemática — MOC da área
- [[Química]] — Roadmap da graduação
- [[Funções]] — pré-requisito direto (definição formal, domínio/imagem, classificação, inversa)
- [[Conjuntos Numéricos]] — eixos cartesianos baseados em $\mathbb{R}$; intervalos usados na descrição de monotonicidade e imagem
- [[Funções Trigonométricas]] — aplicação do estudo de gráficos às funções sen, cos, tg
- [[Trigonometria na Circunferência]] — fornece os valores que definem as funções trigonométricas
- Física — gráficos de posição × tempo, velocidade × tempo; funções afim e quadrática em cinemática

## Fontes

- GUIDORIZZI, Hamilton Luiz. *Um Curso de Cálculo* — Vol. 1, Cap. 1: Funções. LTC.
