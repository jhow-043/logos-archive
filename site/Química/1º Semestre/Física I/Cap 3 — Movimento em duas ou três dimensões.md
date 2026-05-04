---
title: Cap 3 â€” Movimento em duas ou trÃªs dimensÃµes
description: O movimento no plano e no espaÃ§o Ã© descrito pelos mesmos conceitos
  do Cap 2 â€” posiÃ§Ã£o, velocidade e aceleraÃ§Ã£o â€” porÃ©m agora como vetores.
  As compone…
tags:
- quimica
date: 2026-04-30
tipo: estudo
disciplina: fisica
semestre: 1
---
# Cap 3 â€” Movimento em duas ou trÃªs dimensÃµes

> O movimento no plano e no espaÃ§o Ã© descrito pelos mesmos conceitos do Cap 2 â€” posiÃ§Ã£o, velocidade e aceleraÃ§Ã£o â€” porÃ©m agora como **vetores**. As componentes sÃ£o independentes: cada eixo obedece Ã s leis do Cap 2 separadamente.

---

## DefiniÃ§Ã£o

Em 2D/3D, cada grandeza cinemÃ¡tica Ã© um vetor:

$$\vec{r} = x\,\hat{i} + y\,\hat{j} \quad \text{(posiÃ§Ã£o)}$$
$$\vec{v} = v_x\,\hat{i} + v_y\,\hat{j} \quad \text{(velocidade)}$$
$$\vec{a} = a_x\,\hat{i} + a_y\,\hat{j} \quad \text{(aceleraÃ§Ã£o)}$$

**PrincÃ­pio fundamental:** as componentes $x$ e $y$ evoluem **independentemente**, cada uma governada pelas equaÃ§Ãµes cinemÃ¡ticas do Cap 2.

---

## Teoria & Fundamentos

### 3.1 Vetor posiÃ§Ã£o e vetor velocidade

**Vetor posiÃ§Ã£o** de uma partÃ­cula no ponto $P(x, y)$:

$$\vec{r} = x\,\hat{i} + y\,\hat{j}$$

**Vetor deslocamento** entre $P_1$ e $P_2$:

$$\Delta\vec{r} = \vec{r}_2 - \vec{r}_1 = (x_2 - x_1)\,\hat{i} + (y_2 - y_1)\,\hat{j}$$

**Velocidade mÃ©dia** (vetor):

$$\vec{v}_{\text{med}} = \dfrac{\Delta\vec{r}}{\Delta t}$$

**Velocidade instantÃ¢nea** (tangente Ã  trajetÃ³ria):

$$\vec{v} = \dfrac{d\vec{r}}{dt} = \dfrac{dx}{dt}\,\hat{i} + \dfrac{dy}{dt}\,\hat{j} = v_x\,\hat{i} + v_y\,\hat{j}$$

A velocidade instantÃ¢nea Ã© sempre **tangente Ã  curva** da trajetÃ³ria.

```
TrajetÃ³ria e vetor velocidade:

  y
  |         â†’ v (tangente)
  |        /â†—
  |    â—--'   â† partÃ­cula em P
  |   /
  |  /  trajetÃ³ria
  +-â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ x
```

### 3.2 Vetor aceleraÃ§Ã£o

**AceleraÃ§Ã£o mÃ©dia:**

$$\vec{a}_{\text{med}} = \dfrac{\Delta\vec{v}}{\Delta t}$$

**AceleraÃ§Ã£o instantÃ¢nea:**

$$\vec{a} = \dfrac{d\vec{v}}{dt} = \dfrac{d^2\vec{r}}{dt^2} = a_x\,\hat{i} + a_y\,\hat{j}$$

> Em 2D/3D, $\vec{a}$ **nÃ£o precisa ser paralelo a** $\vec{v}$. Se $\vec{a}$ tem componente perpendicular a $\vec{v}$, a partÃ­cula **muda de direÃ§Ã£o** (mesmo que a rapidez seja constante â€” ex.: movimento circular uniforme).

### 3.3 Movimento de um projÃ©til

