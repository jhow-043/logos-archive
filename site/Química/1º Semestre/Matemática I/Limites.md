---
title: Limites
description: O limite formaliza a ideia de "tendÃªncia" â€” o valor para o qual uma
  funÃ§Ã£o se aproxima quando a variÃ¡vel independente se aproxima de um ponto, independent…
tags:
- quimica
date: 2026-04-24
tipo: estudo
disciplina: matematica
semestre: 1
---
# Limites

> O limite formaliza a ideia de "tendÃªncia" â€” o valor para o qual uma funÃ§Ã£o se aproxima quando a variÃ¡vel independente se aproxima de um ponto, independentemente do valor da funÃ§Ã£o nesse ponto. Ã‰ o alicerce rigoroso do CÃ¡lculo.

---

## DefiniÃ§Ã£o

### NoÃ§Ã£o intuitiva

Diz-se que $L$ Ã© o **limite** de $f(x)$ quando $x$ tende a $p$, e escreve-se:

$$\lim_{x \to p} f(x) = L$$

quando $f(x)$ fica arbitrariamente prÃ³ximo de $L$ sempre que $x$ estiver suficientemente prÃ³ximo de $p$ â€” **sem que $x$ precise assumir o valor $p$**.

> O que importa Ã© o **comportamento de $f$ na vizinhanÃ§a de $p$**, nÃ£o o valor $f(p)$ (que pode atÃ© nÃ£o existir).

**GrÃ¡fico â€” noÃ§Ã£o intuitiva de limite:**

```
  y
  |
  |          . â† f(x) se aproxima de L
  |       .
L |......â—‹.............  â† L  (limite)
  |       .  â†‘
  |          f(p): pode ser diferente de L, ou nÃ£o existir
  |
  +----------+â”€â”€â”€â”€â”€â”€â”€â”€â”€ x
             p
```
_O comportamento de $f$ ao **redor** de $p$ determina o limite â€” o valor (ou existÃªncia) de $f(p)$ Ã© irrelevante._

### DefiniÃ§Ã£o formal (DefiniÃ§Ã£o $\varepsilon$-$\delta$)

(Guidorizzi Vol.1, pg. 69)

$$\lim_{x \to p} f(x) = L \;\iff\; \forall\, \varepsilon > 0,\; \exists\, \delta > 0 \;\text{ tal que }\; 0 < |x - p| < \delta \;\implies\; |f(x) - L| < \varepsilon$$

**InterpretaÃ§Ã£o geomÃ©trica:**

- $|f(x) - L| < \varepsilon$: o valor $f(x)$ estÃ¡ dentro da **faixa horizontal** $(L - \varepsilon,\, L + \varepsilon)$
- $0 < |x - p| < \delta$: o ponto $x$ estÃ¡ dentro da **vizinhanÃ§a furada** $(p - \delta,\, p + \delta) \setminus \{p\}$
- A definiÃ§Ã£o diz: qualquer que seja a precisÃ£o $\varepsilon$ exigida em $y$, sempre existe um "raio" $\delta$ em $x$ que garante essa precisÃ£o.

> O sÃ­mbolo $0 < |x - p|$ ("vizinhanÃ§a furada") formaliza que $x \neq p$: o limite descreve o que acontece **ao redor de** $p$, nÃ£o **em** $p$.

**GrÃ¡fico â€” interpretaÃ§Ã£o da definiÃ§Ã£o $\varepsilon$-$\delta$:**

```
  y
  |
L+Îµ  - - - - - - - - - - -  â† faixa Îµ (superior)
  |           /\
  L  â”€â”€â”€â”€â”€â”€â”€â”€/  \â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€  â† valor do limite L
  |         /    \
L-Îµ  - - - - - - - - - - -  â† faixa Îµ (inferior)
  |          â†‘  â†‘  â†‘
  +â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€+â”€â”€+â”€â”€+â”€â”€â”€â”€â”€â”€â”€â”€ x
            p-Î´  p  p+Î´
                 â†‘
           (excluÃ­do: x â‰  p)
```
_Para qualquer "precisÃ£o" $\varepsilon$ exigida em $y$, existe um raio $\delta$ em $x$ tal que todo $x$ na vizinhanÃ§a furada de $p$ produz $f(x)$ dentro da faixa $\varepsilon$ ao redor de $L$._

