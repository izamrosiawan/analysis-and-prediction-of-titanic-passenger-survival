# Analisis dan Prediksi Kelangsungan Hidup Penumpang Titanic

---

## 🎯 Pernyataan Masalah Bisnis
Mengembangkan protokol keselamatan dan evakuasi yang kuat memerlukan pemahaman tentang faktor demografis dan struktural yang menentukan tingkat kelangsungan hidup darurat. Proyek ini memanfaatkan log penumpang historis untuk memodelkan aturan klasifikasi guna mengidentifikasi prediktor utama keselamatan dalam keadaan darurat maritim.

---

## 📌 Ringkasan Eksekutif (30 Detik Baca)
* **Tujuan**: Membangun model klasifikasi biner menggunakan Python untuk memprediksi keselamatan penumpang Titanic (`Survived = 1` vs `0`), menganalisis faktor demografis dan sosial ekonomi utama.
* **Temuan Utama**:
  - **Faktor Jenis Kelamin**: Jenis kelamin adalah penentu keselamatan paling krusial. Tingkat keselamatan perempuan mencapai **74,20%**, sedangkan laki-laki hanya **18,89%**, mencerminkan prioritas evakuasi untuk perempuan dan anak-anak.
  - **Faktor Kelas Sosial**: Kelas tiket (Pclass) berpengaruh besar terhadap keselamatan. Penumpang Kelas 1 memiliki peluang selamat **62,96%**, Kelas 2 sebesar **47,28%**, dan Kelas 3 hanya **24,24%**.
  - **Perbandingan Akurasi Model**: Model **Decision Tree** dan **Random Forest** menghasilkan akurasi tertinggi sebesar **83,24%** dibanding **Logistic Regression** sebesar **80,45%**.
  - **Model Terbaik**: Decision Tree Classifier dipilih untuk prediksi akhir karena memiliki akurasi tertinggi (**83,24%**), metrik precision-recall yang seimbang, dan kemudahan interpretasi struktur keputusannya.
* **Rekomendasi Analisis**:
  - **Utamakan Interpretasi Fitur**: Tekankan pemahaman faktor penentu daripada sekadar skor akurasi model. Grafik *feature importance* menunjukkan Jenis Kelamin, Kelas Tiket, dan Tarif adalah prediktor utama.
  - **Pra-pemrosesan yang Kuat**: Pengisian data kosong (*missing values*) untuk Umur dan Tarif menggunakan nilai median harus dilakukan setelah split data untuk menghindari kebocoran data (*data leakage*).
  - **Rekayasa Fitur**: Buat fitur komposit baru (seperti Jumlah Keluarga = SibSp + Parch + 1) untuk menangkap dinamika kelompok, yang terbukti meningkatkan akurasi klasifikasi.

---

## 🛡️ Kualitas Data & Asumsi
* **Missing Values**: Fitur `Age` memiliki 177 data kosong (19,8% data latih) dan diimputasi dengan nilai median penumpang berdasarkan kelompok Pclass dan Sex. Fitur `Cabin` dibuang karena tingkat kekosongan yang sangat tinggi (77,1%). Data kosong pada `Embarked` (2 data) diimputasi dengan nilai modus.
* **Outlier Treatment**: Tarif tiket dengan nilai ekstrem (seperti harga tiket 512 BRL) tetap dipertahankan karena mencerminkan kabin kelas atas dan menunjukkan variansi kekayaan nyata, bukan kesalahan input data.
* **Asumsi**: Mengasumsikan kelas tiket (`Pclass`) mewakili indikator status sosial ekonomi dan menunjukkan kedekatan dek kabin dengan akses sekoci penyelamat.

---

## 📊 Metrik Evaluasi & Perbandingan Model

Semua pengklasifikasi dilatih dengan rasio 80/20 data latih-validasi dan dievaluasi pada dataset validasi:

| Model | Akurasi | Kelas | Presisi (Precision) | Recall | F1-Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Decision Tree Classifier** | **0.8324** | **0 (Tidak Selamat)**<br>**1 (Selamat)** | **0.85**<br>**0.80** | **0.88**<br>**0.75** | **0.87**<br>**0.78** |
| **Random Forest Classifier** | **0.8324** | **0 (Tidak Selamat)**<br>**1 (Selamat)** | **0.84**<br>**0.81** | **0.89**<br>**0.74** | **0.87**<br>**0.77** |
| **Logistic Regression** | **0.8045** | **0 (Tidak Selamat)**<br>**1 (Selamat)** | **0.81**<br>**0.79** | **0.89**<br>**0.67** | **0.85**<br>**0.72** |

---

## 📊 Wawasan Utama & Visualisasi

### 1. Keselamatan Berdasarkan Jenis Kelamin
Tingkat keselamatan perempuan jauh lebih tinggi (**74,20%**) dibandingkan penumpang laki-laki (**18,89%**).
![Survival Berdasarkan Sex](visual/survival_by_sex.png)

### 2. Keselamatan Berdasarkan Kelas Tiket
Penumpang Kelas 1 memiliki tingkat keselamatan tertinggi (**62,96%**), disusul Kelas 2 (**47,28%**), dan Kelas 3 (**24,24%**).
![Survival Berdasarkan Pclass](visual/survival_by_pclass.png)

### 3. Korelasi Fitur Numerik
Korelasi numerik menunjukkan korelasi terkuat terhadap keselamatan diduduki oleh tarif tiket (`Fare`) dan kelas kabin (`Pclass`).
![Heatmap Korelasi](visual/numerical_correlation.png)

### 4. Confusion Matrix Model
Menampilkan performa prediksi pada masing-masing kelas untuk model Decision Tree, Random Forest, dan Logistic Regression pada data validasi.
![Confusion Matrices](visual/confusion_matrices.png)

---

## ⚠️ Keterbatasan & Langkah Selanjutnya
* **Keterbatasan**: Analisis ini bergantung pada data historis yang kecil dan tidak memiliki variabel perilaku (seperti kebugaran fisik, kondisi mental darurat, atau kerja sama tim penumpang) yang secara riil memengaruhi evakuasi.
* **Langkah Selanjutnya**:
  1. Terapkan teknik ansambel (XGBoost/LightGBM) untuk menguji batasan performa model.
  2. Gunakan visualisasi SHAP (SHapley Additive exPlanations) untuk menerangkan kontribusi fitur pada setiap individu.

---

## 🔄 Reproduksibilitas
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
