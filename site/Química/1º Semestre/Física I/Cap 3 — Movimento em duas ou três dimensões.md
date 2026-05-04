---
title: Cap 3 — Movimento em duas ou três dimensões
description: O movimento no plano e no espaço é descrito pelos mesmos conceitos do
  Cap 2 — posição, velocidade e aceleração — porém agora como vetores. As componentes
  são in…
tags:
- quimica
date: 2026-04-30
tipo: estudo
disciplina: fisica
semestre: 1
---
# Cap 3 — Movimento em duas ou três dimensões

> O movimento no plano e no espaço é descrito pelos mesmos conceitos do Cap 2 — posição, velocidade e aceleração — porém agora como **vetores**. As componentes são independentes: cada eixo obedece às leis do Cap 2 separadamente.

---

## Definição

Em 2D/3D, cada grandeza cinemática é um vetor:

$$\vec{r} = x\,\hat{i} + y\,\hat{j} \quad \text{(posição)}$$
$$\vec{v} = v_x\,\hat{i} + v_y\,\hat{j} \quad \text{(velocidade)}$$
$$\vec{a} = a_x\,\hat{i} + a_y\,\hat{j} \quad \text{(aceleração)}$$

**Princípio fundamental:** as componentes $x$ e $y$ evoluem **independentemente**, cada uma governada pelas equações cinemáticas do Cap 2.

---

## Teoria & Fundamentos

### 3.1 Vetor posição e vetor velocidade

**Vetor posição** de uma partícula no ponto $P(x, y)$:

$$\vec{r} = x\,\hat{i} + y\,\hat{j}$$

**Vetor deslocamento** entre $P_1$ e $P_2$:

$$\Delta\vec{r} = \vec{r}_2 - \vec{r}_1 = (x_2 - x_1)\,\hat{i} + (y_2 - y_1)\,\hat{j}$$

**Velocidade média** (vetor):

$$\vec{v}_{\text{med}} = \dfrac{\Delta\vec{r}}{\Delta t}$$

**Velocidade instantânea** (tangente à trajetória):

$$\vec{v} = \dfrac{d\vec{r}}{dt} = \dfrac{dx}{dt}\,\hat{i} + \dfrac{dy}{dt}\,\hat{j} = v_x\,\hat{i} + v_y\,\hat{j}$$

A velocidade instantânea é sempre **tangente à curva** da trajetória.

```
Trajetória e vetor velocidade:

  y
  |         → v (tangente)
  |        /↗
  |    ●--'   ← partícula em P
  |   /
  |  /  trajetória
  +-────────── x
```

### 3.2 Vetor aceleração

**Aceleração média:**

$$\vec{a}_{\text{med}} = \dfrac{\Delta\vec{v}}{\Delta t}$$

**Aceleração instantânea:**

$$\vec{a} = \dfrac{d\vec{v}}{dt} = \dfrac{d^2\vec{r}}{dt^2} = a_x\,\hat{i} + a_y\,\hat{j}$$

> Em 2D/3D, $\vec{a}$ **não precisa ser paralelo a** $\vec{v}$. Se $\vec{a}$ tem componente perpendicular a $\vec{v}$, a partícula **muda de direção** (mesmo que a rapidez seja constante — ex.: movimento circular uniforme).

### 3.3 Movimento de um projétil

**Lançamento oblíquo**: objeto lançado com velocidade inicial $v_0$ ao ângulo $\alpha$ acima da horizontal.

```
Trajetória parabólica do projétil:

  y
  |         *
  |      *     *
  |    *         *
  |  *             *
  | * α              *
  +●─────────────────●── x
  lançamento        queda
  (x=0, y=0)       (y=0)
```

**Condições iniciais:**

$$v_{0x} = v_0\cos\alpha \qquad v_{0y} = v_0\operatorname{sen}\alpha$$

**Equações do movimento** (aceleração: $a_x = 0$, $a_y = -g$):

| Eixo | Velocidade | Posição |
| ---- | ---------- | ------- |
| $x$ (horizontal) | $v_x = v_{0x} = v_0\cos\alpha$ | $x = v_{0x}\,t$ |
| $y$ (vertical) | $v_y = v_{0y} - gt$ | $y = v_{0y}\,t - \frac{1}{2}gt^2$ |

**Resultados importantes** (para $y_0 = 0$ e queda no mesmo nível):

- **Tempo de voo:** $t_{\text{voo}} = \dfrac{2v_0\operatorname{sen}\alpha}{g}$

