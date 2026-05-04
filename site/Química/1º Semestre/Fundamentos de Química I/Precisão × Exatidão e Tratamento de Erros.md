---
title: Precisão × Exatidão e Tratamento de Erros
description: Precisão e exatidão são conceitos distintos e frequentemente confundidos.
  Toda medida experimental está sujeita a erros — entender sua natureza (sistemático
  vs.…
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: quimica-geral
semestre: 1
---
> **Precisão** e **exatidão** são conceitos distintos e frequentemente confundidos. Toda medida experimental está sujeita a erros — entender sua natureza (sistemático vs. aleatório) é o que diferencia um cientista que interpreta dados de um que apenas os coleta.

---

## Definição

> **Definição (Brown et al., 2005, cap. 1; Atkins & Jones, 2011, cap. 1):**
>
> - **Exatidão** (*accuracy*): quão próximo o valor medido está do **valor verdadeiro** (ou aceito).
> - **Precisão** (*precision*): quão **reprodutíveis** são as medidas — o quão próximas entre si estão medidas repetidas, independentemente de estarem certas.
>
> Uma medida pode ser precisa sem ser exata, exata sem ser precisa, ambas ou nenhuma.

---

## Teoria & Fundamentos

### Alvo como analogia visual

```
   EXATA e PRECISA     SÓ PRECISA (não exata)   SÓ EXATA (não precisa)    NEM UMA NEM OUTRA

        ┌───┐                ┌───┐                     ┌───┐                   ┌───┐
       /  ● \              /  ·  \                   /  ·  \                 /  ·  \
      | ●  ● |            | ●●●  |                  |  · ● \                | ·  ·  |
       \  ● /              \  ●● /                   \ ●  · /                \ ●  · /
        └───┘                └───┘                     └───┘                   └───┘
   Tiros agrupados        Tiros agrupados           Tiros dispersos         Tiros dispersos
   NO centro              FORA do centro            AO REDOR do centro      e fora do centro
```

_O centro do alvo = valor verdadeiro. Cada ponto = uma medida._

### Tipos de erro

Os erros de medição se dividem em dois tipos fundamentais:

**Erro sistemático (erro determinado)**

- Afeta todas as medidas na **mesma direção** (sempre para mais ou sempre para menos).
- **Reduz a exatidão**, mas não necessariamente a precisão.
- **Causas:** instrumento descalibrado, zero incorreto, método com viés, reagente impuro.
- **Detectado por:** comparação com valor de referência (padrão), ou mudança de método.
- **Corrijo com:** recalibração, correção do método.
- Exemplo: balança que mostra sistematicamente 0,5 g a mais.

**Erro aleatório (erro indeterminado)**

- Afeta as medidas de forma **irregular**, para mais ou para menos, sem padrão.
- **Reduz a precisão** — aumenta a dispersão dos dados.
- **Causas:** variações ambientais (temperatura, vibração), limitação do operador, flutuações do instrumento.
- **Detectado por:** repetição das medidas — dispersão alta indica erro aleatório grande.
- **Minimizado com:** maior número de medidas (média estatística) e ambiente controlado.
- Exemplo: variação de ±0,02 g entre pesagens consecutivas da mesma amostra.

### Comparação: Erro sistemático × Erro aleatório

| Critério | Erro sistemático | Erro aleatório |
|----------|-----------------|----------------|
| Direção | Sempre igual (+ ou −) | Aleatória (+ e −) |
| Afeta | **Exatidão** | **Precisão** |
| Reprodutibilidade | Alta (medidas sempre iguais, mas erradas) | Baixa (medidas dispersas) |
| Causas | Instrumento, método, reagente | Ambiente, operador, flutuação |
| Solução | Recalibrar, corrigir método | Repetir medidas, média |
| Detectado por | Comparação com padrão | Desvio padrão alto |

### Métricas quantitativas de erro

**Erro absoluto:**

$$E_{\text{abs}} = |V_{\text{medido}} - V_{\text{verdadeiro}}|$$

**Erro relativo percentual:**

$$E_{\text{rel}} = \dfrac{|V_{\text{medido}} - V_{\text{verdadeiro}}|}{V_{\text{verdadeiro}}} \times 100\%$$

**Média aritmética** (estimativa do valor verdadeiro com n medidas):

$$\bar{x} = \dfrac{\displaystyle\sum_{i=1}^{n} x_i}{n}$$

**Desvio padrão** (medida de precisão — dispersão das medidas):

$$s = \sqrt{\dfrac{\displaystyle\sum_{i=1}^{n}(x_i - \bar{x})^2}{n - 1}}$$

> **Interpretação:** $s$ pequeno → medidas agrupadas → alta precisão. $s$ grande → medidas dispersas → baixa precisão.

**Desvio padrão relativo (DPR) ou coeficiente de variação (CV):**

$$\text{CV} = \dfrac{s}{\bar{x}} \times 100\%$$

### Propagação de incerteza (introdução)

Quando grandezas com incerteza são combinadas em um cálculo, a incerteza **se propaga** para o resultado. A regra prática é a dos algarismos significativos (nota anterior). A propagação formal será aprofundada em disciplinas de Química Analítica.

---

## Fórmulas & Equações

**Erro absoluto:**

$$E_{\text{abs}} = |V_{\text{medido}} - V_{\text{verdadeiro}}|$$

**Erro relativo:**

$$E_{\text{rel}} (\%) = \dfrac{E_{\text{abs}}}{V_{\text{verdadeiro}}} \times 100$$

**Média:**

$$\bar{x} = \dfrac{x_1 + x_2 + \cdots + x_n}{n}$$

**Desvio padrão (amostra):**

$$s = \sqrt{\dfrac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}}$$

