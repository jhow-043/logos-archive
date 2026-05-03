---
title: Algarismos Significativos
description: Toda medida experimental carrega incerteza. Os algarismos significativos
  (AS) são os dígitos de um número que carregam informação real sobre a medida — incluind
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: quimica-geral
semestre: 1
---

# Algarismos Significativos

> Toda medida experimental carrega incerteza. Os **algarismos significativos (AS)** são os dígitos de um número que carregam informação real sobre a medida — incluindo o último dígito incerto (estimado). Saber contar e operar com AS é essencial para comunicar resultados experimentais com a honestidade adequada.

---

## Definição

> **Definição (Brown et al., 2005, cap. 1; Atkins & Jones, 2011, cap. 1):**
> Os **algarismos significativos** de um número são todos os dígitos certos mais o **primeiro dígito incerto** (estimado) registrado numa medida. Representam o limite real de precisão do instrumento ou do método utilizado.

Consequências diretas:

- O número de AS reflete a **qualidade da medida**, não apenas o valor numérico.
- $25{,}0\ \text{g}$ tem 3 AS; $25{,}00\ \text{g}$ tem 4 AS — e são informações **diferentes** sobre a medida.
- Em cálculos, o resultado não pode ser **mais preciso** que a medida menos precisa.

---

## Teoria & Fundamentos

### Regras para contar algarismos significativos

**Regra 1 — Dígitos não-zero são sempre significativos.**

$$1{,}234 \rightarrow 4\ \text{AS} \qquad 56 \rightarrow 2\ \text{AS} \qquad 9{,}8765 \rightarrow 5\ \text{AS}$$

**Regra 2 — Zeros intercalados (entre dígitos não-zero) são sempre significativos.**

$$1{,}002 \rightarrow 4\ \text{AS} \qquad 30{,}05 \rightarrow 4\ \text{AS} \qquad 50007 \rightarrow 5\ \text{AS}$$

**Regra 3 — Zeros à esquerda (antes do primeiro dígito não-zero) NÃO são significativos.** São apenas localizadores de casa decimal.

$$0{,}025 \rightarrow 2\ \text{AS} \qquad 0{,}0034 \rightarrow 2\ \text{AS} \qquad 0{,}00100 \rightarrow 3\ \text{AS}$$

**Regra 4 — Zeros à direita em números com ponto decimal são significativos.**

$$2{,}500 \rightarrow 4\ \text{AS} \qquad 10{,}0 \rightarrow 3\ \text{AS} \qquad 1{,}00 \times 10^3 \rightarrow 3\ \text{AS}$$

**Regra 5 — Zeros à direita em números inteiros sem ponto decimal são ambíguos.** Use notação científica para eliminar a ambiguidade.

$$3000 \rightarrow \text{ambíguo: 1, 2, 3 ou 4 AS?}$$
$$3{,}0 \times 10^3 \rightarrow 2\ \text{AS} \qquad 3{,}000 \times 10^3 \rightarrow 4\ \text{AS}$$

**Regra 6 — Números exatos têm infinitos AS.** Contagens (12 maçãs) e definições (1 kg = 1000 g) não limitam o número de AS do resultado.

### Resumo visual das regras

```
Número        AS    Regra aplicada
─────────────────────────────────────────────────
1 2 3 4       4     Dígitos não-zero (R1)
1 0 0 2       4     Zeros intercalados (R2)
0,0 0 2 5     2     Zeros à esquerda não contam (R3)
0,0 0 1 0 0   3     Zero à esq. não conta; zeros
                    à direita com ponto contam (R3+R4)
2,5 0 0       4     Zeros à direita com ponto (R4)
3 0 0 0       ?     Ambíguo → usar notação científica (R5)
1 2 unidades  ∞     Número exato (R6)
```

### Regras para operações com AS

**Adição e Subtração — alinha-se pela casa decimal:**

> O resultado deve ter o mesmo **número de casas decimais** que o componente com **menos casas decimais**.

$$\underbrace{12{,}11}_{\text{2 dec.}} + \underbrace{18{,}0}_{\text{1 dec.}} + \underbrace{1{,}013}_{\text{3 dec.}} = 31{,}123 \xrightarrow{\text{arredonda}} 31{,}1 \quad (1\ \text{casa decimal})$$

**Multiplicação e Divisão — conta-se o número de AS:**

> O resultado deve ter o mesmo **número de AS** que o fator com **menos AS**.

$$\underbrace{4{,}56}_{\text{3 AS}} \times \underbrace{1{,}4}_{\text{2 AS}} = 6{,}384 \xrightarrow{\text{arredonda}} 6{,}4 \quad (2\ \text{AS})$$

**Regra do arredondamento:**

