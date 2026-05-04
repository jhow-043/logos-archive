---
title: Trigonometria na CircunferÃªncia
description: GeneralizaÃ§Ã£o das razÃµes trigonomÃ©tricas para qualquer Ã¢ngulo real
  via ciclo trigonomÃ©trico â€” extensÃ£o natural do triÃ¢ngulo retÃ¢ngulo para a
  circunfe…
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: matematica
semestre: 1
---
# Trigonometria na CircunferÃªncia

> GeneralizaÃ§Ã£o das razÃµes trigonomÃ©tricas para qualquer Ã¢ngulo real via ciclo trigonomÃ©trico â€” extensÃ£o natural do triÃ¢ngulo retÃ¢ngulo para a circunferÃªncia unitÃ¡ria.

---

## DefiniÃ§Ã£o

A trigonometria na circunferÃªncia (ou ciclo trigonomÃ©trico) estende as definiÃ§Ãµes de seno, cosseno e tangente â€” antes restritas a Ã¢ngulos agudos no triÃ¢ngulo retÃ¢ngulo â€” para **qualquer Ã¢ngulo real**, incluindo Ã¢ngulos obtusos, negativos e maiores que 360Â°. A ideia central Ã© representar Ã¢ngulos como arcos sobre uma **circunferÃªncia de raio 1 centrada na origem** (o ciclo trigonomÃ©trico), e definir as razÃµes trigonomÃ©tricas a partir das **coordenadas do ponto** correspondente a cada arco.

Essa generalizaÃ§Ã£o permite tratar as funÃ§Ãµes trigonomÃ©tricas como funÃ§Ãµes do conjunto dos reais, base para aplicaÃ§Ãµes em fÃ­sica (ondas, MCU) e para o estudo de equaÃ§Ãµes e identidades trigonomÃ©tricas.

## Teoria & Fundamentos

### Arcos e Ã¢ngulos centrais

Dado uma circunferÃªncia de raio $r$ e um Ã¢ngulo central $\theta$, o arco $\ell$ correspondente satisfaz:

$$\ell = r\theta \quad (\theta \text{ em radianos})$$

HÃ¡ uma correspondÃªncia biunÃ­voca entre Ã¢ngulo central e arco â€” basta fixar o raio. No ciclo trigonomÃ©trico ($r = 1$), o comprimento de arco numericamente iguala o Ã¢ngulo em radianos: $\ell = \theta$.

### Grau e radiano

| Unidade | DefiniÃ§Ã£o | Volta completa |
| ------- | --------- | -------------- |
| Grau (Â°) | $\frac{1}{360}$ de volta completa | $360Â°$ |
| Radiano (rad) | Ã¢ngulo cujo arco Ã© igual ao raio | $2\pi$ rad |

A relaÃ§Ã£o de conversÃ£o fundamental Ã©:

$$180Â° = \pi \text{ rad}$$

**ConversÃ£o graus â†’ radianos:** multiplica por $\dfrac{\pi}{180}$

**ConversÃ£o radianos â†’ graus:** multiplica por $\dfrac{180}{\pi}$

### Tabela de arcos notÃ¡veis

| Graus | $0Â°$ | $30Â°$ | $45Â°$ | $60Â°$ | $90Â°$ | $120Â°$ | $135Â°$ | $150Â°$ | $180Â°$ | $270Â°$ | $360Â°$ |
| ------ | --- | ----- | ----- | ----- | ----- | ------ | ------ | ------ | ------ | ------ | ------ |
| Radianos | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\dfrac{2\pi}{3}$ | $\dfrac{3\pi}{4}$ | $\dfrac{5\pi}{6}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |

### Ciclo trigonomÃ©trico

O **ciclo trigonomÃ©trico** Ã© a circunferÃªncia de raio 1 centrada na origem do plano cartesiano, com:

- **Ponto de origem:** $A = (1, 0)$ â€” ponto inicial do arco
- **Sentido positivo:** anti-horÃ¡rio
- **Sentido negativo:** horÃ¡rio
- **Ponto $P$:** extremidade do arco de medida $\alpha$ percorrido a partir de $A$

Os quadrantes sÃ£o definidos pelos semieixos coordenados:

