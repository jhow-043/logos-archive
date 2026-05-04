---
title: Cap 5 — Aplicações das leis de Newton
description: 'Com as Leis de Newton estabelecidas, este capítulo as aplica a situações
  reais: equilíbrio de partículas, dinâmica com múltiplas forças, forças de atrito
  e movi…'
tags:
- quimica
date: 2026-04-30
tipo: estudo
disciplina: fisica
semestre: 1
---
# Cap 5 — Aplicações das leis de Newton

> Com as Leis de Newton estabelecidas, este capítulo as aplica a situações reais: equilíbrio de partículas, dinâmica com múltiplas forças, forças de atrito e movimento circular. A ferramenta central continua sendo o **diagrama do corpo livre**.

---

## Definição

Este capítulo usa sistematicamente a 2ª Lei ($\sum \vec{F} = m\vec{a}$) em três contextos:

1. **Equilíbrio** ($\vec{a} = \vec{0}$): soma de forças nula
2. **Dinâmica** ($\vec{a} \neq \vec{0}$): calcular aceleração ou força desconhecida
3. **Movimento circular** ($\vec{a} = a_{\text{cent}}$ para o centro): força centrípeta

---

## Teoria & Fundamentos

### 5.1 Primeira Lei de Newton: partículas em equilíbrio

Uma partícula está em **equilíbrio** quando $\vec{a} = \vec{0}$, ou seja:

$$\sum F_x = 0 \qquad \sum F_y = 0$$

Isso inclui tanto o **repouso** quanto o **MRU** (movimento retilíneo uniforme).

**Exemplo típico — objeto suspenso por dois fios:**

```
         ●  (teto)
        /|
   T1  / | T2
      /  |
     /θ1 |θ2
    /    |
   ●─────●── objeto (m)
         ↓ P = mg
```

Para o nó central em equilíbrio:
$$\sum F_x = T_2\cos\theta_2 - T_1\cos\theta_1 = 0$$
$$\sum F_y = T_1\operatorname{sen}\theta_1 + T_2\operatorname{sen}\theta_2 - mg = 0$$

### 5.2 Segunda Lei de Newton: dinâmica das partículas

Quando $\vec{a} \neq \vec{0}$, aplica-se:

$$\sum F_x = ma_x \qquad \sum F_y = ma_y$$

**Estratégia geral:**
1. Desenhar o DCL (diagrama do corpo livre)
2. Escolher eixos convenientes (geralmente $x$ na direção da aceleração)
3. Escrever as equações por componente
4. Resolver para as incógnitas

> Nos problemas com múltiplos corpos, escreva uma equação da 2ª Lei para **cada corpo separadamente** e use a condição de movimento conjunto (mesma aceleração se conectados por fio inextensível).

### 5.3 Forças de atrito

O atrito é uma força de **contato** que atua na interface entre superfícies, **paralela** à superfície e **oposta** ao movimento (ou à tendência de movimento).

#### Atrito estático ($f_e$)

Impede o início do movimento. Pode ter qualquer valor de $0$ até $f_{e,\max}$:

$$f_e \leq \mu_e N$$

onde $\mu_e$ é o **coeficiente de atrito estático** e $N$ é a força normal.

#### Atrito cinético ($f_c$)

Age quando as superfícies estão em movimento relativo. Tem magnitude constante:

$$f_c = \mu_c N$$

onde $\mu_c$ é o **coeficiente de atrito cinético**.

**Relação importante:** $\mu_c < \mu_e$ (sempre). É mais fácil manter o movimento do que iniciá-lo.

```
Força de atrito em função da força aplicada:

  f
  |        f_e,max = μe·N
  |────────●
  |       /│← deslizamento começa
  |      / │  f_c = μc·N (constante)
  |     /  ──────────────────
  |    /
  |   / (estático: f = F_aplic)
  |  /
  +──────────────────── F_aplicada
```

#### Coeficientes típicos (aproximados):

| Par de superfícies | $\mu_e$ | $\mu_c$ |
| ------------------ | ------- | ------- |
| Aço sobre aço | 0,74 | 0,57 |
| Alumínio sobre aço | 0,61 | 0,47 |
| Borracha sobre concreto seco | 1,0 | 0,8 |
| Madeira sobre madeira | 0,25–0,5 | 0,2 |
| Teflon sobre aço | 0,04 | 0,04 |

