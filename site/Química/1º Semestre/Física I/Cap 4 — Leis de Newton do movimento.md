---
title: Cap 4 — Leis de Newton do movimento
description: 'A dinâmica responde à pergunta que a cinemática ignora: por que um objeto
  acelera? As três Leis de Newton estabelecem a relação entre força e movimento —
  base d…'
tags:
- quimica
date: 2026-04-30
tipo: estudo
disciplina: fisica
semestre: 1
---
# Cap 4 — Leis de Newton do movimento

> A dinâmica responde à pergunta que a cinemática ignora: **por que** um objeto acelera? As três Leis de Newton estabelecem a relação entre **força** e **movimento** — base de toda a mecânica clássica.

---

## Definição

**Força** é uma interação entre dois objetos que pode alterar o estado de movimento de um deles. É uma grandeza **vetorial** (tem magnitude, direção e sentido).

**As três Leis de Newton** descrevem como forças produzem acelerações:

| Lei | Enunciado resumido |
| --- | ------------------ |
| 1ª Lei (inércia) | Sem força resultante → sem aceleração |
| 2ª Lei | $\vec{F}_{\text{res}} = m\vec{a}$ |
| 3ª Lei (ação e reação) | Forças surgem sempre aos pares, iguais e opostas |

---

## Teoria & Fundamentos

### 4.1 Força e interações

Forças sempre envolvem **dois objetos** interagindo. Podem ser:

- **De contato:** normal, atrito, tração, mola
- **À distância (de campo):** gravitacional, elétrica, magnética

O **diagrama do corpo livre (DCL)** representa apenas as forças que **agem sobre** o objeto de interesse, não as que ele exerce sobre outros.

```
DCL de uma caixa empurrada horizontalmente:

         N (normal)
         ↑
  f_at ←●→ F_aplicada
         ↓
         P (peso)

N: normal do piso sobre a caixa
P: peso (gravidade sobre a caixa)
F: força aplicada
f_at: atrito do piso sobre a caixa
```

### 4.2 Primeira Lei de Newton (Lei da Inércia)

> *"Um corpo em repouso permanece em repouso, e um corpo em movimento retilíneo uniforme continua em movimento retilíneo uniforme, a menos que uma força resultante não nula atue sobre ele."*

$$\vec{F}_{\text{res}} = \vec{0} \implies \vec{a} = \vec{0}$$

**Inércia** é a tendência de um corpo a resistir à mudança de seu estado de movimento. A **massa** é a medida quantitativa da inércia.

**Referencial inercial:** aquele em que a 1ª Lei é válida. Referenciais em aceleração (não inerciais) exigem forças fictícias — não são tratados aqui.

### 4.3 Segunda Lei de Newton

> *"A aceleração de um objeto é diretamente proporcional à força resultante sobre ele e inversamente proporcional à sua massa."*

$$\vec{F}_{\text{res}} = m\vec{a}$$

Em componentes:

$$\sum F_x = ma_x \qquad \sum F_y = ma_y \qquad \sum F_z = ma_z$$

**Unidade de força:** Newton (N)

$$1\ \text{N} = 1\ \text{kg} \cdot \text{m/s}^2$$

> A 2ª Lei relaciona a **soma vetorial** de todas as forças sobre o objeto à aceleração resultante. Uma força isolada só produz a aceleração descrita se for a **única** força, ou a **resultante** de todas as forças.

### 4.4 Massa e peso

**Massa** ($m$): medida de inércia — propriedade intrínseca do objeto. Escalar, em kg.

**Peso** ($\vec{P}$): força gravitacional sobre o objeto. Vetor.

$$\vec{P} = m\vec{g} \qquad P = mg$$

Com $g = 9{,}80\ \text{m/s}^2$ na superfície terrestre.

> Massa e peso são grandezas distintas. Em órbita, um astronauta tem **massa** (e portanto inércia), mas é **sem peso** (força gravitacional equilibrada pela queda livre orbital).

```
Massa vs. Peso:

  Terra:     m = 70 kg  →  P = 686 N
  Lua:       m = 70 kg  →  P = 114 N  (g_lua ≈ 1,62 m/s²)
  Órbita:    m = 70 kg  →  P ≈ 0 N   (imponderabilidade)

  A massa nunca muda; o peso depende de g local.
```

