# Titanic Survival Prediction

Proyek machine learning ini memprediksi apakah penumpang Titanic selamat (`Survived = 1`) atau tidak selamat (`Survived = 0`) menggunakan dataset dari Kaggle.

Notebook utama ada di [notebook.ipynb](notebook.ipynb) dan hasil prediksi disimpan ke [submission.csv](submission.csv).

## Deskripsi Proyek

Tujuan proyek ini adalah membangun pipeline machine learning sederhana dan mudah dipahami pemula, mulai dari pemuatan data, eksplorasi data, preprocessing, pelatihan model, evaluasi, hingga prediksi pada data test.

## Dataset yang Digunakan

Dataset yang digunakan adalah dataset Titanic Survival Prediction dari Kaggle:

- `train.csv` — data latih dengan target `Survived`
- `test.csv` — data uji untuk menghasilkan file submission

## Tahapan Pengerjaan

1. Import library
2. Load dataset train dan test
3. Exploratory Data Analysis (EDA)
4. Data preprocessing
5. Feature selection
6. Train-test split
7. Pelatihan model machine learning
8. Evaluasi model
9. Model comparison
10. Prediksi data test dan pembuatan `submission.csv`

## Algoritma yang Digunakan

Tiga model dibandingkan dalam proyek ini:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

## Hasil Evaluasi

Hasil evaluasi pada data validasi menunjukkan:

| Model | Accuracy |
| --- | ---: |
| Decision Tree Classifier | 0.8324 |
| Random Forest Classifier | 0.8324 |
| Logistic Regression | 0.8045 |

Model terbaik pada notebook ini adalah **Decision Tree Classifier** dengan accuracy **0.8324**.

## Cara Menjalankan Proyek

1. Buka folder proyek ini di VS Code atau Jupyter Notebook.
2. Pastikan file `train.csv` dan `test.csv` berada di folder yang sama dengan `notebook.ipynb`.
3. Jalankan semua cell pada [notebook.ipynb](notebook.ipynb) secara berurutan.
4. Setelah cell prediksi dijalankan, file `submission.csv` akan dibuat otomatis.

## Output

- [notebook.ipynb](notebook.ipynb)
- [README.md](README.md)
- [submission.csv](submission.csv)
