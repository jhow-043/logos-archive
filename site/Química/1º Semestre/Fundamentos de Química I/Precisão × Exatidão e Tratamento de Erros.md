---
title: PrecisÃ£o Ã— ExatidÃ£o e Tratamento de Erros
description: PrecisÃ£o e exatidÃ£o sÃ£o conceitos distintos e frequentemente confundidos.
  Toda medida experimental estÃ¡ sujeita a erros â€” entender sua natureza (sistemÃ¡t…
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: quimica-geral
semestre: 1
---
# PrecisÃ£o Ã— ExatidÃ£o e Tratamento de Erros

> **PrecisÃ£o** e **exatidÃ£o** sÃ£o conceitos distintos e frequentemente confundidos. Toda medida experimental estÃ¡ sujeita a erros â€” entender sua natureza (sistemÃ¡tico vs. aleatÃ³rio) Ã© o que diferencia um cientista que interpreta dados de um que apenas os coleta.

---

## DefiniÃ§Ã£o

> **DefiniÃ§Ã£o (Brown et al., 2005, cap. 1; Atkins & Jones, 2011, cap. 1):**
>
> - **ExatidÃ£o** (*accuracy*): quÃ£o prÃ³ximo o valor medido estÃ¡ do **valor verdadeiro** (ou aceito).
> - **PrecisÃ£o** (*precision*): quÃ£o **reprodutÃ­veis** sÃ£o as medidas â€” o quÃ£o prÃ³ximas entre si estÃ£o medidas repetidas, independentemente de estarem certas.
>
> Uma medida pode ser precisa sem ser exata, exata sem ser precisa, ambas ou nenhuma.

---

## Teoria & Fundamentos

### Alvo como analogia visual

```
   EXATA e PRECISA     SÃ“ PRECISA (nÃ£o exata)   SÃ“ EXATA (nÃ£o precisa)    NEM UMA NEM OUTRA

        â”Œâ”€â”€â”€â”                â”Œâ”€â”€â”€â”                     â”Œâ”€â”€â”€â”                   â”Œâ”€â”€â”€â”
       /  â— \              /  Â·  \                   /  Â·  \                 /  Â·  \
      | â—  â— |            | â—â—â—  |                  |  Â· â— \                | Â·  Â·  |
       \  â— /              \  â—â— /                   \ â—  Â· /                \ â—  Â· /
        â””â”€â”€â”€â”˜                â””â”€â”€â”€â”˜                     â””â”€â”€â”€â”˜                   â””â”€â”€â”€â”˜
   Tiros agrupados        Tiros agrupados           Tiros dispersos         Tiros dispersos
   NO centro              FORA do centro            AO REDOR do centro      e fora do centro
```

_O centro do alvo = valor verdadeiro. Cada ponto = uma medida._

### Tipos de erro

Os erros de mediÃ§Ã£o se dividem em dois tipos fundamentais:

**Erro sistemÃ¡tico (erro determinado)**

- Afeta todas as medidas na **mesma direÃ§Ã£o** (sempre para mais ou sempre para menos).
- **Reduz a exatidÃ£o**, mas nÃ£o necessariamente a precisÃ£o.
- **Causas:** instrumento descalibrado, zero incorreto, mÃ©todo com viÃ©s, reagente impuro.
- **Detectado por:** comparaÃ§Ã£o com valor de referÃªncia (padrÃ£o), ou mudanÃ§a de mÃ©todo.
- **Corrijo com:** recalibraÃ§Ã£o, correÃ§Ã£o do mÃ©todo.
- Exemplo: balanÃ§a que mostra sistematicamente 0,5 g a mais.

**Erro aleatÃ³rio (erro indeterminado)**

- Afeta as medidas de forma **irregular**, para mais ou para menos, sem padrÃ£o.
- **Reduz a precisÃ£o** â€” aumenta a dispersÃ£o dos dados.
- **Causas:** variaÃ§Ãµes ambientais (temperatura, vibraÃ§Ã£o), limitaÃ§Ã£o do operador, flutuaÃ§Ãµes do instrumento.
- **Detectado por:** repetiÃ§Ã£o das medidas â€” dispersÃ£o alta indica erro aleatÃ³rio grande.
- **Minimizado com:** maior nÃºmero de medidas (mÃ©dia estatÃ­stica) e ambiente controlado.
- Exemplo: variaÃ§Ã£o de Â±0,02 g entre pesagens consecutivas da mesma amostra.

### ComparaÃ§Ã£o: Erro sistemÃ¡tico Ã— Erro aleatÃ³rio

| CritÃ©rio | Erro sistemÃ¡tico | Erro aleatÃ³rio |
|----------|-----------------|----------------|
| DireÃ§Ã£o | Sempre igual (+ ou âˆ’) | AleatÃ³ria (+ e âˆ’) |
| Afeta | **ExatidÃ£o** | **PrecisÃ£o** |
| Reprodutibilidade | Alta (medidas sempre iguais, mas erradas) | Baixa (medidas dispersas) |
| Causas | Instrumento, mÃ©todo, reagente | Ambiente, operador, flutuaÃ§Ã£o |
| SoluÃ§Ã£o | Recalibrar, corrigir mÃ©todo | Repetir medidas, mÃ©dia |
| Detectado por | ComparaÃ§Ã£o com padrÃ£o | Desvio padrÃ£o alto |

### MÃ©tricas quantitativas de erro

**Erro absoluto:**

$$E_{\text{abs}} = |V_{\text{medido}} - V_{\text{verdadeiro}}|$$

**Erro relativo percentual:**

$$E_{\text{rel}} = \dfrac{|V_{\text{medido}} - V_{\text{verdadeiro}}|}{V_{\text{verdadeiro}}} \times 100\%$$

**MÃ©dia aritmÃ©tica** (estimativa do valor verdadeiro com n medidas):

$$\bar{x} = \dfrac{\displaystyle\sum_{i=1}^{n} x_i}{n}$$

**Desvio padrÃ£o** (medida de precisÃ£o â€” dispersÃ£o das medidas):

$$s = \sqrt{\dfrac{\displaystyle\sum_{i=1}^{n}(x_i - \bar{x})^2}{n - 1}}$$

> **InterpretaÃ§Ã£o:** $s$ pequeno â†’ medidas agrupadas â†’ alta precisÃ£o. $s$ grande â†’ medidas dispersas â†’ baixa precisÃ£o.

**Desvio padrÃ£o relativo (DPR) ou coeficiente de variaÃ§Ã£o (CV):**

$$\text{CV} = \dfrac{s}{\bar{x}} \times 100\%$$

### PropagaÃ§Ã£o de incerteza (introduÃ§Ã£o)

Quando grandezas com incerteza sÃ£o combinadas em um cÃ¡lculo, a incerteza **se propaga** para o resultado. A regra prÃ¡tica Ã© a dos algarismos significativos (nota anterior). A propagaÃ§Ã£o formal serÃ¡ aprofundada em disciplinas de QuÃ­mica AnalÃ­tica.

---

## FÃ³rmulas & EquaÃ§Ãµes

**Erro absoluto:**

$$E_{\text{abs}} = |V_{\text{medido}} - V_{\text{verdadeiro}}|$$

**Erro relativo:**

$$E_{\text{rel}} (\%) = \dfrac{E_{\text{abs}}}{V_{\text{verdadeiro}}} \times 100$$

**MÃ©dia:**

$$\bar{x} = \dfrac{x_1 + x_2 + \cdots + x_n}{n}$$

**Desvio padrÃ£o (amostra):**

$$s = \sqrt{\dfrac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}}$$