### 4.5 Terceira Lei de Newton (Ação e Reação)

> *"Se o objeto A exerce uma força sobre o objeto B, então B exerce sobre A uma força de mesma magnitude, mesma direção e sentido oposto."*

$$\vec{F}_{A \to B} = -\vec{F}_{B \to A}$$

**Ponto crítico:** o par ação-reação age sobre **objetos diferentes** — nunca se cancelam no DCL de um único objeto.

```
Exemplo — livro sobre a mesa:

  Livro → exerce peso P↓ sobre a mesa
  Mesa  → exerce normal N↑ sobre o livro   (par ação-reação com P)

  No DCL do livro:  N↑ e P↓  → se N = P, livro em equilíbrio
  Mas N e P NÃO são par ação-reação entre si
  (agem sobre o mesmo objeto — o livro)
```

### 4.6 Exemplos de diagramas do corpo livre

**Método sistemático:**

1. Identificar o objeto de interesse
2. Listar todas as forças que **agem sobre** ele (excluir forças que ele exerce)
3. Escolher sistema de coordenadas conveniente (geralmente $x$ na direção do movimento)
4. Escrever $\sum F_x = ma_x$ e $\sum F_y = ma_y$
5. Resolver o sistema de equações

**Forças comuns:**

| Força | Símbolo | Descrição |
| ----- | ------- | --------- |
| Peso | $\vec{P} = m\vec{g}$ | Para baixo, sempre |
| Normal | $\vec{N}$ | Perpendicular à superfície de contato |
| Tração | $\vec{T}$ | Ao longo do fio/cabo, afastando do objeto |
| Atrito | $\vec{f}$ | Paralelo à superfície, oposto ao movimento |
| Mola (Hooke) | $\vec{F} = -k\vec{x}$ | Proporcional ao estiramento |

---

## Fórmulas & Equações

| Fórmula | Descrição | Unidade |
| ------- | --------- | ------- |
| $\vec{F}_{\text{res}} = m\vec{a}$ | 2ª Lei de Newton | N |
| $\sum F_x = ma_x$ | Componente $x$ da 2ª Lei | N |
| $\sum F_y = ma_y$ | Componente $y$ da 2ª Lei | N |
| $P = mg$ | Magnitude do peso | N |
| $1\ \text{N} = 1\ \text{kg} \cdot \text{m/s}^2$ | Definição do Newton | — |
| $\vec{F}_{AB} = -\vec{F}_{BA}$ | 3ª Lei (ação-reação) | N |

---

## Exemplos Resolvidos

**Exemplo 1 — 2ª Lei: força resultante (básico)**

Uma caixa de $m = 5{,}00\ \text{kg}$ está sobre uma superfície sem atrito. Duas forças horizontais agem sobre ela: $F_1 = 12{,}0\ \text{N}$ para a direita e $F_2 = 7{,}00\ \text{N}$ para a esquerda. Qual a aceleração?

**Resolução:**

$$\sum F_x = F_1 - F_2 = 12{,}0 - 7{,}00 = 5{,}00\ \text{N}$$

$$a_x = \dfrac{\sum F_x}{m} = \dfrac{5{,}00}{5{,}00} = 1{,}00\ \text{m/s}^2 \text{ (para a direita)}$$

$$\boxed{a = 1{,}00\ \text{m/s}^2\ \text{para a direita}}$$

---

**Exemplo 2 — DCL em 2D: bloco em plano inclinado sem atrito (intermediário)**

Um bloco de $m = 8{,}00\ \text{kg}$ repousa sobre um plano inclinado sem atrito de $\theta = 30{,}0°$. Encontre a aceleração do bloco e a força normal.

**DCL e sistema de coordenadas:**

```
        N (perpendicular ao plano)
        ↑↗
   ────●──────
      /|\ θ
     / | \
    /  ↓  \
   /  mg    \
  /θ          \
 ──────────────
```

Eixo $x$: paralelo ao plano (positivo morro abaixo)  
Eixo $y$: perpendicular ao plano (positivo afastando do plano)