### 5.4 Dinâmica do movimento circular

Para que uma partícula percorra uma trajetória circular, deve existir uma **força resultante** apontando para o centro (força centrípeta). Aplicando a 2ª Lei na direção radial (para o centro = positivo):

$$\sum F_{\text{radial}} = \dfrac{mv^2}{R}$$

> "Força centrípeta" **não é** um novo tipo de força — é o **papel** que forças reais (normal, tensão, gravitação, atrito) desempenham ao curvar a trajetória.

**Casos comuns:**

| Situação | Força que faz o papel centrípeto |
| -------- | -------------------------------- |
| Carro em curva horizontal | Atrito estático entre pneu e pista |
| Objeto em balanço circular (corda) | Tensão na corda |
| Satélite em órbita | Força gravitacional |
| Pista curvada com inclinação (*banked*) | Componente da normal |

```
Carro em curva — vista de cima:

        ← f_atrito (centrípeto)
        ●──── v (tangente)
       /
      / R
     ●  (centro da curva)
```

### 5.5 As forças fundamentais da natureza *(seção complementar)*

Toda interação na natureza decorre de quatro forças fundamentais:

| Força | Alcance | Exemplo |
| ----- | ------- | ------- |
| Gravitacional | infinito | Órbitas, peso |
| Eletromagnética | infinito | Atrito, normal, química |
| Nuclear forte | $\sim 10^{-15}$ m | Liga prótons no núcleo |
| Nuclear fraca | $\sim 10^{-18}$ m | Decaimento radioativo |

> Atrito, normal e tração são manifestações macroscópicas da força **eletromagnética** entre átomos.

---

## Fórmulas & Equações

| Fórmula | Descrição | Condição |
| ------- | --------- | -------- |
| $\sum F_x = 0,\ \sum F_y = 0$ | Equilíbrio | $a = 0$ |
| $\sum F_x = ma_x,\ \sum F_y = ma_y$ | 2ª Lei geral | — |
| $f_e \leq \mu_e N$ | Atrito estático máximo | Superfícies em repouso relativo |
| $f_c = \mu_c N$ | Atrito cinético | Superfícies em movimento relativo |
| $\mu_c < \mu_e$ | Relação entre coeficientes | Sempre válido |
| $\sum F_{\text{radial}} = mv^2/R$ | 2ª Lei no movimento circular | Trajetória circular |

---

## Exemplos Resolvidos

**Exemplo 1 — Equilíbrio com dois fios (básico)**

Um lustre de $m = 15{,}0\ \text{kg}$ é suspenso por dois fios: um faz $\theta_1 = 60{,}0°$ e o outro $\theta_2 = 30{,}0°$ com a horizontal. Encontre as tensões $T_1$ e $T_2$.

**Resolução:**

$$P = mg = 15{,}0 \times 9{,}80 = 147\ \text{N}$$

Equilíbrio:
$$\sum F_x = T_2\cos(30°) - T_1\cos(60°) = 0 \implies T_2 \times 0{,}866 = T_1 \times 0{,}500 \quad \text{...(i)}$$
$$\sum F_y = T_1\operatorname{sen}(60°) + T_2\operatorname{sen}(30°) - 147 = 0 \quad \text{...(ii)}$$

De (i): $T_2 = 0{,}577\,T_1$

Substituindo em (ii):
$$T_1 \times 0{,}866 + (0{,}577\,T_1) \times 0{,}500 = 147$$
$$T_1(0{,}866 + 0{,}289) = 147 \implies T_1 = \dfrac{147}{1{,}155} = 127\ \text{N}$$
$$T_2 = 0{,}577 \times 127 = 73{,}3\ \text{N}$$

$$\boxed{T_1 = 127\ \text{N};\quad T_2 = 73{,}3\ \text{N}}$$

---

**Exemplo 2 — Plano inclinado com atrito cinético (intermediário)**

Uma caixa de $m = 10{,}0\ \text{kg}$ desliza morro abaixo em um plano de $\theta = 37{,}0°$ com $\mu_c = 0{,}300$. Calcule a aceleração.