| Quadrante | Intervalo (graus) | Intervalo (radianos) | $x$ | $y$ |
| --------- | ----------------- | -------------------- | --- | --- |
| 1Âº | $0Â° < \alpha < 90Â°$ | $0 < \alpha < \dfrac{\pi}{2}$ | $+$ | $+$ |
| 2Âº | $90Â° < \alpha < 180Â°$ | $\dfrac{\pi}{2} < \alpha < \pi$ | $-$ | $+$ |
| 3Âº | $180Â° < \alpha < 270Â°$ | $\pi < \alpha < \dfrac{3\pi}{2}$ | $-$ | $-$ |
| 4Âº | $270Â° < \alpha < 360Â°$ | $\dfrac{3\pi}{2} < \alpha < 2\pi$ | $+$ | $-$ |

### Arcos cÃ´ngruos

Dois arcos sÃ£o **cÃ´ngruos** (determinam o mesmo ponto $P$ no ciclo) quando diferem de uma volta inteira:

$$\alpha' = \alpha + 2k\pi, \quad k \in \mathbb{Z}$$

A **1Âª determinaÃ§Ã£o positiva** de um arco Ã© o cÃ´ngruo no intervalo $[0, 2\pi)$.

### DefiniÃ§Ã£o de seno e cosseno no ciclo

Dado o arco $\alpha$ com extremidade $P = (x_P, y_P)$ no ciclo trigonomÃ©trico:

$$\operatorname{cos}\alpha = x_P \qquad \operatorname{sen}\alpha = y_P$$

Como $P$ estÃ¡ na circunferÃªncia unitÃ¡ria, vale sempre $x_P^2 + y_P^2 = 1$, o que dÃ¡ a **relaÃ§Ã£o fundamental**:

$$\operatorname{sen}^2\alpha + \operatorname{cos}^2\alpha = 1$$

### Tangente no ciclo

A **tangente** Ã© definida geometricamente como o valor da ordenada do ponto onde a reta $OP$ (prolongada) intersecta o eixo das tangentes ($x = 1$):

$$\operatorname{tg}\alpha = \frac{\operatorname{sen}\alpha}{\operatorname{cos}\alpha}, \quad \operatorname{cos}\alpha \neq 0$$

A tangente **nÃ£o existe** quando $\operatorname{cos}\alpha = 0$, i.e., $\alpha = \dfrac{\pi}{2} + k\pi,\ k \in \mathbb{Z}$.

### Cotangente, secante e cossecante

As outras trÃªs razÃµes sÃ£o recÃ­procas das anteriores:

$$\operatorname{cotg}\alpha = \frac{\operatorname{cos}\alpha}{\operatorname{sen}\alpha} = \frac{1}{\operatorname{tg}\alpha}, \quad \operatorname{sen}\alpha \neq 0$$

$$\sec\alpha = \frac{1}{\operatorname{cos}\alpha}, \quad \operatorname{cos}\alpha \neq 0$$

$$\csc\alpha = \frac{1}{\operatorname{sen}\alpha}, \quad \operatorname{sen}\alpha \neq 0$$

> **DomÃ­nio:** cotg e csc nÃ£o existem quando $\operatorname{sen}\alpha = 0$, i.e., $\alpha = k\pi,\ k \in \mathbb{Z}$.

### Sinais das funÃ§Ãµes por quadrante

| FunÃ§Ã£o | 1Âº | 2Âº | 3Âº | 4Âº |
| ------ | -- | -- | -- | -- |
| $\operatorname{sen}$ | $+$ | $+$ | $-$ | $-$ |
| $\operatorname{cos}$ | $+$ | $-$ | $-$ | $+$ |
| $\operatorname{tg}$ | $+$ | $-$ | $+$ | $-$ |
| $\operatorname{cotg}$ | $+$ | $-$ | $+$ | $-$ |
| $\sec$ | $+$ | $-$ | $-$ | $+$ |
| $\csc$ | $+$ | $+$ | $-$ | $-$ |

> **MnemÃ´nico CAST** (4Âº â†’ 1Âº â†’ 2Âº â†’ 3Âº): **C**osseno, **A**ll (todos), **S**eno, **T**angente â€” indica qual funÃ§Ã£o Ã© positiva em cada quadrante percorrendo sentido anti-horÃ¡rio a partir do 4Âº.

### ReduÃ§Ã£o ao 1Âº quadrante

Qualquer arco pode ser reduzido a um arco do 1Âº quadrante usando as relaÃ§Ãµes abaixo, onde $x \in \left(0, \dfrac{\pi}{2}\right)$:

| Arco | $\operatorname{sen}$ | $\operatorname{cos}$ | $\operatorname{tg}$ |
| ---- | -------------------- | ------ | -------------------- |
| $\pi - x$ (2Âº quadrante) | $+\operatorname{sen}x$ | $-\operatorname{cos} x$ | $-\operatorname{tg}x$ |
| $\pi + x$ (3Âº quadrante) | $-\operatorname{sen}x$ | $-\operatorname{cos} x$ | $+\operatorname{tg}x$ |
| $2\pi - x$ (4Âº quadrante) | $-\operatorname{sen}x$ | $+\operatorname{cos} x$ | $-\operatorname{tg}x$ |

> **Regra prÃ¡tica:** o valor absoluto da funÃ§Ã£o Ã© o mesmo do arco do 1Âº quadrante; o sinal vem do quadrante de origem (tabela de sinais acima).

### Periodicidade

$$\operatorname{sen}(\alpha + 2\pi) = \operatorname{sen}\alpha \qquad \operatorname{cos}(\alpha + 2\pi) = \operatorname{cos}\alpha \quad \Rightarrow \text{ perÃ­odo } 2\pi$$

$$\operatorname{tg}(\alpha + \pi) = \operatorname{tg}\alpha \qquad \operatorname{cotg}(\alpha + \pi) = \operatorname{cotg}\alpha \quad \Rightarrow \text{ perÃ­odo } \pi$$

### RelaÃ§Ãµes fundamentais estendidas

Da identidade $\operatorname{sen}^2\alpha + \operatorname{cos}^2\alpha = 1$, dividindo por $\operatorname{cos}^2\alpha$ e por $\operatorname{sen}^2\alpha$ respectivamente:

$$1 + \operatorname{tg}^2\alpha = \sec^2\alpha$$

$$1 + \operatorname{cotg}^2\alpha = \csc^2\alpha$$

## FÃ³rmulas & EquaÃ§Ãµes

### SÃ­mbolos e variÃ¡veis

| SÃ­mbolo | Significado | ObservaÃ§Ã£o |
| ------- | ----------- | ---------- |
| $\alpha$ | Arco/Ã¢ngulo no ciclo | Qualquer valor real (graus ou radianos) |
| $P = (x_P, y_P)$ | Ponto no ciclo | $x_P^2 + y_P^2 = 1$ |
| $k$ | Inteiro arbitrÃ¡rio | Representa voltas completas |
| $\operatorname{sen}\alpha$ | Seno | Ordenada $y_P$ |
| $\operatorname{cos}\alpha$ | Cosseno | Abscissa $x_P$ |
| $\operatorname{tg}\alpha$ | Tangente | $\operatorname{sen}\alpha / \operatorname{cos}\alpha$ |
| $\operatorname{cotg}\alpha$ | Cotangente | $\operatorname{cos}\alpha / \operatorname{sen}\alpha$ |
| $\sec\alpha$ | Secante | $1/\operatorname{cos}\alpha$ |
| $\csc\alpha$ | Cossecante | $1/\operatorname{sen}\alpha$ |

### Valores notÃ¡veis completos

| Arco | $\operatorname{sen}$ | $\operatorname{cos}$ | $\operatorname{tg}$ | $\operatorname{cotg}$ | $\sec$ | $\csc$ |
| ---- | -------------------- | ------ | -------------------- | --------------------- | ------ | ------ |
| $0$ | $0$ | $1$ | $0$ | â€” | $1$ | â€” |
| $\dfrac{\pi}{6}$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{3}}{3}$ | $\sqrt{3}$ | $\dfrac{2\sqrt{3}}{3}$ | $2$ |
| $\dfrac{\pi}{4}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $1$ | $1$ | $\sqrt{2}$ | $\sqrt{2}$ |
| $\dfrac{\pi}{3}$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{1}{2}$ | $\sqrt{3}$ | $\dfrac{\sqrt{3}}{3}$ | $2$ | $\dfrac{2\sqrt{3}}{3}$ |
| $\dfrac{\pi}{2}$ | $1$ | $0$ | â€” | $0$ | â€” | $1$ |

### RelaÃ§Ãµes fundamentais

$$\operatorname{sen}^2\alpha + \operatorname{cos}^2\alpha = 1$$

$$1 + \operatorname{tg}^2\alpha = \sec^2\alpha$$

