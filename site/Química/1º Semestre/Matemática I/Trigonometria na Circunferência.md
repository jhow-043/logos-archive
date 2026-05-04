---
title: Trigonometria na Circunferência
description: Generalização das razões trigonométricas para qualquer ângulo real via
  ciclo trigonométrico — extensão natural do triângulo retângulo para a circunferência
  unit…
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: matematica
semestre: 1
---
# Trigonometria na Circunferência

> Generalização das razões trigonométricas para qualquer ângulo real via ciclo trigonométrico — extensão natural do triângulo retângulo para a circunferência unitária.

---

## Definição

A trigonometria na circunferência (ou ciclo trigonométrico) estende as definições de seno, cosseno e tangente — antes restritas a ângulos agudos no triângulo retângulo — para **qualquer ângulo real**, incluindo ângulos obtusos, negativos e maiores que 360°. A ideia central é representar ângulos como arcos sobre uma **circunferência de raio 1 centrada na origem** (o ciclo trigonométrico), e definir as razões trigonométricas a partir das **coordenadas do ponto** correspondente a cada arco.

Essa generalização permite tratar as funções trigonométricas como funções do conjunto dos reais, base para aplicações em física (ondas, MCU) e para o estudo de equações e identidades trigonométricas.

## Teoria & Fundamentos

### Arcos e ângulos centrais

Dado uma circunferência de raio $r$ e um ângulo central $\theta$, o arco $\ell$ correspondente satisfaz:

$$\ell = r\theta \quad (\theta \text{ em radianos})$$

Há uma correspondência biunívoca entre ângulo central e arco — basta fixar o raio. No ciclo trigonométrico ($r = 1$), o comprimento de arco numericamente iguala o ângulo em radianos: $\ell = \theta$.

### Grau e radiano

| Unidade | Definição | Volta completa |
| ------- | --------- | -------------- |
| Grau (°) | $\frac{1}{360}$ de volta completa | $360°$ |
| Radiano (rad) | ângulo cujo arco é igual ao raio | $2\pi$ rad |

A relação de conversão fundamental é:

$$180° = \pi \text{ rad}$$

**Conversão graus → radianos:** multiplica por $\dfrac{\pi}{180}$

**Conversão radianos → graus:** multiplica por $\dfrac{180}{\pi}$

### Tabela de arcos notáveis

| Graus | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $120°$ | $135°$ | $150°$ | $180°$ | $270°$ | $360°$ |
| ------ | --- | ----- | ----- | ----- | ----- | ------ | ------ | ------ | ------ | ------ | ------ |
| Radianos | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\dfrac{2\pi}{3}$ | $\dfrac{3\pi}{4}$ | $\dfrac{5\pi}{6}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |

### Ciclo trigonométrico

O **ciclo trigonométrico** é a circunferência de raio 1 centrada na origem do plano cartesiano, com:

- **Ponto de origem:** $A = (1, 0)$ — ponto inicial do arco
- **Sentido positivo:** anti-horário
- **Sentido negativo:** horário
- **Ponto $P$:** extremidade do arco de medida $\alpha$ percorrido a partir de $A$

Os quadrantes são definidos pelos semieixos coordenados:

| Quadrante | Intervalo (graus) | Intervalo (radianos) | $x$ | $y$ |
| --------- | ----------------- | -------------------- | --- | --- |
| 1º | $0° < \alpha < 90°$ | $0 < \alpha < \dfrac{\pi}{2}$ | $+$ | $+$ |
| 2º | $90° < \alpha < 180°$ | $\dfrac{\pi}{2} < \alpha < \pi$ | $-$ | $+$ |
| 3º | $180° < \alpha < 270°$ | $\pi < \alpha < \dfrac{3\pi}{2}$ | $-$ | $-$ |
| 4º | $270° < \alpha < 360°$ | $\dfrac{3\pi}{2} < \alpha < 2\pi$ | $+$ | $-$ |

### Arcos côngruos

Dois arcos são **côngruos** (determinam o mesmo ponto $P$ no ciclo) quando diferem de uma volta inteira:

$$\alpha' = \alpha + 2k\pi, \quad k \in \mathbb{Z}$$

A **1ª determinação positiva** de um arco é o côngruo no intervalo $[0, 2\pi)$.

### Definição de seno e cosseno no ciclo

Dado o arco $\alpha$ com extremidade $P = (x_P, y_P)$ no ciclo trigonométrico:

$$\operatorname{cos}\alpha = x_P \qquad \operatorname{sen}\alpha = y_P$$

