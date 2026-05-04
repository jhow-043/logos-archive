---
title: Limites
description: O limite formaliza a ideia de "tendência" — o valor para o qual uma função
  se aproxima quando a variável independente se aproxima de um ponto, independentemente…
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: matematica
semestre: 1
---
# Limites

> O limite formaliza a ideia de "tendência" — o valor para o qual uma função se aproxima quando a variável independente se aproxima de um ponto, independentemente do valor da função nesse ponto. É o alicerce rigoroso do Cálculo.

---

## Definição

### Noção intuitiva

Diz-se que $L$ é o **limite** de $f(x)$ quando $x$ tende a $p$, e escreve-se:

$$\lim_{x \to p} f(x) = L$$

quando $f(x)$ fica arbitrariamente próximo de $L$ sempre que $x$ estiver suficientemente próximo de $p$ — **sem que $x$ precise assumir o valor $p$**.

> O que importa é o **comportamento de $f$ na vizinhança de $p$**, não o valor $f(p)$ (que pode até não existir).

**Gráfico — noção intuitiva de limite:**

```
  y
  |
  |          . ← f(x) se aproxima de L
  |       .
L |......○.............  ← L  (limite)
  |       .  ↑
  |          f(p): pode ser diferente de L, ou não existir
  |
  +----------+───────── x
             p
```
_O comportamento de $f$ ao **redor** de $p$ determina o limite — o valor (ou existência) de $f(p)$ é irrelevante._

### Definição formal (Definição $\varepsilon$-$\delta$)

(Guidorizzi Vol.1, pg. 69)

$$\lim_{x \to p} f(x) = L \;\iff\; \forall\, \varepsilon > 0,\; \exists\, \delta > 0 \;\text{ tal que }\; 0 < |x - p| < \delta \;\implies\; |f(x) - L| < \varepsilon$$

**Interpretação geométrica:**

- $|f(x) - L| < \varepsilon$: o valor $f(x)$ está dentro da **faixa horizontal** $(L - \varepsilon,\, L + \varepsilon)$
- $0 < |x - p| < \delta$: o ponto $x$ está dentro da **vizinhança furada** $(p - \delta,\, p + \delta) \setminus \{p\}$
- A definição diz: qualquer que seja a precisão $\varepsilon$ exigida em $y$, sempre existe um "raio" $\delta$ em $x$ que garante essa precisão.

> O símbolo $0 < |x - p|$ ("vizinhança furada") formaliza que $x \neq p$: o limite descreve o que acontece **ao redor de** $p$, não **em** $p$.

**Gráfico — interpretação da definição $\varepsilon$-$\delta$:**

```
  y
  |
L+ε  - - - - - - - - - - -  ← faixa ε (superior)
  |           /\
  L  ────────/  \──────────  ← valor do limite L
  |         /    \
L-ε  - - - - - - - - - - -  ← faixa ε (inferior)
  |          ↑  ↑  ↑
  +──────────+──+──+──────── x
            p-δ  p  p+δ
                 ↑
           (excluído: x ≠ p)
```
_Para qualquer "precisão" $\varepsilon$ exigida em $y$, existe um raio $\delta$ em $x$ tal que todo $x$ na vizinhança furada de $p$ produz $f(x)$ dentro da faixa $\varepsilon$ ao redor de $L$._

## Teoria & Fundamentos

### Unicidade do limite

> **Teorema:** Se $\displaystyle\lim_{x \to p} f(x) = L$ e $\displaystyle\lim_{x \to p} f(x) = M$, então $L = M$.

O limite, quando existe, é único. (Demonstração por absurdo usando a definição $\varepsilon$-$\delta$.)

### Limites laterais

**Limite lateral esquerdo** (para $x$ vindo de valores menores que $p$):

$$\lim_{x \to p^-} f(x) = L^- \;\iff\; \forall\, \varepsilon > 0,\; \exists\, \delta > 0 \;\text{ tal que }\; p - \delta < x < p \;\implies\; |f(x) - L^-| < \varepsilon$$

**Limite lateral direito** (para $x$ vindo de valores maiores que $p$):

