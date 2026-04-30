---
title: Grandezas Físicas e Sistema Internacional (SI)
description: Toda medida em Ciência exige uma grandeza (o que se mede), uma unidade
  (a referência padrão) e um número (quantas vezes a unidade cabe na grandeza). O
  Sistema I
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: quimica-geral
semestre: 1
---

# Grandezas Físicas e Sistema Internacional (SI)

> Toda medida em Ciência exige uma **grandeza** (o que se mede), uma **unidade** (a referência padrão) e um **número** (quantas vezes a unidade cabe na grandeza). O **Sistema Internacional de Unidades (SI)** padroniza essas unidades globalmente, garantindo que experimentos realizados em qualquer laboratório do mundo possam ser comparados e reproduzidos.

---

## Definição

> **Definição (BIPM, 2019 — 9ª edição do SI):**
> Uma **grandeza física** é uma propriedade de um fenômeno, corpo ou substância que pode ser quantificada por medição. Toda grandeza é expressa como o produto de um **valor numérico** e uma **unidade de medida**:
>
> $$\text{grandeza} = \text{valor numérico} \times \text{unidade}$$
>
> O **SI** é o sistema de unidades baseado em **sete grandezas de base** independentes, das quais todas as demais grandezas (derivadas) podem ser obtidas.

Em Química, as grandezas mais usadas são: **massa, volume, temperatura, quantidade de matéria, pressão, energia** e **concentração**. Todas derivam das unidades de base do SI.

---

## Teoria & Fundamentos

### As 7 grandezas de base do SI

| Grandeza de base | Símbolo | Unidade SI | Símbolo da unidade |
|-----------------|---------|------------|-------------------|
| Comprimento | $l$ | metro | m |
| Massa | $m$ | quilograma | kg |
| Tempo | $t$ | segundo | s |
| Corrente elétrica | $I$ | ampere | A |
| Temperatura termodinâmica | $T$ | kelvin | K |
| Quantidade de matéria | $n$ | mol | mol |
| Intensidade luminosa | $I_v$ | candela | cd |

> **Em Química, as mais relevantes são: kg, m, s, K e mol.**

### Grandezas derivadas mais usadas em Química

| Grandeza | Símbolo | Expressão em unidades de base | Unidade SI | Unidade prática |
|----------|---------|-------------------------------|-----------|----------------|
| Volume | $V$ | m³ | m³ | L = dm³, mL = cm³ |
| Densidade | $d$ | kg/m³ | kg·m⁻³ | g/cm³ = g/mL |
| Velocidade | $v$ | m/s | m·s⁻¹ | — |
| Pressão | $p$ | kg/(m·s²) | Pa = N/m² | atm, bar, mmHg |
| Energia | $E$ | kg·m²/s² | J = kg·m²·s⁻² | cal, kJ |
| Concentração | $C$ | mol/m³ | mol·m⁻³ | mol/L = M |
| Frequência | $f$ | 1/s | Hz | — |

### Prefixos do SI

Quando os valores são muito grandes ou muito pequenos, usa-se um **prefixo** que multiplica a unidade por uma potência de 10:

| Prefixo | Símbolo | Fator | Exemplo |
|---------|---------|-------|---------|
| giga | G | $10^{9}$ | 1 Gm = 10⁹ m |
| mega | M | $10^{6}$ | 1 MHz = 10⁶ Hz |
| quilo | k | $10^{3}$ | 1 kg = 10³ g |
| hecto | h | $10^{2}$ | 1 hPa = 10² Pa |
| deci | d | $10^{-1}$ | 1 dm = 10⁻¹ m |
| centi | c | $10^{-2}$ | 1 cm = 10⁻² m |
| mili | m | $10^{-3}$ | 1 mL = 10⁻³ L |
| micro | μ | $10^{-6}$ | 1 μg = 10⁻⁶ g |
| nano | n | $10^{-9}$ | 1 nm = 10⁻⁹ m |
| pico | p | $10^{-12}$ | 1 pm = 10⁻¹² m |

