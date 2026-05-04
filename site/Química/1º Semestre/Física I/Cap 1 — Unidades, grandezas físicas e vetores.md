---
title: Cap 1 — Unidades, grandezas físicas e vetores
description: Toda medição em Física exige uma unidade de referência. Este capítulo
  estabelece o Sistema Internacional (SI), define grandezas escalares e vetoriais,
  e apresen…
tags:
- quimica
date: 2026-04-30
tipo: estudo
disciplina: fisica
semestre: 1
---
> Toda medição em Física exige uma unidade de referência. Este capítulo estabelece o Sistema Internacional (SI), define grandezas escalares e vetoriais, e apresenta as operações com vetores — ferramentas essenciais para todos os capítulos seguintes.

---

## Definição

**Grandeza física** é tudo aquilo que pode ser medido. Toda grandeza física é expressa como um **valor numérico** acompanhado de uma **unidade de medida**.

- **Grandeza escalar:** descrita completamente por um número e uma unidade. Ex.: massa ($m = 5{,}0\ \text{kg}$), temperatura, tempo.
- **Grandeza vetorial:** exige também uma **direção** e um **sentido** para ser descrita completamente. Ex.: deslocamento, velocidade, força.

> Sem unidade, um número não tem significado físico. Dizer "a distância é 3" é incompleto; "3 metros" é uma afirmação física precisa.

---

## Teoria & Fundamentos

### 1.1 A natureza da Física

A Física busca descrever o mundo natural por meio de leis quantitativas, verificáveis por experimento. O método científico (observação → hipótese → previsão → verificação) é o alicerce da disciplina.

### 1.2 Solução de problemas de física

Young & Freedman propõem uma estratégia em quatro etapas:

1. **Identificar** as grandezas envolvidas e o que se pede
2. **Montar** o modelo: diagrama, lista de dados conhecidos
3. **Executar** os cálculos com as equações corretas
4. **Avaliar** a resposta (ordem de grandeza, coerência de unidades, sinal)

### 1.3 Padrões e unidades — Sistema Internacional (SI)

O SI define sete grandezas-base:

| Grandeza | Unidade SI | Símbolo |
| -------- | ---------- | ------- |
| Comprimento | metro | m |
| Massa | quilograma | kg |
| Tempo | segundo | s |
| Corrente elétrica | ampère | A |
| Temperatura termodinâmica | kelvin | K |
| Quantidade de matéria | mol | mol |
| Intensidade luminosa | candela | cd |

Grandezas derivadas são combinações dessas: velocidade ($\text{m/s}$), força ($\text{N} = \text{kg} \cdot \text{m/s}^2$), energia ($\text{J} = \text{kg} \cdot \text{m}^2/\text{s}^2$).

### 1.4 Coerência e conversão de unidades

**Regra de ouro:** toda equação física deve ser dimensionalmente homogênea — os dois lados devem ter as mesmas dimensões.

**Método das frações unitárias** (fator de conversão):

$$d = 5{,}0\ \text{km} \times \dfrac{1000\ \text{m}}{1\ \text{km}} = 5{,}0 \times 10^3\ \text{m}$$

Prefixos SI mais comuns:

| Prefixo | Símbolo | Fator |
| ------- | ------- | ----- |
| giga | G | $10^9$ |
| mega | M | $10^6$ |
| kilo | k | $10^3$ |
| centi | c | $10^{-2}$ |
| mili | m | $10^{-3}$ |
| micro | μ | $10^{-6}$ |
| nano | n | $10^{-9}$ |

### 1.5 Incerteza e algarismos significativos

Toda medição tem incerteza. O número de **algarismos significativos** (a.s.) indica a precisão:

- **Regra da multiplicação/divisão:** o resultado tem o mesmo número de a.s. que o fator com **menos** a.s.
- **Regra da adição/subtração:** o resultado tem a mesma **casa decimal** que o valor com maior incerteza.

Exemplos:
- $3{,}14 \times 2{,}5 = 7{,}9$ (2 a.s.)
- $12{,}35 + 0{,}1 = 12{,}5$ (1 casa decimal)

### 1.6 Estimativas e ordens de grandeza

Quando a precisão exata não é necessária, estimativas de **ordem de grandeza** (potências de 10) são úteis.

Exemplo: uma pessoa de $70\ \text{kg}$ tem aproximadamente $10^{28}$ átomos — ordem de grandeza $10^{28}$.

### 1.7 Vetores e soma vetorial

Um **vetor** é representado graficamente por uma seta: o comprimento representa a **magnitude** e a orientação da seta indica **direção e sentido**.

Notação: $\vec{A}$, magnitude: $|\vec{A}|$ ou $A$.