$$1 + \operatorname{cotg}^2\alpha = \csc^2\alpha$$

## Exemplos Resolvidos

**Exemplo 1 â€” BÃ¡sico: converter graus para radianos e localizar no ciclo**

> **Enunciado:** Converter $210Â°$ para radianos e determinar em qual quadrante o arco se encontra.

**Passo 1 â€” Montar a proporÃ§Ã£o de conversÃ£o.**

A relaÃ§Ã£o fundamental entre as duas unidades Ã© $180Â° = \pi$ rad. Para converter qualquer Ã¢ngulo em graus para radianos, multiplica-se por $\dfrac{\pi}{180}$:

$$210Â° \times \frac{\pi}{180}$$

**Passo 2 â€” Calcular o produto e simplificar a fraÃ§Ã£o.**

Multiplica-se numerador com numerador e coloca o denominador:

$$\frac{210\pi}{180}$$

Simplificar: $\operatorname{mdc}(210, 180) = 30$. Divido ambos por 30:

$$\frac{210 \div 30}{180 \div 30}\,\pi = \frac{7}{6}\pi = \frac{7\pi}{6}$$

**Passo 3 â€” Localizar o arco no ciclo comparando com os limites de quadrante.**

Os limites em radianos sÃ£o:
- Fim do 2Âº quadrante: $\pi = \dfrac{6\pi}{6}$
- Fim do 3Âº quadrante: $\dfrac{3\pi}{2} = \dfrac{9\pi}{6}$

Como $\dfrac{6\pi}{6} < \dfrac{7\pi}{6} < \dfrac{9\pi}{6}$, ou seja $\pi < \dfrac{7\pi}{6} < \dfrac{3\pi}{2}$, o arco estÃ¡ no **3Âº quadrante**.

> **Resultado:** $210Â° = \dfrac{7\pi}{6}$ rad â†’ **3Âº quadrante**.

---

**Exemplo 2 â€” IntermediÃ¡rio: calcular trÃªs funÃ§Ãµes por reduÃ§Ã£o ao 1Âº quadrante**

> **Enunciado:** Calcular $\operatorname{sen}\!\left(\dfrac{5\pi}{6}\right)$, $\operatorname{cos}\!\left(\dfrac{5\pi}{6}\right)$ e $\operatorname{tg}\!\left(\dfrac{5\pi}{6}\right)$.

**Passo 1 â€” Identificar o quadrante do arco.**

Comparar $\dfrac{5\pi}{6}$ com os limites do ciclo (denominador comum 6):

$$\frac{\pi}{2} = \frac{3\pi}{6} \qquad \pi = \frac{6\pi}{6}$$

Como $\dfrac{3\pi}{6} < \dfrac{5\pi}{6} < \dfrac{6\pi}{6}$, o arco pertence ao **2Âº quadrante**.

**Passo 2 â€” Escrever o arco na forma $\pi - x$ para encontrar o arco equivalente no 1Âº quadrante.**

Para um arco do 2Âº quadrante, a fÃ³rmula de reduÃ§Ã£o Ã© $\alpha = \pi - x$, onde $x$ Ã© o arco do 1Âº quadrante correspondente. Isolo $x$:

$$\frac{5\pi}{6} = \pi - x \implies x = \pi - \frac{5\pi}{6}$$

Fazer a subtraÃ§Ã£o (denominador comum 6):

$$x = \frac{6\pi}{6} - \frac{5\pi}{6} = \frac{\pi}{6}$$

O arco reduzido ao 1Âº quadrante Ã© $\dfrac{\pi}{6}$ â€” um arco notÃ¡vel.

**Passo 3 â€” Determinar os sinais das funÃ§Ãµes no 2Âº quadrante.**

No 2Âº quadrante: $x < 0$ e $y > 0$. Portanto:
- $\operatorname{sen} > 0$ (positivo, pois depende de $y$)
- $\operatorname{cos} < 0$ (negativo, pois depende de $x$)
- $\operatorname{tg} < 0$ (negativo, pois $\operatorname{tg} = y/x$ e $y > 0$, $x < 0$)

**Passo 4 â€” Aplicar os valores notÃ¡veis de $\dfrac{\pi}{6}$ com os sinais do 2Âº quadrante.**