---

## Exemplos Resolvidos

**Exemplo 1 â€” BÃ¡sico: Classificar situaÃ§Ãµes como erro de precisÃ£o ou exatidÃ£o**

> **Enunciado:** Classifique cada situaÃ§Ã£o como problema de **precisÃ£o**, **exatidÃ£o**, **ambos** ou **nenhum**. Justifique.
> (a) Um estudante mede o ponto de ebuliÃ§Ã£o da Ã¡gua (100,0 Â°C) e obtÃ©m: 99,8 Â°C; 99,9 Â°C; 99,8 Â°C.
> (b) Outro mede e obtÃ©m: 95,1 Â°C; 104,8 Â°C; 99,9 Â°C.
> (c) Um terceiro obtÃ©m: 95,2 Â°C; 95,1 Â°C; 95,3 Â°C.
> (d) Um quarto obtÃ©m: 100,0 Â°C; 100,1 Â°C; 100,0 Â°C.

| Caso | Resultados | PrÃ³ximos entre si? | PrÃ³ximos de 100,0Â°C? | DiagnÃ³stico |
|------|-----------|-------------------|---------------------|-------------|
| (a) | 99,8; 99,9; 99,8 | âœ… Sim | âœ… Sim (Â±0,1) | **Preciso e exato** |
| (b) | 95,1; 104,8; 99,9 | âŒ NÃ£o | â‰ˆ MÃ©dia | **SÃ³ preciso em mÃ©dia â€” baixa precisÃ£o e baixa exatidÃ£o** |
| (c) | 95,2; 95,1; 95,3 | âœ… Sim | âŒ NÃ£o (~5Â°C abaixo) | **Preciso mas nÃ£o exato** â†’ erro sistemÃ¡tico |
| (d) | 100,0; 100,1; 100,0 | âœ… Sim | âœ… Sim | **Preciso e exato** |