## Teoria & Fundamentos

### Unicidade do limite

> **Teorema:** Se $\displaystyle\lim_{x \to p} f(x) = L$ e $\displaystyle\lim_{x \to p} f(x) = M$, entÃ£o $L = M$.

O limite, quando existe, Ã© Ãºnico. (DemonstraÃ§Ã£o por absurdo usando a definiÃ§Ã£o $\varepsilon$-$\delta$.)

### Limites laterais

**Limite lateral esquerdo** (para $x$ vindo de valores menores que $p$):

$$\lim_{x \to p^-} f(x) = L^- \;\iff\; \forall\, \varepsilon > 0,\; \exists\, \delta > 0 \;\text{ tal que }\; p - \delta < x < p \;\implies\; |f(x) - L^-| < \varepsilon$$

**Limite lateral direito** (para $x$ vindo de valores maiores que $p$):

$$\lim_{x \to p^+} f(x) = L^+ \;\iff\; \forall\, \varepsilon > 0,\; \exists\, \delta > 0 \;\text{ tal que }\; p < x < p + \delta \;\implies\; |f(x) - L^+| < \varepsilon$$

**CritÃ©rio de existÃªncia:**

$$\lim_{x \to p} f(x) = L \;\iff\; \lim_{x \to p^-} f(x) = \lim_{x \to p^+} f(x) = L$$

O limite bilateral existe **se e somente se** os dois limites laterais existem e sÃ£o iguais.

**GrÃ¡fico â€” limites laterais distintos (limite bilateral nÃ£o existe):**

```
  y
  |
1 |          â€¢â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€  â† limâº = +1  (â€¢ = ponto incluÃ­do)
  |
0 +â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€+â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ x
  |          0
  |
-1|â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â—‹            â† limâ» = âˆ’1  (â—‹ = ponto excluÃ­do)
  |
  limâ» = âˆ’1  â‰   +1 = limâº   â†’   limite bilateral NÃƒO existe
```
_Como os laterais convergem para valores diferentes, o limite de $|x|/x$ em $x = 0$ nÃ£o existe. O grÃ¡fico exibe um "salto"._

### Propriedades operatÃ³rias dos limites

Sejam $\displaystyle\lim_{x \to p} f(x) = L$ e $\displaystyle\lim_{x \to p} g(x) = M$. EntÃ£o:

| Propriedade | FÃ³rmula |
| ----------- | ------- |
| Soma | $\displaystyle\lim_{x \to p}[f(x) + g(x)] = L + M$ |
| DiferenÃ§a | $\displaystyle\lim_{x \to p}[f(x) - g(x)] = L - M$ |
| MÃºltiplo por constante | $\displaystyle\lim_{x \to p}[k \cdot f(x)] = k \cdot L$ |
| Produto | $\displaystyle\lim_{x \to p}[f(x) \cdot g(x)] = L \cdot M$ |
| Quociente | $\displaystyle\lim_{x \to p}\frac{f(x)}{g(x)} = \frac{L}{M}$, desde que $M \neq 0$ |
| PotÃªncia | $\displaystyle\lim_{x \to p}[f(x)]^n = L^n$, $n \in \mathbb{N}$ |
| Raiz | $\displaystyle\lim_{x \to p}\sqrt[n]{f(x)} = \sqrt[n]{L}$, desde que $L > 0$ (se $n$ par) |

> **CorolÃ¡rio â€” substituiÃ§Ã£o direta:** Todo polinÃ´mio $p(x)$ satisfaz $\displaystyle\lim_{x \to p} p(x) = p(p)$. Para funÃ§Ãµes racionais $f(x) = p(x)/q(x)$, vale $\displaystyle\lim_{x \to a} f(x) = f(a)$ desde que $q(a) \neq 0$.

### Teorema do Confronto (SanduÃ­che)

> **Teorema:** Se $g(x) \leq f(x) \leq h(x)$ em uma vizinhanÃ§a de $p$ (exceto possivelmente em $p$), e $\displaystyle\lim_{x \to p} g(x) = \lim_{x \to p} h(x) = L$, entÃ£o $\displaystyle\lim_{x \to p} f(x) = L$.

**InterpretaÃ§Ã£o:** $f$ fica "espremida" entre $g$ e $h$; se $g$ e $h$ convergem para o mesmo valor, $f$ Ã© forÃ§ada a convergir tambÃ©m.

