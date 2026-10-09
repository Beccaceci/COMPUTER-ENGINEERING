# Linee Guida per i Diagrammi TikZ e Grafici PGFPlots

Questo documento stabilisce i principi grafici e geometrici per la realizzazione delle figure e dei diagrammi di rete nella Study Guide.

---

## 1. Palette Cromatica Standard
I colori sono definiti in `style/macros.sty`:
- **`secblue` (RGB: 30, 90, 180):** Entità legittime, client affidabili, traffico lecito.
- **`secred` (RGB: 200, 30, 30):** Attaccanti, pacchetti forgiati, vettori di exploit, allarmi.
- **`secgreen` (RGB: 30, 140, 50):** Server protetti, contromisure attive (BCP 38, DHCP Snooping, crittografia).
- **`secorange` (RGB: 220, 110, 0):** Botnet, dispositivi IoT intermedi compromessi.
- **`secgray` (RGB: 100, 110, 120):** Apparati di rete generici, hub, cavi passivi.

---

## 2. Metafore Visive Famigliari e Intuitive
Nelle illustrazioni degli attacchi di rete, adottare un tono visivo narrativo e intuitivo che faciliti la memorizzazione, preservando al 100% la correttezza tecnica del protocollo:
- **L'Attaccante come Ladro:** Raffigurato con maschera da scassinatore (`\faUserSecret\quad\faMask`), con fumetti che esprimono l'intento criminoso in corsivo.
- **La Difesa come Guardia:** Il Border Router raffigurato come sentinella (`\faUserShield`), con il cestino (`\faTrash`) per il packet drop perimetrale.
- **Il Falso Server:** Server chassis con maschera (`\faServer\quad\faMask`) che cerca di vincere la race condition.
- **Botnet come Esercito di Schiavi:** Il criminale burattinaio che comanda elettrodomestici domestici zombie (Wi-Fi, telecamera IP, Smart TV, stampante).
- **Connection Hijacking:** Il ladro interposto che taglia la linea ad Alice tramite `TCP RST` e invia comandi forgiati a Bob.

---

## 3. Regole di Scaling e Spaziatura Geometrica
Per evitare testo sovrapposto o frecce ostruite:
1. **Incapsulamento in `\resizebox`:**
   ```latex
   \begin{figure}[htbp]
   \centering
   \resizebox{0.95\linewidth}{!}{%
   \begin{tikzpicture}[>=Stealth]
   ...
   \end{tikzpicture}%
   }
   \caption{...}
   \label{fig:...}
   \end{figure}
   ```
2. **Larghezza Fissa e `align=center` per Testi Multi-Riga:**
   Specificare sempre `text width=...` o spezzare con `\\` e `align=center` per evitare che nodi con testi lunghi si espandano orizzontalmente riducendo lo spazio delle frecce.
3. **Flussi Paralleli Distinti:**
   Quando due entità si scambiano messaggi bidirezionali (es. richiesta/offerta in DHCP), non usare la stessa linea o archi che si intersecano; differenziare gli ancoraggi (es. da `north` a `west`, e da `south` a `north east`).
4. **Altezza Verticale Generosa:**
   Nelle sequenze temporali (ladder diagrams come Connection Hijacking), posizionare i nodi superiori con almeno 1 cm di margine rispetto alla prima freccia orizzontale e distanziare i passi di almeno 1–1.4 cm.