---

## Exemplos Resolvidos

**Exemplo 1 — Básico: Classificar situações como erro de precisão ou exatidão**

> **Enunciado:** Classifique cada situação como problema de **precisão**, **exatidão**, **ambos** ou **nenhum**. Justifique.
> (a) Um estudante mede o ponto de ebulição da água (100,0 °C) e obtém: 99,8 °C; 99,9 °C; 99,8 °C.
> (b) Outro mede e obtém: 95,1 °C; 104,8 °C; 99,9 °C.
> (c) Um terceiro obtém: 95,2 °C; 95,1 °C; 95,3 °C.
> (d) Um quarto obtém: 100,0 °C; 100,1 °C; 100,0 °C.

| Caso | Resultados | Próximos entre si? | Próximos de 100,0°C? | Diagnóstico |
|------|-----------|-------------------|---------------------|-------------|
| (a) | 99,8; 99,9; 99,8 | ✅ Sim | ✅ Sim (±0,1) | **Preciso e exato** |
| (b) | 95,1; 104,8; 99,9 | ❌ Não | ≈ Média | **Só preciso em média — baixa precisão e baixa exatidão** |
| (c) | 95,2; 95,1; 95,3 | ✅ Sim | ❌ Não (~5°C abaixo) | **Preciso mas não exato** → erro sistemático |
| (d) | 100,0; 100,1; 100,0 | ✅ Sim | ✅ Sim | **Preciso e exato** |

$$\boxed{\text{(a) Prec.+Exat.} \mid \text{(b) Nenhum} \mid \text{(c) Preciso, não exato (sist.)} \mid \text{(d) Prec.+Exat.}}$$

---

**Exemplo 2 — Intermediário: Calcular erro relativo e desvio padrão**

> **Enunciado:** Um estudante mede a densidade do etanol ($d_{\text{aceita}} = 0{,}789\ \text{g/mL}$) em cinco tentativas:
> $0{,}791;\; 0{,}788;\; 0{,}793;\; 0{,}790;\; 0{,}789\ \text{g/mL}$
>
> (a) Calcule a média $\bar{x}$.
> (b) Calcule o desvio padrão $s$.
> (c) Calcule o erro relativo da média em relação ao valor aceito.
> (d) Classifique as medidas quanto à precisão e exatidão.

**Passo 1 — Média.**

$$\bar{x} = \dfrac{0{,}791 + 0{,}788 + 0{,}793 + 0{,}790 + 0{,}789}{5} = \dfrac{3{,}951}{5} = 0{,}7902\ \text{g/mL}$$

**Passo 2 — Desvio padrão.** (usando $\bar{x} \approx 0{,}7902$)

| $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
|-------|----------------|----------------------|
| 0,791 | +0,0008 | $6{,}4 \times 10^{-7}$ |
| 0,788 | −0,0022 | $4{,}84 \times 10^{-6}$ |
| 0,793 | +0,0028 | $7{,}84 \times 10^{-6}$ |
| 0,790 | −0,0002 | $4{,}0 \times 10^{-8}$ |
| 0,789 | −0,0012 | $1{,}44 \times 10^{-6}$ |
| **Soma** | | $1{,}456 \times 10^{-5}$ |

$$s = \sqrt{\dfrac{1{,}456 \times 10^{-5}}{5-1}} = \sqrt{3{,}64 \times 10^{-6}} \approx 0{,}0019\ \text{g/mL}$$

**Passo 3 — Erro relativo da média.**

$$E_{\text{rel}} = \dfrac{|0{,}7902 - 0{,}789|}{0{,}789} \times 100 = \dfrac{0{,}0012}{0{,}789} \times 100 \approx 0{,}15\%$$

**Passo 4 — Classificação.**

- $s = 0{,}002\ \text{g/mL}$ (CV ≈ 0,24%) → **alta precisão**.
- $E_{\text{rel}} = 0{,}15\%$ → muito próximo do valor aceito → **boa exatidão**.
- Diagnóstico: medidas **precisas e exatas**.

$$\boxed{\bar{x} = 0{,}790\ \text{g/mL} \quad;\quad s = 0{,}002\ \text{g/mL} \quad;\quad E_{\text{rel}} = 0{,}15\% \implies \text{preciso e exato}}$$