Como $P$ está na circunferência unitária, vale sempre $x_P^2 + y_P^2 = 1$, o que dá a **relação fundamental**:

$$\operatorname{sen}^2\alpha + \operatorname{cos}^2\alpha = 1$$

### Tangente no ciclo

A **tangente** é definida geometricamente como o valor da ordenada do ponto onde a reta $OP$ (prolongada) intersecta o eixo das tangentes ($x = 1$):

$$\operatorname{tg}\alpha = \frac{\operatorname{sen}\alpha}{\operatorname{cos}\alpha}, \quad \operatorname{cos}\alpha \neq 0$$

A tangente **não existe** quando $\operatorname{cos}\alpha = 0$, i.e., $\alpha = \dfrac{\pi}{2} + k\pi,\ k \in \mathbb{Z}$.

### Cotangente, secante e cossecante

As outras três razões são recíprocas das anteriores:

$$\operatorname{cotg}\alpha = \frac{\operatorname{cos}\alpha}{\operatorname{sen}\alpha} = \frac{1}{\operatorname{tg}\alpha}, \quad \operatorname{sen}\alpha \neq 0$$

$$\sec\alpha = \frac{1}{\operatorname{cos}\alpha}, \quad \operatorname{cos}\alpha \neq 0$$

$$\csc\alpha = \frac{1}{\operatorname{sen}\alpha}, \quad \operatorname{sen}\alpha \neq 0$$

> **Domínio:** cotg e csc não existem quando $\operatorname{sen}\alpha = 0$, i.e., $\alpha = k\pi,\ k \in \mathbb{Z}$.

### Sinais das funções por quadrante

| Função | 1º | 2º | 3º | 4º |
| ------ | -- | -- | -- | -- |
| $\operatorname{sen}$ | $+$ | $+$ | $-$ | $-$ |
| $\operatorname{cos}$ | $+$ | $-$ | $-$ | $+$ |
| $\operatorname{tg}$ | $+$ | $-$ | $+$ | $-$ |
| $\operatorname{cotg}$ | $+$ | $-$ | $+$ | $-$ |
| $\sec$ | $+$ | $-$ | $-$ | $+$ |
| $\csc$ | $+$ | $+$ | $-$ | $-$ |

> **Mnemônico CAST** (4º → 1º → 2º → 3º): **C**osseno, **A**ll (todos), **S**eno, **T**angente — indica qual função é positiva em cada quadrante percorrendo sentido anti-horário a partir do 4º.

### Redução ao 1º quadrante

Qualquer arco pode ser reduzido a um arco do 1º quadrante usando as relações abaixo, onde $x \in \left(0, \dfrac{\pi}{2}\right)$:

| Arco | $\operatorname{sen}$ | $\operatorname{cos}$ | $\operatorname{tg}$ |
| ---- | -------------------- | ------ | -------------------- |
| $\pi - x$ (2º quadrante) | $+\operatorname{sen}x$ | $-\operatorname{cos} x$ | $-\operatorname{tg}x$ |
| $\pi + x$ (3º quadrante) | $-\operatorname{sen}x$ | $-\operatorname{cos} x$ | $+\operatorname{tg}x$ |
| $2\pi - x$ (4º quadrante) | $-\operatorname{sen}x$ | $+\operatorname{cos} x$ | $-\operatorname{tg}x$ |

> **Regra prática:** o valor absoluto da função é o mesmo do arco do 1º quadrante; o sinal vem do quadrante de origem (tabela de sinais acima).

### Periodicidade

$$\operatorname{sen}(\alpha + 2\pi) = \operatorname{sen}\alpha \qquad \operatorname{cos}(\alpha + 2\pi) = \operatorname{cos}\alpha \quad \Rightarrow \text{ período } 2\pi$$

$$\operatorname{tg}(\alpha + \pi) = \operatorname{tg}\alpha \qquad \operatorname{cotg}(\alpha + \pi) = \operatorname{cotg}\alpha \quad \Rightarrow \text{ período } \pi$$

### Relações fundamentais estendidas

Da identidade $\operatorname{sen}^2\alpha + \operatorname{cos}^2\alpha = 1$, dividindo por $\operatorname{cos}^2\alpha$ e por $\operatorname{sen}^2\alpha$ respectivamente:

$$1 + \operatorname{tg}^2\alpha = \sec^2\alpha$$

$$1 + \operatorname{cotg}^2\alpha = \csc^2\alpha$$

## Fórmulas & Equações

### Símbolos e variáveis