- **Alcance horizontal:** $R = \dfrac{v_0^2\operatorname{sen}(2\alpha)}{g}$

- **Altura máxima:** $h_{\max} = \dfrac{(v_0\operatorname{sen}\alpha)^2}{2g}$

- **Alcance máximo:** ocorre quando $\alpha = 45°$ (pois $\operatorname{sen}(2 \times 45°) = \operatorname{sen}(90°) = 1$)

- **Ângulos complementares** ($\alpha$ e $90° - \alpha$) produzem **mesmo alcance**.

### 3.4 Movimento circular

**Movimento circular uniforme (MCU):** rapidez $v$ constante, mas direção de $\vec{v}$ varia → há aceleração.

**Aceleração centrípeta** (centripetal): aponta para o **centro** da trajetória circular.

$$a_{\text{cent}} = \dfrac{v^2}{R}$$

Onde $R$ é o raio da circunferência.

```
Aceleração centrípeta:

         v (tangente)
         ↑
    ────●────
   /    |    \
  |  ←a_c    |   a_c aponta para o centro
   \    |    /
    ────●────
         centro
```

**Período** $T$ (tempo para uma volta completa) e **frequência** $f$:

$$v = \dfrac{2\pi R}{T} = 2\pi R f$$

$$a_{\text{cent}} = \dfrac{4\pi^2 R}{T^2}$$

**Movimento circular não uniforme:** rapidez varia → existe também **aceleração tangencial** $a_{\text{tan}}$ (paralela a $\vec{v}$).

$$a_{\text{total}} = \sqrt{a_{\text{cent}}^2 + a_{\text{tan}}^2}$$

### 3.5 Velocidade relativa

A velocidade de um objeto depende do **referencial** (sistema de coordenadas) do observador.

**Notação:** $\vec{v}_{A/B}$ = velocidade de $A$ em relação a $B$.

**Lei de composição de velocidades** (referencial não relativístico):

$$\vec{v}_{P/A} = \vec{v}_{P/B} + \vec{v}_{B/A}$$

Exemplo: avião ($P$) em relação ao solo ($A$), sabendo a velocidade do avião em relação ao vento ($B$) e do vento em relação ao solo:

$$\vec{v}_{\text{avião/solo}} = \vec{v}_{\text{avião/vento}} + \vec{v}_{\text{vento/solo}}$$

---

## Fórmulas & Equações

| Fórmula | Descrição |
| ------- | --------- |
| $\vec{r} = x\,\hat{i} + y\,\hat{j}$ | Vetor posição (2D) |
| $\vec{v} = d\vec{r}/dt$ | Velocidade instantânea |
| $\vec{a} = d\vec{v}/dt$ | Aceleração instantânea |
| $v_{0x} = v_0\cos\alpha,\; v_{0y} = v_0\operatorname{sen}\alpha$ | Componentes iniciais do projétil |
| $x = v_{0x}\,t,\; y = v_{0y}\,t - \frac{1}{2}gt^2$ | Equações do projétil |
| $R = v_0^2\operatorname{sen}(2\alpha)/g$ | Alcance do projétil |
| $h_{\max} = v_{0y}^2/(2g)$ | Altura máxima |
| $a_{\text{cent}} = v^2/R$ | Aceleração centrípeta |
| $\vec{v}_{P/A} = \vec{v}_{P/B} + \vec{v}_{B/A}$ | Composição de velocidades |

---

## Exemplos Resolvidos

**Exemplo 1 — Alcance e altura máxima (básico)**

Um projétil é lançado com $v_0 = 20{,}0\ \text{m/s}$ e $\alpha = 30{,}0°$. Encontre o alcance $R$ e a altura máxima $h_{\max}$. (Despreze a resistência do ar, $g = 9{,}80\ \text{m/s}^2$)

**Resolução:**

$$v_{0x} = 20{,}0\cos(30{,}0°) = 20{,}0 \times 0{,}866 = 17{,}3\ \text{m/s}$$
$$v_{0y} = 20{,}0\operatorname{sen}(30{,}0°) = 20{,}0 \times 0{,}500 = 10{,}0\ \text{m/s}$$

$$R = \dfrac{v_0^2\operatorname{sen}(2\alpha)}{g} = \dfrac{(20{,}0)^2\operatorname{sen}(60°)}{9{,}80} = \dfrac{400 \times 0{,}866}{9{,}80} = 35{,}3\ \text{m}$$

$$h_{\max} = \dfrac{v_{0y}^2}{2g} = \dfrac{(10{,}0)^2}{2 \times 9{,}80} = \dfrac{100}{19{,}6} = 5{,}10\ \text{m}$$