**Soma de vetores — método gráfico (ponta a cauda):**

```
       B
      /
     /
    /  A+B (resultante)
   /  ↗
  A→→→
```

- **Propriedade comutativa:** $\vec{A} + \vec{B} = \vec{B} + \vec{A}$
- **Vetor oposto:** $-\vec{A}$ tem mesma magnitude que $\vec{A}$, sentido contrário
- **Subtração:** $\vec{A} - \vec{B} = \vec{A} + (-\vec{B})$

### 1.8 Componentes de vetores

Decompor $\vec{A}$ em componentes ao longo dos eixos $x$ e $y$:

```
  y
  |    /
  |   / |A|
Ay|  /  |
  | /θ  |
  +--------- x
     Ax
```

$$A_x = A \cos\theta \qquad A_y = A \operatorname{sen}\theta$$

$$A = |\vec{A}| = \sqrt{A_x^2 + A_y^2} \qquad \theta = \operatorname{arctg}\!\left(\dfrac{A_y}{A_x}\right)$$

**Soma de vetores por componentes:**

$$\vec{R} = \vec{A} + \vec{B} \implies R_x = A_x + B_x, \quad R_y = A_y + B_y$$

### 1.9 Vetores unitários

Vetores de magnitude 1 que definem direção e sentido dos eixos:

$$\hat{i} \text{ (eixo } x\text{)}, \quad \hat{j} \text{ (eixo } y\text{)}, \quad \hat{k} \text{ (eixo } z\text{)}$$

Representação vetorial completa:

$$\vec{A} = A_x\,\hat{i} + A_y\,\hat{j} + A_z\,\hat{k}$$

### 1.10 Produtos de vetores

**Produto escalar (ponto):**

$$\vec{A} \cdot \vec{B} = AB\cos\phi = A_xB_x + A_yB_y + A_zB_z$$

- Resultado: **escalar**
- $\phi$ = ângulo entre os vetores
- $\vec{A} \cdot \vec{B} = 0$ se $\vec{A} \perp \vec{B}$

**Produto vetorial (cruz):**

$$|\vec{A} \times \vec{B}| = AB\operatorname{sen}\phi$$

- Resultado: **vetor** perpendicular ao plano de $\vec{A}$ e $\vec{B}$
- Direção determinada pela **regra da mão direita**
- Anti-comutativo: $\vec{A} \times \vec{B} = -(\vec{B} \times \vec{A})$

Forma matricial (determinante):

$$\vec{A} \times \vec{B} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ A_x & A_y & A_z \\ B_x & B_y & B_z \end{vmatrix}$$

---

## Fórmulas & Equações

| Símbolo/Equação | Significado | Unidade |
| --------------- | ----------- | ------- |
| $A_x = A\cos\theta$ | Componente $x$ do vetor $\vec{A}$ | mesma de $A$ |
| $A_y = A\operatorname{sen}\theta$ | Componente $y$ do vetor $\vec{A}$ | mesma de $A$ |
| $A = \sqrt{A_x^2 + A_y^2}$ | Magnitude de $\vec{A}$ (2D) | mesma de $A$ |
| $\theta = \operatorname{arctg}(A_y/A_x)$ | Ângulo de $\vec{A}$ com eixo $x$ | rad ou ° |
| $\vec{A} \cdot \vec{B} = AB\cos\phi$ | Produto escalar | escalar |
| $\|\vec{A} \times \vec{B}\| = AB\operatorname{sen}\phi$ | Magnitude do produto vetorial | mesma de $A \cdot B$ |

---

## Exemplos Resolvidos

**Exemplo 1 — Conversão de unidades (básico)**

Uma corrida tem $10{,}0\ \text{km}$. Expresse em metros e em centímetros.

**Resolução:**

$$10{,}0\ \text{km} \times \dfrac{1000\ \text{m}}{1\ \text{km}} = 1{,}00 \times 10^4\ \text{m}$$

$$1{,}00 \times 10^4\ \text{m} \times \dfrac{100\ \text{cm}}{1\ \text{m}} = 1{,}00 \times 10^6\ \text{cm}$$

$$\boxed{10{,}0\ \text{km} = 1{,}00 \times 10^4\ \text{m} = 1{,}00 \times 10^6\ \text{cm}}$$

---

**Exemplo 2 — Componentes e magnitude de vetor (intermediário)**

Um vetor deslocamento $\vec{A}$ tem magnitude $12{,}0\ \text{m}$ e faz ângulo de $37{,}0°$ com o eixo $x$ positivo. Encontre as componentes $A_x$ e $A_y$ e represente $\vec{A}$ em notação de vetores unitários.

**Resolução:**