**Resolução:**

Normal (eixo perpendicular ao plano):
$$N = mg\cos\theta = 10{,}0 \times 9{,}80 \times \cos(37°) = 98{,}0 \times 0{,}799 = 78{,}3\ \text{N}$$

Atrito cinético (oposto ao movimento, ou seja, morro acima):
$$f_c = \mu_c N = 0{,}300 \times 78{,}3 = 23{,}5\ \text{N}$$

2ª Lei ao longo do plano (positivo morro abaixo):
$$\sum F_x = mg\operatorname{sen}\theta - f_c = ma_x$$
$$10{,}0 \times 9{,}80 \times \operatorname{sen}(37°) - 23{,}5 = 10{,}0\,a_x$$
$$98{,}0 \times 0{,}602 - 23{,}5 = 10{,}0\,a_x$$
$$59{,}0 - 23{,}5 = 10{,}0\,a_x$$
$$a_x = \dfrac{35{,}5}{10{,}0} = 3{,}55\ \text{m/s}^2$$

$$\boxed{a = 3{,}55\ \text{m/s}^2\ \text{(morro abaixo)}}$$

---

**Exemplo 3 — Dinâmica do movimento circular: pista inclinada (avançado)**

Uma pista curva com raio $R = 120\ \text{m}$ está inclinada de $\theta = 18{,}0°$ (sem atrito). Qual a velocidade $v$ para a qual o carro percorre a curva sem deslizar?

**DCL (vista frontal):**

```
         N
         ↑ (perpendicular à pista)
          \
           \ θ
            \
          ───●───   (centro da curva → esquerda)
             ↓
             mg
```

**Resolução:**

Eixo $y$ (vertical): $N\cos\theta - mg = 0 \implies N = \dfrac{mg}{\cos\theta}$

Eixo $x$ (horizontal, em direção ao centro):
$$N\operatorname{sen}\theta = \dfrac{mv^2}{R}$$

Dividindo:
$$\operatorname{tg}\theta = \dfrac{v^2}{Rg} \implies v = \sqrt{Rg\operatorname{tg}\theta}$$

$$v = \sqrt{120 \times 9{,}80 \times \operatorname{tg}(18{,}0°)} = \sqrt{120 \times 9{,}80 \times 0{,}3249}$$
$$v = \sqrt{381{,}9} = 19{,}5\ \text{m/s}$$

$$\boxed{v = 19{,}5\ \text{m/s}\ (\approx 70\ \text{km/h})}$$

---

## Armadilhas & Edge Cases

- **Atrito estático não é sempre $\mu_e N$:** esse é o valor **máximo**. O atrito estático assume qualquer valor de $0$ até $\mu_e N$ conforme necessário para manter o equilíbrio.
- **Força centrípeta não é força real:** não aparece no DCL como "força centrípeta" — é o **resultado líquido** de forças reais. Escreva a 2ª Lei com as forças reais e iguale a $mv^2/R$.
- **Normal nem sempre é $mg$:** em planos inclinados, aceleradores verticais ou curvas, $N \neq mg$. Sempre derivar $N$ das equações da 2ª Lei.
- **Sentido do atrito cinético:** sempre oposto ao movimento **relativo** entre as superfícies, não ao movimento absoluto. Em uma esteira que puxa um objeto, o atrito pode ser no mesmo sentido que o movimento.
- **$\mu_c < \mu_e$ sempre:** um objeto que está parado precisa de mais força para começar a mover do que para manter o movimento.

---

## Conexões

- [[Cap 4 — Leis de Newton do movimento]] ← base teórica (3 leis, DCL)
- [[Cap 3 — Movimento em duas ou três dimensões]] ← aceleração centrípeta ($v^2/R$)
- [[Cap 6 — Trabalho e energia cinética]] → método energético como alternativa à 2ª Lei
- [[Física I]] ← MOC da disciplina
- [[Física]] ← MOC de área

---

## Fontes

- YOUNG, Hugh D.; FREEDMAN, Roger A. **Física I: Mecânica**. 12. ed. São Paulo: Pearson Addison Wesley, 2008. Cap. 5, p. 135–170.
