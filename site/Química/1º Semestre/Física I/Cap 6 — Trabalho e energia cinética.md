---
title: Cap 6 â€” Trabalho e energia cinÃ©tica
description: 'O conceito de energia oferece uma alternativa poderosa Ã  2Âª Lei de
  Newton: em vez de analisar forÃ§as a cada instante, relacionamos o estado inicial
  e final d…'
tags:
- quimica
date: 2026-04-30
tipo: estudo
disciplina: fisica
semestre: 1
---
# Cap 6 â€” Trabalho e energia cinÃ©tica

> O conceito de **energia** oferece uma alternativa poderosa Ã  2Âª Lei de Newton: em vez de analisar forÃ§as a cada instante, relacionamos o estado inicial e final do movimento. O **Teorema do Trabalho-Energia** Ã© o elo central deste capÃ­tulo.

---

## DefiniÃ§Ã£o

**Trabalho** ($W$) Ã© a transferÃªncia de energia de um agente para um objeto por meio de uma forÃ§a. SÃ³ hÃ¡ trabalho quando a forÃ§a tem componente **na direÃ§Ã£o do deslocamento**.

**Energia cinÃ©tica** ($K$) Ã© a energia associada ao **movimento** de um objeto:

$$K = \dfrac{1}{2}mv^2$$

**Teorema do Trabalho-Energia:** o trabalho total realizado sobre uma partÃ­cula Ã© igual Ã  variaÃ§Ã£o de sua energia cinÃ©tica:

$$W_{\text{total}} = \Delta K = K_f - K_i$$

---

## Teoria & Fundamentos

### 6.1 Trabalho

#### ForÃ§a constante e deslocamento reto

Para uma forÃ§a constante $\vec{F}$ que age enquanto o objeto sofre deslocamento $\vec{s}$:

$$W = \vec{F} \cdot \vec{s} = Fs\cos\phi$$

onde $\phi$ Ã© o Ã¢ngulo entre $\vec{F}$ e $\vec{s}$.

```
Trabalho e Ã¢ngulo Ï†:

  caso Ï† = 0Â°:   Fâ†’  sâ†’    W = Fs   (mÃ¡ximo positivo)
  caso Ï† = 90Â°:  Fâ†‘  sâ†’    W = 0    (forÃ§a perpendicular)
  caso Ï† = 180Â°: Fâ†  sâ†’    W = -Fs  (forÃ§a oposta ao deslocamento)
```

**Unidade:** Joule (J) = NÂ·m = kgÂ·mÂ²/sÂ²

**Sinal do trabalho:**

| CondiÃ§Ã£o | Sinal de $W$ | Efeito |
| --------- | ----------- | ------ |
| $0Â° \leq \phi < 90Â°$ | $W > 0$ | Acelera o objeto |
| $\phi = 90Â°$ | $W = 0$ | NÃ£o altera a rapidez |
| $90Â° < \phi \leq 180Â°$ | $W < 0$ | Desacelera o objeto |

> **Importante:** trabalho **nÃ£o Ã©** uma propriedade do objeto â€” Ã© uma grandeza de **processo** (depende da trajetÃ³ria e da forÃ§a aplicada).

#### Trabalho realizado pelo peso

Para um deslocamento vertical $\Delta y = y_f - y_i$ (positivo para cima):

$$W_{\text{peso}} = -mg\Delta y = mg(y_i - y_f)$$

- O peso realiza trabalho **positivo** quando o objeto desce ($y_f < y_i$).
- O peso realiza trabalho **negativo** quando o objeto sobe ($y_f > y_i$).

#### Trabalho realizado pela forÃ§a normal

A forÃ§a normal Ã© sempre perpendicular ao deslocamento ($\phi = 90Â°$), portanto:

$$W_N = 0$$

### 6.2 Energia cinÃ©tica e o Teorema do Trabalho-Energia

**Energia cinÃ©tica:**

$$K = \dfrac{1}{2}mv^2$$

