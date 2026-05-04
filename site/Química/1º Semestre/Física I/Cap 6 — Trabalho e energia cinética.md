---
title: Cap 6 — Trabalho e energia cinética
description: 'O conceito de energia oferece uma alternativa poderosa à 2ª Lei de Newton:
  em vez de analisar forças a cada instante, relacionamos o estado inicial e final
  do m…'
tags:
- quimica
date: 2026-04-30
tipo: estudo
disciplina: fisica
semestre: 1
---
# Cap 6 — Trabalho e energia cinética

> O conceito de **energia** oferece uma alternativa poderosa à 2ª Lei de Newton: em vez de analisar forças a cada instante, relacionamos o estado inicial e final do movimento. O **Teorema do Trabalho-Energia** é o elo central deste capítulo.

---

## Definição

**Trabalho** ($W$) é a transferência de energia de um agente para um objeto por meio de uma força. Só há trabalho quando a força tem componente **na direção do deslocamento**.

**Energia cinética** ($K$) é a energia associada ao **movimento** de um objeto:

$$K = \dfrac{1}{2}mv^2$$

**Teorema do Trabalho-Energia:** o trabalho total realizado sobre uma partícula é igual à variação de sua energia cinética:

$$W_{\text{total}} = \Delta K = K_f - K_i$$

---

## Teoria & Fundamentos

### 6.1 Trabalho

#### Força constante e deslocamento reto

Para uma força constante $\vec{F}$ que age enquanto o objeto sofre deslocamento $\vec{s}$:

$$W = \vec{F} \cdot \vec{s} = Fs\cos\phi$$

onde $\phi$ é o ângulo entre $\vec{F}$ e $\vec{s}$.

```
Trabalho e ângulo φ:

  caso φ = 0°:   F→  s→    W = Fs   (máximo positivo)
  caso φ = 90°:  F↑  s→    W = 0    (força perpendicular)
  caso φ = 180°: F←  s→    W = -Fs  (força oposta ao deslocamento)
```

**Unidade:** Joule (J) = N·m = kg·m²/s²

**Sinal do trabalho:**

| Condição | Sinal de $W$ | Efeito |
| --------- | ----------- | ------ |
| $0° \leq \phi < 90°$ | $W > 0$ | Acelera o objeto |
| $\phi = 90°$ | $W = 0$ | Não altera a rapidez |
| $90° < \phi \leq 180°$ | $W < 0$ | Desacelera o objeto |

> **Importante:** trabalho **não é** uma propriedade do objeto — é uma grandeza de **processo** (depende da trajetória e da força aplicada).

#### Trabalho realizado pelo peso

Para um deslocamento vertical $\Delta y = y_f - y_i$ (positivo para cima):

$$W_{\text{peso}} = -mg\Delta y = mg(y_i - y_f)$$

- O peso realiza trabalho **positivo** quando o objeto desce ($y_f < y_i$).
- O peso realiza trabalho **negativo** quando o objeto sobe ($y_f > y_i$).

#### Trabalho realizado pela força normal

A força normal é sempre perpendicular ao deslocamento ($\phi = 90°$), portanto:

$$W_N = 0$$

### 6.2 Energia cinética e o Teorema do Trabalho-Energia

**Energia cinética:**

$$K = \dfrac{1}{2}mv^2$$

**Demonstração do Teorema (caso 1D, força e aceleração constantes):**

Usando $v^2 = v_0^2 + 2a\Delta x$ e $F = ma$:

$$W = F\Delta x = ma\Delta x = m \cdot \dfrac{v^2 - v_0^2}{2} = \dfrac{1}{2}mv^2 - \dfrac{1}{2}mv_0^2 = K_f - K_i$$

$$\boxed{W_{\text{total}} = \Delta K}$$

> O teorema é válido para **força variável** e **trajetória curva** — desde que $W_{\text{total}}$ seja calculado corretamente (ver 6.3).

### 6.3 Trabalho e energia com forças variáveis

Quando $F_x$ varia com a posição, o trabalho é a **integral** (área sob a curva $F_x \times x$):

$$W = \int_{x_1}^{x_2} F_x\,dx$$

```
Gráfico F×x — trabalho = área sombreada:

  F (N)
  |  ╔════╗
  |  ║    ║ ← área = W
  |  ║    ╚══════
  |  ║
  +──+────+──── x (m)
     x1   x2
```

**Lei de Hooke — mola:**

$$F_{\text{mola}} = -kx$$

