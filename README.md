# Titanic Passenger Survival Prediction & Classification Analytics

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Classification-orange.svg)](https://scikit-learn.org/)
[![Domain](https://img.shields.io/badge/Domain-Disaster%20Analytics-blue.svg)](#)
[![Tests](https://img.shields.io/badge/Tests-Pytest%20Passing-brightgreen.svg)](#)

---

## 1. Pembahasan Bisnis & Konteks Analitis

Tragedi tenggelamnya kapal RMS Titanic pada tahun 1912 merupakan salah satu peristiwa paling bersejarah dalam analisis keselamatan maritim. Proyek ini membedah faktor sosio-demografis yang mempengaruhi peluang kelangsungan hidup penumpang (*Survival Rate*) menggunakan pendekatan pembelajaran mesin (*Machine Learning Classification*).

---

## 2. Struktur Repositori

```text
analysis-and-prediction-of-titanic-passenger-survival/
├── .gitignore          # Konfigurasi pengabaian cache Git
├── data/               # Dataset Titanic mentah & bersih (train.csv, test.csv, gender_submission.csv)
├── visual/             # Visualisasi eksplorasi data (EDA) 300 DPI
├── src/                # Modular Python classifier engine (TitanicSurvivalPredictor)
├── tests/              # Automated unit tests (Pytest)
├── notebook.ipynb      # Mesin pemrosesan: Feature engineering, EDA, dan pemodelan Random Forest
├── requirements.txt    # Pinned stable dependencies
└── README.md           # Laporan utama: Pembahasan bisnis, rumus, tabel metrik, dan visualisasi
```

---

## 3. Implementasi Modular & Pengujian Otomatis

Modul inferensi kelangsungan hidup tersedia di `src/titanic_engine.py`:

```python
from src.titanic_engine import TitanicSurvivalPredictor
import pandas as pd

predictor = TitanicSurvivalPredictor()
# Preprocessing dan inferensi
```

Jalankan automated test:
```bash
pytest tests/
```

---

## 4. Cara Menjalankan

1. **Pasang Dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Eksekusi Notebook**:
   ```bash
   jupyter notebook notebook.ipynb
   ```

---
*Titanic Passenger Survival Analysis & Prediction Project.*