**DemonstraÃ§Ã£o do Teorema (caso 1D, forÃ§a e aceleraÃ§Ã£o constantes):**

Usando $v^2 = v_0^2 + 2a\Delta x$ e $F = ma$:

$$W = F\Delta x = ma\Delta x = m \cdot \dfrac{v^2 - v_0^2}{2} = \dfrac{1}{2}mv^2 - \dfrac{1}{2}mv_0^2 = K_f - K_i$$

$$\boxed{W_{\text{total}} = \Delta K}$$

> O teorema Ã© vÃ¡lido para **forÃ§a variÃ¡vel** e **trajetÃ³ria curva** â€” desde que $W_{\text{total}}$ seja calculado corretamente (ver 6.3).

### 6.3 Trabalho e energia com forÃ§as variÃ¡veis

Quando $F_x$ varia com a posiÃ§Ã£o, o trabalho Ã© a **integral** (Ã¡rea sob a curva $F_x \times x$):

$$W = \int_{x_1}^{x_2} F_x\,dx$$

```
GrÃ¡fico FÃ—x â€” trabalho = Ã¡rea sombreada:

  F (N)
  |  â•”â•â•â•â•â•—
  |  â•‘    â•‘ â† Ã¡rea = W
  |  â•‘    â•šâ•â•â•â•â•â•
  |  â•‘
  +â”€â”€+â”€â”€â”€â”€+â”€â”€â”€â”€ x (m)
     x1   x2
```

**Lei de Hooke â€” mola:**

$$F_{\text{mola}} = -kx$$

onde $k$ Ã© a constante elÃ¡stica (N/m) e $x$ Ã© a deformaÃ§Ã£o em relaÃ§Ã£o ao ponto de equilÃ­brio.

O trabalho realizado pela forÃ§a da mola (de $x_1$ para $x_2$):

$$W_{\text{mola}} = \int_{x_1}^{x_2}(-kx)\,dx = -\dfrac{1}{2}k x_2^2 + \dfrac{1}{2}k x_1^2 = \dfrac{1}{2}k x_1^2 - \dfrac{1}{2}k x_2^2$$

E o trabalho realizado por uma forÃ§a **externa** que estica a mola de $0$ atÃ© $X$:

$$W_{\text{externo}} = \dfrac{1}{2}kX^2$$

```
ForÃ§a da mola vs. deformaÃ§Ã£o:

  F_ext (N)
  |       /
  |      /
  |     / slope = k
  |    /
  |   / W = Ã¡rea do triÃ¢ngulo = Â½kXÂ²
  |  /
  +-/â”€â”€â”€â”€â”€â”€â”€ x (m)
    0    X
```

### 6.4 PotÃªncia

**PotÃªncia** Ã© a taxa de realizaÃ§Ã£o de trabalho â€” trabalho por unidade de tempo:

$$P = \dfrac{dW}{dt} = \vec{F} \cdot \vec{v} = Fv\cos\phi$$

**Unidade:** Watt (W) = J/s = kgÂ·mÂ²/sÂ³

ConversÃ£o comum: $1\ \text{cv (cavalo-vapor)} = 746\ \text{W}$

**PotÃªncia mÃ©dia:**

$$P_{\text{med}} = \dfrac{W}{\Delta t}$$

> PotÃªncia nÃ£o diz **quanto** trabalho foi feito, mas **quÃ£o rÃ¡pido**. Um motor potente faz o mesmo trabalho em menos tempo.

---

## FÃ³rmulas & EquaÃ§Ãµes