### Temperatura: Kelvin, Celsius e Fahrenheit

A temperatura é uma grandeza intensiva que mede a **energia cinética média** das partículas. O SI usa o **kelvin (K)**, mas o laboratório usa frequentemente o **grau Celsius (°C)**.

```
Escala Kelvin (K):       0 K = zero absoluto (menor T possível)
Escala Celsius (°C):     0 °C = ponto de fusão da água (1 atm)
Escala Fahrenheit (°F):  32 °F = ponto de fusão da água (1 atm)

  −273,15 °C           0 °C          100 °C
      │                  │               │
  ────┼──────────────────┼───────────────┼──────▶  Celsius
      │                  │               │
      0 K            273,15 K        373,15 K
  ────┼──────────────────┼───────────────┼──────▶  Kelvin
```

**Conversões:**

$$T(\text{K}) = T(°\text{C}) + 273{,}15$$

$$T(°\text{C}) = T(\text{K}) - 273{,}15$$

$$T(°\text{F}) = \dfrac{9}{5} \cdot T(°\text{C}) + 32$$

$$T(°\text{C}) = \dfrac{5}{9} \cdot [T(°\text{F}) - 32]$$

> **Por que o SI usa kelvin e não Celsius?** Porque muitas leis físicas (lei dos gases ideais, termodinâmica) exigem temperatura **absoluta** — que nunca pode ser negativa. 0 K = zero absoluto = energia cinética mínima.

### Volume: unidades de laboratório

No SI, o volume é medido em **m³**, mas o laboratório usa **litro (L)** e **mililitro (mL)**:

$$1\ \text{m}^3 = 1000\ \text{L} = 10^6\ \text{mL}$$

$$1\ \text{L} = 1\ \text{dm}^3 = 1000\ \text{mL} = 1000\ \text{cm}^3$$

$$1\ \text{mL} = 1\ \text{cm}^3$$

> **Atenção:** 1 mL = 1 cm³, mas 1 L ≠ 1 m³. Erro comum ao converter densidades de g/mL para kg/m³.

### Notação científica

Para lidar com números muito grandes ou muito pequenos sem perder precisão:

$$a \times 10^n \quad \text{onde} \quad 1 \leq a < 10 \quad \text{e} \quad n \in \mathbb{Z}$$

Exemplos em Química:

| Grandeza | Valor | Notação científica |
|----------|-------|-------------------|
| Número de Avogadro | 602 214 076 000 000 000 000 000 | $6{,}022 \times 10^{23}\ \text{mol}^{-1}$ |
| Massa de um próton | 0,000 000 000 000 000 000 000 001 672 kg | $1{,}672 \times 10^{-27}\ \text{kg}$ |
| Diâmetro de um átomo (ordem) | 0,000 000 000 1 m | $1 \times 10^{-10}\ \text{m} = 1\ \text{Å}$ |

---

## Fórmulas & Equações

**Conversão de temperatura:**

$$T(\text{K}) = T(°\text{C}) + 273{,}15$$

**Conversão de volume:**

$$1\ \text{L} = 10^{-3}\ \text{m}^3 \qquad 1\ \text{mL} = 10^{-6}\ \text{m}^3 = 1\ \text{cm}^3$$

**Conversão de densidade (g/mL → kg/m³):**

$$d\ [\text{kg/m}^3] = d\ [\text{g/mL}] \times 1000$$

_Demonstração:_

$$\dfrac{1\ \text{g}}{1\ \text{mL}} = \dfrac{10^{-3}\ \text{kg}}{10^{-6}\ \text{m}^3} = \dfrac{10^{-3}}{10^{-6}}\ \dfrac{\text{kg}}{\text{m}^3} = 10^3\ \dfrac{\text{kg}}{\text{m}^3} = 1000\ \dfrac{\text{kg}}{\text{m}^3}$$

