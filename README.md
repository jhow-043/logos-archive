# Logos Archive

[![Build & Deploy](https://github.com/jhow-043/logos-archive/actions/workflows/deploy.yml/badge.svg)](https://github.com/jhow-043/logos-archive/actions/workflows/deploy.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Built with Quartz](https://img.shields.io/badge/Built%20with-Quartz%20v4-8B5CF6)](https://quartz.jzhao.xyz)
[![Obsidian](https://img.shields.io/badge/Obsidian-powered-7C3AED?logo=obsidian&logoColor=white)](https://obsidian.md)
[![GitHub Pages](https://img.shields.io/badge/Hosted%20on-GitHub%20Pages-222?logo=github)](https://pages.github.com)

> Template de digital garden: vault [Obsidian](https://obsidian.md/) publicada como site estático via [Quartz v4](https://quartz.jzhao.xyz/) com sync automatizado e deploy no GitHub Pages.

**🌐 Site ao vivo:** <https://jhow-043.github.io/logos-archive/>

---

## Sobre

Pipeline completo para transformar um vault Obsidian em um site público navegável, sem necessidade de exportar arquivos manualmente.

**Funcionalidades:**
- Sync seletivo do vault (filtra apenas as pastas que você quer publicar)
- Conversão automática de frontmatter e links internos
- Build estático com grafo interativo, backlinks, busca e modo escuro
- Deploy automático via GitHub Actions no push

**Para usar como template:** fork o repositório, edite `tools/sync_from_source.py` para apontar para o seu vault e ajuste `quartz/quartz.config.ts` com seu domínio.

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