| FÃ³rmula | DescriÃ§Ã£o | Unidade |
| ------- | --------- | ------- |
| $W = Fs\cos\phi$ | Trabalho (forÃ§a constante) | J |
| $W = \int_{x_1}^{x_2} F_x\,dx$ | Trabalho (forÃ§a variÃ¡vel) | J |
| $K = \frac{1}{2}mv^2$ | Energia cinÃ©tica | J |
| $W_{\text{total}} = \Delta K = K_f - K_i$ | Teorema do Trabalho-Energia | J |
| $F_{\text{mola}} = -kx$ | Lei de Hooke | N |
| $W_{\text{mola}} = \frac{1}{2}kx_1^2 - \frac{1}{2}kx_2^2$ | Trabalho da mola | J |
| $W_{\text{ext}} = \frac{1}{2}kX^2$ | Trabalho para esticar mola (de 0 a $X$) | J |
| $P = \vec{F}\cdot\vec{v} = Fv\cos\phi$ | PotÃªncia instantÃ¢nea | W |
| $P_{\text{med}} = W/\Delta t$ | PotÃªncia mÃ©dia | W |

---

## Exemplos Resolvidos

**Exemplo 1 â€” Trabalho de mÃºltiplas forÃ§as (bÃ¡sico)**

Uma caixa de $m = 8{,}00\ \text{kg}$ Ã© puxada $3{,}00\ \text{m}$ horizontalmente por uma forÃ§a $F = 25{,}0\ \text{N}$ a $\phi = 37{,}0Â°$ acima da horizontal, em uma superfÃ­cie com $\mu_c = 0{,}200$. Calcule o trabalho de cada forÃ§a e o trabalho total.

**ResoluÃ§Ã£o:**

Normal: $N = mg - F\operatorname{sen}\phi = 8{,}00(9{,}80) - 25{,}0\operatorname{sen}(37Â°) = 78{,}4 - 15{,}0 = 63{,}4\ \text{N}$

Atrito: $f_c = \mu_c N = 0{,}200 \times 63{,}4 = 12{,}7\ \text{N}$

| ForÃ§a | $W$ |
|-------|-----|
| $F$ aplicada | $25{,}0 \times 3{,}00 \times \cos(37Â°) = 75{,}0 \times 0{,}799 = 59{,}9\ \text{J}$ |
| Normal $N$ | $0\ \text{J}$ ($\phi = 90Â°$) |
| Peso $mg$ | $0\ \text{J}$ ($\phi = 90Â°$) |
| Atrito $f_c$ | $-12{,}7 \times 3{,}00 = -38{,}1\ \text{J}$ |

$$W_{\text{total}} = 59{,}9 + 0 + 0 - 38{,}1 = 21{,}8\ \text{J}$$

$$\boxed{W_{\text{total}} = 21{,}8\ \text{J}}$$

---

**Exemplo 2 â€” Teorema do Trabalho-Energia: velocidade final (intermediÃ¡rio)**

Um carro de $m = 1200\ \text{kg}$ parte do repouso e Ã© acelerado por uma forÃ§a resultante constante de $4800\ \text{N}$ por $\Delta x = 100\ \text{m}$. Qual a velocidade ao final do percurso?

**ResoluÃ§Ã£o:**

Trabalho total:
$$W_{\text{total}} = F\Delta x = 4800 \times 100 = 4{,}80 \times 10^5\ \text{J}$$

Pelo Teorema do Trabalho-Energia ($v_i = 0$):
$$W_{\text{total}} = \dfrac{1}{2}mv_f^2 - 0$$
$$v_f = \sqrt{\dfrac{2W}{m}} = \sqrt{\dfrac{2 \times 4{,}80 \times 10^5}{1200}} = \sqrt{800} = 28{,}3\ \text{m/s}$$

$$\boxed{v_f = 28{,}3\ \text{m/s}\ (\approx 102\ \text{km/h})}$$

---

**Exemplo 3 â€” Trabalho da mola + Teorema do Trabalho-Energia (avanÃ§ado)**

Uma mola horizontal ($k = 500\ \text{N/m}$) estÃ¡ comprimida $x_1 = 0{,}120\ \text{m}$ e lanÃ§a um bloco de $m = 0{,}800\ \text{kg}$. A superfÃ­cie tem $\mu_c = 0{,}150$. O bloco percorre $d = 0{,}500\ \text{m}$ atÃ© parar. Encontre a velocidade do bloco no instante em que deixa a mola (em $x = 0$) e verifique a consistÃªncia com a distÃ¢ncia percorrida.

