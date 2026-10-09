# Domande sicurezza

## Indice

- [Capitolo 1](#cap1)
- [Capitolo 2](#cap2)
- [Capitolo 3](#cap3)
- [Capitolo 4](#cap4)
- [Capitolo 5](#cap5)
- [Capitolo 6](#cap6)
- [Capitolo 7](#cap7)
- [Capitolo 8](#cap8)

<div id="cap1"></div>

## Capitolo 1

**D:** *Dire cos'è la window of exposure e dove si può agire per ridurla.*

**R:** Finestra di esposizione. Periodo di tempo tra scoperta di un nuovo bug di un software 
e installazione della patch di sicurezza per sistemare il problema.

- Fase di scoperta:
    
    - Bug scoperto
    - Exploit

- Fase di pubblicazione:

    - Vulnerabilità resa pubblica
    - Prouttore informato della vulnerabilità
    - Produttore informa i suoi clienti
    - Aggiornamento sistemi di protezione (IDS)

- Fase di protezione:

    - Rilascio di una patch
    - Patch resa nota a tutti
    - Installazione della patch

Per ridurla:

- Side thinking: cercare di anticipare gli attaccanti in modo da capire dove possono essere i bug.
- Cercare di utilizzare standard di sicurezza non artigianali.

---

**D:** *Spiegare brevemente la proprietà di sicurezza denominata integrità dicendo da quali attacchi protegge sia quando i dati a cui si riferisce sono memorizzati sia quando sono trasmessi*

**R:** Integrità è la proprietà per cui un messaggio non può essere modificato senza che il mittente o il ricevente se ne possa accorgere, pertanto garantisce che il messaggio non venga manomesso durante la trasmissione.

Difende da attacchi di tipo:

- Cancellazione
- Replay
- Modifica

---

**D:** *Bruce Scheiner ha scritto "security is a process, not a product" spiegare il significato di questa affermazione e fornire un esempio pratico di sua implementazione con elementi tecnici*

**R:** Comprare un singolo prodotto per fare sicurezza non è sufficiente perché un sistema è protetto in quanto il singolo prodotto non è esente da bug, ma è necessario progettare il proprio sistema di sicurezza utilizzando più sistemi in parallelo, possibilmente di produttori diversi in modo da garantire una difesa maggiore.

L'esempio più pratico è utilizzare un firewall di un produttore e un sistema di identificazione di un secondo produttore (IDS), in questo modo in caso di bachi del primo prodotto, subentra il secondo per arginare i danni.

---

**D:** *Definire i termini minaccia, vulnerabilità e security control, quindi spiegare quali relazioni intercorrono tra di loro e fornire un esempio per ciascun termine nel caso di una terna correlata*

**R:** 
- __Vulnerabilità__: debolezza di un asset, bug del software.
- __Minaccia__: evento atto a causare la perdita di una proprietà di sicurezza utilizzando una vulnerabilità come vettore di un attacco.
- __Security control__: monitoraggio del prodotto atto a cercare di proteggerlo dalle minacce, cercando di chiudere le vulnerabilità.

---
---

<div id="cap2"></div>

## Capitolo 2

**D:** *Ordinare dal più veloce al più lento i seguenti algoritmi: SHA, AES_ECB, AES_CBC, RC4*

**R:** RC4 > SHA > AES_ECB > AES_CBC

---

**D:** *Due utenti desiderano scambiarsi via rete una serie di documenti in formato ASCII (.TXT). Suggerire quali operazioni è opportuno svolgere su questi documenti prima di trasmetterli per resistere ad attacchi sulla rete (insicura). Si tenga presente che idocumenti non contengono info riservate. Nota: non si usino protocolli o formati dati complessi. Si esprima la soluzione tramite formula (usando termini appropriati, come aes(k,d) piuttosto che enc(k,d))*

**R:** Operazioni da eseguire:

- K = rand(); // Generazione di una chiave simmetrica
- T = unix_time(); // Per difendersi dagli attacchi di tipo replay
- V = rand(); // Generazione di un IV per utilizzare una modalità di cifratura tipo CBC
- Z = zip(D); // Compressione dei dati
- C = aes_128_cbc(Z, V, K); // Cifratura dati
- H = hmac_sha256(K || C || T || V || K) // MAC del messaggio

K, V inviati tramite RSA cifrati con chiave pubblica RSA del destinatario. 

Dati spediti successivamente con send(C || H)

---

**D:** *Dire i due principali vantaggi degli algoritmi basati su ECC*

**R:** Elliptic curve criptography: utilizza la matematica delle curve ellittiche per creare le chiavi per la cifratura asimmetrica.

Principali vantaggi:

- Per il black hat fattorizzazione delle chiavi più complesso (Logaritmo discreto su una curva)
- Possibilità di utilizzare chiavi più corte (circa 1/10)

---

**D:** *Vantaggi e svantaggi di cifratura fatta con enc(enc(p, k1), k2) con k1 e k2 chiavi diverse ma di lunghezza uguale*

**R:** Vantaggi:

- Maggiore sicurezza

Svantaggi:

- Soffre dell'attacco Meet-In-The-Middle: Supponendo di conoscere C e P, si esegue C'_i = enc(P, k_i) e P'_j = dec(C, k_j) e si trovano le coppie tali per cui C'_i = P'_j, in questo modo si trovano le chiavi k_i e k_j che decifrano il testo. Questo attacco rende la robustezza effettiva delle chiavi pari a N+1, anziché 2N.

---

**D:** *Differenza algoritmi stream e a blocchi*

**R:** Algoritmi stream:

- Criptano/decriptano i dati a blocchi di un bit o byte per volta con una chiave generata pseudorandomicamente durante la cifratura.
- Molto più veloci in quanto utilizzano il solo operatore XOR.
- Adatto per la cifratura di settore di dischi.
- Inadatto per la cifratura di dati inviati nella rete:
    - gestione dei dati a pacchetti,
    - probabilità di perdita dei dati durante il trasporto in rete,
    - difficile gestione del generatore di chiave e sincronizzazione.

Algoritmi a blocchi:
- Criptano/decriptano i dati a blocchi di una certa dimensione B
- Più lenti rispetto ad algoritmi stream
- Più efficienti per la trasmissione in rete dei dati criptati
- Necessitano di padding in casi in cui la lunghezza dei dati non è un multiplo del blocco base.
- La chiave è di dimensione fissa (In base al tipo di algoritmo)

---

**D:** *Come avviene la verifica di un documento firmato*

**R:** Procedura:

- Si prende la parte di firma e la si decripta con la chiave pubblica del firmatario.
- Si prende il documento e si calcola l'hash con lo stesso algoritmo usato per la creazione della firma.
- Si confronta hash del documento con hash decriptato in precedenza
- Se sono uguali, allora la firma è verificata

---

**D:** *Spiegare brevemente la tipologia di cifratura simmetrica e quella asimmetrica, indicando i vantaggi e svantaggi di ciascuna tipologia.*

**R:** Cifratura simmetrica: cifratura di un messaggio utilizzando una chiave simmetrica in grado sia di criptare che di decriptare il messaggio.

Vantaggi:

- Più veloce
- Più efficiente
- Chiavi più corte rispetto a cifratura asimmetrica
- Autenticazione e integrità

Svantaggi:

- Non garantisce la proprietà di non ripudio del messaggio
- Problema di condivisione della chiave segreta
- Problema della confidenzialità (Sono sicuro che il destinatario è chi dice di essere?)

Cifratura asimmetrica: detta anche a chiave pubblica e la caratteristica principale sta nell'utilizzo di due chiavi, con ruolo interscambiabile e con un legame matematico, per criptazione e decriptazione dei dati: una chiave utilizzabile solo per criptazione e l'altra solo per decriptazione.

Vantaggi:

- Garantisce la proprietà di non ripudio
- Utilizzabile per la distribuzione delle chiavi segrete
- Autenticazione e integrità
- Riservatezza senza segreti condivisi

Svantaggi:

- Alto carico di elaborazione
- Chiavi di lunghezza più lunghe, in quanto trasportano un legame matematico
- Rischio di firma involontaria di documenti

---

**D:** *Spiegare cos'è la modalità operativa CTS qual è l'idea principale su cui si basa la sua implementazione e perchè sta assumendo sempre più rilevanza*

**R:** Modalità operativa utilizzata in modo da evitare di creare padding durante la cifratura, ponendo una parte del penultimo blocco cifrato nella parte mancante dell'ultimo blocco da cifrare, in modo da avere un blocco di lunghezza pari al blocco base e scambiando così la posizione dei blocchi C(k) e C(k-1). Utile per la cifratura dei dischi (spazio limitato).

---

**D:** *Dovendo cifrare con AES una password da 12 caratteri con 2 byte di
sale è meglio usare ECB, CBC o CTR?*

**R:** Nonostante CTR è pensato per cifrare dati con blocco inferiore al blocco base, in questi casi è meglio utilizzare ECB in quanto per una quantità di dati così piccola, CTR e CBC dovrebbero portarsi dietro informazioni riguardo IV e, nel caso di CTR, del nonce utilizzato.

---

**D:** *Firma digitale con digest SHA256, chiave privata RSA-2048 su un file da 10MB. Qual'è la dimensione della firma?*

**R:** SHA256 genera un digest di 32 byte, tuttavia RSA per firmare una quantità di dati più piccola della lunghezza della firma, deve allineare il messaggio per farlo arrivare a 2048 bit. Ciò significa che la grandezza della firma sarà appunto di 2048 bit, ovvero 256 byte.

---

**D:** *Un'azienda deve scambiare con un'altra dei file ma possono utilizzare soltanto una chiave di 12 caratteri max, indicare come deve essere implementato il sistema*

**R:** Generazione della chiave: K = KDF(k, itc, salt), in questo modo si genera una chiave sufficientemente randomica.
Scambio chiave: RSA della chiave segreta, criptata con la chiave pubblica della seconda azienda.
(Se serve indicare altro, guardare domanda relativa a scambio file)

---
---

<div id="cap3"></div>

## Capitolo 3

**D:** *Dictionary attack, che cos'è, sotto quali ipotesi può essere eseguito e contromisure*

**R:** Ipotesi: 

- Si conoscono o si può accedere al DB di hash di autenticazione del server da attaccare.
- Si conosce l'algoritmo di hash utilizzato. dal server

Attacco: utilizzando un dizionario di parole comuni che le persone spesso utilizzano come password, si generano un set di passphrase e per ogni elemento di questo set si esegue l'hash con l'algoritmo noto e si salva al coppia (P,H).

Dopodiché, per ogni hash, lo si confronta con l'hash letto dal DB del server e se gli hash coincidono, allora la password è stata trovata.

Contromisure: aggiungere del sale alla password, in modo da rendere imprevedibile il suo hash e, quindi, più difficoltoso questo tipo di attacco.

---

**D:** *spiegare cos'è un sistema di autenticazione a sfida asimmetrica, indicando quali messaggi vengono scambiati tra il client e il server che autentica e quali vantaggi e svantaggi presenta.*

**R:** Autenticazione del client, utilizzando un algoritmo asimmetrico per dimostrare che il client è chi dice di essere, tramite la sua chiave privata.

Messaggi scambiati:

- Client invia il suo certificato a chiave pubblica al server
- Server estrae la chiave pubblica e cifra un numero nonce da inviare al client
- Client decifra il nonce con la chiave privata e invia il nonce decriptato al server
- Server confronta il nonce ricevuto con il nonce generato, se sono uguali allora decirptazione avvenuta con successo.

Vantaggi:

- Server non deve salvare internamente nessun segreto condiviso
- Meccanismo più forte
- Resistente ad attacchi sniffing

Svantaggi:

- Procedura lenta
- Può condurre a firma involontaria
- Client necessita di un certificato a chiave pubblica (X.509)

--- 

**D:** *Authenticated encryption*

**R:** Metodo per raggruppare autenticazione e criptazione dei dati in un passaggio solo. Nel caso in cui si trasportano dei dati extra senza necessità di autenticazione, ma solo di integrità, si parla allora di AEAD (authenticated encryption with associated data)

---

**D:** Spiegare brevemente il concetto di OTP e quale problema di sicurezza risolve. Spiegare, quindi, con l’ausilio di appropriate formule, le fasi di inizializzazione e verifica nel protocollo S/KEY

**R:** One time password, è una tecnica utilizzata per generare password univoche usa-e-getta, in modo da evitare la memorizzazione delle password per gli utenti, o utilizzare password deboli.

S/KEY: si generano le prime N password a lato client con la relazione P(k) = hash(P(k-1)), con P(0) password generata dall'utente e si trasmette al server P(N) e viene utilizzata per verifica. Il server per verificare la i-esima password digitata dall'utente, ne calcola l'hash e lo confronta con P(i+1) salvato in precedenza, se coincidono, allora può accedere e server memorizza P(i) come verificatore.

---

**D:** *Sistemi di autenticazioni a sfida simmetrici: messaggi scambiati, vantaggi e svantaggi*

**R:** Autenticazione basata sul segreto condiviso tra i due peer.

Messaggi scambiati:

- Client invia la richiesta di accesso al server con il proprio ID
- Server invia la challenge: un numero nonce
- Client esegue un calcolo sul nonce, coinvolgendo il segreto condiviso (ad esempio hash(K || nonce)) e invia il risultato al server
- Server esegue lo stesso calcolo e confronta con quello ricevuto

Vantaggi:

- Facile da implementare
- Veloce
- Resistente ad attacchi sniffing

Svantaggi:

- Server deve salvare internamente tutte le password in chiaro per poter eseguire i calcoli di verifica

---
---

<div id="cap4"></div>

## Capitolo 4

**D:** *Descrivere PKCS#7*

**R:** Standard per la creazione di buste sicure per l'invio e impacchettamento di dati, è un formato ricorsivo e una busta PKCS#7 può contenere diversi oggetti, tra cui anche un'altra busta PKCS#7.

Ogni involucro può essere firmato in maniera indipedente.

Utilizzato soprattutto nella posta elettronica sicura.

---

**D:** *Descrivere PKCS#10*

**R:** PKCS#10 è uno standard utilizzato per la richiesta di un certificato X.509 ad una CA. Al suo interno si inserisce la chiave pubblica e il proprio DN e una serie di attributi.

Per dimostrare alla CA di essere i proprietari della richiesta del certificato, si firma la richiesta con la chiave privata, in modo che la CA sia in grado di verificare tale proprietà.

--- 

**D:** *Descrivere PKCS#11*

**R:** Standard per la definizione di API di basso livello per la realizzazione di motori crittografici.

- Software: tramite librerie apposite
- Hardware: installazione di appositi driver

---

**D:** *Descrivere PKCS#12*

**R:**  Definisce uno standard per buste sicure, per il trasporto di materiale crittografico tra un dispositivo e un altro, ad esempio trasporto di chiave privata, o di certificati.

---

**D:** *Cosa è una CRL?*

**R:** Una CRL è un ente per la richiesta di un elenco di certificati revocati, firmati da una CA fidata, o da un delegato con firma digitale.

---

**D:** *Dato un certificato X.509 spiegare quali sono le sue proprietà di sicurezza intrinseche e come sono ottenute.*

**R:**

- Integrità: ottenuto perchè è firmato da una CA
- Autenticazione dei dati contenuti (persona indicata possiede la chiave privata corrispondente): ottenuto perchè è firmato dalla CA (si usa PKCS#10 per effettuare la richiesta).
- Non ripudiabilità da parte della CA emettitrice: ottenuto mediante la firma della CA

---
---

<div id="cap5"></div>

## Capitolo 5

**D:** *Dire che cos'è dns cache poisoning*

**R:** Attacco alla cache del DNS nameserver, due modi possibili:

- Successivamente ad una DNS query, uno shadow server risponde con un indirizzo a sua scelta, più una serie di indirizzi per alcuni siti non richiesti. La vittima riceve la risposta e, siccome è un protocollo non autenticato, salva ciecamente gli indirizzi ricevuti.

- Uno shadow server invia una DNS query ad un nameserver e fornisce immediatamente la risposta, agendo allo stesso modo precedentemente descritto.

---

**D:** *Ping flooding, cos'è e come difendersi in modo da non alterare il normale traffico tcp/ip*

**R:** Attacco di tipo DOS che sfrutta un massiccio uso del protocollo ICMP echo request verso la vittima. Se il numero di queste echo request è sufficientemente elevato, la vittima non sarà più in grado di fornire il proprio servizio. Un modo semplice per eseguire questo attacco è tramite IP spoofing, falsificando il mittente usando IP della vittima e come destinazione usare l'indirizzo broadcast della rete a cui la vittima è collegata.

Per difendersi da questo attacco:

- __MAI__ accettare pacchetti broadcast dall'esterno.
- Network management per attaccanti nella rete interna.

---

**D:** *DNS flash crowd*

**R:** Attacco di tipo DOS contro i nameserver, in quanto non sono progettati per supportare un grosso carico di lavoro. Si organizzano diversi attaccanti, oppure tramite una botnet, si eseguono un numero sufficiente di richieste simultanee ad un DNS nameserver, in modo da bloccarne il servizio in quanto non sarà più in grado di gestire tutte le risposte.

---

**D:** *SA in transport-mode di tipo IPsec ESP, proprietà di sicurezza, dire quali proprietà di sicurezza sono obbligatorie e quali no (spiegazione)*

**R:** ESP è un protocollo di sicurezza che permette la proprietà di riservatezza e, nell'ultima versione, anche autenticazione dei pacchetti.

Creare una SA in transport mode permette di aggiungere un intestazione di sicurezza al pacchetto da inviare, permettendo di autenticare e cifrare il pacchetto, ma non autentica i campi variabili. In particolar modo, transport-mode con ESP:

| header | Esp header |     data     | Esp trailer |

Con l'ultima versione di ESP è possibile mettere an NULL la parte di autenticazione o la parte di riservatezza, ma non entrambe le parti.

---

**D:** *Descrivere Syn Cookie*

**R:** Protocollo pensato per contrastare l'attacco del tipo Syn flooding, che consiste di saturare le porte TCP di handshake per la richiesta di risorse HTTP, non inviando il pacchetto di ACK finale per concludere l'handshake.

Consiste nell'inviare insieme al pacchetto di SYN-ACK, un cookie con id pari al sequence number del pacchetto corrispondente, firmato dal server, con le informazioni del client che ha eseguito la richiesta, in questo modo quando il client richiete una connessione al server, invia anche il cookie così che il server sia in grado di riconoscere chi ha già eseguito una richiesta precedente, senza salvare nulla sul server.

---

**D:** *Disegnare e discutere della End-to-end security with basic VPN*

**R:** Tunnel mode tra due gateway per realizzare il basic VPN e transport mode tra due host per realizzare End-to-end security.

In questa modalità si presuppone che non solo la rete esterna sia non fidata, ma anche la rete interna. Si raddoppia il livello di difesa.

In questa modalità è possibile installare un modulo AH per il transport mode, in modo da garantire autenticazione e integrità dei pacchetti e anche la possibilità al sistemista di monitorare il traffico passante, mentre si può utilizzare anche ESP per il canale sicuro tra gateway per garantire anche riservatezza al di fuori delle reti lan.


---

**D:** *Un'azienda decide di collegare due sue filiali con una vpn del fipo basic vpn: dire caratteristiche, vantaggi e rischi*

**R:** Si instaura un canale sicuro di tipo Tunnel mode tra i gateway delle due filiali, in questo modo si parte dall'idea che le reti esterne alle aziende siano reti non fidate. Essendo un canale in tunnel mode, i pacchetti all'esterno del gateway vengono incapsulati all'interno di un altro pacchetto, in modo da poter proteggere anche i campi variabili all'interno del pacchetto da proteggere e, nel caso si utilizzi ESP con AH, garantire anche riservatezza e autenticazione.

Vantaggi:

- Protezione al di fuori della rete aziendale
- Proprietà di sicurezza quali integrità, autenticazione e riservatezza garantite

Svantaggi:

- Se un attaccante è nella rete interna, è in grado di monitorare i pacchetti prima che passino per il gateway, in quanto la rete interna è considerata fidata e nessun tipo di proprietà di sicurezza viene applicata.

---
---

<div id="cap6"></div>

## Capitolo 6

**D:** *Quali sono gli step di trasformazione dei dati quando inviati tramite un canale TLS con la ciphersuite TLS_DHE_DSS_WITH_AES_128_CBC_SHA con ZIP*

**R:** 

- Frammentazione dei dati
- Compressione con l'algoritmo di ZIP
- Calcolo del padding
- Calcolo digest con SHA su dati e padding
- Cifratura con AES_128_CBC
- Creazione del pacchetto: header || dati cifrati

---

**D:** *TLS, proprietà di sicurezza obbligatorie e facoltative, dire con quali algoritmi e con quali chiavi vengono realizzate*

**R:** Obbligatorio:

- Autenticazione del server: sfida asimmetrica con certificato X.509
- Integrità e autenticazione dei messaggi: tramite SHA-2
- Protezione da replay e cancellazione: pacchetti numerati con un MID

Facoltativo:

- Autenticazione del client: può essere fatto a livello applicativo (possibile mancanza di certificato)
- Riservatezza dei messaggi: algoritmo simmetrico (es: AES), dove il client decide la chiave da utilizzare e la trasmette tramite crittografia a chiave pubblica

---

**D:** *Heartbleed*

**R:** Attacco contro DTLS, ovvero TLS per i datagram UDP, in quando non esiste il concetto di sessione con questo protocollo, è necessario con una certa frequenza, sapere se la connessione TLS è ancora attiva tra i due peer.

Questo attacco sfrutta questi messaggi (protocollo heartbeat), richiedendo una risposta più grande rispetto al messaggio inviato. In questo modo la vittima risponde con la grandezza richiesta, riscontrando un problema del tipo buffer over-read, riuscendo ad ottenere così dati del blocco di RAM dove è stata registrata la richiesta. In questo modo è possibile ottenere dati sensibili come ad esempio pasword, o chiavi private qualora il server non disponga di HSM.

---

**D:** *Indicare quali proprietà di sicurezza sono disponibili tramite il protocollo TLS-1.2. Per ciascuna proprietà indicare se è opzionale o meno, la metodologia usata per implementarla e le eventuali chiavi specifiche o altri parametri di configurazioni necessari*

**R:** Principali modifiche:

- Possibilità di utilizzo di PRF (pseudo random function) per la generazione delle chiavi
- Utilizzo di SHA256 per il calcolo del digest
- Supporto per AE con AES in modalità GCM o CCM
- Ciphersuite: TLS_RSA_WITH_AES_128_CBC_SHA 
- Deprecate IDEA e DES

---

**D:** *TLS client authentication vs HTML form-based authentication: vantaggi, svantaggi e soluzioni*

**R:** TLS client authentication permette l'autenticazione del client tramite certificato a chiave pubblica.

Vantaggi:

- Metodo di autenticazione più forte
- Superficie di attacco piccola (Si può attaccare solo TLS)

Svantaggi:

- Non tutti gli user hanno un certificato a chiave pubblica

HTML form-based authentication è autenticazione tramite form direttamente nella pagina fornita all'utente, in cui è necessario scrivere il proprio nome utente e la propria password ed è compito del programmatore di gestire la parte di sicurezza dei dati dell'utente.

Vantaggi:

- Semplice da implementare
- Nessuna necessità di certificati X.509

Svantaggi:

- Superficie di attacco grande, un attaccante può sfruttare bachi anche del srever web e nel codice delle pagine stesse
- Non sempre i programmatori gestiscono la sicurezza in maniera corretta

Per questo secondo tipo di autenticazione, una maniera per aumentarne la sicurezza è quela di attivare un canale TLS prima dell'autenticazione.

Per generici utenti internet, questa soluzione è la più ideale per la scarsa diffusione di utilizzo di certificati

---

**D:** *Si vuole controllare l’accesso alle pagine web ospitate da un server operando solo sulla configurazione del server stesso. Identificare le possibili tecniche utilizzabili, indicandone vantaggi e svantaggi.*

**R:** 

- Ingress: semplice, ma facilmente aggirbile (IP spoofing)
- IP-SEC: più forte, a basso livello, ma è da configurare anche il client
- TLS: il client necessita di certificato
- HTTP basic/digest: semplice, ma facilmente aggirabile
- Form based: facile da implementare, ma dipende da come è sviluppato

---
---

<div id="cap7"></div>

## Capitolo 7

**D:** *Disegnare e descrivere l'architettura Dual Homed Gateway con vantaggi e svantaggi*

**R:** Router posizionato verso la rete esterna e bastion host tra router e rete interna. In questo modo si ha una doppia difesa, dove sul router si può attivare una funzione di packet filter dei pacchetti entranti, mentre sul bastion host una funzione di application gateway per controllare i pacchetti a livello applicativo.

Vantaggi:

- Facile da realizzare
- Richiede poco hardware
- Mascherazione rete interna
- Doppia linea di difesa

Svantaggi:

- Poco flessibile
- Grosso carico di lavoro per il bastion host

---

**D:** *Descrivere l’architettura firewall screened host gateway indicando attori, vantaggi e svantaggi*

**R:** Router posizionato tra rete esterna e rete interna e bastion host posizionato sulla rete interna.

Il router blocca il traffico e indirizza al bastion host per controllare che sia traffico permesso (da entrambe le direzioni). Tuttavia è possibile abilitare delle eccezioni, ovvero servizi che non necessitano di passare dal bastion host per essere controllati. 

Router in modalità packet filter, Bastion host in modalità circuit/application gateway

Vantaggi: 

- Maggiore flessibilità
- Attivazione di whitelist di alcuni servizi

Svantaggi:

- Singolo punto di rottura
- Più caro
- Complicato da gestire

---

**D:** *Disegnare lo schema dello “Screened Subnet”. Indicare il ruolo dei singoli componenti. Vantaggi e svantaggi di questo schema.*

**R:** Due router e un GW. La rete dove è presente la DMZ è possibile fare filtraggio dei pacchetti e il secondo router fa da ponte tra le due reti

Vantaggi:

- Flessibilità
- Doppia linea di difesa
- DMZ

Svantaggi:

- Costo
- Componenti dello stesso produttore potrebbero avere bug in comune

---

**D:** *Descrivere la tecnologia del packet filter e descrivere vantaggi e limitazioni*

**R:** Tipo di controllo sui pacchetti in grado di leggere l'intestazione IP e di decidere il destino del pacchetto. Veloce, ma insicuro.

Vantaggi:

- Indipendente dalle applicazioni
- Maggiore scalabilità
- Ottime prestazioni
- Basso costo

Svantaggi:

- Controlli poco precisi
- Problema con servizi che allocano porte dinamicamente (FTP)
- Nessun concetto di stato: pacchetti processati indipendentemente dagli altri
- Configurazione complessa: rischio di bloccare traffico TCP involontariamente

**D:** *Con riferimento ad un firewall di rete, spiegare brevemente le modalità di configurazione whitelist e blacklist*

**R:** Whitelist: in questa modalità è possibile utilizzare solo servizi espressamente concessi. Maggiore sicurezza, ma più difficile da gestire.

Blacklist: in questa modalità è possibile utilizzare qualsiasi servizio che non sia espressamente vietato. Minore controllo, ma più facile da gestire.

---

**D:** *Qual è la principale differenza tra un IDS e un IPS?*

**R:** IDS: Intrusion detection system: sistema per identificare individui che usano un pc o una rete senza autorizzazione, oppure utenti che violano i loro privilegi.

Possono essere:

- passivi: controllano il pattern d'azione dell'intruso, oppure utilizzo di checksum crittografiche
- attivi: hanno tre fasi:

    - learning: analisi statistica
    - monitoring: analisi attiva del traffico di dati
    - reaction: reazione al superamento di una soglia

IPS: sistema di prevenzione degli intrusi, agiscono durante l'attacco, chiudendo le porte utilizzate dall'attaccante. Rischio di chiudere traffico innocuo, o di prendere la decisione sbagliata.

---
---

<div id="cap8"></div>

## Capitolo 8

**D:**  *Dire che cosa ha in più APOP rispetto a POP e come lo implementa*

**R:** APOP aggiunge autenticazione a sfida al comando POP, dove la sfida è la parte della riga di HELLO tra '<>', con parentesi incluse. La risposta alla sfida è MD5(sfida + pwd) e codificata in esadecimale

---

**D:** *PGP, dire caratteristiche, vantaggi e svantaggi*

**R:** Pretty Good privacy: è un metodo per fare posta sicura, con autenticazione, integrità e riservatezza. Non utilizza certificati, ma si basa sul concetto di propagazione della fiducia.

---

**D:** *Comando AUTH di ESMTP*

**R:** Permette l'autenticazione dello user su SMTP. Dopo il comando EHLO, il comando AUTH può essere di risposta a questo comando e presenta una lista di meccanismi di autenticazione supportati. Il client ne sceglie uno e viene eseguito il protocollo di autenticazione.

Esempi di comandi AUTH:

- Plain
- Login
- CRAM
- SCRAM

---

**D:** *Differenza in SMIME tra Signed e Clear Signed*

**R:** Signed: Messaggio firmato e decodificato in BASE64

Clear Signed: Messaggio solamente firmato

---

**D:** *Spiegare tre tecniche anti-spam per incoming MTA, identificandone per ognuna vantaggi e svantaggi*

**R:** DNSBL: Black list basato su DNS lookup. Quando si riceve un messaggio di posta elettronica, si fa un lookup sull'indirizzo del sender con il comando nslookup -q=A D.C.B.A.dnsbl.antispam.net e se la risposta è NXDOMAIN, allora non è uno spammer, altrimenti viene fornito un indirizzo del tipo 127.0.0.x, dove x è un codice dello spammer.

Greylisting: basato sul fatto che gli spammer non hanno tempo, si ritarda la ricezione della posta. Se chi ha inviato la posta non è uno spammer, ritenterà l'invio. Ha lo svantaggio di ritardare tutta la posta in ingresso e il MTA deve tenere traccia di chi ha provato l'invio

Nolisting: si mettono a disposizione più MX dove solo uno è attivato. Lo spammer non li proverà tutti, ma solo qualcuno. Ritarda anche l'ham

---

**D:** *Con riferimento ai formati per la creazione di un documento elettronico con firma digitale, descrivere le soluzioni disponibili e discuterne i relativi vantaggi e svantaggi*

**R:** Possibili opzioni:

Enveloping signature: la firma ricopre il documento

Vantaggi:

- Indipendente dal documento da firmare

Svantaggi:

- Richiede modifica applicazioni
- Il documento è prima da estrarre

Enveloped signature: il documento ha il suo spazio per la firma (es. PDF)

Vantaggi:

- Non è necessario modificare le applicazioni

Svantaggi:

- Applicabile solo su alcuni formati

Detached signature: la firma è staccata dal documento e ogni firma ha il puntatore al documento a cui si riferisce

Vantaggi:

- Indipendente dal tipo di documento

Svantaggi:

- Bisogna tenere traccia del link firma-documento