**LanÃ§amento oblÃ­quo**: objeto lanÃ§ado com velocidade inicial $v_0$ ao Ã¢ngulo $\alpha$ acima da horizontal.

```
TrajetÃ³ria parabÃ³lica do projÃ©til:

  y
  |         *
  |      *     *
  |    *         *
  |  *             *
  | * Î±              *
  +â—â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â—â”€â”€ x
  lanÃ§amento        queda
  (x=0, y=0)       (y=0)
```

**CondiÃ§Ãµes iniciais:**

$$v_{0x} = v_0\cos\alpha \qquad v_{0y} = v_0\operatorname{sen}\alpha$$

**EquaÃ§Ãµes do movimento** (aceleraÃ§Ã£o: $a_x = 0$, $a_y = -g$):

| Eixo | Velocidade | PosiÃ§Ã£o |
| ---- | ---------- | ------- |
| $x$ (horizontal) | $v_x = v_{0x} = v_0\cos\alpha$ | $x = v_{0x}\,t$ |
| $y$ (vertical) | $v_y = v_{0y} - gt$ | $y = v_{0y}\,t - \frac{1}{2}gt^2$ |

**Resultados importantes** (para $y_0 = 0$ e queda no mesmo nÃ­vel):

- **Tempo de voo:** $t_{\text{voo}} = \dfrac{2v_0\operatorname{sen}\alpha}{g}$

- **Alcance horizontal:** $R = \dfrac{v_0^2\operatorname{sen}(2\alpha)}{g}$

- **Altura mÃ¡xima:** $h_{\max} = \dfrac{(v_0\operatorname{sen}\alpha)^2}{2g}$

- **Alcance mÃ¡ximo:** ocorre quando $\alpha = 45Â°$ (pois $\operatorname{sen}(2 \times 45Â°) = \operatorname{sen}(90Â°) = 1$)

- **Ã‚ngulos complementares** ($\alpha$ e $90Â° - \alpha$) produzem **mesmo alcance**.

### 3.4 Movimento circular

**Movimento circular uniforme (MCU):** rapidez $v$ constante, mas direÃ§Ã£o de $\vec{v}$ varia â†’ hÃ¡ aceleraÃ§Ã£o.

**AceleraÃ§Ã£o centrÃ­peta** (centripetal): aponta para o **centro** da trajetÃ³ria circular.

$$a_{\text{cent}} = \dfrac{v^2}{R}$$

Onde $R$ Ã© o raio da circunferÃªncia.

```
AceleraÃ§Ã£o centrÃ­peta:

         v (tangente)
         â†‘
    â”€â”€â”€â”€â—â”€â”€â”€â”€
   /    |    \
  |  â†a_c    |   a_c aponta para o centro
   \    |    /
    â”€â”€â”€â”€â—â”€â”€â”€â”€
         centro
```

**PerÃ­odo** $T$ (tempo para uma volta completa) e **frequÃªncia** $f$:

$$v = \dfrac{2\pi R}{T} = 2\pi R f$$

$$a_{\text{cent}} = \dfrac{4\pi^2 R}{T^2}$$

**Movimento circular nÃ£o uniforme:** rapidez varia â†’ existe tambÃ©m **aceleraÃ§Ã£o tangencial** $a_{\text{tan}}$ (paralela a $\vec{v}$).

$$a_{\text{total}} = \sqrt{a_{\text{cent}}^2 + a_{\text{tan}}^2}$$

### 3.5 Velocidade relativa

A velocidade de um objeto depende do **referencial** (sistema de coordenadas) do observador.

**NotaÃ§Ã£o:** $\vec{v}_{A/B}$ = velocidade de $A$ em relaÃ§Ã£o a $B$.

**Lei de composiÃ§Ã£o de velocidades** (referencial nÃ£o relativÃ­stico):

$$\vec{v}_{P/A} = \vec{v}_{P/B} + \vec{v}_{B/A}$$

Exemplo: aviÃ£o ($P$) em relaÃ§Ã£o ao solo ($A$), sabendo a velocidade do aviÃ£o em relaÃ§Ã£o ao vento ($B$) e do vento em relaÃ§Ã£o ao solo:

