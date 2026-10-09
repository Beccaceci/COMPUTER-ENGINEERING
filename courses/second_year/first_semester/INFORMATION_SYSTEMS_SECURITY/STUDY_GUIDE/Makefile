# ==============================================================================
# Makefile per la Study Guide di Sicurezza dei Sistemi Informativi
# ==============================================================================

PDFLATEX = pdflatex -interaction=nonstopmode
PYTHON = python3

.PHONY: all pdf verify clean

all: pdf verify

pdf: main.tex style/macros.sty chapters/ch01_introduzione/ch01_introduzione.tex
	@echo "==> Compilazione LaTeX (Passo 1/2)..."
	@$(PDFLATEX) main.tex > /dev/null
	@echo "==> Compilazione LaTeX (Passo 2/2)..."
	@$(PDFLATEX) main.tex > /dev/null
	@echo "==> Generato: main.pdf"

verify:
	@echo "==> Controllo di Copertura e Stile (Capitolo 1)..."
	@$(PYTHON) scripts/verify_coverage.py \
		--tex-file chapters/ch01_introduzione/ch01_introduzione.tex \
		--keywords-file keywords/ch01_keywords.txt \
		--check-style

clean:
	@echo "==> Rimozione file ausiliari di compilazione..."
	@rm -f main.aux main.log main.out main.toc
	@rm -f chapters/*/*.aux chapters/*/*.log chapters/*/*.out chapters/*/*.toc
	@echo "==> Pulizia completata."
