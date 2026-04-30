---
title: Smoke Test
draft: false
tags: [smoke-test]
---

# Smoke Test — Logos Archive

Esta nota valida os recursos essenciais do Quartz v4.

## KaTeX

Equação inline: $E = mc^2$

Equação em bloco:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

## Wikilink

Referência interna: [[index]]

## Código Python

```python
def fibonacci(n: int) -> list[int]:
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(10))
```
