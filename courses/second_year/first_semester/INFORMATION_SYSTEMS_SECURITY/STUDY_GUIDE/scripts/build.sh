#!/usr/bin/env bash
# ==============================================================================
# Script di Compilazione e Verifica per la Study Guide di Sicurezza dei Sistemi Informativi
# ==============================================================================
set -e

# Determina la cartella base di STUDY_GUIDE indipendentemente da dove viene lanciato
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GUIDE_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${GUIDE_DIR}"

echo "=================================================================="
echo "  Sicurezza dei Sistemi Informativi — Compilazione Study Guide"
echo "  Cartella operativa: ${GUIDE_DIR}"
echo "=================================================================="

# Gestione flag di pulizia
if [ "$1" == "clean" ]; then
    echo "Pulizia file ausiliari di compilazione..."
    rm -f main.aux main.log main.out main.toc
    rm -f chapters/*/*.aux chapters/*/*.log chapters/*/*.out chapters/*/*.toc
    echo "Pulizia completata con successo."
    exit 0
fi

echo ""
echo "[1/3] Primo passaggio di compilazione pdflatex..."
pdflatex -interaction=nonstopmode main.tex > /dev/null

echo "[2/3] Secondo passaggio di compilazione pdflatex (risoluzione riferimenti e TOC)..."
pdflatex -interaction=nonstopmode main.tex > /dev/null

echo ""
echo "[3/3] Esecuzione verifica automatica di copertura e stile..."
python3 scripts/verify_coverage.py \
    --tex-file chapters/ch01_introduzione/ch01_introduzione.tex \
    --keywords-file keywords/ch01_keywords.txt \
    --check-style

echo ""
echo "=================================================================="
echo "  COMPILAZIONE E VERIFICA COMPLETATE CON SUCCESSO!"
if [ -f "main.pdf" ]; then
    PAGES=$(python3 -c "import fitz; print(len(fitz.open('main.pdf')))" 2>/dev/null || echo "N/D")
    SIZE=$(du -h main.pdf | cut -f1)
    echo "  File generato: ${GUIDE_DIR}/main.pdf"
    echo "  Dimensione:    ${SIZE}"
    echo "  Totale Pagine: ${PAGES}"
fi
echo "=================================================================="
