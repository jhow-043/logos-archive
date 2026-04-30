# Logos Archive

[![Build & Deploy](https://github.com/jhow-043/logos-archive/actions/workflows/deploy.yml/badge.svg)](https://github.com/jhow-043/logos-archive/actions/workflows/deploy.yml)

> Vault Obsidian publicado como site estático via [Quartz v4](https://quartz.jzhao.xyz/).

**Site**: https://jhow-043.github.io/logos-archive/

---

## Estrutura do Repositório

```
logos-archive-v1/
├── site/          # Vault Obsidian (abrir esta pasta no Obsidian)
├── quartz/        # Build engine Quartz v4
├── tools/         # Scripts Python de sync e validação
├── docs/          # Documentação do projeto (ADRs, partes, runbooks)
└── .github/       # Workflows CI/CD e skills Copilot
```

## Como usar

### Editar conteúdo

Abra `site/` como vault no Obsidian e edite normalmente.

### Sincronizar e publicar

```bash
make sync      # Sincroniza vault original → site/
make build     # Sync + build estático
make serve     # Servidor local com hot-reload (localhost:8080)
make publish   # Sync + commit + push (dispara deploy no GitHub Pages)
```

### Comandos disponíveis

```bash
make help
```

---

## Pré-requisitos

- [Node.js](https://nodejs.org/) ≥ 18
- [Python](https://python.org/) ≥ 3.10
- [Obsidian](https://obsidian.md/) (para editar o vault)
