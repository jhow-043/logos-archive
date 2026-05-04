---
title: Cap 5 â€” AplicaÃ§Ãµes das leis de Newton
description: 'Com as Leis de Newton estabelecidas, este capÃ­tulo as aplica a situaÃ§Ãµes
  reais: equilÃ­brio de partÃ­culas, dinÃ¢mica com mÃºltiplas forÃ§as, forÃ§as de
  atri…'
tags:
- quimica
date: 2026-04-30
tipo: estudo
disciplina: fisica
semestre: 1
---
# Cap 5 â€” AplicaÃ§Ãµes das leis de Newton

> Com as Leis de Newton estabelecidas, este capÃ­tulo as aplica a situaÃ§Ãµes reais: equilÃ­brio de partÃ­culas, dinÃ¢mica com mÃºltiplas forÃ§as, forÃ§as de atrito e movimento circular. A ferramenta central continua sendo o **diagrama do corpo livre**.

---

## DefiniÃ§Ã£o

Este capÃ­tulo usa sistematicamente a 2Âª Lei ($\sum \vec{F} = m\vec{a}$) em trÃªs contextos:

1. **EquilÃ­brio** ($\vec{a} = \vec{0}$): soma de forÃ§as nula
2. **DinÃ¢mica** ($\vec{a} \neq \vec{0}$): calcular aceleraÃ§Ã£o ou forÃ§a desconhecida
3. **Movimento circular** ($\vec{a} = a_{\text{cent}}$ para o centro): forÃ§a centrÃ­peta

---

## Teoria & Fundamentos

### 5.1 Primeira Lei de Newton: partÃ­culas em equilÃ­brio

Uma partÃ­cula estÃ¡ em **equilÃ­brio** quando $\vec{a} = \vec{0}$, ou seja:

$$\sum F_x = 0 \qquad \sum F_y = 0$$

Isso inclui tanto o **repouso** quanto o **MRU** (movimento retilÃ­neo uniforme).

**Exemplo tÃ­pico â€” objeto suspenso por dois fios:**

```
         â—  (teto)
        /|
   T1  / | T2
      /  |
     /Î¸1 |Î¸2
    /    |
   â—â”€â”€â”€â”€â”€â—â”€â”€ objeto (m)
         â†“ P = mg
```

Para o nÃ³ central em equilÃ­brio:
$$\sum F_x = T_2\cos\theta_2 - T_1\cos\theta_1 = 0$$
$$\sum F_y = T_1\operatorname{sen}\theta_1 + T_2\operatorname{sen}\theta_2 - mg = 0$$

### 5.2 Segunda Lei de Newton: dinÃ¢mica das partÃ­culas

Quando $\vec{a} \neq \vec{0}$, aplica-se:

$$\sum F_x = ma_x \qquad \sum F_y = ma_y$$

**EstratÃ©gia geral:**
1. Desenhar o DCL (diagrama do corpo livre)
2. Escolher eixos convenientes (geralmente $x$ na direÃ§Ã£o da aceleraÃ§Ã£o)
3. Escrever as equaÃ§Ãµes por componente
4. Resolver para as incÃ³gnitas

> Nos problemas com mÃºltiplos corpos, escreva uma equaÃ§Ã£o da 2Âª Lei para **cada corpo separadamente** e use a condiÃ§Ã£o de movimento conjunto (mesma aceleraÃ§Ã£o se conectados por fio inextensÃ­vel).

### 5.3 ForÃ§as de atrito

O atrito Ã© uma forÃ§a de **contato** que atua na interface entre superfÃ­cies, **paralela** Ã  superfÃ­cie e **oposta** ao movimento (ou Ã  tendÃªncia de movimento).

#### Atrito estÃ¡tico ($f_e$)

Impede o inÃ­cio do movimento. Pode ter qualquer valor de $0$ atÃ© $f_{e,\max}$:

$$f_e \leq \mu_e N$$

onde $\mu_e$ Ã© o **coeficiente de atrito estÃ¡tico** e $N$ Ã© a forÃ§a normal.

#### Atrito cinÃ©tico ($f_c$)

Age quando as superfÃ­cies estÃ£o em movimento relativo. Tem magnitude constante:

$$f_c = \mu_c N$$

onde $\mu_c$ Ã© o **coeficiente de atrito cinÃ©tico**.

**RelaÃ§Ã£o importante:** $\mu_c < \mu_e$ (sempre). Ã‰ mais fÃ¡cil manter o movimento do que iniciÃ¡-lo.

```
ForÃ§a de atrito em funÃ§Ã£o da forÃ§a aplicada:

  f
  |        f_e,max = Î¼eÂ·N
  |â”€â”€â”€â”€â”€â”€â”€â”€â—
  |       /â”‚â† deslizamento comeÃ§a
  |      / â”‚  f_c = Î¼cÂ·N (constante)
  |     /  â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  |    /
  |   / (estÃ¡tico: f = F_aplic)
  |  /
  +â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ F_aplicada
```

#### Coeficientes tÃ­picos (aproximados):