**Notação científica — operações:**

$$a \times 10^m \cdot b \times 10^n = (a \cdot b) \times 10^{m+n}$$

$$\dfrac{a \times 10^m}{b \times 10^n} = \dfrac{a}{b} \times 10^{m-n}$$

---

## Exemplos Resolvidos

**Exemplo 1 — Básico: Conversões de unidades**

> **Enunciado:** Converta:
> (a) $T = 25{,}0\ °\text{C}$ para kelvin.
> (b) $V = 250\ \text{mL}$ para litros e para m³.
> (c) $d = 0{,}789\ \text{g/mL}$ (etanol) para kg/m³.

**Passo 1 — Temperatura.**

$$T(\text{K}) = 25{,}0 + 273{,}15 = 298{,}15\ \text{K} \approx 298\ \text{K}$$

**Passo 2 — Volume.**

$$V = 250\ \text{mL} \times \dfrac{1\ \text{L}}{1000\ \text{mL}} = 0{,}250\ \text{L}$$

$$V = 250\ \text{mL} \times \dfrac{1\ \text{m}^3}{10^6\ \text{mL}} = 2{,}50 \times 10^{-4}\ \text{m}^3$$

**Passo 3 — Densidade.**

$$d = 0{,}789\ \text{g/mL} \times 1000\ \dfrac{\text{kg/m}^3}{\text{g/mL}} = 789\ \text{kg/m}^3$$

$$\boxed{T = 298\ \text{K} \quad;\quad V = 0{,}250\ \text{L} = 2{,}50 \times 10^{-4}\ \text{m}^3 \quad;\quad d = 789\ \text{kg/m}^3}$$

---

**Exemplo 2 — Intermediário: Converter Celsius ↔ Fahrenheit e identificar grandeza de base**

> **Enunciado:** A temperatura de ebulição do etanol é $78{,}4\ °\text{C}$.
> (a) Converta para °F e para K.
> (b) Classifique "temperatura de ebulição" como grandeza de base ou derivada.
> (c) Um estudante afirma que a temperatura de ebulição da água em °F é o dobro da de °C. Verifique.

**Passo 1 — Conversão de T.**

$$T(°\text{F}) = \dfrac{9}{5} \times 78{,}4 + 32 = 141{,}12 + 32 = 173{,}1\ °\text{F}$$

$$T(\text{K}) = 78{,}4 + 273{,}15 = 351{,}55\ \text{K} \approx 351{,}6\ \text{K}$$

**Passo 2 — Classificação.**

Temperatura termodinâmica ($T$) é **grandeza de base** do SI (unidade: kelvin). "Temperatura de ebulição" é apenas o valor dessa grandeza em condição específica.

**Passo 3 — Verificar a afirmação do estudante.**

Ebulição da água: $100\ °\text{C}$ e $212\ °\text{F}$.

$$212 \stackrel{?}{=} 2 \times 100 \implies 212 \neq 200$$

A afirmação é **falsa**. A relação entre as escalas é linear ($T_F = \frac{9}{5}T_C + 32$), não de proporcionalidade direta.

$$\boxed{T_{\text{etanol}} = 173{,}1\ °\text{F} = 351{,}6\ \text{K} \quad;\quad \text{afirmação falsa: } 212\ °\text{F} \neq 2 \times 100\ °\text{C}}$$

---

**Exemplo 3 — Avançado: Análise dimensional e conversão encadeada**

> **Enunciado:** A densidade do ouro é $19{,}3\ \text{g/cm}^3$. Uma barra de ouro tem volume de $0{,}500\ \text{L}$.
> (a) Calcule a massa da barra em kg.
> (b) Expresse a densidade em kg/m³ e em t/m³ (toneladas por metro cúbico).
> (c) Indique as unidades de base do SI envolvidas em cada grandeza.

**Passo 1 — Massa da barra.**

