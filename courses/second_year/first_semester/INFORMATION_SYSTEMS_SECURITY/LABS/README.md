# Cybersecurity Laboratories (01UDUOV)
**Politecnico di Torino — Prof. Cataldo Basile**

Welcome to the laboratory repository for the *Information Systems Security / Sicurezza dei Sistemi Informativi* course.

This directory hosts the official assignment texts, exhaustive pedagogical LaTeX/PDF solutions, and raw execution traces across all laboratories.

---

## 🛠️ Simulation Environment Repository

All Docker containers, multi-node network topologies (Alice, Bob, Chuck), automation scripts, and virtual machine setup guides have been consolidated into a dedicated, standalone repository:

[![GitHub Repository](https://img.shields.io/badge/GitHub_Repository-polito--ssi--labinf-blue?logo=github&style=for-the-badge)](https://github.com/Beccaceci/polito-ssi-labinf)

👉 **Access the environment here:** [**https://github.com/Beccaceci/polito-ssi-labinf**](https://github.com/Beccaceci/polito-ssi-labinf)

The dedicated environment repo provides:
* **One-command instant startup** (`./labinf.sh start`) with interactive ANSI terminal menu.
* **Full multi-node topology** on subnet `10.0.2.0/24`: Alice (Server `10.0.2.10`), Bob (Client `10.0.2.20`), Chuck (Kali Attacker `10.0.2.30`).
* **Multi-arch prebuilt images** (`linux/amd64` and `linux/arm64` for Mac Apple Silicon).
* Native Linux kernel capabilities (`NET_ADMIN`, `NET_RAW`, `ip_forward=1`) for `iptables`, `nftables`, and `StrongSwan`.

---

## 📥 One-Click Solutions Download

Click the buttons below to directly download or view the comprehensive pedagogical solution documents:

| Laboratory | Topic | Lab Text | One-Click Solution Download | Shell Execution Log | Status |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Lab 00** | Introduction & Environment Setup | [📄 `lab00.pdf`](lab00/lab00.pdf) | *No exercises required* | — | ✅ Ready |
| **Lab 01** | Network Recon, Nmap, ARP Poisoning & Sniffing | [📄 `lab01.pdf`](lab01/lab01.pdf) | [**📥 Download Solution (PDF)**](lab01/lab01_solution.pdf?raw=true) | [📝 `log.txt`](lab01/log.txt) | ✅ Solved & Verified |
| **Lab 02** | Base Cryptography (OpenSSL, AES, RSA, ECC, Hash) | [📄 `lab02.pdf`](lab02/lab02.pdf) | [**📥 Download Solution (PDF)**](lab02/lab02_solution.pdf?raw=true) | [📝 `log.txt`](lab02/log.txt) | ✅ Solved & Verified |
| **Lab 03** | Applied Cryptography (MAC, HMAC, PBKDF2, PKI, CA, X.509) | [📄 `lab03.pdf`](lab03/lab03.pdf) | *Upcoming* | *Upcoming* | ⏳ Next |
| **Lab 04** | Firewalling (iptables, nftables, conntrack, NAT, DMZ) | [📄 `lab04.pdf`](lab04/lab04.pdf) | *Upcoming* | *Upcoming* | ⏳ Next |
| **Lab 05** | IPsec & Transport Layer Security (StrongSwan, TLS) | [📄 `lab05.pdf`](lab05/lab05.pdf) | *Upcoming* | *Upcoming* | ⏳ Next |

---

## 📂 Laboratory Folder Structure

Each laboratory folder adheres strictly to the following standardized layout:

```text
LABS/
├── README.md               # Master index, one-click solution downloads, environment link
├── lab00/
│   └── lab00.pdf           # Introductory laboratory text
├── lab01/
│   ├── lab01.pdf           # Official professor assignment
│   ├── lab01_solution.pdf  # Comprehensive pedagogical solution (TikZ diagrams, macOS terminal outputs)
│   └── log.txt             # Raw shell execution traces (Alice, Bob, Chuck)
├── lab02/
│   ├── lab02.pdf           # Official professor assignment
│   ├── lab02_solution.pdf  # Comprehensive pedagogical solution (AES, RSA, ECC, Hash, Brute Force)
│   └── log.txt             # Raw shell execution traces
├── lab03/
│   └── lab03.pdf           # Official professor assignment
├── lab04/
│   └── lab04.pdf           # Official professor assignment
└── lab05/
    └── lab05.pdf           # Official professor assignment
```

### Pedagogical Standards of the Solutions
Every `labxx_solution.pdf` document includes:
1. **Architectural Overview**: Kurose-Ross style native TikZ network topologies.
2. **Granular Command Deconstruction**: Every command explained in its global context, tactical rationale, syntax dissection, and macOS terminal frame.
3. **Linear Output Analysis**: Dissection of every field, flag, response code, and protocol header.
4. **Long-Term Cybersecurity Insight**: RFC standards, real-world attack vectors, defense mechanisms, and exam insights.