$$\vec{v}_{\text{aviÃ£o/solo}} = \vec{v}_{\text{aviÃ£o/vento}} + \vec{v}_{\text{vento/solo}}$$

---

## FÃ³rmulas & EquaÃ§Ãµes

| FÃ³rmula | DescriÃ§Ã£o |
| ------- | --------- |
| $\vec{r} = x\,\hat{i} + y\,\hat{j}$ | Vetor posiÃ§Ã£o (2D) |
| $\vec{v} = d\vec{r}/dt$ | Velocidade instantÃ¢nea |
| $\vec{a} = d\vec{v}/dt$ | AceleraÃ§Ã£o instantÃ¢nea |
| $v_{0x} = v_0\cos\alpha,\; v_{0y} = v_0\operatorname{sen}\alpha$ | Componentes iniciais do projÃ©til |
| $x = v_{0x}\,t,\; y = v_{0y}\,t - \frac{1}{2}gt^2$ | EquaÃ§Ãµes do projÃ©til |
| $R = v_0^2\operatorname{sen}(2\alpha)/g$ | Alcance do projÃ©til |
| $h_{\max} = v_{0y}^2/(2g)$ | Altura mÃ¡xima |
| $a_{\text{cent}} = v^2/R$ | AceleraÃ§Ã£o centrÃ­peta |
| $\vec{v}_{P/A} = \vec{v}_{P/B} + \vec{v}_{B/A}$ | ComposiÃ§Ã£o de velocidades |

---

## Exemplos Resolvidos

**Exemplo 1 â€” Alcance e altura mÃ¡xima (bÃ¡sico)**

Um projÃ©til Ã© lanÃ§ado com $v_0 = 20{,}0\ \text{m/s}$ e $\alpha = 30{,}0Â°$. Encontre o alcance $R$ e a altura mÃ¡xima $h_{\max}$. (Despreze a resistÃªncia do ar, $g = 9{,}80\ \text{m/s}^2$)

**ResoluÃ§Ã£o:**

$$v_{0x} = 20{,}0\cos(30{,}0Â°) = 20{,}0 \times 0{,}866 = 17{,}3\ \text{m/s}$$
$$v_{0y} = 20{,}0\operatorname{sen}(30{,}0Â°) = 20{,}0 \times 0{,}500 = 10{,}0\ \text{m/s}$$

$$R = \dfrac{v_0^2\operatorname{sen}(2\alpha)}{g} = \dfrac{(20{,}0)^2\operatorname{sen}(60Â°)}{9{,}80} = \dfrac{400 \times 0{,}866}{9{,}80} = 35{,}3\ \text{m}$$

$$h_{\max} = \dfrac{v_{0y}^2}{2g} = \dfrac{(10{,}0)^2}{2 \times 9{,}80} = \dfrac{100}{19{,}6} = 5{,}10\ \text{m}$$

$$\boxed{R = 35{,}3\ \text{m};\quad h_{\max} = 5{,}10\ \text{m}}$$

---

**Exemplo 2 â€” AceleraÃ§Ã£o centrÃ­peta (intermediÃ¡rio)**

Um carro percorre uma curva circular de raio $R = 50{,}0\ \text{m}$ Ã  velocidade constante de $v = 15{,}0\ \text{m/s}$. Calcule: (a) a aceleraÃ§Ã£o centrÃ­peta; (b) o perÃ­odo da volta.

**ResoluÃ§Ã£o â€” (a):**

$$a_{\text{cent}} = \dfrac{v^2}{R} = \dfrac{(15{,}0)^2}{50{,}0} = \dfrac{225}{50{,}0} = 4{,}50\ \text{m/s}^2$$

**ResoluÃ§Ã£o â€” (b):**

$$T = \dfrac{2\pi R}{v} = \dfrac{2\pi \times 50{,}0}{15{,}0} = \dfrac{314}{15{,}0} = 20{,}9\ \text{s}$$

$$\boxed{a_{\text{cent}} = 4{,}50\ \text{m/s}^2;\quad T = 20{,}9\ \text{s}}$$

---

**Exemplo 3 â€” Velocidade relativa com vetores (avanÃ§ado)**

