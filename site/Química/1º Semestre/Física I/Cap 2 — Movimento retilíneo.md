---
title: Cap 2 â€” Movimento retilÃ­neo
description: 'CinemÃ¡tica unidimensional: descreve como um objeto se move ao longo
  de uma reta â€” posiÃ§Ã£o, velocidade e aceleraÃ§Ã£o â€” sem se preocupar com a
  causa do mo…'
tags:
- quimica
date: 2026-04-30
tipo: estudo
disciplina: fisica
semestre: 1
---
# Cap 2 â€” Movimento retilÃ­neo

> CinemÃ¡tica unidimensional: descreve **como** um objeto se move ao longo de uma reta â€” posiÃ§Ã£o, velocidade e aceleraÃ§Ã£o â€” sem se preocupar com a **causa** do movimento (isso Ã© dinÃ¢mica, Cap 4-5).

---

## DefiniÃ§Ã£o

**Movimento retilÃ­neo** Ã© o movimento ao longo de uma linha reta. A cinemÃ¡tica 1D usa trÃªs grandezas fundamentais:

| Grandeza | SÃ­mbolo | Unidade SI |
| -------- | ------- | ---------- |
| PosiÃ§Ã£o | $x$ | m |
| Velocidade | $v$ | m/s |
| AceleraÃ§Ã£o | $a$ | m/sÂ² |

> Todas sÃ£o escalares em 1D (o sinal indica sentido: $+$ ou $-$).

---

## Teoria & Fundamentos

### 2.1 Deslocamento, tempo e velocidade mÃ©dia

**PosiÃ§Ã£o** $x$: coordenada do objeto em relaÃ§Ã£o a um ponto de referÃªncia (origem).

**Deslocamento** $\Delta x$: variaÃ§Ã£o de posiÃ§Ã£o (nÃ£o confundir com distÃ¢ncia percorrida):

$$\Delta x = x_2 - x_1$$

**Velocidade mÃ©dia:**

$$v_{\text{med}} = \dfrac{\Delta x}{\Delta t} = \dfrac{x_2 - x_1}{t_2 - t_1}$$

```
GrÃ¡fico xÃ—t â€” velocidade mÃ©dia = inclinaÃ§Ã£o da secante

  x (m)
  |          â— P2 (t2, x2)
  |         /
  |        /  â† inclinaÃ§Ã£o = Î”x/Î”t = vmÃ©d
  |       /
  |      â— P1 (t1, x1)
  |
  +â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ t (s)
```

### 2.2 Velocidade instantÃ¢nea

Velocidade em um instante exato â€” limite da velocidade mÃ©dia quando $\Delta t \to 0$:

$$v_x = \lim_{\Delta t \to 0} \dfrac{\Delta x}{\Delta t} = \dfrac{dx}{dt}$$

Graficamente: **inclinaÃ§Ã£o da reta tangente** Ã  curva $x(t)$ no ponto $t$.

```
  x (m)
  |        /â† tangente em P = velocidade instantÃ¢nea
  |       /
  |    . P
  |   /
  | .'
  +â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ t (s)
```

- $v_x > 0$: movimento no sentido positivo de $x$
- $v_x < 0$: movimento no sentido negativo de $x$
- $v_x = 0$: partÃ­cula em repouso (ou no ponto de retorno)

**Rapidez** (speed): valor absoluto da velocidade, $|v_x|$ â€” sempre $\geq 0$.

### 2.3 AceleraÃ§Ã£o instantÃ¢nea e mÃ©dia

**AceleraÃ§Ã£o mÃ©dia:**

$$a_{\text{med}} = \dfrac{\Delta v_x}{\Delta t} = \dfrac{v_{x2} - v_{x1}}{t_2 - t_1}$$

**AceleraÃ§Ã£o instantÃ¢nea:**

$$a_x = \dfrac{dv_x}{dt} = \dfrac{d^2x}{dt^2}$$

Graficamente: **inclinaÃ§Ã£o da curva** $v_x(t)$.

> AtenÃ§Ã£o: aceleraÃ§Ã£o e velocidade com sinais opostos â†’ objeto **desacelera** (velocidade diminui em magnitude).

### 2.4 Movimento com aceleraÃ§Ã£o constante (MRUV)

Quando $a_x = \text{constante}$, derivamos as **quatro equaÃ§Ãµes cinemÃ¡ticas**:

| Eq. | FÃ³rmula | Grandeza ausente |
| --- | ------- | ---------------- |
| (1) | $v_x = v_{0x} + a_x t$ | $x$ |
| (2) | $x = x_0 + v_{0x}t + \dfrac{1}{2}a_x t^2$ | $v_x$ |
| (3) | $v_x^2 = v_{0x}^2 + 2a_x(x - x_0)$ | $t$ |
| (4) | $x = x_0 + \dfrac{v_{0x} + v_x}{2}\,t$ | $a_x$ |