$$\boxed{\text{(a) Prec.+Exat.} \mid \text{(b) Nenhum} \mid \text{(c) Preciso, nÃ£o exato (sist.)} \mid \text{(d) Prec.+Exat.}}$$

---

**Exemplo 2 â€” IntermediÃ¡rio: Calcular erro relativo e desvio padrÃ£o**

> **Enunciado:** Um estudante mede a densidade do etanol ($d_{\text{aceita}} = 0{,}789\ \text{g/mL}$) em cinco tentativas:
> $0{,}791;\; 0{,}788;\; 0{,}793;\; 0{,}790;\; 0{,}789\ \text{g/mL}$
>
> (a) Calcule a mÃ©dia $\bar{x}$.
> (b) Calcule o desvio padrÃ£o $s$.
> (c) Calcule o erro relativo da mÃ©dia em relaÃ§Ã£o ao valor aceito.
> (d) Classifique as medidas quanto Ã  precisÃ£o e exatidÃ£o.

**Passo 1 â€” MÃ©dia.**

$$\bar{x} = \dfrac{0{,}791 + 0{,}788 + 0{,}793 + 0{,}790 + 0{,}789}{5} = \dfrac{3{,}951}{5} = 0{,}7902\ \text{g/mL}$$

**Passo 2 â€” Desvio padrÃ£o.** (usando $\bar{x} \approx 0{,}7902$)

| $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
|-------|----------------|----------------------|
| 0,791 | +0,0008 | $6{,}4 \times 10^{-7}$ |
| 0,788 | âˆ’0,0022 | $4{,}84 \times 10^{-6}$ |
| 0,793 | +0,0028 | $7{,}84 \times 10^{-6}$ |
| 0,790 | âˆ’0,0002 | $4{,}0 \times 10^{-8}$ |
| 0,789 | âˆ’0,0012 | $1{,}44 \times 10^{-6}$ |
| **Soma** | | $1{,}456 \times 10^{-5}$ |

$$s = \sqrt{\dfrac{1{,}456 \times 10^{-5}}{5-1}} = \sqrt{3{,}64 \times 10^{-6}} \approx 0{,}0019\ \text{g/mL}$$

**Passo 3 â€” Erro relativo da mÃ©dia.**

$$E_{\text{rel}} = \dfrac{|0{,}7902 - 0{,}789|}{0{,}789} \times 100 = \dfrac{0{,}0012}{0{,}789} \times 100 \approx 0{,}15\%$$

**Passo 4 â€” ClassificaÃ§Ã£o.**

- $s = 0{,}002\ \text{g/mL}$ (CV â‰ˆ 0,24%) â†’ **alta precisÃ£o**.
- $E_{\text{rel}} = 0{,}15\%$ â†’ muito prÃ³ximo do valor aceito â†’ **boa exatidÃ£o**.
- DiagnÃ³stico: medidas **precisas e exatas**.

$$\boxed{\bar{x} = 0{,}790\ \text{g/mL} \quad;\quad s = 0{,}002\ \text{g/mL} \quad;\quad E_{\text{rel}} = 0{,}15\% \implies \text{preciso e exato}}$$

---

**Exemplo 3 â€” AvanÃ§ado: Identificar e classificar fonte de erro**

> **Enunciado:** Dois grupos medem a massa de uma amostra de NaCl (valor aceito: $5{,}000\ \text{g}$):
>
> | Grupo A | Grupo B |
> |---------|---------|
> | 5,421 g | 4,998 g |
> | 5,419 g | 5,001 g |
> | 5,420 g | 4,999 g |
>
> (a) Calcule a mÃ©dia e o desvio padrÃ£o de cada grupo.
> (b) Classifique quanto Ã  precisÃ£o e exatidÃ£o.
> (c) Que tipo de erro afeta cada grupo? Sugira uma causa plausÃ­vel.

**Passo 1 â€” Grupo A.**

$$\bar{x}_A = \dfrac{5{,}421 + 5{,}419 + 5{,}420}{3} = 5{,}420\ \text{g}$$

$$s_A = \sqrt{\dfrac{(0{,}001)^2 + (-0{,}001)^2 + (0)^2}{2}} = \sqrt{\dfrac{2 \times 10^{-6}}{2}} = 0{,}001\ \text{g}$$

$$E_{\text{rel},A} = \dfrac{|5{,}420 - 5{,}000|}{5{,}000} \times 100 = 8{,}4\%$$

