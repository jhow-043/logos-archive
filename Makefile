.PHONY: sync sync-dry build serve publish test audit help

PYTHON ?= python3

# Sincroniza vault original → site/
sync:
	$(PYTHON) tools/sync_from_source.py

# Sync sem executar (modo dry-run)
sync-dry:
	$(PYTHON) tools/sync_from_source.py --dry-run

# Build local do site
build: sync
	cd quartz && npx quartz build

# Servidor local com hot-reload
serve:
	cd quartz && npx quartz build --serve

# Publica: sync + commit + push (dispara GH Actions)
publish: sync
	git add -A && git commit -m "sync: $(shell date +%Y-%m-%d)" && git push

# Smoke tests
test:
	$(PYTHON) tools/smoke_test.py

# Auditoria completa (links, stubs, frontmatter)
audit:
	$(PYTHON) tools/sync_from_source.py --validate-stubs --report-only

# Ajuda
help:
	@echo "Targets disponíveis:"
	@echo "  sync       — Sincroniza vault → site/"
	@echo "  sync-dry   — Simula sync sem copiar arquivos"
	@echo "  build      — Sync + build estático"
	@echo "  serve      — Serve o site localmente (hot-reload)"
	@echo "  publish    — sync + commit + push (dispara deploy)"
	@echo "  test       — Executa smoke tests"
	@echo "  audit      — Valida links e stubs"
