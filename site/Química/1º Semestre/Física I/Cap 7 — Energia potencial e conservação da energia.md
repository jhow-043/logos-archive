---
title: Cap 7 — Energia potencial e conservação da energia
description: Quando forças conservativas atuam, podemos armazenar energia no sistema
  como energia potencial e usar o poderoso princípio da conservação da energia mecânica
  —…
tags:
- quimica
date: 2026-04-30
tipo: estudo
disciplina: fisica
semestre: 1
---
> Quando forças conservativas atuam, podemos armazenar energia no sistema como **energia potencial** e usar o poderoso princípio da **conservação da energia mecânica** — que dispensa o cálculo de forças a cada instante.

---

## Definição

**Energia potencial** ($U$) é a energia armazenada em um sistema em função da **configuração** (posição relativa dos objetos). Ela pode ser convertida em energia cinética e vice-versa.

**Lei de conservação da energia mecânica** (válida apenas para forças conservativas):

$$K_i + U_i = K_f + U_f \quad \implies \quad E_{\text{mec}} = K + U = \text{constante}$$

**Energia mecânica total:** $E_{\text{mec}} = K + U$

---

## Teoria & Fundamentos

### 7.1 Energia potencial gravitacional

Define-se a **energia potencial gravitacional** de um objeto em relação a um nível de referência (onde $U_{\text{grav}} = 0$):

$$U_{\text{grav}} = mgy$$

onde $y$ é a altura em relação ao nível de referência escolhido (positivo para cima).

**Trabalho da gravidade em função de $U_{\text{grav}}$:**

$$W_{\text{grav}} = -\Delta U_{\text{grav}} = -(U_f - U_i) = U_i - U_f = mg(y_i - y_f)$$

> O trabalho da gravidade não depende do caminho — apenas da diferença de altura. Essa é a característica das forças **conservativas**.

**Conservação da energia mecânica (só gravidade):**

$$\dfrac{1}{2}mv_i^2 + mgy_i = \dfrac{1}{2}mv_f^2 + mgy_f$$

```
Diagrama energia — queda livre:

  altura  K      U       E_mec
  ──────────────────────────────
  h       0      mgh     mgh
  h/2    ½mgh   ½mgh    mgh
  0       mgh    0       mgh

  E_mec = K + U = constante ✓
```

**Escolha do nível de referência:** $U_{\text{grav}} = 0$ pode ser escolhido em qualquer altura. O que importa é a **diferença** $\Delta U$, nunca o valor absoluto de $U$.

### 7.2 Energia potencial elástica

Uma mola com constante $k$ deformada de $x$ em relação ao equilíbrio armazena:

$$U_{\text{el}} = \dfrac{1}{2}kx^2$$

**Trabalho da força da mola:**

$$W_{\text{mola}} = -\Delta U_{\text{el}} = -\!\left(\dfrac{1}{2}kx_f^2 - \dfrac{1}{2}kx_i^2\right)$$

**Conservação com mola (sem atrito):**

$$\dfrac{1}{2}mv_i^2 + \dfrac{1}{2}kx_i^2 = \dfrac{1}{2}mv_f^2 + \dfrac{1}{2}kx_f^2$$

```
Diagrama energia — oscilação em mola horizontal:

  posição x:   -A    0    +A
                ●────●────●
               máx equil  máx
               U    K     U

  x = ±A (amplitude): K = 0, U = ½kA² (máximo)
  x = 0  (equilíbrio): U = 0, K = ½mv² (máximo)
  E_mec = ½kA² = constante
```

### 7.3 Forças conservativas e forças não conservativas

**Força conservativa:** o trabalho realizado por ela ao mover um objeto entre dois pontos é **independente do caminho** percorrido — depende apenas dos pontos inicial e final.

Equivalentemente: o trabalho em qualquer percurso **fechado** é zero.

$$W_{\text{conservativa, fechado}} = 0$$

**Exemplos:**
- Gravidade ✓
- Força elástica (mola) ✓
- Força elétrica ✓

**Força não conservativa:** o trabalho **depende do caminho**. Energia mecânica não se conserva — parte é convertida em calor, som, deformação.

**Exemplos:**
- Atrito cinético ✗
- Resistência do ar ✗
- Tensão muscular ✗

```
Força conservativa vs. não conservativa:

  Conservativa (gravidade):
  A──────B   W_AB = -ΔU (mesmo por qualquer caminho)
     ou
  A╭────╮B   mesmo W_AB

  Não conservativa (atrito):
  A──────B   W_AB = -f_c × d_AB (depende do comprimento)
     ou
  A╭────╮B   W_AB = -f_c × d_curvo > W anterior
```

**Teorema do Trabalho-Energia generalizado** (forças conservativas e não conservativas):

