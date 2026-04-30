# Logos Archive

[![Build & Deploy](https://github.com/jhow-043/logos-archive/actions/workflows/deploy.yml/badge.svg)](https://github.com/jhow-043/logos-archive/actions/workflows/deploy.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Built with Quartz](https://img.shields.io/badge/Built%20with-Quartz%20v4-8B5CF6)](https://quartz.jzhao.xyz)

> Digital garden pessoal publicado como site estático via [Quartz v4](https://quartz.jzhao.xyz/). Notas de estudo sincronizadas a partir de um vault [Obsidian](https://obsidian.md/) e hospedadas no GitHub Pages.

**🌐 Site ao vivo:** <https://jhow-043.github.io/logos-archive/>

---

## Sobre

Este repositório contém a infraestrutura para publicar seleções do vault *O Grafo de Alexandria* como um site navegável. O conteúdo atual abrange:

- **Química** — notas da Graduação em Química (1º semestre)
- Roadmaps e materiais de estudo organizados por área

O fluxo é: editar no Obsidian → `make publish` → GitHub Actions faz o build e deploya automaticamente via GitHub Pages.

---

## Stack

| Camada | Tecnologia |
|--------|-----------|
| Editor | [Obsidian](https://obsidian.md/) |
| Build engine | [Quartz v4](https://quartz.jzhao.xyz/) |
| Sync | Python 3.10+ (`tools/sync_from_source.py`) |
| CI/CD | GitHub Actions |
| Hospedagem | GitHub Pages |

---

## Começando

### Pré-requisitos

- [Node.js](https://nodejs.org/) ≥ 18
- [Python](https://python.org/) ≥ 3.10
- [Obsidian](https://obsidian.md/) (para editar o vault)

### Instalação

```bash
git clone https://github.com/jhow-043/logos-archive.git
cd logos-archive
npm install --prefix quartz
```

### Comandos

```bash
make sync      # Sincroniza vault original → site/
make build     # Sync + build estático
make serve     # Servidor local com hot-reload em localhost:8080
make publish   # Sync + commit + push → dispara deploy automático
make help      # Lista todos os comandos disponíveis
```

---

## Estrutura do Repositório

```
logos-archive-v1/
├── site/          # Vault Obsidian publicada (abrir esta pasta no Obsidian)
├── quartz/        # Engine de build Quartz v4
├── tools/         # Scripts Python de sync e validação
├── docs/          # Documentação do projeto (ADRs, runbook, architecture)
└── .github/       # Workflows CI/CD
```

---

## Documentação

| Documento | Descrição |
|-----------|-----------|
| [docs/architecture.md](docs/architecture.md) | Arquitetura e decisões de design |
| [docs/runbook.md](docs/runbook.md) | Guia operacional (sync, build, debug) |
| [docs/decisions/](docs/decisions/) | Architecture Decision Records (ADRs) |

---

## Licença

O código de infraestrutura (scripts, configurações, workflows) está licenciado sob a [MIT License](LICENSE).

O conteúdo das notas (arquivos em `site/`) é de autoria própria — todos os direitos reservados salvo indicação contrária.