$$A_x = A\cos\theta = 12{,}0 \times \cos(37{,}0°) = 12{,}0 \times 0{,}7986 \approx 9{,}58\ \text{m}$$

$$A_y = A\operatorname{sen}\theta = 12{,}0 \times \operatorname{sen}(37{,}0°) = 12{,}0 \times 0{,}6018 \approx 7{,}22\ \text{m}$$

Em notação de vetores unitários:

$$\vec{A} = 9{,}58\,\hat{i} + 7{,}22\,\hat{j}\ \text{(m)}$$

$$\boxed{\vec{A} = 9{,}58\,\hat{i} + 7{,}22\,\hat{j}\ \text{m}}$$

---

**Exemplo 3 — Soma de vetores por componentes + produto escalar (avançado)**

Dois vetores força: $\vec{F}_1 = 6{,}00\,\hat{i} + 3{,}00\,\hat{j}\ \text{N}$ e $\vec{F}_2 = -2{,}00\,\hat{i} + 5{,}00\,\hat{j}\ \text{N}$.

**(a)** Encontre a resultante $\vec{R} = \vec{F}_1 + \vec{F}_2$ e sua magnitude.  
**(b)** Calcule o produto escalar $\vec{F}_1 \cdot \vec{F}_2$ e o ângulo entre eles.

**Resolução — (a):**

$$R_x = 6{,}00 + (-2{,}00) = 4{,}00\ \text{N}$$
$$R_y = 3{,}00 + 5{,}00 = 8{,}00\ \text{N}$$
$$\vec{R} = 4{,}00\,\hat{i} + 8{,}00\,\hat{j}\ \text{N}$$
$$|\vec{R}| = \sqrt{4{,}00^2 + 8{,}00^2} = \sqrt{16 + 64} = \sqrt{80} \approx 8{,}94\ \text{N}$$

**Resolução — (b):**

$$\vec{F}_1 \cdot \vec{F}_2 = (6{,}00)(-2{,}00) + (3{,}00)(5{,}00) = -12{,}0 + 15{,}0 = 3{,}00\ \text{N}^2$$

$$|\vec{F}_1| = \sqrt{6^2 + 3^2} = \sqrt{45} = 6{,}71\ \text{N} \qquad |\vec{F}_2| = \sqrt{4 + 25} = \sqrt{29} = 5{,}39\ \text{N}$$

$$\cos\phi = \dfrac{\vec{F}_1 \cdot \vec{F}_2}{|\vec{F}_1||\vec{F}_2|} = \dfrac{3{,}00}{6{,}71 \times 5{,}39} = \dfrac{3{,}00}{36{,}2} = 0{,}0829$$

$$\phi = \arccos(0{,}0829) \approx 85{,}2°$$

$$\boxed{|\vec{R}| \approx 8{,}94\ \text{N};\quad \vec{F}_1 \cdot \vec{F}_2 = 3{,}00\ \text{N}^2;\quad \phi \approx 85{,}2°}$$

---

## Armadilhas & Edge Cases

- **Ângulo de referência errado:** $\cos$ e $\operatorname{sen}$ dependem do ângulo medido a partir do eixo $x$ positivo (sentido anti-horário). Se o vetor estiver em outro quadrante, as componentes podem ter sinal negativo — confie nas componentes, não no valor absoluto.
- **Confundir escalar com vetor:** massa é escalar; peso é vetor. $P = mg$ é magnitude; o vetor peso é $\vec{P} = m\vec{g}$ (aponta para baixo).
- **Arredondamento prematuro:** carregue algarismos extras nos cálculos intermediários; arredonde apenas no resultado final.
- **$\operatorname{arctg}$ ambíguo:** a função $\operatorname{arctg}(A_y/A_x)$ retorna ângulo em $(-90°, 90°)$. Para vetores no 2º e 3º quadrantes, some $180°$ ao resultado.
- **Produto vetorial não é comutativo:** $\vec{A} \times \vec{B} \neq \vec{B} \times \vec{A}$; a inversão muda o sentido da resultante.

---

## Conexões

- [[Física I]] ← MOC da disciplina
- [[Cap 2 — Movimento retilíneo]] → próximo capítulo (aplica unidades e escalares)
- [[Cap 3 — Movimento em duas ou três dimensões]] → usa vetores extensivamente
- [[Matemática I]] — trigonometria e geometria analítica (base para componentes vetoriais)
- [[Física]] ← MOC de área

---

## Fontes

- YOUNG, Hugh D.; FREEDMAN, Roger A. **Física I: Mecânica**. 12. ed. São Paulo: Pearson Addison Wesley, 2008. Cap. 1, p. 1–30.