**Passo 2 â€” Grupo B.**

$$\bar{x}_B = \dfrac{4{,}998 + 5{,}001 + 4{,}999}{3} = 4{,}999\ \text{g}$$

$$s_B = \sqrt{\dfrac{(-0{,}001)^2 + (0{,}002)^2 + (0)^2}{2}} \approx 0{,}0015\ \text{g}$$

$$E_{\text{rel},B} = \dfrac{|4{,}999 - 5{,}000|}{5{,}000} \times 100 = 0{,}02\%$$

**Passo 3 â€” ComparaÃ§Ã£o.**

| Grupo | $\bar{x}$ | $s$ | $E_{\text{rel}}$ | Preciso? | Exato? | Tipo de erro |
|-------|----------|-----|-----------------|---------|-------|--------------|
| A | 5,420 g | 0,001 g | 8,4% | âœ… Sim | âŒ NÃ£o | **SistemÃ¡tico** |
| B | 4,999 g | 0,002 g | 0,02% | âœ… Sim | âœ… Sim | Nenhum relevante |

**Causa plausÃ­vel para o Grupo A:** balanÃ§a com tara incorreta (mostra sistematicamente 0,42 g a mais). A calibraÃ§Ã£o resolve o problema.

$$\boxed{\bar{x}_A = 5{,}420\ \text{g},\, s_A = 0{,}001\ \text{g} \text{ (preciso, erro sist. de +8,4\%)} \mid \bar{x}_B = 4{,}999\ \text{g},\, s_B \approx 0{,}002\ \text{g} \text{ (preciso e exato)}}$$

---

## Armadilhas & Edge Cases

- **PrecisÃ£o alta â‰  exatidÃ£o:** o Grupo A do Exemplo 3 Ã© altamente preciso ($s = 0{,}001\ \text{g}$) mas errado em 8,4%. Confundir os dois conceitos Ã© um dos erros mais comuns em laboratÃ³rio.
- **MÃ©dia de dados imprecisos nÃ£o Ã© exata:** calcular a mÃ©dia de medidas com grande dispersÃ£o nÃ£o garante convergÃªncia para o valor verdadeiro se houver erro sistemÃ¡tico.
- **$n-1$ no denominador do desvio padrÃ£o:** usa-se $n-1$ (desvio padrÃ£o **amostral**), nÃ£o $n$ (desvio padrÃ£o populacional), porque trabalhamos com uma amostra finita. Com $n$ pequeno, a diferenÃ§a Ã© significativa.
- **Erro relativo depende do valor verdadeiro:** um erro absoluto de 0,1 g Ã© grave ao pesar 1 g de amostra (10%), mas desprezÃ­vel ao pesar 1 kg (0,01%).
- **"ReprodutÃ­vel" nÃ£o significa "correto":** um mÃ©todo sistematicamente errado pode ser perfeitamente reprodutÃ­vel â€” e enganosamente confiÃ¡vel.
- **CV > 5%:** em QuÃ­mica AnalÃ­tica, CV acima de 5% geralmente indica precisÃ£o inadequada para fins analÃ­ticos quantitativos.

---

## ConexÃµes

- [[Algarismos Significativos]] â€” nota anterior (nÃºmero de AS reflete a precisÃ£o da medida)
- [[Grandezas FÃ­sicas e Sistema Internacional (SI)]] â€” unidades e magnitude das medidas
- [[Fundamentos de QuÃ­mica I]] â€” MOC da disciplina â€” **Ãºltima nota da U1**
- [[QuÃ­mica]] â€” MOC da Ã¡rea
- [[GraduaÃ§Ã£o em QuÃ­mica]] â€” Roadmap da graduaÃ§Ã£o
- [[1Âº Semestre]] â€” Semestre ativo
- [[MatemÃ¡tica I]] â€” EstatÃ­stica descritiva: mÃ©dia, desvio padrÃ£o, variÃ¢ncia

---

## Fontes

- ATKINS, P.; JONES, L. *PrincÃ­pios de QuÃ­mica: Questionando a vida moderna e o meio ambiente*. 5Âª ed. Porto Alegre: Bookman, 2011. Cap. 1 (seÃ§Ã£o sobre medidas e incertezas).
- BROWN, T. L. et al. *QuÃ­mica: A CiÃªncia Central*. 9Âª ed. SÃ£o Paulo: Pearson Prentice Hall, 2005. Cap. 1.5 â€” Incerteza na medida.
- Material da disciplina: *U1 - Conceitos fundamentais de quÃ­mica* (PDF fornecido pela professora, 2026).