- Se o dígito a eliminar for **< 5**: trunca (arredonda para baixo).
- Se o dígito a eliminar for **> 5**: arredonda para cima.
- Se o dígito a eliminar for **exatamente 5**: arredonda para o **dígito par** mais próximo (regra do arredondamento bancário).

$$2{,}35 \rightarrow 2{,}4 \qquad 2{,}45 \rightarrow 2{,}4 \qquad 2{,}55 \rightarrow 2{,}6$$

### Operações em cadeia

Em cálculos com várias etapas, **não arredonde os resultados intermediários** — guarde todos os dígitos e arredonde apenas o resultado final. Arredondamento prematuro acumula erro.

---

## Fórmulas & Equações

**Densidade com AS corretos:**

$$d = \dfrac{m}{V} = \dfrac{\overbrace{25{,}5\ \text{g}}^{3\ \text{AS}}}{\underbrace{3{,}42\ \text{mL}}_{3\ \text{AS}}} = 7{,}456\ldots \approx 7{,}46\ \text{g/mL} \quad (3\ \text{AS})$$

**Notação científica como ferramenta de AS:**

$$a \times 10^n \implies \text{número de AS} = \text{dígitos em}\ a$$

Exemplos:

| Número | Notação científica | AS |
|--------|-------------------|-----|
| 0,00420 | $4{,}20 \times 10^{-3}$ | 3 |
| 5000 | $5 \times 10^3$ | 1 (ou ambíguo) |
| 5000,0 | $5{,}0000 \times 10^3$ | 5 |
| 0,000100 | $1{,}00 \times 10^{-4}$ | 3 |

---

## Exemplos Resolvidos

**Exemplo 1 — Básico: Contar algarismos significativos**

> **Enunciado:** Determine o número de AS em cada medida:
> (a) $0{,}00340\ \text{g}$ — (b) $1{,}0050\ \text{L}$ — (c) $3500\ \text{m}$ — (d) $3{,}500 \times 10^3\ \text{m}$ — (e) $100{,}0\ \text{mL}$ — (f) $0{,}040\ \text{kg}$

**Passo 1 — Aplicar as 6 regras.**

| Medida | Análise | AS |
|--------|---------|-----|
| (a) $0{,}00340$ | Zeros à esq. não contam; 3, 4, 0 final contam | **3** |
| (b) $1{,}0050$ | 1, 0 (intercalado), 0 (intercalado), 5, 0 (final c/ ponto) | **5** |
| (c) $3500$ | Zeros à direita sem ponto → ambíguo | **ambíguo (2–4)** |
| (d) $3{,}500 \times 10^3$ | Dígitos em 3,500: 3, 5, 0, 0 | **4** |
| (e) $100{,}0$ | 1, 0 (intercalado), 0 (intercalado), 0 (final c/ ponto) | **4** |
| (f) $0{,}040$ | Zero à esq. não conta; 4, 0 (final c/ ponto) contam | **2** |

$$\boxed{\text{(a) 3} \mid \text{(b) 5} \mid \text{(c) ambíguo} \mid \text{(d) 4} \mid \text{(e) 4} \mid \text{(f) 2}}$$

---

**Exemplo 2 — Intermediário: Operações com AS**

> **Enunciado:** Realize cada operação e expresse o resultado com o número correto de AS.
> (a) $13{,}7\ \text{g} + 0{,}2984\ \text{g} + 4{,}23\ \text{g}$
> (b) $5{,}678\ \text{cm} \times 2{,}1\ \text{cm}$
> (c) $\dfrac{11{,}3\ \text{g}}{4{,}150\ \text{mL}}$

**Passo 1 — (a) Adição: reger pela menor quantidade de casas decimais.**

$$13{,}\mathbf{7} + 0{,}2984 + 4{,}\mathbf{23} = 18{,}2284 \xrightarrow{1\ \text{casa decimal}} \mathbf{18{,}2}\ \text{g}$$

O limite é $13{,}7$ (1 casa decimal).

**Passo 2 — (b) Multiplicação: reger pelo menor número de AS.**

$$5{,}678 \times 2{,}1 = 11{,}9238 \xrightarrow{2\ \text{AS}} \mathbf{12}\ \text{cm}^2$$

O limite é $2{,}1$ (2 AS).

**Passo 3 — (c) Divisão: reger pelo menor número de AS.**

$$\dfrac{11{,}3}{4{,}150} = 2{,}7229\ldots \xrightarrow{3\ \text{AS}} \mathbf{2{,}72}\ \text{g/mL}$$

O limite é $11{,}3$ (3 AS).

$$\boxed{\text{(a) } 18{,}2\ \text{g} \mid \text{(b) } 12\ \text{cm}^2 \mid \text{(c) } 2{,}72\ \text{g/mL}}$$

---

**Exemplo 3 — Avançado: Cálculo em cadeia com AS + interpretação experimental**

