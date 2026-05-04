# Logos Archive — Documentação

Referência técnica do projeto. Leia antes de editar qualquer arquivo de infraestrutura.

---

## O que é este projeto

**Logos Archive** é um site estático gerado a partir de um vault Obsidian privado
chamado **O Grafo de Alexandria**. Os dois repositórios são separados intencionalmente:

| Repositório | Visibilidade | Propósito |
|---|---|---|
| `O Grafo de Alexandria` | Privado (local) | Vault de estudo com todo o conteúdo |
| `logos-archive` | Público (GitHub) | Subconjunto publicado do vault |

O conteúdo nunca é editado diretamente em `logos-archive/site/`. Toda edição
acontece no Grafo; o sync extrai e transforma para o logos.

---

## Stack

| Camada | Tecnologia |
|---|---|
| Editor | Obsidian |
| Build engine | Quartz v4 |
| Sync vault → site | Python 3.10+ (`tools/sync_from_source.py`) |
| CI/CD | GitHub Actions |
| Hospedagem | GitHub Pages |

---

## Estrutura do repositório

```
logos-archive/
├── site/           ← Conteúdo publicado (gerado pelo sync — não editar manualmente)
├── quartz/         ← Engine de build Quartz v4
├── tools/          ← Scripts Python de sync e validação
│   ├── sync_from_source.py   ← Script principal de sync
│   ├── _audit.py
│   ├── _fix_encoding.py
│   └── _process_banners.py
├── docs/           ← Esta pasta — documentação do projeto
│   ├── index.md    ← Este arquivo
│   ├── sync.md     ← Detalhes do pipeline de sync
│   └── patterns.md ← Padrões de MOC e notas
├── Makefile        ← Comandos de uso
└── .github/        ← Workflows CI/CD
```

---

## Comandos rápidos

```bash
make sync       # Sincroniza vault → site/ (não faz build)
make sync-dry   # Simula o sync sem gravar arquivos
make build      # sync + build estático do Quartz
make serve      # Serve o site localmente em localhost:8080 (hot-reload)
make publish    # sync + git commit + git push → dispara deploy automático
make audit      # Valida links internos (encontra wikilinks sem destino)
```

---

## Documentação

| Arquivo | Conteúdo |
|---|---|
| [sync.md](sync.md) | Como o sync funciona: regras de inclusão, transformações de frontmatter, remoção de seções vault-only |
| [patterns.md](patterns.md) | Padrões de MOC e nota: estrutura esperada no vault e no site |
