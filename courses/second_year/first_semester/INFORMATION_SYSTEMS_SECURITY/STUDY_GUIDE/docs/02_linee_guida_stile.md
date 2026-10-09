# Linee Guida di Stile e Standard LaTeX

Questo documento formalizza le convenzioni tipografiche, strutturali e stilistiche obbligatorie per la Study Guide di **Sicurezza dei Sistemi Informativi**.

---

## 1. Convenzioni Tipografiche e Titoli
- **Capitalizzazione dei Titoli:** Adottare rigorosamente lo stile *sentence case* per tutti i titoli (es. `Sicurezza dei sistemi informativi`, `Minacce e problemi di base`, `Attacchi e tecniche`). Non usare mai *UpperCamelCase* per i titoli di sezioni, ad eccezione di nomi propri o acronimi standard (es. `Stuxnet`, `BCP 38`, `TCP SYN Flood`).
- **Profondità dell'Indice:** Limitare la numerazione e la visualizzazione nell'indice ai primi due livelli:
  ```latex
  \setcounter{tocdepth}{1}   % Nell'indice solo capitoli e sezioni
  \setcounter{secnumdepth}{2} % Numerati solo capitoli, sezioni e sottosezioni
  ```
- **Voce Narrativa:** Esclusivamente terza persona accademica diretta e autorevole. Vietata qualsiasi attribuzione meta-testuale come *"Come spiegato a lezione"*, *"Il docente sottolinea"* o *"Secondo le slide"*. Il testo deve spiegare il concetto direttamente.

---

## 2. Struttura del Documento e Modularità
- **File Master (`main.tex`):** Contiene il preambolo globale, il caricamento di `style/macros.sty`, frontespizio, indice (`\tableofcontents`) e l'inclusione dei capitoli tramite `\subfile{chapters/...}`.
- **Capitoli Modulari:** Ciascun capitolo risiede nella propria sottocartella `chapters/chXX_<nome>/` ed è un file autonomo che include `\documentclass[../../main.tex]{subfiles}`.

---

## 3. Ambienti Grafici Personalizzati (`macros.sty`)
- **Box di Definizione Formale:**
  ```latex
  \begin{defbox}{Titolo del Concetto}
  Definizione rigorosa del concetto secondo standard RFC o NIST.
  \end{defbox}
  ```
- **Box di Insight d'Esame:**
  ```latex
  \begin{examinsight}[Archetipo Quesito / Trabocchetto Moodle]
  Testo del quesito, valutazione V/F e analisi tecnica del trabocchetto.
  \end{examinsight}
  ```
- **Snippet di Codice:**
  Formattati tramite l'ambiente `lstlisting` con font monospace `\ttfamily`, numerazione di riga ed evidenziazione semantica.

---

## 4. Verifica Automatica della Qualità
Prima di considerare concluso un capitolo, eseguire il test di conformità:
```bash
python3 scripts/verify_coverage.py \
  --tex-file chapters/chXX_<nome>/chXX_<nome>.tex \
  --keywords-file keywords/chXX_keywords.txt \
  --check-style
```
Il capitolo deve superare sia la verifica dei concetti obbligatori (100% coperti) sia i check di stile.