**Resolução:**

Componentes do peso:
$$P_x = mg\operatorname{sen}\theta = 8{,}00 \times 9{,}80 \times \operatorname{sen}(30°) = 78{,}4 \times 0{,}500 = 39{,}2\ \text{N}$$
$$P_y = mg\cos\theta = 78{,}4 \times \cos(30°) = 78{,}4 \times 0{,}866 = 67{,}9\ \text{N}$$

Eixo $y$ (sem aceleração perpendicular):
$$\sum F_y = N - P_y = 0 \implies N = 67{,}9\ \text{N}$$

Eixo $x$:
$$\sum F_x = P_x = ma_x \implies a_x = \dfrac{39{,}2}{8{,}00} = 4{,}90\ \text{m/s}^2$$

$$\boxed{a = 4{,}90\ \text{m/s}^2\ \text{(morro abaixo)};\quad N = 67{,}9\ \text{N}}$$

---

**Exemplo 3 — Sistema de dois blocos com polia (avançado)**

Dois blocos estão conectados por um fio ideal (massa e atrito desprezíveis) passando por uma polia ideal: bloco $A$ ($m_A = 4{,}00\ \text{kg}$) sobre uma mesa horizontal sem atrito; bloco $B$ ($m_B = 3{,}00\ \text{kg}$) pendurado verticalmente. Encontre a aceleração do sistema e a tensão no fio.

**DCL do sistema:**

```
  [A] →T          T↑
  mesa (sem atrito)   |
                      [B]
                      ↓ m_B·g
```

**Resolução:**

Para o bloco $A$ (movimento horizontal):
$$T = m_A\,a \quad \text{...(i)}$$

Para o bloco $B$ (movimento vertical, positivo para baixo):
$$m_B\,g - T = m_B\,a \quad \text{...(ii)}$$

Somando (i) e (ii):
$$m_B\,g = (m_A + m_B)\,a$$
$$a = \dfrac{m_B\,g}{m_A + m_B} = \dfrac{3{,}00 \times 9{,}80}{4{,}00 + 3{,}00} = \dfrac{29{,}4}{7{,}00} = 4{,}20\ \text{m/s}^2$$

Substituindo em (i):
$$T = 4{,}00 \times 4{,}20 = 16{,}8\ \text{N}$$

$$\boxed{a = 4{,}20\ \text{m/s}^2;\quad T = 16{,}8\ \text{N}}$$

---

## Armadilhas & Edge Cases

- **Par ação-reação ≠ equilíbrio:** $N$ (mesa sobre o livro) e $P$ (peso do livro) são iguais e opostos num livro em repouso, mas **não são par ação-reação** — agem sobre o mesmo corpo. O par de $N$ é a força do livro sobre a mesa; o par de $P$ é a força do livro sobre a Terra.
- **Fio ideal:** tensão igual em todos os pontos apenas quando o fio é inextensível e de massa desprezível. Se a polia tem massa, o problema muda (ver Cap 10 — Torque).
- **Superfície sem atrito ≠ sem normal:** a normal existe sempre que há contato — o atrito que pode ser zero.
- **Componentes do peso no plano inclinado:** $P_\parallel = mg\operatorname{sen}\theta$ (ao longo do plano) e $P_\perp = mg\cos\theta$ (perpendicular ao plano). Confundir $\operatorname{sen}$ e $\cos$ é o erro mais comum.
- **Massa em kg, força em N:** nunca substitua peso (N) diretamente no lugar de massa (kg) na 2ª Lei.

---

## Conexões

- [[Cap 3 — Movimento em duas ou três dimensões]] ← cinemática que fornece $\vec{a}$
- [[Cap 5 — Aplicações das Leis de Newton]] → atrito, dinâmica circular, casos complexos
- [[Cap 6 — Trabalho e energia cinética]] → energia como alternativa à 2ª Lei
- [[Física I]] ← MOC da disciplina
- [[Física]] ← MOC de área

---

## Fontes

- YOUNG, Hugh D.; FREEDMAN, Roger A. **Física I: Mecânica**. 12. ed. São Paulo: Pearson Addison Wesley, 2008. Cap. 4, p. 106–132.
