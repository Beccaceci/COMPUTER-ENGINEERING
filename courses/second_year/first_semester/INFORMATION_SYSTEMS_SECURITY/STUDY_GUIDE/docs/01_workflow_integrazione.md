# Workflow Standard di Integrazione a 3 Fasi

Questo documento descrive il protocollo operativo standard per l'integrazione delle dispense ufficiali del corso di **Sicurezza dei Sistemi Informativi** (Prof. Cataldo Basile, Politecnico di Torino).

---

## Regola Fondamentale: Zero Inquinamento della Cartella Radice

Tutti i file generati, estratti o elaborati durante la creazione della guida di studio devono risiedere **esclusivamente** nella loro sottocartella dedicata all'interno di `STUDY_GUIDE/`. È severamente vietato salvare file di testo, script, bozze o file temporanei nella radice del repository.

- **`notes/`**: PDF originali delle dispense fornite dal docente.
- **`extracted/`**: Testo estratto dalle dispense e dump OCR/testo dalle slide.
- **`chapters/<ch_id>/`**: File sorgente LaTeX del capitolo e risorse correlate.
- **`keywords/`**: File di keyword per l'audit automatico di copertura (`chXX_keywords.txt`).
- **`style/`**: Pacchetti di stile e macro personalizzate LaTeX.
- **`scripts/`**: Script di build, estrazione e verifica.
- **`docs/`**: Documentazione e linee guida operative.
- **`main.tex` / `main.pdf`**: Documento master e PDF compilato (nella radice di `STUDY_GUIDE/`).
- **`LECTURE TRANSCRIPTIONS/`**: Solo trascrizioni finali formattate in Markdown.
- **`/tmp/`**: File audio intermedi e output grezzi di Whisper (mai nel repository).

---

## Panoramica del Processo

```
+-------------------------------------------------------------------------+
|                  PIPELINE DI INTEGRAZIONE A 4 FASI                      |
+-------------------------------------------------------------------------+
|                                                                         |
|  FASE 0: Acquisizione e Trascrizione Automatica delle Lezioni           |
|          -> Rilevamento registrazioni video (Downloads/ o fornite)      |
|          -> Trascrizione via scripts/transcribe_lecture.py              |
|          -> Isolamento file audio temporanei in /tmp/ (autopulizia)     |
|          -> Markdown strutturato con timestamp in LECTURE TRANSCRIPTIONS/|
|                                                                         |
|                                 |                                       |
|                                 v                                       |
|                                                                         |
|  FASE 1: Riproduzione Fedele 1:1 (LaTeX Baseline)                       |
|          -> Ingestione della dispensa PDF con scripts/extract_notes.py  |
|          -> Riproduzione esatta parola per parola e della struttura     |
|          -> Zero omissioni rispetto alla dispensa ufficiale             |
|                                                                         |
|                                 |                                       |
|                                 v                                       |
|                                                                         |
|  FASE 2: Ispezione Approfondita e Arricchimento Sul Posto               |
|          -> Triangolazione con LECTURE TRANSCRIPTIONS/ e BOOKS/         |
|          -> Integrazione del "perché" sistemico e aneddoti del prof     |
|          -> Approfondimenti d'esame e trabocchetti Moodle nel testo     |
|             (senza box separati examinsight / chapteroverview)          |
|                                                                         |
|                                 |                                       |
|                                 v                                       |
|                                                                         |
|  FASE 3: Integrazione Visiva ed Evidenze Empiriche (Zero Slide Dep.)   |
|          -> Recupero dati quantitativi e statistiche dalle slide        |
|          -> Grafici nativi in PGFPlots (es. Verizon DBIR)               |
|          -> Diagrammi topologici TikZ con tono famigliare (ladro/guardia)|
|                                                                         |
|                                 |                                       |
|                                 v                                       |
|                                                                         |
|  GATE DI QUALITÀ: Verifica Copertura e Compilazione                     |
|          -> python3 scripts/verify_coverage.py --check-style            |
|          -> Compilazione master: pdflatex main.tex (exit code 0)        |
+-------------------------------------------------------------------------+
```

---

## Dettaglio Operativo

### Fase 0: Trascrizione Automatica delle Lezioni
1. Eseguire lo script standardizzato:
   ```bash
   /Users/nicolabeccaceci/miniconda3/bin/python3 STUDY_GUIDE/scripts/transcribe_lecture.py \
     --input-video "/Users/nicolabeccaceci/Downloads/<file_video>.mp4" \
     --output-md "LECTURE TRANSCRIPTIONS/XX_YYYY-MM-DD_<Titolo>.md" \
     --lecture-num "XX" \
     --lecture-date "<Data>" \
     --topic "<Argomento>" \
     --summary "<Punto 1>" "<Punto 2>" \
     --prompt "<Prompt terminologico>"
   ```
2. I file audio scratch (.wav) vengono generati e rimossi automaticamente in `/tmp/`.
3. Verificare l'assenza assoluta di file nella directory radice.

### Fase 1: Riproduzione Baseline 1:1
1. Estrarre il testo della dispensa ufficiale:
   ```bash
   python3 scripts/extract_notes.py \
     --pdf notes/2025_SS___Materiale_Corso_CapitoloI.pdf \
     --output-txt extracted/dispensa_cap1_extracted.txt
   ```
2. Creare il file di capitolo `chapters/chXX_<nome>/chXX_<nome>.tex`.
3. Trascrivere la struttura esatta (sezioni, sottosezioni) e la prosa letterale della dispensa.
4. Verificare che il documento compili come baseline senza errori.

### Fase 2: Arricchimento Concettuale e Insight d'Esame
1. **Triangolazione delle Fonti**:
   - Trascrizioni lezioni (`LECTURE TRANSCRIPTIONS/`).
   - Testi di riferimento (`BOOKS/`: William Stallings, Bruce Schneier).
   - Domande d'esame passate e quiz Moodle (`EXAMS/`).
2. **Arricchimento nel Flusso**:
   - Spiegare il meccanismo causale alla radice di ogni vulnerabilità.
   - Introdurre i modelli economici d'attacco (asimmetria dei costi, ROI del cybercrime).
   - Includere gli avvertimenti d'esame e le distinzioni terminologiche sottili direttamente nella prosa della sezione o in sottosezioni dedicate (evitando box separati `examinsight` o `chapteroverview`).

### Fase 3: Asset Visivi ed Evidenze Empiriche
1. **Gap Filling dalle Slide**:
   - Identificare tabelle, statistiche e dati empirici presentati nelle slide ma assenti nella prosa della dispensa (es. Verizon DBIR).
   - Redigere tabelle comparative strutturate (es. tabella costi diretti/indiretti).
2. **Grafici PGFPlots Nativi**:
   - Visualizzare distribuzioni e confronti tramite PGFPlots nativo in LaTeX.
3. **Diagrammi di Rete TikZ**:
   - Disegnare gli scenari d'attacco e difesa impiegando metafore visive intuitive (il ladro mascherato, la guardia di sicurezza, gli elettrodomestici zombie), garantendo al contempo assoluto rigore tecnico sui protocolli.