| Símbolo | Significado | Observação |
| ------- | ----------- | ---------- |
| $\alpha$ | Arco/ângulo no ciclo | Qualquer valor real (graus ou radianos) |
| $P = (x_P, y_P)$ | Ponto no ciclo | $x_P^2 + y_P^2 = 1$ |
| $k$ | Inteiro arbitrário | Representa voltas completas |
| $\operatorname{sen}\alpha$ | Seno | Ordenada $y_P$ |
| $\operatorname{cos}\alpha$ | Cosseno | Abscissa $x_P$ |
| $\operatorname{tg}\alpha$ | Tangente | $\operatorname{sen}\alpha / \operatorname{cos}\alpha$ |
| $\operatorname{cotg}\alpha$ | Cotangente | $\operatorname{cos}\alpha / \operatorname{sen}\alpha$ |
| $\sec\alpha$ | Secante | $1/\operatorname{cos}\alpha$ |
| $\csc\alpha$ | Cossecante | $1/\operatorname{sen}\alpha$ |

### Valores notáveis completos

| Arco | $\operatorname{sen}$ | $\operatorname{cos}$ | $\operatorname{tg}$ | $\operatorname{cotg}$ | $\sec$ | $\csc$ |
| ---- | -------------------- | ------ | -------------------- | --------------------- | ------ | ------ |
| $0$ | $0$ | $1$ | $0$ | — | $1$ | — |
| $\dfrac{\pi}{6}$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{3}}{3}$ | $\sqrt{3}$ | $\dfrac{2\sqrt{3}}{3}$ | $2$ |
| $\dfrac{\pi}{4}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $1$ | $1$ | $\sqrt{2}$ | $\sqrt{2}$ |
| $\dfrac{\pi}{3}$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{1}{2}$ | $\sqrt{3}$ | $\dfrac{\sqrt{3}}{3}$ | $2$ | $\dfrac{2\sqrt{3}}{3}$ |
| $\dfrac{\pi}{2}$ | $1$ | $0$ | — | $0$ | — | $1$ |

### Relações fundamentais

$$\operatorname{sen}^2\alpha + \operatorname{cos}^2\alpha = 1$$

$$1 + \operatorname{tg}^2\alpha = \sec^2\alpha$$

$$1 + \operatorname{cotg}^2\alpha = \csc^2\alpha$$

## Exemplos Resolvidos

**Exemplo 1 — Básico: converter graus para radianos e localizar no ciclo**

> **Enunciado:** Converter $210°$ para radianos e determinar em qual quadrante o arco se encontra.

**Passo 1 — Montar a proporção de conversão.**

A relação fundamental entre as duas unidades é $180° = \pi$ rad. Para converter qualquer ângulo em graus para radianos, multiplica-se por $\dfrac{\pi}{180}$:

$$210° \times \frac{\pi}{180}$$

**Passo 2 — Calcular o produto e simplificar a fração.**

Multiplica-se numerador com numerador e coloca o denominador:

$$\frac{210\pi}{180}$$

Simplificar: $\operatorname{mdc}(210, 180) = 30$. Divido ambos por 30:

$$\frac{210 \div 30}{180 \div 30}\,\pi = \frac{7}{6}\pi = \frac{7\pi}{6}$$

**Passo 3 — Localizar o arco no ciclo comparando com os limites de quadrante.**

Os limites em radianos são:
- Fim do 2º quadrante: $\pi = \dfrac{6\pi}{6}$
- Fim do 3º quadrante: $\dfrac{3\pi}{2} = \dfrac{9\pi}{6}$

Como $\dfrac{6\pi}{6} < \dfrac{7\pi}{6} < \dfrac{9\pi}{6}$, ou seja $\pi < \dfrac{7\pi}{6} < \dfrac{3\pi}{2}$, o arco está no **3º quadrante**.

> **Resultado:** $210° = \dfrac{7\pi}{6}$ rad → **3º quadrante**.

---

**Exemplo 2 — Intermediário: calcular três funções por redução ao 1º quadrante**

> **Enunciado:** Calcular $\operatorname{sen}\!\left(\dfrac{5\pi}{6}\right)$, $\operatorname{cos}\!\left(\dfrac{5\pi}{6}\right)$ e $\operatorname{tg}\!\left(\dfrac{5\pi}{6}\right)$.

**Passo 1 — Identificar o quadrante do arco.**

Comparar $\dfrac{5\pi}{6}$ com os limites do ciclo (denominador comum 6):

$$\frac{\pi}{2} = \frac{3\pi}{6} \qquad \pi = \frac{6\pi}{6}$$