> **Enunciado:** Um estudante mede a massa e o volume de uma amostra de alumínio em três tentativas:
>
> | Tentativa | Massa (g) | Volume (mL) |
> |-----------|----------|------------|
> | 1 | 13,57 | 5,02 |
> | 2 | 13,5 | 5,0 |
> | 3 | 13,574 | 5,020 |
>
> (a) Calcule a densidade em cada tentativa com o número correto de AS.
> (b) Qual tentativa tem maior precisão? Justifique usando AS.
> (c) A densidade do alumínio é $2{,}70\ \text{g/mL}$. O estudante acertou o valor?

**Passo 1 — Calcular densidades com AS.**

Tentativa 1: $d = \dfrac{13{,}57}{5{,}02} = 2{,}7032\ldots$ → limite: 3 AS ($5{,}02$) → $d = \mathbf{2{,}70}\ \text{g/mL}$

Tentativa 2: $d = \dfrac{13{,}5}{5{,}0} = 2{,}70$ → limite: 2 AS ($13{,}5$ e $5{,}0$) → $d = \mathbf{2{,}7}\ \text{g/mL}$

Tentativa 3: $d = \dfrac{13{,}574}{5{,}020} = 2{,}7040\ldots$ → limite: 4 AS ($5{,}020$) → $d = \mathbf{2{,}704}\ \text{g/mL}$

**Passo 2 — Comparar precisão.**

| Tentativa | Resultado | AS | Precisão |
|-----------|----------|-----|---------|
| 1 | $2{,}70\ \text{g/mL}$ | 3 | Média |
| 2 | $2{,}7\ \text{g/mL}$ | 2 | **Menor** |
| 3 | $2{,}704\ \text{g/mL}$ | 4 | **Maior** |

A Tentativa 3 tem maior precisão porque os instrumentos usados (balança com ±0,001 g e proveta com ±0,001 mL) fornecem mais dígitos confiáveis.

**Passo 3 — Comparar com o valor aceito.**

- Tentativa 1: $2{,}70\ \text{g/mL}$ ✅ (3 AS — concorda com o valor aceito)
- Tentativa 2: $2{,}7\ \text{g/mL}$ ✅ (2 AS — concorda dentro do limite de precisão)
- Tentativa 3: $2{,}704\ \text{g/mL}$ — difere no 4º AS, pode indicar erro sistemático pequeno ou o valor aceito tem apenas 3 AS de precisão

$$\boxed{d_1 = 2{,}70\ \text{g/mL} \mid d_2 = 2{,}7\ \text{g/mL} \mid d_3 = 2{,}704\ \text{g/mL} \mid \text{Tentativa 3 mais precisa}}$$

---

## Armadilhas & Edge Cases

- **Zeros à direita sem ponto decimal são ambíguos:** escrever $3500$ não informa quantos AS há. Sempre use notação científica: $3{,}50 \times 10^3$ (3 AS) ou $3{,}500 \times 10^3$ (4 AS).
- **Não confundir casas decimais com AS:** $0{,}0034$ tem 2 AS mas 4 casas decimais. São conceitos diferentes.
- **Arredondamento prematuro:** nunca arredonde resultados intermediários em cálculos em cadeia. Arredonde apenas o resultado final.
- **Número exato não limita AS:** se você multiplica $\pi \times r^2$ e o raio $r$ tem 3 AS, o resultado tem 3 AS — o "2" do expoente é exato (não limita).
- **Regra do dígito 5:** ao arredondar $2{,}45$ para 1 casa decimal, o resultado correto é $2{,}4$ (arredonda para o par), não $2{,}5$. Muitos calculam errado.
- **Cálculos mistos (adição + multiplicação):** aplicar a regra da operação de cada etapa separadamente, guardando dígitos extras nos intermediários.

---

## Conexões

- [[Grandezas Físicas e Sistema Internacional (SI)]] — nota anterior (unidades e notação científica)
- [[Fundamentos de Química I]] — MOC da disciplina
- [[Química]] — MOC da área
- [[Graduação em Química]] — Roadmap da graduação
- [[1º Semestre]] — Semestre ativo
- [[Matemática I]] — Arredondamento, potências de 10, notação científica
- [[Precisão × Exatidão e Tratamento de Erros]] — próximo tópico da U1

---

## Fontes

- ATKINS, P.; JONES, L. *Princípios de Química: Questionando a vida moderna e o meio ambiente*. 5ª ed. Porto Alegre: Bookman, 2011. Cap. 1 (seção sobre medidas e incertezas).
- BROWN, T. L. et al. *Química: A Ciência Central*. 9ª ed. São Paulo: Pearson Prentice Hall, 2005. Cap. 1.5 — Incerteza na medida.
- Material da disciplina: *U1 - Conceitos fundamentais de química* (PDF fornecido pela professora, 2026).