| Par de superfÃ­cies | $\mu_e$ | $\mu_c$ |
| ------------------ | ------- | ------- |
| AÃ§o sobre aÃ§o | 0,74 | 0,57 |
| AlumÃ­nio sobre aÃ§o | 0,61 | 0,47 |
| Borracha sobre concreto seco | 1,0 | 0,8 |
| Madeira sobre madeira | 0,25â€“0,5 | 0,2 |
| Teflon sobre aÃ§o | 0,04 | 0,04 |

### 5.4 DinÃ¢mica do movimento circular

Para que uma partÃ­cula percorra uma trajetÃ³ria circular, deve existir uma **forÃ§a resultante** apontando para o centro (forÃ§a centrÃ­peta). Aplicando a 2Âª Lei na direÃ§Ã£o radial (para o centro = positivo):

$$\sum F_{\text{radial}} = \dfrac{mv^2}{R}$$

> "ForÃ§a centrÃ­peta" **nÃ£o Ã©** um novo tipo de forÃ§a â€” Ã© o **papel** que forÃ§as reais (normal, tensÃ£o, gravitaÃ§Ã£o, atrito) desempenham ao curvar a trajetÃ³ria.

**Casos comuns:**

| SituaÃ§Ã£o | ForÃ§a que faz o papel centrÃ­peto |
| -------- | -------------------------------- |
| Carro em curva horizontal | Atrito estÃ¡tico entre pneu e pista |
| Objeto em balanÃ§o circular (corda) | TensÃ£o na corda |
| SatÃ©lite em Ã³rbita | ForÃ§a gravitacional |
| Pista curvada com inclinaÃ§Ã£o (*banked*) | Componente da normal |

```
Carro em curva â€” vista de cima:

        â† f_atrito (centrÃ­peto)
        â—â”€â”€â”€â”€ v (tangente)
       /
      / R
     â—  (centro da curva)
```

### 5.5 As forÃ§as fundamentais da natureza *(seÃ§Ã£o complementar)*

Toda interaÃ§Ã£o na natureza decorre de quatro forÃ§as fundamentais:

| ForÃ§a | Alcance | Exemplo |
| ----- | ------- | ------- |
| Gravitacional | infinito | Ã“rbitas, peso |
| EletromagnÃ©tica | infinito | Atrito, normal, quÃ­mica |
| Nuclear forte | $\sim 10^{-15}$ m | Liga prÃ³tons no nÃºcleo |
| Nuclear fraca | $\sim 10^{-18}$ m | Decaimento radioativo |

> Atrito, normal e traÃ§Ã£o sÃ£o manifestaÃ§Ãµes macroscÃ³picas da forÃ§a **eletromagnÃ©tica** entre Ã¡tomos.

---

## FÃ³rmulas & EquaÃ§Ãµes

| FÃ³rmula | DescriÃ§Ã£o | CondiÃ§Ã£o |
| ------- | --------- | -------- |
| $\sum F_x = 0,\ \sum F_y = 0$ | EquilÃ­brio | $a = 0$ |
| $\sum F_x = ma_x,\ \sum F_y = ma_y$ | 2Âª Lei geral | â€” |
| $f_e \leq \mu_e N$ | Atrito estÃ¡tico mÃ¡ximo | SuperfÃ­cies em repouso relativo |
| $f_c = \mu_c N$ | Atrito cinÃ©tico | SuperfÃ­cies em movimento relativo |
| $\mu_c < \mu_e$ | RelaÃ§Ã£o entre coeficientes | Sempre vÃ¡lido |
| $\sum F_{\text{radial}} = mv^2/R$ | 2Âª Lei no movimento circular | TrajetÃ³ria circular |

---

## Exemplos Resolvidos

**Exemplo 1 â€” EquilÃ­brio com dois fios (bÃ¡sico)**

Um lustre de $m = 15{,}0\ \text{kg}$ Ã© suspenso por dois fios: um faz $\theta_1 = 60{,}0Â°$ e o outro $\theta_2 = 30{,}0Â°$ com a horizontal. Encontre as tensÃµes $T_1$ e $T_2$.

**ResoluÃ§Ã£o:**

$$P = mg = 15{,}0 \times 9{,}80 = 147\ \text{N}$$

EquilÃ­brio:
$$\sum F_x = T_2\cos(30Â°) - T_1\cos(60Â°) = 0 \implies T_2 \times 0{,}866 = T_1 \times 0{,}500 \quad \text{...(i)}$$
$$\sum F_y = T_1\operatorname{sen}(60Â°) + T_2\operatorname{sen}(30Â°) - 147 = 0 \quad \text{...(ii)}$$

De (i): $T_2 = 0{,}577\,T_1$

Substituindo em (ii):
$$T_1 \times 0{,}866 + (0{,}577\,T_1) \times 0{,}500 = 147$$
$$T_1(0{,}866 + 0{,}289) = 147 \implies T_1 = \dfrac{147}{1{,}155} = 127\ \text{N}$$
$$T_2 = 0{,}577 \times 127 = 73{,}3\ \text{N}$$

$$\boxed{T_1 = 127\ \text{N};\quad T_2 = 73{,}3\ \text{N}}$$

---

**Exemplo 2 â€” Plano inclinado com atrito cinÃ©tico (intermediÃ¡rio)**

