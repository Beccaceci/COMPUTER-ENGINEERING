# Procedura di Configurazione Ambiente LABINF su Mac Apple Silicon (M-series / ARM64)

Questa guida illustra la configurazione completa per riprodurre in locale su macOS il laboratorio **LABINF (Politecnico di Torino)** del corso *Sicurezza dei Sistemi Informativi* (Prof. Cataldo Basile), garantendo piena fedeltà agli attacchi di rete Layer 2 (ARP poisoning con Ettercap, sniffing con Wireshark, scansioni Nmap).

---

## 1. Perché l'approccio UTM (Opzione B) su Mac ARM

Nelle istruzioni ufficiali (`Istruzioni per i laboratori.pdf`) viene indicato Oracle VM VirtualBox su architettura x86_64. Su processori Apple Silicon (M1/M2/M3/M4/M5):
1. **VirtualBox** non supporta nativamente la virtualizzazione hardware ARM64 di Linux né gestisce agilmente la conversione x86_64 senza gravi penalità di prestazioni.
2. **Docker bridge** su macOS non consente attacchi Layer 2 reali (*ARP cache poisoning*) tra container o verso l'host perché il daemon gira dentro una VM HypervisorKit isolata con una singola interfaccia di rete virtuale NATtata.
3. **UTM** sfrutta il framework nativo `Hypervisor.framework` di macOS, consentendo di eseguire istanze Linux ARM64 a piena velocità hardware con interfacce di rete configurabili in modalità **Host Only** o **Shared Network (NAT)**.

---

## 2. Download dell'Immagine Kali Linux per Mac ARM

Puoi utilizzare l'installer ufficiale Kali Linux per architettura ARM64:

* **Download Diretto (Mirror Ufficiale GARR / Kali):**
  * Versione Installer ISO: [kali-linux-2026.2-installer-arm64.iso](https://kali.mirror.garr.it/kali-images/kali-2026.2/kali-linux-2026.2-installer-arm64.iso)
  * Pagina base releases: [https://www.kali.org/get-kali/#kali-arm](https://www.kali.org/get-kali/#kali-arm)

* In alternativa, dalla galleria UTM:
  * È disponibile la VM pre-impostata pronta all'uso su UTM: [Kali Linux ARM64 UTM Gallery](https://mac.getutm.app/gallery/kali-2023)

---

## 3. Configurazione della Rete Virtuale su UTM

Per svolgere le esercitazioni che richiedono 3 nodi (**Alice**, **Bob**, **Chuck**):

1. **Creazione della Macchina Master:**
   * Apri **UTM** (`/Applications/UTM.app`).
   * Clicca su **+** -> **Virtualize** -> **Linux**.
   * Seleziona l'immagine ISO Kali ARM64 scaricata.
   * Assegna alla macchina:
     * **RAM:** 2 GB - 3 GB (avendo 16 GB totali, puoi allocare 2.5 GB a ciascuna VM).
     * **CPU:** 2 vCPU.
     * **Disco:** 20-30 GB.
   * Completa l'installazione (creando l'utente `kali` con password `kali`, come previsto dal Lab).

2. **Configurazione Scheda di Rete:**
   * Nelle impostazioni della VM -> Sezione **Network**:
   * Imposta **Network Mode:** `Shared Network` (oppure `Host Only`).
   * Le VM riceveranno IP nella medesima sottorete (es. `192.168.64.0/24` o `10.0.2.0/24`) e saranno reciprocamente raggiungibili con comunicazioni broadcast/ARP non bloccate.

3. **Clonazione Rapida delle VM:**
   * Una volta installato il sistema master con tutti i tool, arresta la VM.
   * Fai click destro sulla VM in UTM -> **Clone**.
   * Crea:
     * `Kali-Alice` (Vittima / Server)
     * `Kali-Bob` (Client)
     * `Kali-Chuck` (Attaccante MITM)

---

## 4. Installazione Pacchetti di Laboratorio (Appendice A)

All'interno della macchina Kali (prima di clonarla), apri un terminale ed esegui l'installazione dei package richiesti dal corso:

```bash
sudo apt update && sudo apt install -y \
  vsftpd \
  hexedit \
  strongswan \
  libstrongswan-extra-plugins \
  dkms \
  lynx \
  s-nail \
  alien \
  nsis \
  httptunnel \
  net-tools \
  ettercap-text-only \
  ettercap-graphical \
  ptunnel \
  nmap \
  openssl \
  hashdeep \
  p7zip-full \
  apache2 \
  docker.io \
  wireshark \
  tshark
```

---

## 5. Esecuzione dei Servizi Target (Mac ARM) per Lab 01

Per il **Laboratorio 01**, puoi avviare i servizi vulnerabili di Alice direttamente su Alice (sia all'interno della VM Alice che su Docker Mac ARM tramite lo script predisposto):

1. Posizionati nella cartella:
   ```bash
   cd "LABS/Lab01_Attacchi_di_Base/Materiale per Mac ARM"
   ```
2. Gestisci i servizi con lo script automatizzato `run_arm.sh`:
   * Avviare i servizi:
     ```bash
     ./run_arm.sh run
     ```
   * Verificare la casella email di Alice:
     ```bash
     ./run_arm.sh read_email
     ```
   * Accedere alla shell interna del container:
     ```bash
     ./run_arm.sh shell
     ```
   * Spegnere e rimuovere i servizi:
     ```bash
     ./run_arm.sh clean
     ```