$$W_{\text{total}} = W_{\text{cons}} + W_{\text{não-cons}} = \Delta K$$

Como $W_{\text{cons}} = -\Delta U$:

$$W_{\text{não-cons}} = \Delta K + \Delta U = \Delta E_{\text{mec}}$$

$$\boxed{W_{\text{não-cons}} = E_{\text{mec},f} - E_{\text{mec},i}}$$

O trabalho das forças não conservativas é igual à **variação** da energia mecânica total. Se $W_{\text{não-cons}} < 0$ (atrito), a energia mecânica diminui — foi convertida em energia interna (calor).

### 7.4 Força e energia potencial

A força conservativa é a **derivada negativa** da energia potencial em relação à posição:

$$F_x = -\dfrac{dU}{dx}$$

Em 3D:

$$\vec{F} = -\left(\dfrac{\partial U}{\partial x}\,\hat{i} + \dfrac{\partial U}{\partial y}\,\hat{j} + \dfrac{\partial U}{\partial z}\,\hat{k}\right) = -\vec{\nabla}U$$

**Verificações:**

- Gravidade: $U = mgy \implies F_y = -d(mgy)/dy = -mg$ ✓ (peso para baixo)
- Mola: $U = \frac{1}{2}kx^2 \implies F_x = -kx$ ✓ (Lei de Hooke)

### 7.5 Diagramas de energia

O gráfico $U(x)$ fornece informações qualitativas sobre o movimento sem resolver equações diferenciais:

$$E_{\text{mec}} = K + U(x) \implies K(x) = E_{\text{mec}} - U(x)$$

```
Diagrama de energia potencial U(x):

  U
  |     ╭─────╮         ← região proibida (K < 0)
  |    /       \   E_mec ─────────────────────────
  |   /         ╰────╮
  |  /    K > 0       \
  | /                  ╰──
  +─────────────────────── x
    x1           x2  x3
    ↑            ↑   ↑
  ponto de     ponto de  assintota
  retorno      retorno   (partícula escapa)
```

- **Pontos de retorno:** onde $U(x) = E_{\text{mec}}$ → $K = 0$ → partícula inverte o sentido
- **Região proibida:** onde $U(x) > E_{\text{mec}}$ → $K < 0$ (impossível classicamente)
- **Equilíbrio estável:** mínimo de $U$ (partícula retorna se perturbada)
- **Equilíbrio instável:** máximo de $U$ (partícula se afasta se perturbada)

---

## Fórmulas & Equações

| Fórmula | Descrição | Unidade |
| ------- | --------- | ------- |
| $U_{\text{grav}} = mgy$ | Energia potencial gravitacional | J |
| $U_{\text{el}} = \frac{1}{2}kx^2$ | Energia potencial elástica | J |
| $W_{\text{cons}} = -\Delta U$ | Trabalho de força conservativa | J |
| $E_{\text{mec}} = K + U$ | Energia mecânica total | J |
| $K_i + U_i = K_f + U_f$ | Conservação (sem forças não conservativas) | J |
| $W_{\text{não-cons}} = \Delta E_{\text{mec}}$ | Variação de energia com atrito | J |
| $F_x = -dU/dx$ | Força a partir da energia potencial | N |

---

## Exemplos Resolvidos

**Exemplo 1 — Conservação com gravidade: velocidade na queda (básico)**

Uma bola de $m = 0{,}500\ \text{kg}$ é lançada do repouso de uma altura $h = 12{,}0\ \text{m}$. Tomando o solo como $U = 0$, encontre a velocidade ao atingir o solo. (Despreze o ar.)

**Resolução:**

$$K_i + U_i = K_f + U_f$$
$$0 + mgh = \dfrac{1}{2}mv_f^2 + 0$$
$$v_f = \sqrt{2gh} = \sqrt{2 \times 9{,}80 \times 12{,}0} = \sqrt{235{,}2} = 15{,}3\ \text{m/s}$$

$$\boxed{v_f = 15{,}3\ \text{m/s}}$$

---

**Exemplo 2 — Mola + gravidade: velocidade máxima (intermediário)**

Um bloco de $m = 2{,}00\ \text{kg}$ comprime uma mola vertical ($k = 800\ \text{N/m}$) de $x = 0{,}100\ \text{m}$ e é liberado do repouso. A mola está na vertical, com o bloco em cima. Tomando a posição de repouso da mola (não comprimida) como $y = 0$ e $U_{\text{grav}} = 0$:

**(a)** Qual a velocidade do bloco quando a mola volta à posição natural ($y = 0$)?  
**(b)** Qual a altura máxima atingida pelo bloco acima de $y = 0$?

**Resolução — (a):** estado inicial: $v_i = 0$, $y_i = -x = -0{,}100\ \text{m}$, mola comprimida de $x$