Converter $V = 0{,}500\ \text{L}$ para cm³: $0{,}500\ \text{L} \times 1000\ \text{cm}^3/\text{L} = 500\ \text{cm}^3$

$$m = d \cdot V = 19{,}3\ \dfrac{\text{g}}{\text{cm}^3} \times 500\ \text{cm}^3 = 9650\ \text{g} = 9{,}65\ \text{kg}$$

**Passo 2 — Converter densidade.**

$$d = 19{,}3\ \text{g/cm}^3 \times 1000\ \dfrac{\text{kg/m}^3}{\text{g/cm}^3} = 19\,300\ \text{kg/m}^3$$

$$d = 19\,300\ \dfrac{\text{kg}}{\text{m}^3} \times \dfrac{1\ \text{t}}{1000\ \text{kg}} = 19{,}3\ \text{t/m}^3$$

**Passo 3 — Unidades de base envolvidas.**

| Grandeza | Unidade usada | Unidades de base SI |
|----------|--------------|---------------------|
| Massa ($m$) | kg | **kg** (base) |
| Volume ($V$) | L = dm³ | **m³** (comprimento³) |
| Densidade ($d$) | g/cm³ → kg/m³ | **kg · m⁻³** |

$$\boxed{m = 9{,}65\ \text{kg} \quad;\quad d = 19\,300\ \text{kg/m}^3 = 19{,}3\ \text{t/m}^3}$$

---

## Armadilhas & Edge Cases

- **kg ≠ g como unidade de base:** a unidade de massa no SI é o **quilograma (kg)**, não o grama. É a única unidade de base que contém um prefixo. Consequência: 1 g = 10⁻³ kg, e densidade 1 g/mL = 1000 kg/m³.
- **Kelvin não usa "grau":** escreve-se $298\ \text{K}$, não $298\ °\text{K}$. O símbolo correto é K (sem símbolo de grau).
- **Conversão Celsius → Kelvin:** $+273{,}15$, não $+273$. Em cálculos de precisão, a diferença importa.
- **1 mL = 1 cm³ ≠ 1 m³:** confusão clássica. O cubo de 1 m de aresta tem volume 1 m³ = 10⁶ cm³ = 10⁶ mL = 1000 L.
- **Prefixo "m" (mili) ≠ grandeza "m" (metro):** $\text{mm}$ = milímetro (prefixo mili + metro); $\text{ms}$ = milissegundo. Ler o contexto para não confundir.
- **Fahrenheit em contexto internacional:** nas ciências, Celsius e Kelvin são universais. Fahrenheit só aparece em contextos norte-americanos e em algumas conversões de problema.
- **Análise dimensional como verificação:** se o resultado de um cálculo tiver unidades erradas, o cálculo está errado. Sempre verificar as unidades ao final.

---

## Conexões

- [[Misturas Homogêneas, Heterogêneas e Coloides]] — nota anterior (concentração de misturas já usa g/L e %m/V)
- [[Fundamentos de Química I]] — MOC da disciplina
- [[Química]] — MOC da área
- [[Química]] — Roadmap da graduação
- [[1º Semestre]] — Semestre ativo
- [[Matemática I]] — Notação científica, potências de 10, álgebra dimensional
- [[Física]] — Grandezas físicas, SI, análise dimensional
- [[Algarismos Significativos]] — próximo tópico da U1

---

## Fontes

- ATKINS, P.; JONES, L. *Princípios de Química: Questionando a vida moderna e o meio ambiente*. 5ª ed. Porto Alegre: Bookman, 2011. Cap. 1 (Apêndice de unidades).
- BROWN, T. L. et al. *Química: A Ciência Central*. 9ª ed. São Paulo: Pearson Prentice Hall, 2005. Apêndice B — Unidades SI.
- BIPM. *The International System of Units (SI)*. 9ª ed., 2019. Disponível em: https://www.bipm.org/en/publications/si-brochure
- Material da disciplina: *U1 - Conceitos fundamentais de química* (PDF fornecido pela professora, 2026).