$$\lim_{x \to p^+} f(x) = L^+ \;\iff\; \forall\, \varepsilon > 0,\; \exists\, \delta > 0 \;\text{ tal que }\; p < x < p + \delta \;\implies\; |f(x) - L^+| < \varepsilon$$

**Critério de existência:**

$$\lim_{x \to p} f(x) = L \;\iff\; \lim_{x \to p^-} f(x) = \lim_{x \to p^+} f(x) = L$$

O limite bilateral existe **se e somente se** os dois limites laterais existem e são iguais.

**Gráfico — limites laterais distintos (limite bilateral não existe):**

```
  y
  |
1 |          •──────────  ← lim⁺ = +1  (• = ponto incluído)
  |
0 +──────────+─────────── x
  |          0
  |
-1|──────────○            ← lim⁻ = −1  (○ = ponto excluído)
  |
  lim⁻ = −1  ≠  +1 = lim⁺   →   limite bilateral NÃO existe
```
_Como os laterais convergem para valores diferentes, o limite de $|x|/x$ em $x = 0$ não existe. O gráfico exibe um "salto"._

### Propriedades operatórias dos limites

Sejam $\displaystyle\lim_{x \to p} f(x) = L$ e $\displaystyle\lim_{x \to p} g(x) = M$. Então:

| Propriedade | Fórmula |
| ----------- | ------- |
| Soma | $\displaystyle\lim_{x \to p}[f(x) + g(x)] = L + M$ |
| Diferença | $\displaystyle\lim_{x \to p}[f(x) - g(x)] = L - M$ |
| Múltiplo por constante | $\displaystyle\lim_{x \to p}[k \cdot f(x)] = k \cdot L$ |
| Produto | $\displaystyle\lim_{x \to p}[f(x) \cdot g(x)] = L \cdot M$ |
| Quociente | $\displaystyle\lim_{x \to p}\frac{f(x)}{g(x)} = \frac{L}{M}$, desde que $M \neq 0$ |
| Potência | $\displaystyle\lim_{x \to p}[f(x)]^n = L^n$, $n \in \mathbb{N}$ |
| Raiz | $\displaystyle\lim_{x \to p}\sqrt[n]{f(x)} = \sqrt[n]{L}$, desde que $L > 0$ (se $n$ par) |

> **Corolário — substituição direta:** Todo polinômio $p(x)$ satisfaz $\displaystyle\lim_{x \to p} p(x) = p(p)$. Para funções racionais $f(x) = p(x)/q(x)$, vale $\displaystyle\lim_{x \to a} f(x) = f(a)$ desde que $q(a) \neq 0$.

### Teorema do Confronto (Sanduíche)

> **Teorema:** Se $g(x) \leq f(x) \leq h(x)$ em uma vizinhança de $p$ (exceto possivelmente em $p$), e $\displaystyle\lim_{x \to p} g(x) = \lim_{x \to p} h(x) = L$, então $\displaystyle\lim_{x \to p} f(x) = L$.

**Interpretação:** $f$ fica "espremida" entre $g$ e $h$; se $g$ e $h$ convergem para o mesmo valor, $f$ é forçada a convergir também.

**Aplicação principal:** demonstrar o limite fundamental trigonométrico.

**Gráfico — Teorema do Confronto:**

```
  y
  |         h(x)
  |        /‾‾‾\            ← cota superior
  |       / f(x)\
  L ─────*───────*────────  ← g, f e h → L quando x → p
  |       \ g(x)/
  |        \___/            ← cota inferior
  |
  +──────────+──────────── x
             p
```
_$g(x) \leq f(x) \leq h(x)$ e $\lim g = \lim h = L$ $\implies$ $\lim f = L$ — $f$ é "espremida" e obrigada a convergir._

### Limite fundamental trigonométrico

$$\lim_{x \to 0} \frac{\operatorname{sen} x}{x} = 1 \qquad (x \text{ em radianos})$$

**Esboço da demonstração via Sanduíche:**

Para $0 < x < \pi/2$, vale a desigualdade geométrica (comparando áreas de triângulos e setor circular):

$$\operatorname{cos} x < \frac{\operatorname{sen} x}{x} < 1$$