Onde:
- $x_0$, $v_{0x}$: posiÃ§Ã£o e velocidade iniciais (em $t = 0$)
- $x$, $v_x$: posiÃ§Ã£o e velocidade em $t$
- $a_x$: aceleraÃ§Ã£o (constante)

**GrÃ¡ficos tÃ­picos do MRUV ($a_x > 0$):**

```
v (m/s)         x (m)
|   /           |    âŒ’
|  /            |   /
| /             |  /
|/              | /
+â”€â”€â”€â”€â”€â”€ t       +â”€â”€â”€â”€â”€â”€ t

vÃ—t: reta         xÃ—t: parÃ¡bola
inclinaÃ§Ã£o=a      abertura para cima se a>0
```

### 2.5 Queda livre de corpos

Caso especial de MRUV: aceleraÃ§Ã£o constante para baixo, $\vec{g}$ (aceleraÃ§Ã£o gravitacional).

No SI, adotando $y$ positivo para cima:

$$a_y = -g = -9{,}80\ \text{m/s}^2$$

As quatro equaÃ§Ãµes cinemÃ¡ticas se aplicam com $a_y = -g$:

$$v_y = v_{0y} - gt$$
$$y = y_0 + v_{0y}t - \dfrac{1}{2}gt^2$$
$$v_y^2 = v_{0y}^2 - 2g(y - y_0)$$

> O valor de $g$ varia ligeiramente com a latitude e altitude, mas usa-se $g = 9{,}80\ \text{m/s}^2$ salvo indicaÃ§Ã£o contrÃ¡ria.

**Fatos importantes da queda livre:**
- No ponto mais alto ($v_y = 0$), a aceleraÃ§Ã£o **nÃ£o Ã© zero** â€” continua sendo $g$ para baixo.
- Objetos de massas diferentes caem com a mesma aceleraÃ§Ã£o (desprezando o ar).

### 2.6 Velocidade e posiÃ§Ã£o por integraÃ§Ã£o *(seÃ§Ã£o complementar)*

Quando $a_x$ **nÃ£o Ã© constante**, integra-se:

$$v_x = v_{0x} + \int_0^t a_x\,dt'$$

$$x = x_0 + \int_0^t v_x\,dt'$$

Graficamente: **Ã¡rea sob a curva** $a_x(t)$ dÃ¡ $\Delta v_x$; **Ã¡rea sob** $v_x(t)$ dÃ¡ $\Delta x$.

---

## FÃ³rmulas & EquaÃ§Ãµes

| FÃ³rmula | DescriÃ§Ã£o |
| ------- | --------- |
| $\Delta x = x_2 - x_1$ | Deslocamento |
| $v_{\text{med}} = \Delta x / \Delta t$ | Velocidade mÃ©dia |
| $v_x = dx/dt$ | Velocidade instantÃ¢nea |
| $a_x = dv_x/dt$ | AceleraÃ§Ã£o instantÃ¢nea |
| $v_x = v_{0x} + a_x t$ | Velocidade em funÃ§Ã£o do tempo (MRUV) |
| $x = x_0 + v_{0x}t + \frac{1}{2}a_x t^2$ | PosiÃ§Ã£o em funÃ§Ã£o do tempo (MRUV) |
| $v_x^2 = v_{0x}^2 + 2a_x\Delta x$ | Velocidade em funÃ§Ã£o da posiÃ§Ã£o (MRUV) |
| $a_y = -g = -9{,}80\ \text{m/s}^2$ | AceleraÃ§Ã£o na queda livre ($y$ positivo para cima) |

---

## Exemplos Resolvidos

**Exemplo 1 â€” Velocidade mÃ©dia e instantÃ¢nea (bÃ¡sico)**

Um carro percorre $120\ \text{km}$ em $1{,}50\ \text{h}$ em linha reta. Calcule a velocidade mÃ©dia em m/s.

**ResoluÃ§Ã£o:**

$$\Delta x = 120\ \text{km} = 1{,}20 \times 10^5\ \text{m}$$
$$\Delta t = 1{,}50\ \text{h} \times 3600\ \text{s/h} = 5400\ \text{s}$$
$$v_{\text{med}} = \dfrac{1{,}20 \times 10^5}{5400} = 22{,}2\ \text{m/s}$$

$$\boxed{v_{\text{med}} = 22{,}2\ \text{m/s} \approx 80\ \text{km/h}}$$

---

**Exemplo 2 â€” MRUV: frenagem de veÃ­culo (intermediÃ¡rio)**

Um automÃ³vel viaja a $v_0 = 30{,}0\ \text{m/s}$ (108 km/h) e freia com aceleraÃ§Ã£o constante $a_x = -5{,}00\ \text{m/s}^2$. (a) Quanto tempo atÃ© parar? (b) Qual a distÃ¢ncia de frenagem?

**ResoluÃ§Ã£o â€” (a):** usar eq. (1), $v_x = 0$:

$$0 = 30{,}0 + (-5{,}00)\,t \implies t = \dfrac{30{,}0}{5{,}00} = 6{,}00\ \text{s}$$

**ResoluÃ§Ã£o â€” (b):** usar eq. (3), $v_x = 0$:

$$0 = (30{,}0)^2 + 2(-5{,}00)\Delta x$$
$$\Delta x = \dfrac{900}{10{,}0} = 90{,}0\ \text{m}$$

$$\boxed{t = 6{,}00\ \text{s} \quad \text{e} \quad \Delta x = 90{,}0\ \text{m}}$$

---

**Exemplo 3 â€” Queda livre com lanÃ§amento vertical (avanÃ§ado)**

Uma bola Ã© lanÃ§ada **para cima** de uma janela a $h = 20{,}0\ \text{m}$ do solo com velocidade inicial $v_0 = 15{,}0\ \text{m/s}$. Tomando $y_0 = 0$ na janela e $y$ positivo para cima:

**(a)** Qual a altura mÃ¡xima atingida acima da janela?  
**(b)** Em que instante a bola atinge o solo?  
**(c)** Qual a velocidade ao atingir o solo?

**ResoluÃ§Ã£o â€” (a)** No ponto mais alto, $v_y = 0$:

$$0 = v_0^2 - 2g\,y_{\max} \implies y_{\max} = \dfrac{v_0^2}{2g} = \dfrac{(15{,}0)^2}{2 \times 9{,}80} = \dfrac{225}{19{,}6} = 11{,}5\ \text{m}$$

**ResoluÃ§Ã£o â€” (b)** Solo: $y = -20{,}0\ \text{m}$:

$$-20{,}0 = 15{,}0\,t - \dfrac{1}{2}(9{,}80)t^2$$
$$4{,}90\,t^2 - 15{,}0\,t - 20{,}0 = 0$$

FÃ³rmula de Bhaskara: $t = \dfrac{15{,}0 \pm \sqrt{225 + 4 \times 4{,}90 \times 20{,}0}}{2 \times 4{,}90} = \dfrac{15{,}0 \pm \sqrt{617}}{9{,}80}$

$\sqrt{617} \approx 24{,}84$

$t_1 = \dfrac{15{,}0 + 24{,}84}{9{,}80} \approx 4{,}07\ \text{s}$ âœ“ (positivo, fisicamente relevante)

**ResoluÃ§Ã£o â€” (c)**:

$$v_y = 15{,}0 - (9{,}80)(4{,}07) = 15{,}0 - 39{,}9 = -24{,}9\ \text{m/s}$$

$$\boxed{y_{\max} = 11{,}5\ \text{m acima da janela};\quad t = 4{,}07\ \text{s};\quad v_y = -24{,}9\ \text{m/s (para baixo)}}$$

---

## Armadilhas & Edge Cases

- **Deslocamento â‰  distÃ¢ncia percorrida:** um objeto que vai e volta pode ter $\Delta x = 0$ mas ter percorrido uma distÃ¢ncia real.
- **AceleraÃ§Ã£o e desaceleraÃ§Ã£o:** se $v_x$ e $a_x$ tÃªm o **mesmo sinal**, o objeto acelera; sinais **opostos**, desacelera. NÃ£o confunda "aceleraÃ§Ã£o negativa" com "desaceleraÃ§Ã£o".
- **$g$ sempre positivo:** $g = 9{,}80\ \text{m/s}^2$ Ã© a **magnitude**. O sinal aparece na equaÃ§Ã£o: $a_y = -g$ (com $y$ positivo para cima).
- **Escolha de origem:** a posiÃ§Ã£o inicial $x_0$ pode ser qualquer valor. Escolha a origem que simplifica o problema.
- **Duas raÃ­zes na equaÃ§Ã£o quadrÃ¡tica:** ao resolver $y(t) = \text{cte}$, podem aparecer dois valores de $t$. Identifique qual Ã© fisicamente relevante (geralmente $t > 0$ e o contexto do problema).

---

## ConexÃµes

- [[Cap 1 â€” Unidades, grandezas fÃ­sicas e vetores]] â† capÃ­tulo anterior (unidades e escalares)
- [[Cap 3 â€” Movimento em duas ou trÃªs dimensÃµes]] â†’ generaliza para 2D e 3D usando vetores
- [[Cap 4 â€” Leis de Newton do movimento]] â†’ explica **por que** hÃ¡ aceleraÃ§Ã£o (causa do movimento)
- [[FÃ­sica I]] â† MOC da disciplina
- [[FÃ­sica]] â† MOC de Ã¡rea

---

## Fontes

- YOUNG, Hugh D.; FREEDMAN, Roger A. **FÃ­sica I: MecÃ¢nica**. 12. ed. SÃ£o Paulo: Pearson Addison Wesley, 2008. Cap. 2, p. 35â€“67.