$$E_i = 0 + mgy_i + \dfrac{1}{2}kx^2 = (2{,}00)(9{,}80)(-0{,}100) + \dfrac{1}{2}(800)(0{,}100)^2$$
$$E_i = -1{,}96 + 4{,}00 = 2{,}04\ \text{J}$$

Estado final ($y = 0$, mola natural):
$$E_f = \dfrac{1}{2}mv_f^2 + 0 + 0$$

Conservação: $E_i = E_f$
$$v_f = \sqrt{\dfrac{2 \times 2{,}04}{2{,}00}} = \sqrt{2{,}04} = 1{,}43\ \text{m/s}$$

**Resolução — (b):** no ponto mais alto $v = 0$, mola natural ($U_{\text{el}} = 0$):

$$E_i = mgy_{\max}$$
$$y_{\max} = \dfrac{E_i}{mg} = \dfrac{2{,}04}{(2{,}00)(9{,}80)} = \dfrac{2{,}04}{19{,}6} = 0{,}104\ \text{m}$$

$$\boxed{v_f = 1{,}43\ \text{m/s};\quad y_{\max} = 0{,}104\ \text{m acima da posição natural}}$$

---

**Exemplo 3 — Conservação com atrito: rampa + superfície horizontal (avançado)**

Um bloco de $m = 3{,}00\ \text{kg}$ desliza por uma rampa sem atrito de altura $h = 4{,}00\ \text{m}$ e em seguida percorre uma superfície horizontal com $\mu_c = 0{,}250$ até parar. Encontre: (a) a velocidade ao pé da rampa; (b) a distância percorrida na horizontal.

**Resolução — (a):** rampa sem atrito → conservação da energia:

$$mgh = \dfrac{1}{2}mv_1^2$$
$$v_1 = \sqrt{2gh} = \sqrt{2 \times 9{,}80 \times 4{,}00} = \sqrt{78{,}4} = 8{,}85\ \text{m/s}$$

**Resolução — (b):** superfície horizontal com atrito, $v_f = 0$:

$$W_{\text{atrito}} = \Delta E_{\text{mec}}$$
$$-\mu_c mg\,d = 0 - \dfrac{1}{2}mv_1^2$$
$$d = \dfrac{v_1^2}{2\mu_c g} = \dfrac{(8{,}85)^2}{2 \times 0{,}250 \times 9{,}80} = \dfrac{78{,}3}{4{,}90} = 16{,}0\ \text{m}$$

**Verificação alternativa** (método completo, de $A$ ao repouso final):

$$W_{\text{não-cons}} = \Delta E_{\text{mec}} = (0 + 0) - (0 + mgh) = -mgh$$
$$-\mu_c mg\,d = -mgh \implies d = \dfrac{h}{\mu_c} = \dfrac{4{,}00}{0{,}250} = 16{,}0\ \text{m}\ \checkmark$$

$$\boxed{v_1 = 8{,}85\ \text{m/s};\quad d = 16{,}0\ \text{m}}$$

---

## Armadilhas & Edge Cases

- **Nível de referência é livre, diferença não:** $U = mgy$ depende da origem escolhida. Mas $\Delta U = mg\Delta y$ é independente da origem — nunca misture origens diferentes dentro do mesmo problema.
- **Conservação só vale sem forças não conservativas** (ou quando $W_{\text{não-cons}} = 0$). Se há atrito, use $W_{\text{não-cons}} = \Delta E_{\text{mec}}$ em vez de $K_i + U_i = K_f + U_f$.
- **$U_{\text{el}} = \frac{1}{2}kx^2$ sempre positiva:** independentemente de compressão ou estiramento, $x^2 > 0$. A mola sempre armazena energia, nunca a "deve".
- **Força conservativa = derivada de $U$:** se $U$ aumenta na direção $+x$, a força aponta para $-x$ (o sinal negativo em $F_x = -dU/dx$). A força "empurra" o sistema para mínimos de $U$.
- **Velocidade máxima:** em sistemas mola-massa ou rampa, a velocidade é máxima onde $K$ é máxima, ou seja, onde $U$ é mínima. No diagrama de energia, é o ponto mais baixo de $U(x)$ abaixo de $E_{\text{mec}}$.

---

## Conexões

- [[Cap 6 — Trabalho e energia cinética]] ← teorema do trabalho-energia (base deste capítulo)
- [[Cap 5 — Aplicações das leis de Newton]] ← atrito como força não conservativa
- [[Cap 4 — Leis de Newton do movimento]] ← origem das forças conservativas
- [[Física I]] ← MOC da disciplina
- [[Física]] ← MOC de área

---

## Fontes

- YOUNG, Hugh D.; FREEDMAN, Roger A. **Física I: Mecânica**. 12. ed. São Paulo: Pearson Addison Wesley, 2008. Cap. 7, p. 213–246.