Tomando $\lim_{x \to 0^+}$: $\displaystyle\lim_{x \to 0^+} \operatorname{cos} x = 1$ e o limite da cota superior também é $1$. Pelo Sanduíche:

$$\lim_{x \to 0^+} \frac{\operatorname{sen} x}{x} = 1$$

Como $\operatorname{sen} x / x$ é **par** (ambos são funções ímpares, então o quociente é par), o limite lateral esquerdo também é $1$. Logo o limite bilateral existe e vale $1$.

> **Consequência imediata:** $\displaystyle\lim_{x \to 0} \frac{1 - \operatorname{cos} x}{x} = 0$

**Gráfico — $f(x) = \dfrac{\operatorname{sen} x}{x}$:**

```
  y
  |
1 |........○.............  ← limite = 1  (○: indefinido em x=0)
  |       /|\ 
  |      / | \                    ·
  |     /  |  \               ·
  |    /   |   ·         ·
  |___/    |    ·    ·
  +─────── +────────────────────── x
          0
```
_A curva se aproxima de $1$ pelos dois lados de $x = 0$. O Teorema do Confronto ($\operatorname{cos} x < \operatorname{sen} x / x < 1$) confirma que o limite vale exatamente $1$._

### Indeterminações

Quando substituição direta produz uma das formas abaixo, o resultado é **indeterminado** — é necessário manipulação algébrica antes de concluir:

| Forma indeterminada | Estratégias típicas de resolução |
| ------------------- | -------------------------------- |
| $\dfrac{0}{0}$ | Fatoração, racionalização (multiplicar pelo conjugado), simplificação |
| $\dfrac{\infty}{\infty}$ | Dividir pelo maior grau (polinômios), identificar o termo dominante |
| $0 \cdot \infty$ | Reescrever como $\dfrac{0}{1/\infty}$ ou $\dfrac{\infty}{1/0}$ |
| $\infty - \infty$ | Fatoração, denominador comum, conjugado |
| $0^0$, $\infty^0$, $1^\infty$ | Reescrever com exponencial e logaritmo (ver módulo Derivadas — L'Hôpital) |

> Indeterminação **não significa que o limite não existe** — significa apenas que é necessário continuar trabalhando.

### Limites infinitos e no infinito

**Limite infinito** ($f(x)$ cresce sem cota quando $x \to p$):

$$\lim_{x \to p} f(x) = +\infty \;\iff\; \forall M > 0,\; \exists\, \delta > 0 \;\text{ tal que }\; 0 < |x-p| < \delta \implies f(x) > M$$

→ A reta $x = p$ é **assíntota vertical** do gráfico de $f$.

**Limite no infinito** ($x$ cresce sem cota, $f(x)$ tende a $L$):

$$\lim_{x \to +\infty} f(x) = L \;\iff\; \forall\, \varepsilon > 0,\; \exists\, N > 0 \;\text{ tal que }\; x > N \implies |f(x) - L| < \varepsilon$$

→ A reta $y = L$ é **assíntota horizontal** do gráfico de $f$.

| Tipo | Notação | Descrição |
| ---- | ------- | --------- |
| Limite infinito | $\displaystyle\lim_{x \to p} f(x) = \pm\infty$ | $f$ diverge ao redor de $p$ → assíntota vertical |
| Limite no infinito | $\displaystyle\lim_{x \to \pm\infty} f(x) = L$ | $f$ estabiliza quando $x$ cresce → assíntota horizontal |

**Gráficos — assíntota vertical vs. assíntota horizontal:**

```
Assíntota vertical: lim_{x→p} f(x) = +∞

  y
  |  ↑    |  ↑
  | /     | /
  |/      |/
  +───────+──────── x
          p
  ← f cresce sem cota ao se aproximar de x = p (reta vertical x = p)


Assíntota horizontal: lim_{x→+∞} f(x) = L

  y
  |
L |. . . . .__________  ← f(x) → L  (reta horizontal y = L)
  |         /
  |        /
  |_______/
  +─────────────────── x
                → +∞
```

> **Distinção fundamental:** "limite **no** infinito" ($x \to \infty$) vs. "limite **infinito**" ($f \to \infty$) — são situações diferentes e frequentemente confundidas.

### Limite de função composta

> **Teorema:** Se $\displaystyle\lim_{x \to p} g(x) = q$ e $\displaystyle\lim_{y \to q} f(y) = L$, e $f$ é contínua em $q$ (ou $g(x) \neq q$ numa vizinhança furada de $p$), então:
>
> $$\lim_{x \to p} f(g(x)) = f\!\left(\lim_{x \to p} g(x)\right) = f(q) = L$$

## Fórmulas & Equações

### Definição $\varepsilon$-$\delta$

$$\lim_{x \to p} f(x) = L \;\iff\; \forall\, \varepsilon > 0,\; \exists\, \delta > 0 :\; 0 < |x - p| < \delta \implies |f(x) - L| < \varepsilon$$

### Critério dos limites laterais

$$\lim_{x \to p} f(x) \text{ existe} \;\iff\; \lim_{x \to p^-} f(x) = \lim_{x \to p^+} f(x)$$

### Limites notáveis

$$\lim_{x \to 0} \frac{\operatorname{sen} x}{x} = 1 \qquad \lim_{x \to 0} \frac{1 - \operatorname{cos} x}{x} = 0 \qquad \lim_{x \to 0} \frac{\operatorname{tg} x}{x} = 1$$

### Limite de polinômio / racional por substituição direta

$$\lim_{x \to a} p(x) = p(a) \qquad \lim_{x \to a} \frac{p(x)}{q(x)} = \frac{p(a)}{q(a)}, \; q(a) \neq 0$$

## Exemplos Resolvidos

**Exemplo 1 — Básico: substituição direta em polinômio**

> **Enunciado:** Calcule $\displaystyle\lim_{x \to 2}(x^2 - 3x + 5)$.

**Passo 1 — Identificar o tipo de função.**

$f(x) = x^2 - 3x + 5$ é um **polinômio**. Polinômios são contínuos em todo $\mathbb{R}$, logo as propriedades operatórias dos limites garantem que o limite pode ser calculado por substituição direta.

**Passo 2 — Tentar substituição direta.**

Substituir $x = 2$ na expressão:

$$\lim_{x \to 2}(x^2 - 3x + 5) = (2)^2 - 3 \cdot (2) + 5$$

**Passo 3 — Calcular cada parcela.**

$(2)^2 = 4$

$3 \cdot (2) = 6$

Portanto:

$$4 - 6 + 5 = 3$$

**Passo 4 — Verificar a resposta.**

O resultado é $3$: o limite existe, é finito, e foi obtido por substituição direta (válida pois o denominador — inexistente neste caso — não cria problemas).

$$\boxed{\lim_{x \to 2}(x^2 - 3x + 5) = 3}$$

---

**Exemplo 2 — Intermediário: indeterminação $0/0$ por fatoração**

> **Enunciado:** Calcule $\displaystyle\lim_{x \to 3} \dfrac{x^2 - 9}{x - 3}$.

**Passo 1 — Tentar substituição direta.**

Substituir $x = 3$:

$$\frac{(3)^2 - 9}{3 - 3} = \frac{9 - 9}{0} = \frac{0}{0}$$

Forma indeterminada $\dfrac{0}{0}$. **Não é possível concluir diretamente** — é necessário manipulação algébrica.

**Passo 2 — Reconhecer a estrutura do numerador.**

$x^2 - 9$ é **diferença de quadrados**: $x^2 - 9 = x^2 - 3^2$.

Aplicar a identidade $a^2 - b^2 = (a-b)(a+b)$:

$$x^2 - 9 = (x - 3)(x + 3)$$

**Passo 3 — Reescrever a fração com o numerador fatorado.**

$$\frac{x^2 - 9}{x - 3} = \frac{(x-3)(x+3)}{x-3}$$

**Passo 4 — Simplificar o fator comum.**

Como estamos calculando o limite com $x \to 3$ e **$x \neq 3$**, o fator $(x - 3)$ nunca é zero durante o processo de aproximação. Logo é lícito cancelar:

$$\frac{(x-3)(x+3)}{x-3} = x + 3, \quad \text{para } x \neq 3$$

**Passo 5 — Calcular o limite da expressão simplificada.**

A função $x + 3$ é um polinômio, e o limite pode ser calculado por substituição direta:

$$\lim_{x \to 3}(x + 3) = 3 + 3 = 6$$

**Passo 6 — Confirmar o resultado.**

Como $\dfrac{x^2 - 9}{x-3} = x+3$ para todo $x \neq 3$, e o limite só examina o que acontece **próximo de** (não em) $x = 3$:

$$\boxed{\lim_{x \to 3} \frac{x^2 - 9}{x - 3} = 6}$$

> **Observação:** A função original não está definida em $x = 3$ (denominador zero), mas o limite existe e vale $6$. Isso é um exemplo de descontinuidade removível — será formalizado na nota de Continuidade.

**Gráfico — "buraco" em $x = 3$:**

```
  y
  |
6 |..........○  ← buraco: f(3) indefinido, mas lim_{x→3} = 6
  |         /
  |        /     f(x) = x + 3  para x ≠ 3
  |       /
  |      /
  +──────+──────────── x
         3
```
_O gráfico é a reta $y = x + 3$ com um único ponto removido em $(3,\,6)$. O limite "enxerga" a reta — não o buraco._

---

**Exemplo 3 — Avançado: limite fundamental trigonométrico + limites laterais**

> **Enunciado (parte A):** Calcule $\displaystyle\lim_{x \to 0} \dfrac{\operatorname{sen}(3x)}{x}$.

**Passo 1 — Tentar substituição direta.**

Substituir $x = 0$:

$$\frac{\operatorname{sen}(3 \cdot 0)}{0} = \frac{\operatorname{sen}(0)}{0} = \frac{0}{0}$$

Indeterminação $\dfrac{0}{0}$. A estratégia aqui é usar o **limite fundamental** $\displaystyle\lim_{u \to 0} \dfrac{\operatorname{sen} u}{u} = 1$, mas o argumento e o denominador precisam ser **idênticos**.

**Passo 2 — Manipular para criar a forma $\operatorname{sen}(u)/u$.**

O argumento do seno é $3x$; o denominador é $x$. Multiplicar e dividir por $3$:

$$\frac{\operatorname{sen}(3x)}{x} = \frac{\operatorname{sen}(3x)}{x} \cdot \frac{3}{3} = 3 \cdot \frac{\operatorname{sen}(3x)}{3x}$$

**Passo 3 — Fazer a substituição $u = 3x$.**

Quando $x \to 0$, temos $u = 3x \to 0$. Portanto:

$$\lim_{x \to 0} 3 \cdot \frac{\operatorname{sen}(3x)}{3x} = 3 \cdot \lim_{u \to 0} \frac{\operatorname{sen}(u)}{u}$$

**Passo 4 — Aplicar o limite fundamental.**

$$3 \cdot \lim_{u \to 0} \frac{\operatorname{sen}(u)}{u} = 3 \cdot 1 = 3$$

$$\boxed{\lim_{x \to 0} \frac{\operatorname{sen}(3x)}{x} = 3}$$

---

> **Enunciado (parte B):** Determine se $\displaystyle\lim_{x \to 0} \dfrac{|x|}{x}$ existe.

**Passo 1 — Calcular o limite lateral esquerdo ($x \to 0^-$).**

Para $x < 0$: $|x| = -x$ (o módulo inverte o sinal de um número negativo).

Portanto, para $x < 0$:

$$\frac{|x|}{x} = \frac{-x}{x} = -1$$

Como a expressão é constante $-1$ para qualquer $x < 0$:

$$\lim_{x \to 0^-} \frac{|x|}{x} = -1$$

**Passo 2 — Calcular o limite lateral direito ($x \to 0^+$).**

Para $x > 0$: $|x| = x$.

Portanto, para $x > 0$:

$$\frac{|x|}{x} = \frac{x}{x} = 1$$

Como a expressão é constante $1$ para qualquer $x > 0$:

$$\lim_{x \to 0^+} \frac{|x|}{x} = 1$$

**Passo 3 — Comparar os limites laterais.**

$$\lim_{x \to 0^-} \frac{|x|}{x} = -1 \neq 1 = \lim_{x \to 0^+} \frac{|x|}{x}$$

Os limites laterais **são diferentes**. Pelo critério de existência:

$$\boxed{\lim_{x \to 0} \frac{|x|}{x} \text{ não existe}}$$

> **Interpretação geométrica:** o gráfico de $|x|/x$ é a função degrau: vale $-1$ para $x < 0$ e $+1$ para $x > 0$, com um "salto" em $x = 0$. Os limites laterais capturam exatamente esse salto.

**Gráfico — função degrau $|x|/x$:**

```
  y
  |
1 |          •──────────  ← lim⁺ = +1
  |
0 +──────────+─────────── x
  |          0
  |
-1|──────────○            ← lim⁻ = −1
  |
  lim⁻ ≠ lim⁺  →  limite bilateral NÃO existe em x = 0
```
_Cada lado converge para um valor diferente: o limite bilateral é impossível._

## Armadilhas & Edge Cases

- **O limite não depende de $f(p)$** — pode existir mesmo se $f(p)$ não está definido; confundir o valor do limite com o valor da função é o erro mais comum em limites
- **Substituição direta não é sempre válida** — só funciona quando $f$ é contínua em $p$ (polinômios sim, racionais com denominador $\neq 0$ sim; racionais com denominador $0$ exigem manipulação)
- **$0/0$ não significa "limite inexistente"** — é uma indeterminação que exige análise adicional; o limite pode existir, não existir, ou ser infinito
- **$\infty$ não é número** — "$\infty - \infty = 0$" é **errado**; $\infty - \infty$ é uma das formas indeterminadas e precisa ser tratada algebricamente
- **"Limite no infinito" ≠ "limite infinito"**: $\displaystyle\lim_{x \to \infty} f(x) = 3$ (assíntota horizontal) é radicalmente diferente de $\displaystyle\lim_{x \to 2} f(x) = \infty$ (assíntota vertical)
- **Cancelamento de $(x-p)$ exige $x \neq p$** — ao fatorar e cancelar, essa condição está implícita na definição de limite (vizinhança furada); o cancelamento é lícito
- **Limite fundamental: argumento e denominador devem ser iguais** — $\operatorname{sen}(3x)/x$ não é diretamente o limite fundamental; é preciso manipular para criar $\operatorname{sen}(3x)/(3x)$ antes de aplicar
- **Argumento em radianos** — o limite $\operatorname{sen} x / x = 1$ vale somente com $x$ em radianos; em graus, o limite seria $\pi/180 \neq 1$
- **Limite existir ≠ limite bilateral**: verificar sempre ambos os lados quando a função apresenta comportamento distinto à esquerda e à direita

## Conexões

- [[Matemática]] — MOC da área
- [[Graduação em Química]] — Roadmap da graduação
- [[Funções]] — pré-requisito: conceito de função, domínio; limite é propriedade do comportamento de funções
- [[Funções e Gráficos]] — pré-requisito: interpretação visual de assíntotas verticais (limite infinito) e horizontais (limite no infinito)
- [[Funções Trigonométricas]] — pré-requisito: $\operatorname{sen} x$, $\operatorname{cos} x$, $\operatorname{tg} x$ — usados no limite fundamental
- [[Trigonometria na Circunferência]] — base para a desigualdade geométrica usada na demonstração do limite fundamental
- [[Conjuntos Numéricos]] — vizinhança $0 < |x-p| < \delta$ é intervalo aberto; $\varepsilon$, $\delta$ pertencem a $\mathbb{R}^+$
- Continuidade (próximo tópico — aula 27/abr) — usa limites para definir quando $f$ é contínua em $p$
- [[Física]] — velocidade instantânea como $\displaystyle\lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t}$; taxa de reação como limite de razões de variação

## Fontes

- GUIDORIZZI, Hamilton Luiz. *Um Curso de Cálculo* — Vol. 1, Cap. 3: Limite e Continuidade (a partir da pg. 69). LTC.
