---
title: Técnicas de Pesagem e Medidas de Volume
description: Toda grandeza medida em laboratório carrega incerteza. Esta prática quantifica
  o erro experimental das vidrarias mais comuns (proveta, pipeta volumétrica e bure…
tags:
- quimica
date: 2026-04-30
tipo: estudo
disciplina: quimica-experimental
semestre: 1
---
# Técnicas de Pesagem e Medidas de Volume

> Toda grandeza medida em laboratório carrega incerteza. Esta prática quantifica o erro experimental das vidrarias mais comuns (proveta, pipeta volumétrica e bureta) por gravimetria e consolida os conceitos de exatidão, precisão, algarismos significativos e notação científica aplicados à prática experimental.

---

## Definição

- **Valor verdadeiro**: valor que se obteria com técnicas, amostras e instrumentos perfeitos — nunca diretamente acessível.
- **Erro experimental**: diferença entre o valor medido e o valor verdadeiro.
- **Exatidão** (*accuracy*): quão próximo o valor medido está do valor verdadeiro.
- **Precisão** (*precision*): reprodutibilidade das medidas — quão próximas entre si estão as repetições, independentemente de serem corretas.

> Uma medida pode ser **precisa sem ser exata**, e vice-versa.

---

## Teoria & Fundamentos

### Tipos de erro experimental

| Tipo | Descrição | Pode ser eliminado? |
|------|-----------|:-------------------:|
| **Sistemático** (determinado) | Identificável — erros pessoais, do método ou da aparelhagem | ✅ com correção |
| **Aleatório** (casual/indeterminado) | Causado por variáveis não controláveis; produz faixa de valores | ❌ trata-se estatisticamente |

**Fontes de erro sistemático:**
- *Pessoais*: leitura defeituosa do menisco, dificuldade em distinguir cores.
- *Do método*: escolha inadequada de indicador em uma titulação.
- *Da aparelhagem*: buretas ou pipetas mal calibradas ou usadas em temperatura diferente da calibração; reagentes impuros.

### Algarismos significativos (AS)

**Regras para contar:**

| Situação | AS? | Exemplo |
|----------|:---:|---------|
| Dígitos não-zero | ✅ | $1{,}473$ → 4 AS |
| Zeros intercalados | ✅ | $1{,}002$ → 4 AS |
| Zeros à esquerda | ❌ | $0{,}0065$ → 2 AS |
| Zeros à direita **com** ponto decimal | ✅ | $0{,}0620$ → 3 AS |
| Zeros à direita **sem** ponto decimal | ambíguo | $3000$ → usar notação científica |
| Números exatos | ∞ | 12 alunos, 1 kg = 1000 g |

### Precisão em cálculos

**Adição e subtração** — mesmo número de **casas decimais** que o componente com **menos casas decimais**:

$$11{,}51 + 137 = 148{,}51 \xrightarrow{\text{arredonda}} \boxed{149\ \text{g}}$$

**Multiplicação e divisão** — mesmo número de **AS** que o fator com **menos AS**:

$$\dfrac{1{,}473}{2{,}6} = 0{,}5665 \xrightarrow{\text{arredonda}} \boxed{0{,}57} \quad (2\ \text{AS})$$

$$3{,}94 \times 2{,}122345 = 8{,}36$$

### Notação científica (exponencial)

$$a{,}xxx \times 10^n \qquad \text{com } 1 \leq a < 10$$

$$0{,}0062 = 6{,}2 \times 10^{-3} \qquad 3700 = 3{,}7 \times 10^3$$

### Determinação experimental do erro volumétrico

**Princípio:** medir 10,00 mL de água destilada com cada vidraria → pesar o volume obtido → comparar com o valor esperado.

Como $\rho_{\text{água}} \approx 1{,}00\ \text{g mL}^{-1}$ a 20 °C, espera-se:

$$m_{\text{esperada}} = 10{,}00\ \text{mL} \times 1{,}00\ \text{g mL}^{-1} = 10{,}00\ \text{g}$$

$$m_{\text{água}} = m_{\text{(tara + água)}} - m_{\text{tara}}$$

O **desvio padrão** entre as 5 repetições indica a **precisão** de cada vidraria.

### Hierarquia de precisão volumétrica

$$\text{Bureta} \approx \text{Pipeta volumétrica} \gg \text{Proveta}$$

---

## Fórmulas & Equações

| Grandeza | Fórmula | Unidade |
|----------|---------|---------|
| Erro absoluto | $E = \lvert V_{\text{medido}} - V_{\text{verdadeiro}} \rvert$ | mL |
| Erro relativo | $E_r = \dfrac{E}{V_{\text{verdadeiro}}} \times 100$ | % |
| Desvio padrão | $s = \sqrt{\dfrac{\sum(x_i - \bar{x})^2}{n-1}}$ | mL ou g |
| Densidade da água (20 °C) | $\rho = 0{,}9982\ \text{g mL}^{-1}$ | g mL⁻¹ |
| Volume a partir da massa | $V = \dfrac{m}{\rho}$ | mL |

---

## Exemplos Resolvidos

**Exemplo 1 — Básico (contar algarismos significativos):**

| Número | AS | Regra aplicada |
|--------|:--:|----------------|
| $167$ | 3 | Todos dígitos não-zero |
| $1{,}0238$ | 5 | Todos dígitos não-zero |
| $0{,}0065$ | 2 | Zeros à esquerda não contam |
| $0{,}0620$ | 3 | Zero final com ponto decimal conta |
| $17{,}0900$ | 6 | Zeros finais com ponto decimal contam |

**Exemplo 2 — Intermediário (cálculo com regras de AS):**

Massa de NaCl = 11,51 g; Massa do béquer = 137 g.

$$\text{Massa total} = 11{,}51 + 137 = 148{,}51 \xrightarrow{\text{0 casas dec.}} \boxed{149\ \text{g}}$$

**Exemplo 3 — Avançado (determinação do erro relativo da proveta):**

Massas obtidas ao medir 10,00 mL de água destilada com proveta (5 repetições):
$9{,}87;\ 9{,}91;\ 9{,}85;\ 9{,}92;\ 9{,}88\ \text{g}$

$$\bar{m} = \dfrac{9{,}87 + 9{,}91 + 9{,}85 + 9{,}92 + 9{,}88}{5} = 9{,}886\ \text{g}$$

$$E_r = \dfrac{\lvert 9{,}886 - 10{,}00 \rvert}{10{,}00} \times 100 \approx \boxed{1{,}1\%}$$

Comparar com a pipeta volumétrica — que deve apresentar $E_r < 0{,}1\%$.

---

## Armadilhas & Edge Cases

- **Não anotar todas as casas decimais** da balança analítica: a balança lê até 0,0001 g — registre todos os dígitos exibidos.
- **Confundir casas decimais com AS**: $52{,}7$ e $0{,}0527$ têm os **mesmos 3 AS** mas casas decimais diferentes.
- **Zero à direita sem ponto decimal é ambíguo**: escreva $3{,}0 \times 10^3$ em vez de $3000$ para deixar claro que são 2 AS.
- **Tubo de ensaio inclinado na pesagem**: o protocolo exige posição vertical — inclinar altera o resultado.
- **Desvio padrão ≠ erro absoluto**: o desvio padrão mede precisão; o afastamento da média verdadeira mede exatidão.
- **Temperatura diferente de 20 °C**: a densidade da água varia — se necessário, consultar tabela de $\rho_{\text{água}}(T)$.

---

## Conexões

- [[Introdução à Química Experimental I]] — MOC da disciplina
- [[Vidrarias e Equipamentos de Laboratório]] — Prática anterior: identificação e uso das vidrarias
- [[Preparo de Soluções]] — Próxima prática: aplicação das técnicas de pesagem e medida
- [[Algarismos Significativos]] — Nota teórica complementar (Fundamentos de Química I)
- [[Precisão × Exatidão e Tratamento de Erros]] — Nota teórica complementar
- [[Química]] — MOC da área

---

## Fontes

- ROMAGNOLI, É. S.; CERVANTES, T. *Apostila — Introdução à Química Experimental I (2QUI204)*. UEL, Londrina, 2026.
- SILVA, R. R. et al. *Introdução à Química Experimental*. São Carlos: EdUFSCar, 2021.
- ATKINS, P.; JONES, L. *Princípios de Química*. 5ª ed. Porto Alegre: Bookman, 2011. Cap. 1.
- BROWN, T. L. et al. *Química: A Ciência Central*. 9ª ed. São Paulo: Pearson Prentice Hall, 2005. Cap. 1.