Da tabela de valores notÃ¡veis: $\operatorname{sen}\!\left(\dfrac{\pi}{6}\right) = \dfrac{1}{2}$, $\operatorname{cos}\!\left(\dfrac{\pi}{6}\right) = \dfrac{\sqrt{3}}{2}$, $\operatorname{tg}\!\left(\dfrac{\pi}{6}\right) = \dfrac{\sqrt{3}}{3}$.

Aplicando os sinais do 2Âº quadrante:

$$\operatorname{sen}\!\left(\frac{5\pi}{6}\right) = +\operatorname{sen}\!\left(\frac{\pi}{6}\right) = +\frac{1}{2} = \boxed{\frac{1}{2}}$$

$$\operatorname{cos}\!\left(\frac{5\pi}{6}\right) = -\operatorname{cos}\!\left(\frac{\pi}{6}\right) = -\frac{\sqrt{3}}{2} = \boxed{-\frac{\sqrt{3}}{2}}$$

$$\operatorname{tg}\!\left(\frac{5\pi}{6}\right) = -\operatorname{tg}\!\left(\frac{\pi}{6}\right) = -\frac{\sqrt{3}}{3} = \boxed{-\frac{\sqrt{3}}{3}}$$

**VerificaÃ§Ã£o rÃ¡pida:** $\operatorname{sen}^2 + \operatorname{cos}^2 = \left(\dfrac{1}{2}\right)^2 + \left(-\dfrac{\sqrt{3}}{2}\right)^2 = \dfrac{1}{4} + \dfrac{3}{4} = 1$ âœ“

---

**Exemplo 3 â€” AvanÃ§ado: determinar as 6 funÃ§Ãµes a partir de uma razÃ£o dada**

> **Enunciado:** Dado $\operatorname{sen}\alpha = -\dfrac{3}{5}$ com $\alpha$ no **3Âº quadrante**, encontrar $\operatorname{cos}\alpha$, $\operatorname{tg}\alpha$, $\operatorname{cotg}\alpha$, $\sec\alpha$ e $\csc\alpha$.

**Passo 1 â€” Verificar a consistÃªncia do dado com o quadrante.**

No 3Âº quadrante, $\operatorname{sen} < 0$. O dado $\operatorname{sen}\alpha = -\dfrac{3}{5} < 0$ Ã© consistente. âœ“

**Passo 2 â€” Encontrar $\operatorname{cos}\alpha$ usando a relaÃ§Ã£o fundamental.**

Partir de $\operatorname{sen}^2\alpha + \operatorname{cos}^2\alpha = 1$ e **isolar $\operatorname{cos}^2\alpha$**:

$$\operatorname{cos}^2\alpha = 1 - \operatorname{sen}^2\alpha$$

Substituir o valor dado:

$$\operatorname{cos}^2\alpha = 1 - \left(-\frac{3}{5}\right)^2 = 1 - \frac{9}{25}$$

Calcular a subtraÃ§Ã£o (denominador comum 25):

$$\operatorname{cos}^2\alpha = \frac{25}{25} - \frac{9}{25} = \frac{16}{25}$$

Extrair a raiz quadrada dos dois lados:

$$|\operatorname{cos}\alpha| = \sqrt{\frac{16}{25}} = \frac{\sqrt{16}}{\sqrt{25}} = \frac{4}{5}$$

**Determinar o sinal:** No 3Âº quadrante, $\operatorname{cos} < 0$, portanto:

$$\operatorname{cos}\alpha = -\frac{4}{5}$$

**Passo 3 â€” Calcular $\operatorname{tg}\alpha$ pela definiÃ§Ã£o.**

$$\operatorname{tg}\alpha = \frac{\operatorname{sen}\alpha}{\operatorname{cos}\alpha} = \frac{-\dfrac{3}{5}}{-\dfrac{4}{5}}$$

Dividir fraÃ§Ãµes (multiplica pelo inverso do denominador):

$$\operatorname{tg}\alpha = \left(-\frac{3}{5}\right) \times \left(-\frac{5}{4}\right) = \frac{(-3) \times (-5)}{5 \times 4} = \frac{15}{20} = \frac{3}{4}$$

**VerificaÃ§Ã£o do sinal:** No 3Âº quadrante, $\operatorname{tg} > 0$. O resultado $\dfrac{3}{4} > 0$ Ã© coerente. âœ“

**Passo 4 â€” Calcular as trÃªs recÃ­procas.**