**Fase 1 â€” bloco sai da mola ($x_1 \to 0$):**

$$W_{\text{mola}} = \dfrac{1}{2}kx_1^2 = \dfrac{1}{2}(500)(0{,}120)^2 = \dfrac{1}{2}(500)(0{,}0144) = 3{,}60\ \text{J}$$

$$W_{\text{atrito, fase 1}} = -\mu_c mg \cdot x_1 = -(0{,}150)(0{,}800)(9{,}80)(0{,}120) = -0{,}141\ \text{J}$$

$$W_{\text{total, fase 1}} = 3{,}60 - 0{,}141 = 3{,}46\ \text{J}$$

Teorema: $W_{\text{total}} = \frac{1}{2}mv_1^2 - 0$

$$v_1 = \sqrt{\dfrac{2 \times 3{,}46}{0{,}800}} = \sqrt{8{,}65} = 2{,}94\ \text{m/s}$$

**VerificaÃ§Ã£o â€” Fase 2 ($v_1$ atÃ© parar, percurso $d = 0{,}500\ \text{m}$):**

$$W_{\text{atrito, fase 2}} = -\mu_c mg\,d = -(0{,}150)(0{,}800)(9{,}80)(0{,}500) = -0{,}588\ \text{J}$$

$$\Delta K = 0 - \dfrac{1}{2}(0{,}800)(2{,}94)^2 = -3{,}46\ \text{J}$$

$$W_{\text{atrito, fase 2}} \approx -3{,}46\ \text{J}\ \checkmark$$

$$\boxed{v_1 = 2{,}94\ \text{m/s}\ \text{ao sair da mola}}$$

---

## Armadilhas & Edge Cases

- **Trabalho depende do deslocamento, nÃ£o da trajetÃ³ria** (para forÃ§a constante). Para forÃ§as variÃ¡veis ou conservativas, a trajetÃ³ria importa â€” ver Cap 7.
- **$W = 0$ nÃ£o significa forÃ§a nula:** a normal e a forÃ§a centrÃ­peta fazem trabalho zero (perpendiculares ao deslocamento), mas existem e sÃ£o cruciais para o movimento.
- **Sinal de $W$ da mola:** $W_{\text{mola}} = \frac{1}{2}kx_1^2 - \frac{1}{2}kx_2^2$. Se a mola volta para $x=0$ (de $x_1$ para $0$), $W_{\text{mola}} = +\frac{1}{2}kx_1^2 > 0$ â€” a mola **entrega** energia. Se a forÃ§a externa a estica, $W_{\text{ext}} = +\frac{1}{2}kX^2 > 0$.
- **PotÃªncia Ã— trabalho:** um motor de alta potÃªncia nÃ£o necessariamente faz mais trabalho â€” apenas faz o mesmo trabalho mais rÃ¡pido.
- **Unidades:** $1\ \text{kWh} = 3{,}6 \times 10^6\ \text{J}$ (energia elÃ©trica). NÃ£o confundir kW (potÃªncia) com kWh (energia).

---

## ConexÃµes

- [[Cap 5 â€” AplicaÃ§Ãµes das leis de Newton]] â† 2Âª Lei como ponto de partida do teorema
- [[Cap 7 â€” Energia potencial e conservaÃ§Ã£o da energia]] â†’ prÃ³ximo capÃ­tulo (energia potencial + conservaÃ§Ã£o)
- [[Cap 4 â€” Leis de Newton do movimento]] â† forÃ§a como grandeza fundamental
- [[FÃ­sica I]] â† MOC da disciplina
- [[FÃ­sica]] â† MOC de Ã¡rea

---

## Fontes

- YOUNG, Hugh D.; FREEDMAN, Roger A. **FÃ­sica I: MecÃ¢nica**. 12. ed. SÃ£o Paulo: Pearson Addison Wesley, 2008. Cap. 6, p. 181â€“210.
