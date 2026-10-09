# 💻 Computer Engineering Academic Repository — Politecnico di Torino

[![LaTeX](https://img.shields.io/badge/LaTeX-Typeset-008080?style=flat&logo=latex&logoColor=white)](https://www.latex-project.org/)
[![University](https://img.shields.io/badge/University-Politecnico%20di%20Torino-002D62?style=flat&logo=academia&logoColor=white)](https://www.polito.it/)
[![Degree](https://img.shields.io/badge/Master's%20Degree-Computer%20Engineering%20(LM--32)-FF8C00?style=flat)](https://didattica.polito.it/)
[![Build and Release](https://github.com/Beccaceci/COMPUTER-ENGINEERING/actions/workflows/build-and-release.yml/badge.svg)](https://github.com/Beccaceci/COMPUTER-ENGINEERING/actions/workflows/build-and-release.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Personal study notes, LaTeX lecture guides, exam resolutions with step-by-step mathematical derivations, laboratory implementations, and embedded firmware for the **Master of Science in Computer Engineering (LM-32)** at **Politecnico di Torino**.

---

## 💡 Why This Repository Exists

> ### *"Knowledge belongs to everyone, not just those who can afford it."*

The core motivation behind this project is the unwavering conviction that **education, research-grade study materials, and rigorous code implementations should be free, open-source, and accessible to everyone without barriers**.

In light of this:
- **Selling notes and exam solutions is unacceptable.** No student should ever have to pay for class notes, summaries, or exam preparation material created by fellow peers.
- **Equal opportunities in higher education.** Every student, regardless of background or financial means, deserves direct access to clean, mathematically rigorous, and carefully typeset materials to prepare for their exams.

This repository embodies this commitment: providing university-level Computer Engineering knowledge that anyone can clone, study, and build upon for free.

---

## 🏛️ Building a Complete Academic Computer Engineering Archive

This repository organizes courses following the official **Computer Engineering (Ingegneria Informatica)** curriculum at **Politecnico di Torino**:

> **The Vision:** To establish a unified, open-source, centralized archive covering the fundamental and advanced pillars of the Master of Science curriculum: from low-level architectures and operating system internals to machine learning foundations and modern generative AI.

Community contributions are warmly welcomed:
- **Share your notes & solutions:** If you have complete notes, summaries, cheatsheets, or solved exams for additional courses, feel free to contribute!
- **Spread the word:** Share this repository with fellow engineering students to expand access to high-quality academic resources.

---

## 🛠️ Feedback, Improvements & Contributions

Continuous refinement ensures these materials remain accurate and useful:
- **Open an Issue:** Found a typo, missing proof step, unclear diagram, or bug? Submit a report via [GitHub Issues](https://github.com/Beccaceci/COMPUTER-ENGINEERING/issues).
- **Submit a Pull Request:** Want to correct a typo or expand a chapter in LaTeX/code? Fork the repository and open a [Pull Request](https://github.com/Beccaceci/COMPUTER-ENGINEERING/pulls).
- **Star the Repository:** If these materials aid your studies, starring the repository helps other engineering students discover it.

---

## 📥 Direct 1-Click Downloads

### 📦 Download Complete Course Bundle (All Study Guides in 1-Click)
[![Download All Notes ZIP](https://img.shields.io/badge/Download_All_Study_Guides-Complete_ZIP_Bundle-1e293b?style=for-the-badge&logo=zip&logoColor=white)](https://github.com/Beccaceci/COMPUTER-ENGINEERING/archive/refs/heads/main.zip)

---

### 📄 Direct Course Guides & Practical Deliverables

#### 1️⃣ First Year

| Period | Course | Course Guide | Direct Download / Core Artifacts |
| :--- | :--- | :--- | ---: |
| **Semester 1 (Fall)** | **Computer Architectures** (`02GOLOV` / `02LSEOV`) | [Open Guide](courses/first_year/first_semester/COMPUTER_ARCHITECTURES/README.md) | [![Download Firmware Code](https://img.shields.io/badge/Download-LPC1768_Tetris_Firmware-0052cc?style=for-the-badge&logo=c&logoColor=white)](courses/first_year/first_semester/COMPUTER_ARCHITECTURES/Source/) |
| **Semester 2 (Spring)** | **Machine Learning** (`01URWOV` / `01URWYG`) | [Open Guide](courses/first_year/second_semester/MACHINE_LEARNING/README.md) | [![Download ML Labs](https://img.shields.io/badge/Download-ML_Labs_01--10-2e7d32?style=for-the-badge&logo=python&logoColor=white)](courses/first_year/second_semester/MACHINE_LEARNING/) |
| **Semester 2 (Spring)** | **System Programming (PDS)** (`02GRSOV` / `01NYHOV`) | [Open Guide](courses/first_year/second_semester/SYSTEM_PROGRAMMING/README.md) | [![Download Rust & OS Guide](https://img.shields.io/badge/Download-PDS_Study_Guide.pdf-d32f2f?style=for-the-badge&logo=rust&logoColor=white)](courses/first_year/second_semester/SYSTEM_PROGRAMMING/API%20PROGRAMMING/STUDY_GUIDE/) |

#### 2️⃣ Second Year

| Period | Course | Course Guide | Direct Download / Core Artifacts |
| :--- | :--- | :--- | ---: |
| **Semester 1 (Fall)** | **Large Language Models for Software Engineering (LLM4SE)** | [Open Guide](courses/second_year/first_semester/LLM_FOR_SOFTWARE_ENGINEERING/README.md) | [![Download Theory Guide](https://img.shields.io/badge/Download-LLM4SE_Theory.pdf-7b1fa2?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](courses/second_year/first_semester/LLM_FOR_SOFTWARE_ENGINEERING/STUDY_GUIDE/lectures/main.pdf) [![Download Lab Guide](https://img.shields.io/badge/Download-LLM4SE_Labs.pdf-e65100?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](courses/second_year/first_semester/LLM_FOR_SOFTWARE_ENGINEERING/STUDY_GUIDE/laboratories/labs.pdf) |

---

## 📂 Repository Architecture

The repository adheres to a standardized academic hierarchy:

```text
COMPUTER-ENGINEERING/
├── .github/
│   └── workflows/
│       └── build-and-release.yml                    # Automated LaTeX CI/CD & release generator
├── courses/
│   ├── first_year/
│   │   ├── first_semester/
│   │   │   └── COMPUTER_ARCHITECTURES/              # NXP LPC1768 ARM Cortex-M3 Project (Tetris, Timers, DAC/ADC)
│   │   │       ├── README.md                        # Hardware peripherals, register specs & Keil build guide
│   │   │       └── Source/                          # C firmware, drivers, assembly startup, and project files
│   │   └── second_semester/
│   │       ├── MACHINE_LEARNING/                    # Statistical Pattern Recognition & ML Labs (2025/2026)
│   │       │   ├── README.md                        # Mathematical derivations, syllabus & lab overview
│   │       │   ├── LAB01 - PYTHON NUMERICAL LIBS/
│   │       │   ├── LAB02 - IRIS DATASET/
│   │       │   ├── LAB03 - DIMENSIONALITY REDUCTION/
│   │       │   ├── LAB04 - PROBABILITY AND DENSITY ESTIMATION/
│   │       │   ├── LAB05 - GENERATIVE GAUSSIAN MODELS/
│   │       │   ├── LAB06 - BAYES RISK AND MODEL EVALUATION/
│   │       │   ├── LAB07 - LOGISTIC REGRESSION/
│   │       │   ├── LAB08 - SUPPORT VECTOR MACHINES/
│   │       │   ├── LAB09 - GMM/
│   │       │   └── LAB10 - CALIBRATION FUSION/
│   │       └── SYSTEM_PROGRAMMING/                  # System & Device Programming (PDS)
│   │           ├── README.md                        # Master guide covering API Programming & OS Internals
│   │           ├── API PROGRAMMING/                 # Safe Rust, Tokio, Georuggine project & 55 simulations
│   │           │   ├── STUDY_GUIDE/                 # LaTeX Study Guide (Memory, Concurrency, Async, FFI)
│   │           │   ├── EXAMS/                       # Past exam resolutions & test suites
│   │           │   └── SIMULATIONS/                 # 55 trait-driven concurrent exam simulations
│   │           └── OS INTERNALS/                    # Operating Systems Kernel internals & OS161
│   │               ├── EXAMS/                       # Solved OS Internals past exam papers
│   │               └── LABS/                        # Synchronization and kernel lab guides
│   └── second_year/
│       └── first_semester/
│           └── LLM_FOR_SOFTWARE_ENGINEERING/        # LLMs for Software Engineering (LLM4SE)
│               ├── README.md                        # Course overview, exam resolutions table & lecture index
│               ├── STUDY_GUIDE/                     # Publication-grade LaTeX Volumes (Theory & Labs)
│               │   ├── lectures/                    # Volume I: Foundations to Modern Transformers (96 pages)
│               │   └── laboratories/                # Volume II: PyTorch Autograd & Deep Learning (27 pages)
│               └── EXAMS/                           # 8 Official exam sessions (2025–2026) step-by-step solved
├── .gitignore
├── LICENSE                                          # MIT License
└── README.md                                        # Master repository hub
```

---

## 📄 License

All code implementations, LaTeX guides, and study materials are distributed for academic study, research, and non-commercial educational use under the [MIT License](LICENSE).