Como $\dfrac{3\pi}{6} < \dfrac{5\pi}{6} < \dfrac{6\pi}{6}$, o arco pertence ao **2º quadrante**.

**Passo 2 — Escrever o arco na forma $\pi - x$ para encontrar o arco equivalente no 1º quadrante.**

Para um arco do 2º quadrante, a fórmula de redução é $\alpha = \pi - x$, onde $x$ é o arco do 1º quadrante correspondente. Isolo $x$:

$$\frac{5\pi}{6} = \pi - x \implies x = \pi - \frac{5\pi}{6}$$

Fazer a subtração (denominador comum 6):

$$x = \frac{6\pi}{6} - \frac{5\pi}{6} = \frac{\pi}{6}$$

O arco reduzido ao 1º quadrante é $\dfrac{\pi}{6}$ — um arco notável.

**Passo 3 — Determinar os sinais das funções no 2º quadrante.**

No 2º quadrante: $x < 0$ e $y > 0$. Portanto:
- $\operatorname{sen} > 0$ (positivo, pois depende de $y$)
- $\operatorname{cos} < 0$ (negativo, pois depende de $x$)
- $\operatorname{tg} < 0$ (negativo, pois $\operatorname{tg} = y/x$ e $y > 0$, $x < 0$)

**Passo 4 — Aplicar os valores notáveis de $\dfrac{\pi}{6}$ com os sinais do 2º quadrante.**

Da tabela de valores notáveis: $\operatorname{sen}\!\left(\dfrac{\pi}{6}\right) = \dfrac{1}{2}$, $\operatorname{cos}\!\left(\dfrac{\pi}{6}\right) = \dfrac{\sqrt{3}}{2}$, $\operatorname{tg}\!\left(\dfrac{\pi}{6}\right) = \dfrac{\sqrt{3}}{3}$.

Aplicando os sinais do 2º quadrante:

$$\operatorname{sen}\!\left(\frac{5\pi}{6}\right) = +\operatorname{sen}\!\left(\frac{\pi}{6}\right) = +\frac{1}{2} = \boxed{\frac{1}{2}}$$

$$\operatorname{cos}\!\left(\frac{5\pi}{6}\right) = -\operatorname{cos}\!\left(\frac{\pi}{6}\right) = -\frac{\sqrt{3}}{2} = \boxed{-\frac{\sqrt{3}}{2}}$$

$$\operatorname{tg}\!\left(\frac{5\pi}{6}\right) = -\operatorname{tg}\!\left(\frac{\pi}{6}\right) = -\frac{\sqrt{3}}{3} = \boxed{-\frac{\sqrt{3}}{3}}$$

**Verificação rápida:** $\operatorname{sen}^2 + \operatorname{cos}^2 = \left(\dfrac{1}{2}\right)^2 + \left(-\dfrac{\sqrt{3}}{2}\right)^2 = \dfrac{1}{4} + \dfrac{3}{4} = 1$ ✓

---

**Exemplo 3 — Avançado: determinar as 6 funções a partir de uma razão dada**

> **Enunciado:** Dado $\operatorname{sen}\alpha = -\dfrac{3}{5}$ com $\alpha$ no **3º quadrante**, encontrar $\operatorname{cos}\alpha$, $\operatorname{tg}\alpha$, $\operatorname{cotg}\alpha$, $\sec\alpha$ e $\csc\alpha$.

**Passo 1 — Verificar a consistência do dado com o quadrante.**

No 3º quadrante, $\operatorname{sen} < 0$. O dado $\operatorname{sen}\alpha = -\dfrac{3}{5} < 0$ é consistente. ✓

**Passo 2 — Encontrar $\operatorname{cos}\alpha$ usando a relação fundamental.**

Partir de $\operatorname{sen}^2\alpha + \operatorname{cos}^2\alpha = 1$ e **isolar $\operatorname{cos}^2\alpha$**:

$$\operatorname{cos}^2\alpha = 1 - \operatorname{sen}^2\alpha$$

Substituir o valor dado:

$$\operatorname{cos}^2\alpha = 1 - \left(-\frac{3}{5}\right)^2 = 1 - \frac{9}{25}$$

Calcular a subtração (denominador comum 25):

$$\operatorname{cos}^2\alpha = \frac{25}{25} - \frac{9}{25} = \frac{16}{25}$$

Extrair a raiz quadrada dos dois lados:

$$|\operatorname{cos}\alpha| = \sqrt{\frac{16}{25}} = \frac{\sqrt{16}}{\sqrt{25}} = \frac{4}{5}$$