onde $k$ é a constante elástica (N/m) e $x$ é a deformação em relação ao ponto de equilíbrio.

O trabalho realizado pela força da mola (de $x_1$ para $x_2$):

$$W_{\text{mola}} = \int_{x_1}^{x_2}(-kx)\,dx = -\dfrac{1}{2}k x_2^2 + \dfrac{1}{2}k x_1^2 = \dfrac{1}{2}k x_1^2 - \dfrac{1}{2}k x_2^2$$

E o trabalho realizado por uma força **externa** que estica a mola de $0$ até $X$:

$$W_{\text{externo}} = \dfrac{1}{2}kX^2$$

```
Força da mola vs. deformação:

  F_ext (N)
  |       /
  |      /
  |     / slope = k
  |    /
  |   / W = área do triângulo = ½kX²
  |  /
  +-/─────── x (m)
    0    X
```

### 6.4 Potência

**Potência** é a taxa de realização de trabalho — trabalho por unidade de tempo:

$$P = \dfrac{dW}{dt} = \vec{F} \cdot \vec{v} = Fv\cos\phi$$

**Unidade:** Watt (W) = J/s = kg·m²/s³

Conversão comum: $1\ \text{cv (cavalo-vapor)} = 746\ \text{W}$

**Potência média:**

$$P_{\text{med}} = \dfrac{W}{\Delta t}$$

> Potência não diz **quanto** trabalho foi feito, mas **quão rápido**. Um motor potente faz o mesmo trabalho em menos tempo.

---

## Fórmulas & Equações

| Fórmula | Descrição | Unidade |
| ------- | --------- | ------- |
| $W = Fs\cos\phi$ | Trabalho (força constante) | J |
| $W = \int_{x_1}^{x_2} F_x\,dx$ | Trabalho (força variável) | J |
| $K = \frac{1}{2}mv^2$ | Energia cinética | J |
| $W_{\text{total}} = \Delta K = K_f - K_i$ | Teorema do Trabalho-Energia | J |
| $F_{\text{mola}} = -kx$ | Lei de Hooke | N |
| $W_{\text{mola}} = \frac{1}{2}kx_1^2 - \frac{1}{2}kx_2^2$ | Trabalho da mola | J |
| $W_{\text{ext}} = \frac{1}{2}kX^2$ | Trabalho para esticar mola (de 0 a $X$) | J |
| $P = \vec{F}\cdot\vec{v} = Fv\cos\phi$ | Potência instantânea | W |
| $P_{\text{med}} = W/\Delta t$ | Potência média | W |

---

## Exemplos Resolvidos

**Exemplo 1 — Trabalho de múltiplas forças (básico)**

Uma caixa de $m = 8{,}00\ \text{kg}$ é puxada $3{,}00\ \text{m}$ horizontalmente por uma força $F = 25{,}0\ \text{N}$ a $\phi = 37{,}0°$ acima da horizontal, em uma superfície com $\mu_c = 0{,}200$. Calcule o trabalho de cada força e o trabalho total.

**Resolução:**

Normal: $N = mg - F\operatorname{sen}\phi = 8{,}00(9{,}80) - 25{,}0\operatorname{sen}(37°) = 78{,}4 - 15{,}0 = 63{,}4\ \text{N}$

Atrito: $f_c = \mu_c N = 0{,}200 \times 63{,}4 = 12{,}7\ \text{N}$

| Força | $W$ |
|-------|-----|
| $F$ aplicada | $25{,}0 \times 3{,}00 \times \cos(37°) = 75{,}0 \times 0{,}799 = 59{,}9\ \text{J}$ |
| Normal $N$ | $0\ \text{J}$ ($\phi = 90°$) |
| Peso $mg$ | $0\ \text{J}$ ($\phi = 90°$) |
| Atrito $f_c$ | $-12{,}7 \times 3{,}00 = -38{,}1\ \text{J}$ |

$$W_{\text{total}} = 59{,}9 + 0 + 0 - 38{,}1 = 21{,}8\ \text{J}$$

$$\boxed{W_{\text{total}} = 21{,}8\ \text{J}}$$

---

**Exemplo 2 — Teorema do Trabalho-Energia: velocidade final (intermediário)**

Um carro de $m = 1200\ \text{kg}$ parte do repouso e é acelerado por uma força resultante constante de $4800\ \text{N}$ por $\Delta x = 100\ \text{m}$. Qual a velocidade ao final do percurso?

**Resolução:**

Trabalho total:
$$W_{\text{total}} = F\Delta x = 4800 \times 100 = 4{,}80 \times 10^5\ \text{J}$$