---

**Exemplo 3 — Avançado: Identificar e classificar fonte de erro**

> **Enunciado:** Dois grupos medem a massa de uma amostra de NaCl (valor aceito: $5{,}000\ \text{g}$):
>
> | Grupo A | Grupo B |
> |---------|---------|
> | 5,421 g | 4,998 g |
> | 5,419 g | 5,001 g |
> | 5,420 g | 4,999 g |
>
> (a) Calcule a média e o desvio padrão de cada grupo.
> (b) Classifique quanto à precisão e exatidão.
> (c) Que tipo de erro afeta cada grupo? Sugira uma causa plausível.

**Passo 1 — Grupo A.**

$$\bar{x}_A = \dfrac{5{,}421 + 5{,}419 + 5{,}420}{3} = 5{,}420\ \text{g}$$

$$s_A = \sqrt{\dfrac{(0{,}001)^2 + (-0{,}001)^2 + (0)^2}{2}} = \sqrt{\dfrac{2 \times 10^{-6}}{2}} = 0{,}001\ \text{g}$$

$$E_{\text{rel},A} = \dfrac{|5{,}420 - 5{,}000|}{5{,}000} \times 100 = 8{,}4\%$$

**Passo 2 — Grupo B.**

$$\bar{x}_B = \dfrac{4{,}998 + 5{,}001 + 4{,}999}{3} = 4{,}999\ \text{g}$$

$$s_B = \sqrt{\dfrac{(-0{,}001)^2 + (0{,}002)^2 + (0)^2}{2}} \approx 0{,}0015\ \text{g}$$

$$E_{\text{rel},B} = \dfrac{|4{,}999 - 5{,}000|}{5{,}000} \times 100 = 0{,}02\%$$

**Passo 3 — Comparação.**

| Grupo | $\bar{x}$ | $s$ | $E_{\text{rel}}$ | Preciso? | Exato? | Tipo de erro |
|-------|----------|-----|-----------------|---------|-------|--------------|
| A | 5,420 g | 0,001 g | 8,4% | ✅ Sim | ❌ Não | **Sistemático** |
| B | 4,999 g | 0,002 g | 0,02% | ✅ Sim | ✅ Sim | Nenhum relevante |

**Causa plausível para o Grupo A:** balança com tara incorreta (mostra sistematicamente 0,42 g a mais). A calibração resolve o problema.

$$\boxed{\bar{x}_A = 5{,}420\ \text{g},\, s_A = 0{,}001\ \text{g} \text{ (preciso, erro sist. de +8,4\%)} \mid \bar{x}_B = 4{,}999\ \text{g},\, s_B \approx 0{,}002\ \text{g} \text{ (preciso e exato)}}$$

---

## Armadilhas & Edge Cases

- **Precisão alta ≠ exatidão:** o Grupo A do Exemplo 3 é altamente preciso ($s = 0{,}001\ \text{g}$) mas errado em 8,4%. Confundir os dois conceitos é um dos erros mais comuns em laboratório.
- **Média de dados imprecisos não é exata:** calcular a média de medidas com grande dispersão não garante convergência para o valor verdadeiro se houver erro sistemático.
- **$n-1$ no denominador do desvio padrão:** usa-se $n-1$ (desvio padrão **amostral**), não $n$ (desvio padrão populacional), porque trabalhamos com uma amostra finita. Com $n$ pequeno, a diferença é significativa.
- **Erro relativo depende do valor verdadeiro:** um erro absoluto de 0,1 g é grave ao pesar 1 g de amostra (10%), mas desprezível ao pesar 1 kg (0,01%).
- **"Reprodutível" não significa "correto":** um método sistematicamente errado pode ser perfeitamente reprodutível — e enganosamente confiável.
- **CV > 5%:** em Química Analítica, CV acima de 5% geralmente indica precisão inadequada para fins analíticos quantitativos.

---

## Conexões

- [[Algarismos Significativos]] — nota anterior (número de AS reflete a precisão da medida)
- [[Grandezas Físicas e Sistema Internacional (SI)]] — unidades e magnitude das medidas
- [[Fundamentos de Química I]] — MOC da disciplina — **última nota da U1**
- [[Química]] — MOC da área
- [[Graduação em Química]] — Roadmap da graduação
- [[1º Semestre]] — Semestre ativo
- [[Matemática I]] — Estatística descritiva: média, desvio padrão, variância

---

## Fontes

- ATKINS, P.; JONES, L. *Princípios de Química: Questionando a vida moderna e o meio ambiente*. 5ª ed. Porto Alegre: Bookman, 2011. Cap. 1 (seção sobre medidas e incertezas).
- BROWN, T. L. et al. *Química: A Ciência Central*. 9ª ed. São Paulo: Pearson Prentice Hall, 2005. Cap. 1.5 — Incerteza na medida.
- Material da disciplina: *U1 - Conceitos fundamentais de química* (PDF fornecido pela professora, 2026).