**Determinar o sinal:** No 3º quadrante, $\operatorname{cos} < 0$, portanto:

$$\operatorname{cos}\alpha = -\frac{4}{5}$$

**Passo 3 — Calcular $\operatorname{tg}\alpha$ pela definição.**

$$\operatorname{tg}\alpha = \frac{\operatorname{sen}\alpha}{\operatorname{cos}\alpha} = \frac{-\dfrac{3}{5}}{-\dfrac{4}{5}}$$

Dividir frações (multiplica pelo inverso do denominador):

$$\operatorname{tg}\alpha = \left(-\frac{3}{5}\right) \times \left(-\frac{5}{4}\right) = \frac{(-3) \times (-5)}{5 \times 4} = \frac{15}{20} = \frac{3}{4}$$

**Verificação do sinal:** No 3º quadrante, $\operatorname{tg} > 0$. O resultado $\dfrac{3}{4} > 0$ é coerente. ✓

**Passo 4 — Calcular as três recíprocas.**

Cada recíproca é simplesmente $1$ dividido pela função original:

$$\operatorname{cotg}\alpha = \frac{1}{\operatorname{tg}\alpha} = \frac{1}{\dfrac{3}{4}} = 1 \times \frac{4}{3} = \frac{4}{3}$$

$$\sec\alpha = \frac{1}{\operatorname{cos}\alpha} = \frac{1}{-\dfrac{4}{5}} = 1 \times \left(-\frac{5}{4}\right) = -\frac{5}{4}$$

$$\csc\alpha = \frac{1}{\operatorname{sen}\alpha} = \frac{1}{-\dfrac{3}{5}} = 1 \times \left(-\frac{5}{3}\right) = -\frac{5}{3}$$

**Verificação dos sinais:** No 3º quadrante — cotg $(+)$ ✓, sec $(-)$ ✓, csc $(-)$ ✓

**Passo 5 — Verificação global com a relação estendida.**

Usar $1 + \operatorname{tg}^2\alpha = \sec^2\alpha$:

$$1 + \left(\frac{3}{4}\right)^2 = 1 + \frac{9}{16} = \frac{16}{16} + \frac{9}{16} = \frac{25}{16}$$

$$\sec^2\alpha = \left(-\frac{5}{4}\right)^2 = \frac{25}{16}$$

$\dfrac{25}{16} = \dfrac{25}{16}$ ✓ — resultado confirmado.

> **Resumo:** $\operatorname{cos}\alpha = -\dfrac{4}{5}$, $\operatorname{tg}\alpha = \dfrac{3}{4}$, $\operatorname{cotg}\alpha = \dfrac{4}{3}$, $\sec\alpha = -\dfrac{5}{4}$, $\csc\alpha = -\dfrac{5}{3}$.

## Armadilhas & Edge Cases

- **Confundir sentido do arco** — sentido positivo é **anti-horário**; arcos negativos percorrem no sentido horário
- **Usar $\ell = r\theta$ com $\theta$ em graus** — a fórmula exige $\theta$ em radianos obrigatoriamente
- **Tangente e secante indefinidas em $\pi/2 + k\pi$** — cos = 0 nesses arcos; tg e sec não existem
- **Cotangente e cossecante indefinidas em $k\pi$** — sen = 0 nesses arcos; cotg e csc não existem
- **Sinal errado na redução ao 1º quadrante** — sempre verificar o quadrante de origem para determinar o sinal correto; o módulo vem do arco reduzido, o sinal vem da tabela de sinais
- **Confundir "arco côngruo" com "arco simétrico"** — côngruos têm mesmo ponto terminal; simétricos são reflexões (eixo $x$: $-\alpha$; eixo $y$: $\pi - \alpha$)
- **Afirmar que $\operatorname{sen}\alpha = 2$ tem solução** — seno e cosseno têm imagem $[-1, 1]$; equação sem solução real
- **Esquecer de verificar com a relação fundamental** — sempre confirmar com $\operatorname{sen}^2 + \operatorname{cos}^2 = 1$

## Conexões

- [[Matemática]] — MOC da área
- [[Graduação em Química]] — Roadmap da graduação
- [[Trigonometria no Triângulo Retângulo]] — pré-requisito direto (razões trigonométricas originais)
- Funções Trigonométricas — extensão natural (gráficos de sen, cos, tg no domínio real)
- [[Física]] — movimento circular uniforme, oscilações, decomposição de vetores, ondas

## Fontes

- IEZZI, Gelson et al. *Fundamentos de Matemática Elementar* — Vol. 3: Trigonometria. Cap. II. Atual Editora.