Pelo Teorema do Trabalho-Energia ($v_i = 0$):
$$W_{\text{total}} = \dfrac{1}{2}mv_f^2 - 0$$
$$v_f = \sqrt{\dfrac{2W}{m}} = \sqrt{\dfrac{2 \times 4{,}80 \times 10^5}{1200}} = \sqrt{800} = 28{,}3\ \text{m/s}$$

$$\boxed{v_f = 28{,}3\ \text{m/s}\ (\approx 102\ \text{km/h})}$$

---

**Exemplo 3 — Trabalho da mola + Teorema do Trabalho-Energia (avançado)**

Uma mola horizontal ($k = 500\ \text{N/m}$) está comprimida $x_1 = 0{,}120\ \text{m}$ e lança um bloco de $m = 0{,}800\ \text{kg}$. A superfície tem $\mu_c = 0{,}150$. O bloco percorre $d = 0{,}500\ \text{m}$ até parar. Encontre a velocidade do bloco no instante em que deixa a mola (em $x = 0$) e verifique a consistência com a distância percorrida.

**Fase 1 — bloco sai da mola ($x_1 \to 0$):**

$$W_{\text{mola}} = \dfrac{1}{2}kx_1^2 = \dfrac{1}{2}(500)(0{,}120)^2 = \dfrac{1}{2}(500)(0{,}0144) = 3{,}60\ \text{J}$$

$$W_{\text{atrito, fase 1}} = -\mu_c mg \cdot x_1 = -(0{,}150)(0{,}800)(9{,}80)(0{,}120) = -0{,}141\ \text{J}$$

$$W_{\text{total, fase 1}} = 3{,}60 - 0{,}141 = 3{,}46\ \text{J}$$

Teorema: $W_{\text{total}} = \frac{1}{2}mv_1^2 - 0$

$$v_1 = \sqrt{\dfrac{2 \times 3{,}46}{0{,}800}} = \sqrt{8{,}65} = 2{,}94\ \text{m/s}$$

**Verificação — Fase 2 ($v_1$ até parar, percurso $d = 0{,}500\ \text{m}$):**

$$W_{\text{atrito, fase 2}} = -\mu_c mg\,d = -(0{,}150)(0{,}800)(9{,}80)(0{,}500) = -0{,}588\ \text{J}$$

$$\Delta K = 0 - \dfrac{1}{2}(0{,}800)(2{,}94)^2 = -3{,}46\ \text{J}$$

$$W_{\text{atrito, fase 2}} \approx -3{,}46\ \text{J}\ \checkmark$$

$$\boxed{v_1 = 2{,}94\ \text{m/s}\ \text{ao sair da mola}}$$

---

## Armadilhas & Edge Cases

- **Trabalho depende do deslocamento, não da trajetória** (para força constante). Para forças variáveis ou conservativas, a trajetória importa — ver Cap 7.
- **$W = 0$ não significa força nula:** a normal e a força centrípeta fazem trabalho zero (perpendiculares ao deslocamento), mas existem e são cruciais para o movimento.
- **Sinal de $W$ da mola:** $W_{\text{mola}} = \frac{1}{2}kx_1^2 - \frac{1}{2}kx_2^2$. Se a mola volta para $x=0$ (de $x_1$ para $0$), $W_{\text{mola}} = +\frac{1}{2}kx_1^2 > 0$ — a mola **entrega** energia. Se a força externa a estica, $W_{\text{ext}} = +\frac{1}{2}kX^2 > 0$.
- **Potência × trabalho:** um motor de alta potência não necessariamente faz mais trabalho — apenas faz o mesmo trabalho mais rápido.
- **Unidades:** $1\ \text{kWh} = 3{,}6 \times 10^6\ \text{J}$ (energia elétrica). Não confundir kW (potência) com kWh (energia).

---

## Conexões

- [[Cap 5 — Aplicações das leis de Newton]] ← 2ª Lei como ponto de partida do teorema
- [[Cap 7 — Energia potencial e conservação da energia]] → próximo capítulo (energia potencial + conservação)
- [[Cap 4 — Leis de Newton do movimento]] ← força como grandeza fundamental
- [[Física I]] ← MOC da disciplina
- [[Física]] ← MOC de área

---

## Fontes

- YOUNG, Hugh D.; FREEDMAN, Roger A. **Física I: Mecânica**. 12. ed. São Paulo: Pearson Addison Wesley, 2008. Cap. 6, p. 181–210.