Uma caixa de $m = 10{,}0\ \text{kg}$ desliza morro abaixo em um plano de $\theta = 37{,}0Â°$ com $\mu_c = 0{,}300$. Calcule a aceleraÃ§Ã£o.

**ResoluÃ§Ã£o:**

Normal (eixo perpendicular ao plano):
$$N = mg\cos\theta = 10{,}0 \times 9{,}80 \times \cos(37Â°) = 98{,}0 \times 0{,}799 = 78{,}3\ \text{N}$$

Atrito cinÃ©tico (oposto ao movimento, ou seja, morro acima):
$$f_c = \mu_c N = 0{,}300 \times 78{,}3 = 23{,}5\ \text{N}$$

2Âª Lei ao longo do plano (positivo morro abaixo):
$$\sum F_x = mg\operatorname{sen}\theta - f_c = ma_x$$
$$10{,}0 \times 9{,}80 \times \operatorname{sen}(37Â°) - 23{,}5 = 10{,}0\,a_x$$
$$98{,}0 \times 0{,}602 - 23{,}5 = 10{,}0\,a_x$$
$$59{,}0 - 23{,}5 = 10{,}0\,a_x$$
$$a_x = \dfrac{35{,}5}{10{,}0} = 3{,}55\ \text{m/s}^2$$

$$\boxed{a = 3{,}55\ \text{m/s}^2\ \text{(morro abaixo)}}$$

---

**Exemplo 3 â€” DinÃ¢mica do movimento circular: pista inclinada (avanÃ§ado)**

Uma pista curva com raio $R = 120\ \text{m}$ estÃ¡ inclinada de $\theta = 18{,}0Â°$ (sem atrito). Qual a velocidade $v$ para a qual o carro percorre a curva sem deslizar?

**DCL (vista frontal):**

```
         N
         â†‘ (perpendicular Ã  pista)
          \
           \ Î¸
            \
          â”€â”€â”€â—â”€â”€â”€   (centro da curva â†’ esquerda)
             â†“
             mg
```

**ResoluÃ§Ã£o:**

Eixo $y$ (vertical): $N\cos\theta - mg = 0 \implies N = \dfrac{mg}{\cos\theta}$

Eixo $x$ (horizontal, em direÃ§Ã£o ao centro):
$$N\operatorname{sen}\theta = \dfrac{mv^2}{R}$$

Dividindo:
$$\operatorname{tg}\theta = \dfrac{v^2}{Rg} \implies v = \sqrt{Rg\operatorname{tg}\theta}$$

$$v = \sqrt{120 \times 9{,}80 \times \operatorname{tg}(18{,}0Â°)} = \sqrt{120 \times 9{,}80 \times 0{,}3249}$$
$$v = \sqrt{381{,}9} = 19{,}5\ \text{m/s}$$

$$\boxed{v = 19{,}5\ \text{m/s}\ (\approx 70\ \text{km/h})}$$

---

## Armadilhas & Edge Cases

- **Atrito estÃ¡tico nÃ£o Ã© sempre $\mu_e N$:** esse Ã© o valor **mÃ¡ximo**. O atrito estÃ¡tico assume qualquer valor de $0$ atÃ© $\mu_e N$ conforme necessÃ¡rio para manter o equilÃ­brio.
- **ForÃ§a centrÃ­peta nÃ£o Ã© forÃ§a real:** nÃ£o aparece no DCL como "forÃ§a centrÃ­peta" â€” Ã© o **resultado lÃ­quido** de forÃ§as reais. Escreva a 2Âª Lei com as forÃ§as reais e iguale a $mv^2/R$.
- **Normal nem sempre Ã© $mg$:** em planos inclinados, aceleradores verticais ou curvas, $N \neq mg$. Sempre derivar $N$ das equaÃ§Ãµes da 2Âª Lei.
- **Sentido do atrito cinÃ©tico:** sempre oposto ao movimento **relativo** entre as superfÃ­cies, nÃ£o ao movimento absoluto. Em uma esteira que puxa um objeto, o atrito pode ser no mesmo sentido que o movimento.
- **$\mu_c < \mu_e$ sempre:** um objeto que estÃ¡ parado precisa de mais forÃ§a para comeÃ§ar a mover do que para manter o movimento.

---

## ConexÃµes

- [[Cap 4 â€” Leis de Newton do movimento]] â† base teÃ³rica (3 leis, DCL)
- [[Cap 3 â€” Movimento em duas ou trÃªs dimensÃµes]] â† aceleraÃ§Ã£o centrÃ­peta ($v^2/R$)
- [[Cap 6 â€” Trabalho e energia cinÃ©tica]] â†’ mÃ©todo energÃ©tico como alternativa Ã  2Âª Lei
- [[FÃ­sica I]] â† MOC da disciplina
- [[FÃ­sica]] â† MOC de Ã¡rea

---

## Fontes

- YOUNG, Hugh D.; FREEDMAN, Roger A. **FÃ­sica I: MecÃ¢nica**. 12. ed. SÃ£o Paulo: Pearson Addison Wesley, 2008. Cap. 5, p. 135â€“170.