$$\boxed{R = 35{,}3\ \text{m};\quad h_{\max} = 5{,}10\ \text{m}}$$

---

**Exemplo 2 — Aceleração centrípeta (intermediário)**

Um carro percorre uma curva circular de raio $R = 50{,}0\ \text{m}$ à velocidade constante de $v = 15{,}0\ \text{m/s}$. Calcule: (a) a aceleração centrípeta; (b) o período da volta.

**Resolução — (a):**

$$a_{\text{cent}} = \dfrac{v^2}{R} = \dfrac{(15{,}0)^2}{50{,}0} = \dfrac{225}{50{,}0} = 4{,}50\ \text{m/s}^2$$

**Resolução — (b):**

$$T = \dfrac{2\pi R}{v} = \dfrac{2\pi \times 50{,}0}{15{,}0} = \dfrac{314}{15{,}0} = 20{,}9\ \text{s}$$

$$\boxed{a_{\text{cent}} = 4{,}50\ \text{m/s}^2;\quad T = 20{,}9\ \text{s}}$$

---

**Exemplo 3 — Velocidade relativa com vetores (avançado)**

Um barco pode navegar a $v_{b/á} = 4{,}50\ \text{m/s}$ em relação à água. O rio flui a $v_{á/m} = 3{,}00\ \text{m/s}$ para leste (eixo $+x$). O barco quer atravessar o rio de largura $d = 80{,}0\ \text{m}$ chegando diretamente na margem oposta (norte, eixo $+y$).

**(a)** Em que ângulo $\theta$ (medido a oeste do norte) o barco deve apontar?  
**(b)** Qual o tempo de travessia?

**Resolução — (a):** para que $v_{b/m}$ aponte para norte, a componente $x$ deve ser zero:

$$v_{b/m,x} = v_{b/á}\operatorname{sen}(\theta_{\text{oeste}}) \times (-1) + v_{á/m} = 0$$
$$v_{b/á}\operatorname{sen}\theta = v_{á/m} \implies \operatorname{sen}\theta = \dfrac{3{,}00}{4{,}50} = 0{,}667 \implies \theta = 41{,}8°\ \text{a oeste do norte}$$

**Resolução — (b):** componente norte da velocidade do barco em relação à margem:

$$v_{b/m,y} = v_{b/á}\cos\theta = 4{,}50 \times \cos(41{,}8°) = 4{,}50 \times 0{,}745 = 3{,}35\ \text{m/s}$$

$$t = \dfrac{d}{v_{b/m,y}} = \dfrac{80{,}0}{3{,}35} = 23{,}9\ \text{s}$$

$$\boxed{\theta = 41{,}8°\ \text{(a oeste do norte)};\quad t = 23{,}9\ \text{s}}$$

---

## Armadilhas & Edge Cases

- **Componentes independentes:** o movimento horizontal ($x$) e vertical ($y$) de um projétil são independentes. $a_x = 0$ (sem força horizontal), $a_y = -g$. Nunca misture as equações dos dois eixos.
- **$\alpha = 45°$ maximiza alcance** apenas para $y_{\text{inicial}} = y_{\text{final}}$. Se o projétil cai de uma altura, o ângulo ótimo é menor que $45°$.
- **Velocidade centrípeta constante ≠ sem aceleração:** no MCU a rapidez é constante, mas a aceleração **não é zero** — ela muda a direção de $\vec{v}$. Aceleração zero implica movimento retilíneo.
- **Velocidade relativa em 2D:** a composição $\vec{v}_{P/A} = \vec{v}_{P/B} + \vec{v}_{B/A}$ é uma **soma vetorial** — use componentes, não some as magnitudes diretamente.
- **Ângulos complementares:** $\alpha$ e $(90° - \alpha)$ produzem o mesmo alcance, mas trajetórias diferentes. O maior ângulo dá maior altura máxima.

---

## Conexões

- [[Cap 2 — Movimento retilíneo]] ← extensão para 2D/3D
- [[Cap 4 — Leis de Newton do movimento]] → causa das acelerações aqui estudadas (já criado)
- [[Cap 1 — Unidades, grandezas físicas e vetores]] ← base vetorial (componentes, produtos)
- [[Física I]] ← MOC da disciplina
- [[Física]] ← MOC de área

---

## Fontes

- YOUNG, Hugh D.; FREEDMAN, Roger A. **Física I: Mecânica**. 12. ed. São Paulo: Pearson Addison Wesley, 2008. Cap. 3, p. 69–104.
