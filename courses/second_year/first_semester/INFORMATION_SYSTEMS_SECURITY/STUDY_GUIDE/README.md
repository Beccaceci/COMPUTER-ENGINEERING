# Sicurezza dei Sistemi Informativi — Study Guide Ufficiale

Questa cartella racchiude il progetto completo della **Study Guide Integrata** per il corso di *Sicurezza dei Sistemi Informativi* (Prof. Cataldo Basile, Politecnico di Torino).

Il testo integra parola per parola le **dispense ufficiali**, le **spiegazioni orali delle lezioni**, i trattati accademici di riferimento (**William Stallings** e **Bruce Schneier**), i dati empirici dei report industriali (**Verizon DBIR**, Cloudflare) e le analisi dei trabocchetti delle prove d'esame e quiz Moodle.

---

## Struttura della Cartella

```
STUDY_GUIDE/
├── main.tex                 # File master LaTeX radice (preambolo, frontespizio, TOC)
├── main.pdf                 # Output PDF compilato della Study Guide (29 pagine)
├── Makefile                 # Regole per compilazione rapida, verifica e pulizia
├── chapters/                # Capitoli del documento (struttura modulare)
│   └── ch01_introduzione/
│       └── ch01_introduzione.tex  # Capitolo 1: Introduzione e minacce di base
├── style/
│   └── macros.sty           # Pacchetti LaTeX, colori ufficiali, box e ambienti
├── notes/                   # Dispense ufficiali fornite dal docente (PDF)
│   ├── 2025_SS___Materiale_Corso_CapitoloI.pdf
│   └── 2025_SSI__Materiale_Corso_CapitoloII.pdf
├── extracted/               # Testo grezzo estratto dalle dispense ufficiali
│   └── dispensa_cap1_extracted.txt
├── keywords/                # Liste di concetti chiave per audit di copertura
│   └── ch01_keywords.txt
├── scripts/                 # Utility di automazione, compilazione e verifica
│   ├── build.sh             # Script bash di compilazione (2 passaggi) e verifica
│   ├── extract_notes.py     # Estrazione testo e sezioni da PDF dispensa
│   └── verify_coverage.py   # Controllo automatico di copertura concetti e stile
└── docs/                    # Documentazione metodologica e linee guida
    ├── 01_workflow_integrazione.md  # Protocollo standard a 3 fasi
    ├── 02_linee_guida_stile.md       # Regole tipografiche e stile dispensa
    └── 03_linee_guida_tikz.md        # Principi per diagrammi di rete e grafici
```

---

## Compilazione e Verifica

### 1. Metodo Rapido con Makefile
Dalla cartella `STUDY_GUIDE/`:
```bash
# Compilazione completa (2 passaggi pdflatex) e verifica automatica
make

# Solo compilazione PDF
make pdf

# Esecuzione del test di copertura concetti e stile
make verify

# Pulizia dei file ausiliari (.aux, .log, .out, .toc)
make clean
```

### 2. Metodo con Script Bash
Dalla radice del progetto o da `STUDY_GUIDE/`:
```bash
# Compila e verifica
./STUDY_GUIDE/scripts/build.sh

# Pulizia file temporanei
./STUDY_GUIDE/scripts/build.sh clean
```

### 3. Compilazione Manuale con pdflatex
```bash
cd STUDY_GUIDE
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

---

## Come Aggiungere un Nuovo Capitolo

Seguire il **Protocollo a 3 Fasi** descritto in detail in `docs/01_workflow_integrazione.md`:

1. **Fase 1 (Baseline LaTeX 1:1):**
   - Posizionare la dispensa PDF in `notes/`.
   - Estrarre il testo: `python3 scripts/extract_notes.py --pdf notes/<File>.pdf --output-txt extracted/<Nome>.txt`.
   - Creare la cartella `chapters/chXX_<nome>/` con il file `chXX_<nome>.tex`.
   - Riprodurre fedelmente la struttura delle sezioni e la prosa letterale della dispensa.
   - Includere il capitolo in `main.tex` con `\subfile{chapters/chXX_<nome>/chXX_<nome>}`.
2. **Fase 2 (Arricchimento sul Posto):**
   - Consultare le trascrizioni in `../LECTURE TRANSCRIPTIONS/` e i libri in `../BOOKS/`.
   - Arricchire in-place le spiegazioni (il "perché" sistemico, standard RFC/NIST).
   - Inserire le schede d'esame `\begin{examinsight}[...]` con trabocchetti Moodle e tracce scritte.
3. **Fase 3 (Asset Visivi ed Evidenze Empiriche):**
   - Recuperare dati empirici e tabelle dalle slide in `../SLIDES/`.
   - Disegnare grafici comparativi in PGFPlots e diagrammi di rete TikZ con tono famigliare (ladro, guardia, bot zombie).
4. **Verifica Finale:**
   - Creare `keywords/chXX_keywords.txt` e lanciare:
     ```bash
     python3 scripts/verify_coverage.py \
       --tex-file chapters/chXX_<nome>/chXX_<nome>.tex \
       --keywords-file keywords/chXX_keywords.txt \
       --check-style
     ```
