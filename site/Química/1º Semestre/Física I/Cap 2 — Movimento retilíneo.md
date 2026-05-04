---
title: Cap 2 — Movimento retilíneo
description: 'Cinemática unidimensional: descreve como um objeto se move ao longo
  de uma reta — posição, velocidade e aceleração — sem se preocupar com a causa do
  movimento (…'
tags:
- quimica
date: 2026-04-30
tipo: estudo
disciplina: fisica
semestre: 1
---
# Cap 2 — Movimento retilíneo

> Cinemática unidimensional: descreve **como** um objeto se move ao longo de uma reta — posição, velocidade e aceleração — sem se preocupar com a **causa** do movimento (isso é dinâmica, Cap 4-5).

---

## Definição

**Movimento retilíneo** é o movimento ao longo de uma linha reta. A cinemática 1D usa três grandezas fundamentais:

| Grandeza | Símbolo | Unidade SI |
| -------- | ------- | ---------- |
| Posição | $x$ | m |
| Velocidade | $v$ | m/s |
| Aceleração | $a$ | m/s² |

> Todas são escalares em 1D (o sinal indica sentido: $+$ ou $-$).

---

## Teoria & Fundamentos

### 2.1 Deslocamento, tempo e velocidade média

**Posição** $x$: coordenada do objeto em relação a um ponto de referência (origem).

**Deslocamento** $\Delta x$: variação de posição (não confundir com distância percorrida):

$$\Delta x = x_2 - x_1$$

**Velocidade média:**

$$v_{\text{med}} = \dfrac{\Delta x}{\Delta t} = \dfrac{x_2 - x_1}{t_2 - t_1}$$

```
Gráfico x×t — velocidade média = inclinação da secante

  x (m)
  |          ● P2 (t2, x2)
  |         /
  |        /  ← inclinação = Δx/Δt = vméd
  |       /
  |      ● P1 (t1, x1)
  |
  +──────────── t (s)
```

### 2.2 Velocidade instantânea

Velocidade em um instante exato — limite da velocidade média quando $\Delta t \to 0$:

$$v_x = \lim_{\Delta t \to 0} \dfrac{\Delta x}{\Delta t} = \dfrac{dx}{dt}$$

Graficamente: **inclinação da reta tangente** à curva $x(t)$ no ponto $t$.

```
  x (m)
  |        /← tangente em P = velocidade instantânea
  |       /
  |    . P
  |   /
  | .'
  +──────────── t (s)
```

- $v_x > 0$: movimento no sentido positivo de $x$
- $v_x < 0$: movimento no sentido negativo de $x$
- $v_x = 0$: partícula em repouso (ou no ponto de retorno)

**Rapidez** (speed): valor absoluto da velocidade, $|v_x|$ — sempre $\geq 0$.

### 2.3 Aceleração instantânea e média

**Aceleração média:**

$$a_{\text{med}} = \dfrac{\Delta v_x}{\Delta t} = \dfrac{v_{x2} - v_{x1}}{t_2 - t_1}$$

**Aceleração instantânea:**

$$a_x = \dfrac{dv_x}{dt} = \dfrac{d^2x}{dt^2}$$

Graficamente: **inclinação da curva** $v_x(t)$.

> Atenção: aceleração e velocidade com sinais opostos → objeto **desacelera** (velocidade diminui em magnitude).

### 2.4 Movimento com aceleração constante (MRUV)

Quando $a_x = \text{constante}$, derivamos as **quatro equações cinemáticas**:

| Eq. | Fórmula | Grandeza ausente |
| --- | ------- | ---------------- |
| (1) | $v_x = v_{0x} + a_x t$ | $x$ |
| (2) | $x = x_0 + v_{0x}t + \dfrac{1}{2}a_x t^2$ | $v_x$ |
| (3) | $v_x^2 = v_{0x}^2 + 2a_x(x - x_0)$ | $t$ |
| (4) | $x = x_0 + \dfrac{v_{0x} + v_x}{2}\,t$ | $a_x$ |

Onde:
- $x_0$, $v_{0x}$: posição e velocidade iniciais (em $t = 0$)
- $x$, $v_x$: posição e velocidade em $t$
- $a_x$: aceleração (constante)

**Gráficos típicos do MRUV ($a_x > 0$):**

```
v (m/s)         x (m)
|   /           |    ⌒
|  /            |   /
| /             |  /
|/              | /
+────── t       +────── t

v×t: reta         x×t: parábola
inclinação=a      abertura para cima se a>0
```

### 2.5 Queda livre de corpos

Caso especial de MRUV: aceleração constante para baixo, $\vec{g}$ (aceleração gravitacional).

No SI, adotando $y$ positivo para cima:

$$a_y = -g = -9{,}80\ \text{m/s}^2$$

As quatro equações cinemáticas se aplicam com $a_y = -g$:

$$v_y = v_{0y} - gt$$
$$y = y_0 + v_{0y}t - \dfrac{1}{2}gt^2$$
$$v_y^2 = v_{0y}^2 - 2g(y - y_0)$$

> O valor de $g$ varia ligeiramente com a latitude e altitude, mas usa-se $g = 9{,}80\ \text{m/s}^2$ salvo indicação contrária.

**Fatos importantes da queda livre:**
- No ponto mais alto ($v_y = 0$), a aceleração **não é zero** — continua sendo $g$ para baixo.
- Objetos de massas diferentes caem com a mesma aceleração (desprezando o ar).

### 2.6 Velocidade e posição por integração *(seção complementar)*

Quando $a_x$ **não é constante**, integra-se:

$$v_x = v_{0x} + \int_0^t a_x\,dt'$$

$$x = x_0 + \int_0^t v_x\,dt'$$

Graficamente: **área sob a curva** $a_x(t)$ dá $\Delta v_x$; **área sob** $v_x(t)$ dá $\Delta x$.

---

## Fórmulas & Equações

| Fórmula | Descrição |
| ------- | --------- |
| $\Delta x = x_2 - x_1$ | Deslocamento |
| $v_{\text{med}} = \Delta x / \Delta t$ | Velocidade média |
| $v_x = dx/dt$ | Velocidade instantânea |
| $a_x = dv_x/dt$ | Aceleração instantânea |
| $v_x = v_{0x} + a_x t$ | Velocidade em função do tempo (MRUV) |
| $x = x_0 + v_{0x}t + \frac{1}{2}a_x t^2$ | Posição em função do tempo (MRUV) |
| $v_x^2 = v_{0x}^2 + 2a_x\Delta x$ | Velocidade em função da posição (MRUV) |
| $a_y = -g = -9{,}80\ \text{m/s}^2$ | Aceleração na queda livre ($y$ positivo para cima) |

---

## Exemplos Resolvidos

**Exemplo 1 — Velocidade média e instantânea (básico)**

Um carro percorre $120\ \text{km}$ em $1{,}50\ \text{h}$ em linha reta. Calcule a velocidade média em m/s.

**Resolução:**

$$\Delta x = 120\ \text{km} = 1{,}20 \times 10^5\ \text{m}$$
$$\Delta t = 1{,}50\ \text{h} \times 3600\ \text{s/h} = 5400\ \text{s}$$
$$v_{\text{med}} = \dfrac{1{,}20 \times 10^5}{5400} = 22{,}2\ \text{m/s}$$

$$\boxed{v_{\text{med}} = 22{,}2\ \text{m/s} \approx 80\ \text{km/h}}$$

---

**Exemplo 2 — MRUV: frenagem de veículo (intermediário)**

Um automóvel viaja a $v_0 = 30{,}0\ \text{m/s}$ (108 km/h) e freia com aceleração constante $a_x = -5{,}00\ \text{m/s}^2$. (a) Quanto tempo até parar? (b) Qual a distância de frenagem?

**Resolução — (a):** usar eq. (1), $v_x = 0$:

$$0 = 30{,}0 + (-5{,}00)\,t \implies t = \dfrac{30{,}0}{5{,}00} = 6{,}00\ \text{s}$$

**Resolução — (b):** usar eq. (3), $v_x = 0$:

$$0 = (30{,}0)^2 + 2(-5{,}00)\Delta x$$
$$\Delta x = \dfrac{900}{10{,}0} = 90{,}0\ \text{m}$$

$$\boxed{t = 6{,}00\ \text{s} \quad \text{e} \quad \Delta x = 90{,}0\ \text{m}}$$

---

**Exemplo 3 — Queda livre com lançamento vertical (avançado)**

Uma bola é lançada **para cima** de uma janela a $h = 20{,}0\ \text{m}$ do solo com velocidade inicial $v_0 = 15{,}0\ \text{m/s}$. Tomando $y_0 = 0$ na janela e $y$ positivo para cima:

**(a)** Qual a altura máxima atingida acima da janela?  
**(b)** Em que instante a bola atinge o solo?  
**(c)** Qual a velocidade ao atingir o solo?

**Resolução — (a)** No ponto mais alto, $v_y = 0$:

$$0 = v_0^2 - 2g\,y_{\max} \implies y_{\max} = \dfrac{v_0^2}{2g} = \dfrac{(15{,}0)^2}{2 \times 9{,}80} = \dfrac{225}{19{,}6} = 11{,}5\ \text{m}$$

**Resolução — (b)** Solo: $y = -20{,}0\ \text{m}$:

$$-20{,}0 = 15{,}0\,t - \dfrac{1}{2}(9{,}80)t^2$$
$$4{,}90\,t^2 - 15{,}0\,t - 20{,}0 = 0$$

Fórmula de Bhaskara: $t = \dfrac{15{,}0 \pm \sqrt{225 + 4 \times 4{,}90 \times 20{,}0}}{2 \times 4{,}90} = \dfrac{15{,}0 \pm \sqrt{617}}{9{,}80}$

$\sqrt{617} \approx 24{,}84$

$t_1 = \dfrac{15{,}0 + 24{,}84}{9{,}80} \approx 4{,}07\ \text{s}$ ✓ (positivo, fisicamente relevante)

**Resolução — (c)**:

$$v_y = 15{,}0 - (9{,}80)(4{,}07) = 15{,}0 - 39{,}9 = -24{,}9\ \text{m/s}$$

$$\boxed{y_{\max} = 11{,}5\ \text{m acima da janela};\quad t = 4{,}07\ \text{s};\quad v_y = -24{,}9\ \text{m/s (para baixo)}}$$

---

## Armadilhas & Edge Cases

- **Deslocamento ≠ distância percorrida:** um objeto que vai e volta pode ter $\Delta x = 0$ mas ter percorrido uma distância real.
- **Aceleração e desaceleração:** se $v_x$ e $a_x$ têm o **mesmo sinal**, o objeto acelera; sinais **opostos**, desacelera. Não confunda "aceleração negativa" com "desaceleração".
- **$g$ sempre positivo:** $g = 9{,}80\ \text{m/s}^2$ é a **magnitude**. O sinal aparece na equação: $a_y = -g$ (com $y$ positivo para cima).
- **Escolha de origem:** a posição inicial $x_0$ pode ser qualquer valor. Escolha a origem que simplifica o problema.
- **Duas raízes na equação quadrática:** ao resolver $y(t) = \text{cte}$, podem aparecer dois valores de $t$. Identifique qual é fisicamente relevante (geralmente $t > 0$ e o contexto do problema).

---

## Conexões

- [[Cap 1 — Unidades, grandezas físicas e vetores]] ← capítulo anterior (unidades e escalares)
- [[Cap 3 — Movimento em duas ou três dimensões]] → generaliza para 2D e 3D usando vetores
- [[Cap 4 — Leis de Newton do movimento]] → explica **por que** há aceleração (causa do movimento)
- [[Física I]] ← MOC da disciplina
- [[Física]] ← MOC de área

---

## Fontes

- YOUNG, Hugh D.; FREEDMAN, Roger A. **Física I: Mecânica**. 12. ed. São Paulo: Pearson Addison Wesley, 2008. Cap. 2, p. 35–67.