**AplicaÃ§Ã£o principal:** demonstrar o limite fundamental trigonomÃ©trico.

**GrÃ¡fico â€” Teorema do Confronto:**

```
  y
  |         h(x)
  |        /â€¾â€¾â€¾\            â† cota superior
  |       / f(x)\
  L â”€â”€â”€â”€â”€*â”€â”€â”€â”€â”€â”€â”€*â”€â”€â”€â”€â”€â”€â”€â”€  â† g, f e h â†’ L quando x â†’ p
  |       \ g(x)/
  |        \___/            â† cota inferior
  |
  +â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€+â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ x
             p
```
_$g(x) \leq f(x) \leq h(x)$ e $\lim g = \lim h = L$ $\implies$ $\lim f = L$ â€” $f$ Ã© "espremida" e obrigada a convergir._

### Limite fundamental trigonomÃ©trico

$$\lim_{x \to 0} \frac{\operatorname{sen} x}{x} = 1 \qquad (x \text{ em radianos})$$

**EsboÃ§o da demonstraÃ§Ã£o via SanduÃ­che:**

Para $0 < x < \pi/2$, vale a desigualdade geomÃ©trica (comparando Ã¡reas de triÃ¢ngulos e setor circular):

$$\operatorname{cos} x < \frac{\operatorname{sen} x}{x} < 1$$

Tomando $\lim_{x \to 0^+}$: $\displaystyle\lim_{x \to 0^+} \operatorname{cos} x = 1$ e o limite da cota superior tambÃ©m Ã© $1$. Pelo SanduÃ­che:

$$\lim_{x \to 0^+} \frac{\operatorname{sen} x}{x} = 1$$

Como $\operatorname{sen} x / x$ Ã© **par** (ambos sÃ£o funÃ§Ãµes Ã­mpares, entÃ£o o quociente Ã© par), o limite lateral esquerdo tambÃ©m Ã© $1$. Logo o limite bilateral existe e vale $1$.

> **ConsequÃªncia imediata:** $\displaystyle\lim_{x \to 0} \frac{1 - \operatorname{cos} x}{x} = 0$

**GrÃ¡fico â€” $f(x) = \dfrac{\operatorname{sen} x}{x}$:**

```
  y
  |
1 |........â—‹.............  â† limite = 1  (â—‹: indefinido em x=0)
  |       /|\ 
  |      / | \                    Â·
  |     /  |  \               Â·
  |    /   |   Â·         Â·
  |___/    |    Â·    Â·
  +â”€â”€â”€â”€â”€â”€â”€ +â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ x
          0
```
_A curva se aproxima de $1$ pelos dois lados de $x = 0$. O Teorema do Confronto ($\operatorname{cos} x < \operatorname{sen} x / x < 1$) confirma que o limite vale exatamente $1$._

### IndeterminaÃ§Ãµes

Quando substituiÃ§Ã£o direta produz uma das formas abaixo, o resultado Ã© **indeterminado** â€” Ã© necessÃ¡rio manipulaÃ§Ã£o algÃ©brica antes de concluir:

| Forma indeterminada | EstratÃ©gias tÃ­picas de resoluÃ§Ã£o |
| ------------------- | -------------------------------- |
| $\dfrac{0}{0}$ | FatoraÃ§Ã£o, racionalizaÃ§Ã£o (multiplicar pelo conjugado), simplificaÃ§Ã£o |
| $\dfrac{\infty}{\infty}$ | Dividir pelo maior grau (polinÃ´mios), identificar o termo dominante |
| $0 \cdot \infty$ | Reescrever como $\dfrac{0}{1/\infty}$ ou $\dfrac{\infty}{1/0}$ |
| $\infty - \infty$ | FatoraÃ§Ã£o, denominador comum, conjugado |
| $0^0$, $\infty^0$, $1^\infty$ | Reescrever com exponencial e logaritmo (ver mÃ³dulo Derivadas â€” L'HÃ´pital) |

> IndeterminaÃ§Ã£o **nÃ£o significa que o limite nÃ£o existe** â€” significa apenas que Ã© necessÃ¡rio continuar trabalhando.

### Limites infinitos e no infinito

**Limite infinito** ($f(x)$ cresce sem cota quando $x \to p$):

$$\lim_{x \to p} f(x) = +\infty \;\iff\; \forall M > 0,\; \exists\, \delta > 0 \;\text{ tal que }\; 0 < |x-p| < \delta \implies f(x) > M$$

â†’ A reta $x = p$ Ã© **assÃ­ntota vertical** do grÃ¡fico de $f$.

**Limite no infinito** ($x$ cresce sem cota, $f(x)$ tende a $L$):

$$\lim_{x \to +\infty} f(x) = L \;\iff\; \forall\, \varepsilon > 0,\; \exists\, N > 0 \;\text{ tal que }\; x > N \implies |f(x) - L| < \varepsilon$$

â†’ A reta $y = L$ Ã© **assÃ­ntota horizontal** do grÃ¡fico de $f$.

| Tipo | NotaÃ§Ã£o | DescriÃ§Ã£o |
| ---- | ------- | --------- |
| Limite infinito | $\displaystyle\lim_{x \to p} f(x) = \pm\infty$ | $f$ diverge ao redor de $p$ â†’ assÃ­ntota vertical |
| Limite no infinito | $\displaystyle\lim_{x \to \pm\infty} f(x) = L$ | $f$ estabiliza quando $x$ cresce â†’ assÃ­ntota horizontal |

**GrÃ¡ficos â€” assÃ­ntota vertical vs. assÃ­ntota horizontal:**

```
AssÃ­ntota vertical: lim_{xâ†’p} f(x) = +âˆž

  y
  |  â†‘    |  â†‘
  | /     | /
  |/      |/
  +â”€â”€â”€â”€â”€â”€â”€+â”€â”€â”€â”€â”€â”€â”€â”€ x
          p
  â† f cresce sem cota ao se aproximar de x = p (reta vertical x = p)


AssÃ­ntota horizontal: lim_{xâ†’+âˆž} f(x) = L

  y
  |
L |. . . . .__________  â† f(x) â†’ L  (reta horizontal y = L)
  |         /
  |        /
  |_______/
  +â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ x
                â†’ +âˆž
```

> **DistinÃ§Ã£o fundamental:** "limite **no** infinito" ($x \to \infty$) vs. "limite **infinito**" ($f \to \infty$) â€” sÃ£o situaÃ§Ãµes diferentes e frequentemente confundidas.

### Limite de funÃ§Ã£o composta

> **Teorema:** Se $\displaystyle\lim_{x \to p} g(x) = q$ e $\displaystyle\lim_{y \to q} f(y) = L$, e $f$ Ã© contÃ­nua em $q$ (ou $g(x) \neq q$ numa vizinhanÃ§a furada de $p$), entÃ£o:
>
> $$\lim_{x \to p} f(g(x)) = f\!\left(\lim_{x \to p} g(x)\right) = f(q) = L$$

## FÃ³rmulas & EquaÃ§Ãµes

### DefiniÃ§Ã£o $\varepsilon$-$\delta$

$$\lim_{x \to p} f(x) = L \;\iff\; \forall\, \varepsilon > 0,\; \exists\, \delta > 0 :\; 0 < |x - p| < \delta \implies |f(x) - L| < \varepsilon$$

### CritÃ©rio dos limites laterais

$$\lim_{x \to p} f(x) \text{ existe} \;\iff\; \lim_{x \to p^-} f(x) = \lim_{x \to p^+} f(x)$$

### Limites notÃ¡veis

$$\lim_{x \to 0} \frac{\operatorname{sen} x}{x} = 1 \qquad \lim_{x \to 0} \frac{1 - \operatorname{cos} x}{x} = 0 \qquad \lim_{x \to 0} \frac{\operatorname{tg} x}{x} = 1$$

### Limite de polinÃ´mio / racional por substituiÃ§Ã£o direta

$$\lim_{x \to a} p(x) = p(a) \qquad \lim_{x \to a} \frac{p(x)}{q(x)} = \frac{p(a)}{q(a)}, \; q(a) \neq 0$$

## Exemplos Resolvidos

**Exemplo 1 â€” BÃ¡sico: substituiÃ§Ã£o direta em polinÃ´mio**

> **Enunciado:** Calcule $\displaystyle\lim_{x \to 2}(x^2 - 3x + 5)$.

**Passo 1 â€” Identificar o tipo de funÃ§Ã£o.**

$f(x) = x^2 - 3x + 5$ Ã© um **polinÃ´mio**. PolinÃ´mios sÃ£o contÃ­nuos em todo $\mathbb{R}$, logo as propriedades operatÃ³rias dos limites garantem que o limite pode ser calculado por substituiÃ§Ã£o direta.

**Passo 2 â€” Tentar substituiÃ§Ã£o direta.**

Substituir $x = 2$ na expressÃ£o:

$$\lim_{x \to 2}(x^2 - 3x + 5) = (2)^2 - 3 \cdot (2) + 5$$

**Passo 3 â€” Calcular cada parcela.**

$(2)^2 = 4$

$3 \cdot (2) = 6$

Portanto:

$$4 - 6 + 5 = 3$$

**Passo 4 â€” Verificar a resposta.**

O resultado Ã© $3$: o limite existe, Ã© finito, e foi obtido por substituiÃ§Ã£o direta (vÃ¡lida pois o denominador â€” inexistente neste caso â€” nÃ£o cria problemas).

$$\boxed{\lim_{x \to 2}(x^2 - 3x + 5) = 3}$$

---

**Exemplo 2 â€” IntermediÃ¡rio: indeterminaÃ§Ã£o $0/0$ por fatoraÃ§Ã£o**

> **Enunciado:** Calcule $\displaystyle\lim_{x \to 3} \dfrac{x^2 - 9}{x - 3}$.

**Passo 1 â€” Tentar substituiÃ§Ã£o direta.**

Substituir $x = 3$:

$$\frac{(3)^2 - 9}{3 - 3} = \frac{9 - 9}{0} = \frac{0}{0}$$

Forma indeterminada $\dfrac{0}{0}$. **NÃ£o Ã© possÃ­vel concluir diretamente** â€” Ã© necessÃ¡rio manipulaÃ§Ã£o algÃ©brica.

**Passo 2 â€” Reconhecer a estrutura do numerador.**

$x^2 - 9$ Ã© **diferenÃ§a de quadrados**: $x^2 - 9 = x^2 - 3^2$.

Aplicar a identidade $a^2 - b^2 = (a-b)(a+b)$:

$$x^2 - 9 = (x - 3)(x + 3)$$

**Passo 3 â€” Reescrever a fraÃ§Ã£o com o numerador fatorado.**

$$\frac{x^2 - 9}{x - 3} = \frac{(x-3)(x+3)}{x-3}$$

**Passo 4 â€” Simplificar o fator comum.**

Como estamos calculando o limite com $x \to 3$ e **$x \neq 3$**, o fator $(x - 3)$ nunca Ã© zero durante o processo de aproximaÃ§Ã£o. Logo Ã© lÃ­cito cancelar:

$$\frac{(x-3)(x+3)}{x-3} = x + 3, \quad \text{para } x \neq 3$$

**Passo 5 â€” Calcular o limite da expressÃ£o simplificada.**

A funÃ§Ã£o $x + 3$ Ã© um polinÃ´mio, e o limite pode ser calculado por substituiÃ§Ã£o direta:

$$\lim_{x \to 3}(x + 3) = 3 + 3 = 6$$

**Passo 6 â€” Confirmar o resultado.**

Como $\dfrac{x^2 - 9}{x-3} = x+3$ para todo $x \neq 3$, e o limite sÃ³ examina o que acontece **prÃ³ximo de** (nÃ£o em) $x = 3$:

$$\boxed{\lim_{x \to 3} \frac{x^2 - 9}{x - 3} = 6}$$

> **ObservaÃ§Ã£o:** A funÃ§Ã£o original nÃ£o estÃ¡ definida em $x = 3$ (denominador zero), mas o limite existe e vale $6$. Isso Ã© um exemplo de descontinuidade removÃ­vel â€” serÃ¡ formalizado na nota de Continuidade.

**GrÃ¡fico â€” "buraco" em $x = 3$:**

```
  y
  |
6 |..........â—‹  â† buraco: f(3) indefinido, mas lim_{xâ†’3} = 6
  |         /
  |        /     f(x) = x + 3  para x â‰  3
  |       /
  |      /
  +â”€â”€â”€â”€â”€â”€+â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ x
         3
```
_O grÃ¡fico Ã© a reta $y = x + 3$ com um Ãºnico ponto removido em $(3,\,6)$. O limite "enxerga" a reta â€” nÃ£o o buraco._

---

**Exemplo 3 â€” AvanÃ§ado: limite fundamental trigonomÃ©trico + limites laterais**

> **Enunciado (parte A):** Calcule $\displaystyle\lim_{x \to 0} \dfrac{\operatorname{sen}(3x)}{x}$.

**Passo 1 â€” Tentar substituiÃ§Ã£o direta.**

Substituir $x = 0$:

$$\frac{\operatorname{sen}(3 \cdot 0)}{0} = \frac{\operatorname{sen}(0)}{0} = \frac{0}{0}$$

IndeterminaÃ§Ã£o $\dfrac{0}{0}$. A estratÃ©gia aqui Ã© usar o **limite fundamental** $\displaystyle\lim_{u \to 0} \dfrac{\operatorname{sen} u}{u} = 1$, mas o argumento e o denominador precisam ser **idÃªnticos**.

**Passo 2 â€” Manipular para criar a forma $\operatorname{sen}(u)/u$.**

O argumento do seno Ã© $3x$; o denominador Ã© $x$. Multiplicar e dividir por $3$:

$$\frac{\operatorname{sen}(3x)}{x} = \frac{\operatorname{sen}(3x)}{x} \cdot \frac{3}{3} = 3 \cdot \frac{\operatorname{sen}(3x)}{3x}$$

**Passo 3 â€” Fazer a substituiÃ§Ã£o $u = 3x$.**

Quando $x \to 0$, temos $u = 3x \to 0$. Portanto:

$$\lim_{x \to 0} 3 \cdot \frac{\operatorname{sen}(3x)}{3x} = 3 \cdot \lim_{u \to 0} \frac{\operatorname{sen}(u)}{u}$$

**Passo 4 â€” Aplicar o limite fundamental.**

$$3 \cdot \lim_{u \to 0} \frac{\operatorname{sen}(u)}{u} = 3 \cdot 1 = 3$$

$$\boxed{\lim_{x \to 0} \frac{\operatorname{sen}(3x)}{x} = 3}$$

---

> **Enunciado (parte B):** Determine se $\displaystyle\lim_{x \to 0} \dfrac{|x|}{x}$ existe.

**Passo 1 â€” Calcular o limite lateral esquerdo ($x \to 0^-$).**

Para $x < 0$: $|x| = -x$ (o mÃ³dulo inverte o sinal de um nÃºmero negativo).

Portanto, para $x < 0$:

$$\frac{|x|}{x} = \frac{-x}{x} = -1$$

Como a expressÃ£o Ã© constante $-1$ para qualquer $x < 0$:

$$\lim_{x \to 0^-} \frac{|x|}{x} = -1$$

**Passo 2 â€” Calcular o limite lateral direito ($x \to 0^+$).**

Para $x > 0$: $|x| = x$.

Portanto, para $x > 0$:

$$\frac{|x|}{x} = \frac{x}{x} = 1$$

Como a expressÃ£o Ã© constante $1$ para qualquer $x > 0$:

$$\lim_{x \to 0^+} \frac{|x|}{x} = 1$$

**Passo 3 â€” Comparar os limites laterais.**

$$\lim_{x \to 0^-} \frac{|x|}{x} = -1 \neq 1 = \lim_{x \to 0^+} \frac{|x|}{x}$$

Os limites laterais **sÃ£o diferentes**. Pelo critÃ©rio de existÃªncia:

$$\boxed{\lim_{x \to 0} \frac{|x|}{x} \text{ nÃ£o existe}}$$

> **InterpretaÃ§Ã£o geomÃ©trica:** o grÃ¡fico de $|x|/x$ Ã© a funÃ§Ã£o degrau: vale $-1$ para $x < 0$ e $+1$ para $x > 0$, com um "salto" em $x = 0$. Os limites laterais capturam exatamente esse salto.

**GrÃ¡fico â€” funÃ§Ã£o degrau $|x|/x$:**

```
  y
  |
1 |          â€¢â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€  â† limâº = +1
  |
0 +â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€+â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ x
  |          0
  |
-1|â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â—‹            â† limâ» = âˆ’1
  |
  limâ» â‰  limâº  â†’  limite bilateral NÃƒO existe em x = 0
```
_Cada lado converge para um valor diferente: o limite bilateral Ã© impossÃ­vel._

## Armadilhas & Edge Cases

- **O limite nÃ£o depende de $f(p)$** â€” pode existir mesmo se $f(p)$ nÃ£o estÃ¡ definido; confundir o valor do limite com o valor da funÃ§Ã£o Ã© o erro mais comum em limites
- **SubstituiÃ§Ã£o direta nÃ£o Ã© sempre vÃ¡lida** â€” sÃ³ funciona quando $f$ Ã© contÃ­nua em $p$ (polinÃ´mios sim, racionais com denominador $\neq 0$ sim; racionais com denominador $0$ exigem manipulaÃ§Ã£o)
- **$0/0$ nÃ£o significa "limite inexistente"** â€” Ã© uma indeterminaÃ§Ã£o que exige anÃ¡lise adicional; o limite pode existir, nÃ£o existir, ou ser infinito
- **$\infty$ nÃ£o Ã© nÃºmero** â€” "$\infty - \infty = 0$" Ã© **errado**; $\infty - \infty$ Ã© uma das formas indeterminadas e precisa ser tratada algebricamente
- **"Limite no infinito" â‰  "limite infinito"**: $\displaystyle\lim_{x \to \infty} f(x) = 3$ (assÃ­ntota horizontal) Ã© radicalmente diferente de $\displaystyle\lim_{x \to 2} f(x) = \infty$ (assÃ­ntota vertical)
- **Cancelamento de $(x-p)$ exige $x \neq p$** â€” ao fatorar e cancelar, essa condiÃ§Ã£o estÃ¡ implÃ­cita na definiÃ§Ã£o de limite (vizinhanÃ§a furada); o cancelamento Ã© lÃ­cito
- **Limite fundamental: argumento e denominador devem ser iguais** â€” $\operatorname{sen}(3x)/x$ nÃ£o Ã© diretamente o limite fundamental; Ã© preciso manipular para criar $\operatorname{sen}(3x)/(3x)$ antes de aplicar
- **Argumento em radianos** â€” o limite $\operatorname{sen} x / x = 1$ vale somente com $x$ em radianos; em graus, o limite seria $\pi/180 \neq 1$
- **Limite existir â‰  limite bilateral**: verificar sempre ambos os lados quando a funÃ§Ã£o apresenta comportamento distinto Ã  esquerda e Ã  direita

## ConexÃµes

- [[MatemÃ¡tica]] â€” MOC da Ã¡rea
- [[GraduaÃ§Ã£o em QuÃ­mica]] â€” Roadmap da graduaÃ§Ã£o
- [[FunÃ§Ãµes]] â€” prÃ©-requisito: conceito de funÃ§Ã£o, domÃ­nio; limite Ã© propriedade do comportamento de funÃ§Ãµes
- [[FunÃ§Ãµes e GrÃ¡ficos]] â€” prÃ©-requisito: interpretaÃ§Ã£o visual de assÃ­ntotas verticais (limite infinito) e horizontais (limite no infinito)
- [[FunÃ§Ãµes TrigonomÃ©tricas]] â€” prÃ©-requisito: $\operatorname{sen} x$, $\operatorname{cos} x$, $\operatorname{tg} x$ â€” usados no limite fundamental
- [[Trigonometria na CircunferÃªncia]] â€” base para a desigualdade geomÃ©trica usada na demonstraÃ§Ã£o do limite fundamental
- [[Conjuntos NumÃ©ricos]] â€” vizinhanÃ§a $0 < |x-p| < \delta$ Ã© intervalo aberto; $\varepsilon$, $\delta$ pertencem a $\mathbb{R}^+$
- Continuidade (prÃ³ximo tÃ³pico â€” aula 27/abr) â€” usa limites para definir quando $f$ Ã© contÃ­nua em $p$
- [[FÃ­sica]] â€” velocidade instantÃ¢nea como $\displaystyle\lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t}$; taxa de reaÃ§Ã£o como limite de razÃµes de variaÃ§Ã£o

## Fontes

- GUIDORIZZI, Hamilton Luiz. *Um Curso de CÃ¡lculo* â€” Vol. 1, Cap. 3: Limite e Continuidade (a partir da pg. 69). LTC.
