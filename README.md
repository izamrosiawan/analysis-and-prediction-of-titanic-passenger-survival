# Titanic Passenger Survival Prediction

[English](#english) | [Bahasa Indonesia](#bahasa-indonesia)

---

<a name="english"></a>
## 🇬🇧 English Version

### 🎯 Business Problem Statement
Developing robust safety and evacuation protocols requires understanding the demographic and structural factors that determine emergency survival rates. This project leverages historical passenger logs to model classification rules that identify key predictors of survival in maritime emergencies.

---

### 📌 Executive Summary (30-Second Read)
* **Objective**: Built binary classification models using Python to predict passenger survival (`Survived = 1` vs `0`) on the Titanic, analyzing key demographic and socioeconomic determinants.
* **Key Findings**:
  - **Gender Determinant**: Gender is the most critical survival factor. The female survival rate is **74.20%**, whereas the male survival rate is only **18.89%**, reflecting the "women and children first" evacuation policy.
  - **Socioeconomic Influence**: Passenger class (Pclass) is highly correlated with survival. Pclass 1 (First Class) has the highest survival rate at **62.96%**, followed by Pclass 2 at **47.28%**, and Pclass 3 (Third Class) at **24.24%**.
  - **Model Performance**: Both **Decision Tree** and **Random Forest** achieved a validation accuracy of **83.24%**, outperforming **Logistic Regression** at **80.45%**.
  - **Best Model Selection**: The Decision Tree Classifier was selected for final submission due to its high validation accuracy (**83.24%**), balanced precision-recall metrics, and direct interpretability of decision paths.
* **Actionable Recommendations**:
  - **Focus on Feature Interpretability**: Prioritize model interpretability over pure accuracy. Feature importance plots show that Sex, Pclass, and Fare are the top predictors, making demographic stratification critical in historical survival modeling.
  - **Robust Preprocessing**: Missing value imputation (e.g., median for Age and Fare, mode for Embarked) should be executed carefully with stratified splits to prevent data leakage.
  - **Feature Engineering**: Create composite features (such as Family Size = SibSp + Parch + 1) to capture household dynamics, which can improve predictive accuracy.

---

### 🛡️ Data Quality & Assumptions
* **Missing Values**: The `Age` feature had 177 missing values (19.8% of the training dataset), which were imputed using the median of passengers grouped by Pclass and Sex. The `Cabin` feature was dropped entirely due to a high missingness rate (77.1%). The `Embarked` feature (2 missing rows) was imputed using the mode.
* **Outlier Treatment**: High fares (e.g., ticket price of 512 BRL) were kept in the dataset since they represent genuine wealth variation of first-class passengers rather than data errors.
* **Assumptions**: We assume that ticket class (`Pclass`) is a reliable proxy for socioeconomic status and indicates proximity of cabin decks to lifeboat access.

---

### 📊 Model Evaluation & Comparison Metrics

All classifiers were trained on an 80/20 train-validation split and evaluated on the validation dataset:

| Model | Accuracy | Class | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Decision Tree Classifier** | **0.8324** | **0 (Not Survived)**<br>**1 (Survived)** | **0.85**<br>**0.80** | **0.88**<br>**0.75** | **0.87**<br>**0.78** |
| **Random Forest Classifier** | **0.8324** | **0 (Not Survived)**<br>**1 (Survived)** | **0.84**<br>**0.81** | **0.89**<br>**0.74** | **0.87**<br>**0.77** |
| **Logistic Regression** | **0.8045** | **0 (Not Survived)**<br>**1 (Survived)** | **0.81**<br>**0.79** | **0.89**<br>**0.67** | **0.85**<br>**0.72** |

---

### 📊 Key Insights & Visualizations

#### 1. Survival Rate by Gender
Female passengers had a significantly higher chance of survival (**74.20%**) compared to male passengers (**18.89%**).
![Survival by Sex](visual/survival_by_sex.png)

#### 2. Survival Rate by Ticket Class
Socioeconomic class had a strong impact on survival. First-class passengers achieved a **62.96%** survival rate, while third-class passengers had only **24.24%** survival rate.
![Survival by Pclass](visual/survival_by_pclass.png)

#### 3. Correlation Matrix of Numerical Features
Correlation analysis shows that ticket class (`Pclass`) and fare price (`Fare`) are strongly related to passenger survival.
![Numerical Correlations](visual/numerical_correlation.png)

#### 4. Model Confusion Matrices
The confusion matrices display the true positive/negative counts for the three evaluated classifiers on the validation set.
![Confusion Matrices](visual/confusion_matrices.png)

---

### ⚠️ Limitations & Next Steps
* **Limitations**: The analysis relies on a relatively small historical dataset and does not contain behavioral features (such as passenger physical fitness, psychological reactions, or group cooperation) that could influence evacuation success.
* **Next Steps**:
  1. Apply ensemble gradient boosting models (XGBoost, LightGBM) to improve model boundaries.
  2. Implement SHAP (SHapley Additive exPlanations) to explain feature contributions for individual passengers.

---

### 🔄 Reproducibility
* **Environment**: Python 3.11.x (libraries: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn).
* **Execution Sequence**:
  1. Store the dataset CSV files inside the `data/` directory.
  2. Open and run all cells in [notebook.ipynb](notebook.ipynb) in sequential order.
* **Random Seeds**: The seed `random_state = 42` is set globally for model initializations and train-test splits to guarantee reproducible classification boundaries.

---

<a name="bahasa-indonesia"></a>
## 🇮🇩 Versi Bahasa Indonesia

### 🎯 Business Problem Statement
Mengembangkan protokol keselamatan dan evakuasi yang kuat memerlukan pemahaman tentang faktor demografis dan struktural yang menentukan tingkat kelangsungan hidup darurat. Proyek ini memanfaatkan log penumpang historis untuk memodelkan aturan klasifikasi guna mengidentifikasi prediktor utama keselamatan dalam keadaan darurat maritim.

---

### 📌 Ringkasan Eksekutif (30 Detik Baca)
* **Tujuan**: Membangun model klasifikasi biner menggunakan Python untuk memprediksi keselamatan penumpang Titanic (`Survived = 1` vs `0`), menganalisis faktor demografis dan sosial ekonomi utama.
* **Temuan Utama**:
  - **Faktor Jenis Kelamin**: Jenis kelamin adalah penentu keselamatan paling krusial. Tingkat keselamatan perempuan mencapai **74,20%**, sedangkan laki-laki hanya **18,89%**, mencerminkan prioritas evakuasi untuk perempuan dan anak-anak.
  - **Faktor Kelas Sosial**: Kelas tiket (Pclass) berpengaruh besar terhadap keselamatan. Penumpang Kelas 1 memiliki peluang selamat **62,96%**, Kelas 2 sebesar **47,28%**, dan Kelas 3 hanya **24,24%**.
  - **Perbandingan Akurasi Model**: Model **Decision Tree** dan **Random Forest** menghasilkan akurasi tetinggi sebesar **83,24%** dibanding **Logistic Regression** sebesar **80,45%**.
  - **Model Terbaik**: Decision Tree Classifier dipilih untuk prediksi akhir karena memiliki akurasi tertinggi (**83,24%**), metrik precision-recall yang seimbang, dan kemudahan interpretasi struktur keputusannya.
* **Rekomendasi Analisis**:
  - **Utamakan Interpretasi Fitur**: Tekankan pemahaman faktor penentu daripada sekadar skor akurasi model. Grafik *feature importance* menunjukkan Jenis Kelamin, Kelas Tiket, dan Tarif adalah prediktor utama.
  - **Pra-pemrosesan yang Kuat**: Pengisian data kosong (*missing values*) untuk Umur dan Tarif menggunakan nilai median harus dilakukan setelah split data untuk menghindari kebocoran data (*data leakage*).
  - **Rekayasa Fitur**: Buat fitur komposit baru (seperti Jumlah Keluarga = SibSp + Parch + 1) untuk menangkap dinamika kelompok, yang terbukti meningkatkan akurasi klasifikasi.

---

### 🛡️ Kualitas Data & Asumsi
* **Missing Values**: Fitur `Age` memiliki 177 data kosong (19,8% data latih) dan diimputasi dengan nilai median penumpang berdasarkan kelompok Pclass dan Sex. Fitur `Cabin` dibuang karena tingkat kekosongan yang sangat tinggi (77,1%). Data kosong pada `Embarked` (2 data) diimputasi dengan nilai modus.
* **Outlier Treatment**: Tarif tiket dengan nilai ekstrem (seperti harga tiket 512 BRL) tetap dipertahankan karena mencerminkan kabin kelas atas dan menunjukkan variansi kekayaan nyata, bukan kesalahan input data.
* **Asumsi**: Mengasumsikan kelas tiket (`Pclass`) mewakili indikator status sosial ekonomi dan menunjukkan kedekatan dek kabin dengan akses sekoci penyelamat.

---

### 📊 Metrik Evaluasi & Perbandingan Model

Semua pengklasifikasi dilatih dengan rasio 80/20 data latih-validasi dan dievaluasi pada dataset validasi:

| Model | Akurasi | Kelas | Presisi (Precision) | Recall | F1-Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Decision Tree Classifier** | **0.8324** | **0 (Tidak Selamat)**<br>**1 (Selamat)** | **0.85**<br>**0.80** | **0.88**<br>**0.75** | **0.87**<br>**0.78** |
| **Random Forest Classifier** | **0.8324** | **0 (Tidak Selamat)**<br>**1 (Selamat)** | **0.84**<br>**0.81** | **0.89**<br>**0.74** | **0.87**<br>**0.77** |
| **Logistic Regression** | **0.8045** | **0 (Tidak Selamat)**<br>**1 (Selamat)** | **0.81**<br>**0.79** | **0.89**<br>**0.67** | **0.85**<br>**0.72** |

---

### 📊 Wawasan Utama & Visualisasi

#### 1. Keselamatan Berdasarkan Jenis Kelamin
Tingkat keselamatan perempuan jauh lebih tinggi (**74,20%**) dibandingkan penumpang laki-laki (**18,89%**).
![Survival Berdasarkan Sex](visual/survival_by_sex.png)

#### 2. Keselamatan Berdasarkan Kelas Tiket
Penumpang Kelas 1 memiliki tingkat keselamatan tertinggi (**62,96%**), disusul Kelas 2 (**47,28%**), dan Kelas 3 (**24,24%**).
![Survival Berdasarkan Pclass](visual/survival_by_pclass.png)

#### 3. Korelasi Fitur Numerik
Korelasi numerik menunjukkan korelasi terkuat terhadap keselamatan diduduki oleh tarif tiket (`Fare`) dan kelas kabin (`Pclass`).
![Heatmap Korelasi](visual/numerical_correlation.png)

#### 4. Confusion Matrix Model
Menampilkan performa prediksi pada masing-masing kelas untuk model Decision Tree, Random Forest, dan Logistic Regression pada data validasi.
![Confusion Matrices](visual/confusion_matrices.png)

---

### ⚠️ Keterbatasan & Langkah Selanjutnya
* **Keterbatasan**: Analisis ini bergantung pada data historis yang kecil dan tidak memiliki variabel perilaku (seperti kebugaran fisik, kondisi mental darurat, atau kerja sama tim penumpang) yang secara riil memengaruhi evakuasi.
* **Langkah Selanjutnya**:
  1. Terapkan teknik ansambel (XGBoost/LightGBM) untuk menguji batasan performa model.
  2. Gunakan visualisasi SHAP (SHapley Additive exPlanations) untuk menerangkan kontribusi fitur pada setiap individu.

---

### 🔄 Reproduksibilitas
* **Lingkungan**: Python 3.11.x (pustaka: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn).
* **Urutan Eksekusi**:
  1. Simpan berkas data CSV di dalam direktori `data/`.
  2. Jalankan sel data prep dan rekayasa fitur di [notebook.ipynb](notebook.ipynb) secara berurutan.
* **Random Seeds**: Nilai seed `random_state = 42` disematkan pada seluruh split data dan pemodelan klasifikasi demi hasil evaluasi yang konsisten.

---

## 🗄️ Struktur Folder Proyek
* **`data/`**: Berisi file dataset CSV (`train.csv`, `test.csv`, `gender_submission.csv`).
* **`visual/`**: Menyimpan semua visualisasi grafik hasil analisis data (EDA) dan matriks evaluasi model.
* **`notebook.ipynb`**: File Jupyter Notebook utama untuk analisis dan pemodelan.
* **`submission.csv`**: Hasil prediksi model terbaik pada data uji.