Um barco pode navegar a $v_{b/Ã¡} = 4{,}50\ \text{m/s}$ em relaÃ§Ã£o Ã  Ã¡gua. O rio flui a $v_{Ã¡/m} = 3{,}00\ \text{m/s}$ para leste (eixo $+x$). O barco quer atravessar o rio de largura $d = 80{,}0\ \text{m}$ chegando diretamente na margem oposta (norte, eixo $+y$).

**(a)** Em que Ã¢ngulo $\theta$ (medido a oeste do norte) o barco deve apontar?  
**(b)** Qual o tempo de travessia?

**ResoluÃ§Ã£o â€” (a):** para que $v_{b/m}$ aponte para norte, a componente $x$ deve ser zero:

$$v_{b/m,x} = v_{b/Ã¡}\operatorname{sen}(\theta_{\text{oeste}}) \times (-1) + v_{Ã¡/m} = 0$$
$$v_{b/Ã¡}\operatorname{sen}\theta = v_{Ã¡/m} \implies \operatorname{sen}\theta = \dfrac{3{,}00}{4{,}50} = 0{,}667 \implies \theta = 41{,}8Â°\ \text{a oeste do norte}$$

**ResoluÃ§Ã£o â€” (b):** componente norte da velocidade do barco em relaÃ§Ã£o Ã  margem:

$$v_{b/m,y} = v_{b/Ã¡}\cos\theta = 4{,}50 \times \cos(41{,}8Â°) = 4{,}50 \times 0{,}745 = 3{,}35\ \text{m/s}$$

$$t = \dfrac{d}{v_{b/m,y}} = \dfrac{80{,}0}{3{,}35} = 23{,}9\ \text{s}$$

$$\boxed{\theta = 41{,}8Â°\ \text{(a oeste do norte)};\quad t = 23{,}9\ \text{s}}$$

---

## Armadilhas & Edge Cases

- **Componentes independentes:** o movimento horizontal ($x$) e vertical ($y$) de um projÃ©til sÃ£o independentes. $a_x = 0$ (sem forÃ§a horizontal), $a_y = -g$. Nunca misture as equaÃ§Ãµes dos dois eixos.
- **$\alpha = 45Â°$ maximiza alcance** apenas para $y_{\text{inicial}} = y_{\text{final}}$. Se o projÃ©til cai de uma altura, o Ã¢ngulo Ã³timo Ã© menor que $45Â°$.
- **Velocidade centrÃ­peta constante â‰  sem aceleraÃ§Ã£o:** no MCU a rapidez Ã© constante, mas a aceleraÃ§Ã£o **nÃ£o Ã© zero** â€” ela muda a direÃ§Ã£o de $\vec{v}$. AceleraÃ§Ã£o zero implica movimento retilÃ­neo.
- **Velocidade relativa em 2D:** a composiÃ§Ã£o $\vec{v}_{P/A} = \vec{v}_{P/B} + \vec{v}_{B/A}$ Ã© uma **soma vetorial** â€” use componentes, nÃ£o some as magnitudes diretamente.
- **Ã‚ngulos complementares:** $\alpha$ e $(90Â° - \alpha)$ produzem o mesmo alcance, mas trajetÃ³rias diferentes. O maior Ã¢ngulo dÃ¡ maior altura mÃ¡xima.

---

## ConexÃµes

- [[Cap 2 â€” Movimento retilÃ­neo]] â† extensÃ£o para 2D/3D
- [[Cap 4 â€” Leis de Newton do movimento]] â†’ causa das aceleraÃ§Ãµes aqui estudadas (jÃ¡ criado)
- [[Cap 1 â€” Unidades, grandezas fÃ­sicas e vetores]] â† base vetorial (componentes, produtos)
- [[FÃ­sica I]] â† MOC da disciplina
- [[FÃ­sica]] â† MOC de Ã¡rea

---

## Fontes

- YOUNG, Hugh D.; FREEDMAN, Roger A. **FÃ­sica I: MecÃ¢nica**. 12. ed. SÃ£o Paulo: Pearson Addison Wesley, 2008. Cap. 3, p. 69â€“104.