Cada recÃ­proca Ã© simplesmente $1$ dividido pela funÃ§Ã£o original:

$$\operatorname{cotg}\alpha = \frac{1}{\operatorname{tg}\alpha} = \frac{1}{\dfrac{3}{4}} = 1 \times \frac{4}{3} = \frac{4}{3}$$

$$\sec\alpha = \frac{1}{\operatorname{cos}\alpha} = \frac{1}{-\dfrac{4}{5}} = 1 \times \left(-\frac{5}{4}\right) = -\frac{5}{4}$$

$$\csc\alpha = \frac{1}{\operatorname{sen}\alpha} = \frac{1}{-\dfrac{3}{5}} = 1 \times \left(-\frac{5}{3}\right) = -\frac{5}{3}$$

**VerificaÃ§Ã£o dos sinais:** No 3Âº quadrante â€” cotg $(+)$ âœ“, sec $(-)$ âœ“, csc $(-)$ âœ“

**Passo 5 â€” VerificaÃ§Ã£o global com a relaÃ§Ã£o estendida.**

Usar $1 + \operatorname{tg}^2\alpha = \sec^2\alpha$:

$$1 + \left(\frac{3}{4}\right)^2 = 1 + \frac{9}{16} = \frac{16}{16} + \frac{9}{16} = \frac{25}{16}$$

$$\sec^2\alpha = \left(-\frac{5}{4}\right)^2 = \frac{25}{16}$$

$\dfrac{25}{16} = \dfrac{25}{16}$ âœ“ â€” resultado confirmado.

> **Resumo:** $\operatorname{cos}\alpha = -\dfrac{4}{5}$, $\operatorname{tg}\alpha = \dfrac{3}{4}$, $\operatorname{cotg}\alpha = \dfrac{4}{3}$, $\sec\alpha = -\dfrac{5}{4}$, $\csc\alpha = -\dfrac{5}{3}$.

## Armadilhas & Edge Cases

- **Confundir sentido do arco** â€” sentido positivo Ã© **anti-horÃ¡rio**; arcos negativos percorrem no sentido horÃ¡rio
- **Usar $\ell = r\theta$ com $\theta$ em graus** â€” a fÃ³rmula exige $\theta$ em radianos obrigatoriamente
- **Tangente e secante indefinidas em $\pi/2 + k\pi$** â€” cos = 0 nesses arcos; tg e sec nÃ£o existem
- **Cotangente e cossecante indefinidas em $k\pi$** â€” sen = 0 nesses arcos; cotg e csc nÃ£o existem
- **Sinal errado na reduÃ§Ã£o ao 1Âº quadrante** â€” sempre verificar o quadrante de origem para determinar o sinal correto; o mÃ³dulo vem do arco reduzido, o sinal vem da tabela de sinais
- **Confundir "arco cÃ´ngruo" com "arco simÃ©trico"** â€” cÃ´ngruos tÃªm mesmo ponto terminal; simÃ©tricos sÃ£o reflexÃµes (eixo $x$: $-\alpha$; eixo $y$: $\pi - \alpha$)
- **Afirmar que $\operatorname{sen}\alpha = 2$ tem soluÃ§Ã£o** â€” seno e cosseno tÃªm imagem $[-1, 1]$; equaÃ§Ã£o sem soluÃ§Ã£o real
- **Esquecer de verificar com a relaÃ§Ã£o fundamental** â€” sempre confirmar com $\operatorname{sen}^2 + \operatorname{cos}^2 = 1$

## ConexÃµes

- [[MatemÃ¡tica]] â€” MOC da Ã¡rea
- [[GraduaÃ§Ã£o em QuÃ­mica]] â€” Roadmap da graduaÃ§Ã£o
- [[Trigonometria no TriÃ¢ngulo RetÃ¢ngulo]] â€” prÃ©-requisito direto (razÃµes trigonomÃ©tricas originais)
- FunÃ§Ãµes TrigonomÃ©tricas â€” extensÃ£o natural (grÃ¡ficos de sen, cos, tg no domÃ­nio real)
- [[FÃ­sica]] â€” movimento circular uniforme, oscilaÃ§Ãµes, decomposiÃ§Ã£o de vetores, ondas

## Fontes

- IEZZI, Gelson et al. *Fundamentos de MatemÃ¡tica Elementar* â€” Vol. 3: Trigonometria. Cap. II. Atual Editora.
