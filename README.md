# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik.

### Permasalahan Bisnis
Jaya Jaya institut cenderung memiliki jumlah mahasiswa drop out yang tinggi, hal ini tentunya menjadi masalah besar untuk sebuah institusi pendidikan. Sehingga diperlukannya analisis mendalam untuk dapat mengetahui mahasiswa manakah yang cenderung akan drop out dan dilakukannya bibimngan khusus.

### Cakupan Proyek
1. Melakukan analisis pemahaman data mahasiswa
2. Melakukan training model Machine Learning untuk prediksi status mahasiswa
3. Membuat sebuah dashboard yang menyajikan faktor drop out yang tinggi
4. Membuat website prediksi status droput mahasiswa hingga deployment
### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md 

Setup environment:
Buat enviroment
```
python -m venv .env
```
Aktifkan enviroment
```
.env\Scripts\Activate
```
Install library yang diperlukan
```
pip install -r requirements.txt
```

## Business Dashboard
Pada dashborad yang telah dibuat menjelaskan faktor apa saja yang menjadi penyebab seorang mahasiswa melakukan Drop out. terdapat beberapa matriks yang menjadi dasar identifikasi baik dari segi kurikulum yang ditempuh, beasiswa yang didapat, hutang, metode saat mendaftar, usia, nilai saat masuk dan jenis kelamin.
Link : https://lookerstudio.google.com/reporting/4f939cf5-7b71-4592-a719-81e29b891038
## Menjalankan Sistem Machine Learning
⚠ Pantikan anda telah menginstall library yang dibutuhkan 
Untuk menjalakan model machine learning yang telah dibuat cukup dengan menjalankan kode dibawah ini pada terminal anda
```
streamlit run app.py
```
atau bisa akses melalui link berikut 
Link : https://proyek-akhir-ds-jevcscoh75jnrps5uvjugd.streamlit.app/
## Conclusion
Berdasarkan dashboard yang telah dibuat, dapat disimpulkan bahwa:
1. Jumlah mahasiswa yang dropout mendominasi sebanyak 32.1% dengan jumlah sebanyak 1.421 mahasiswa
2. Rata-rata nilai mahasiswa dengan status dropout pada semester 1 dan 2 cenderung lebih rendah dibandingkan dengan mahasiswa berstatus graduate, yakni 7,26 dan 5,9.
3. Jumlah mahasiswa perempuan lebih tinggi melakukan drop out dibandingkan dengan laki-laki.
4. Tidak ada perbedaan yang terlalu signifikan pada nilai previous qualification grade dan addmission grade pada tiap status mahasiswa. Namun, nilai previous qualification grade cenderung lebih tinggi dibandingkan admission grade. Di antara ketiga status, mahasiswa dropout memiliki nilai terendah pada kedua variabel tersebut.
5. Sebagian besar mahasiswa yang melakukan dropout berada pada rentang usia 18–28 tahun, dengan jumlah tertinggi pada usia 19 tahun.
6. Mayoritas mahasiswa yang dropout tidak memiliki hutang kepada institusi; hanya 31 mahasiswa yang tercatat sebagai debtors.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
1. Intervensi Dini Akademik:
Lakukan pemantauan berkala terhadap nilai mahasiswa, khususnya pada semester pertama dan kedua. Berikan program pembinaan atau mentoring bagi mahasiswa dengan performa rendah.

2. Program Bimbingan Khusus untuk Mahasiswa Baru:
Fokus pada mahasiswa usia muda (18–19 tahun) yang cenderung lebih banyak dropout dengan menyediakan orientasi akademik, konseling psikologis, dan pelatihan manajemen waktu.

3. Strategi Khusus untuk Mahasiswa Perempuan:
Mengingat dropout lebih banyak terjadi pada perempuan, pertimbangkan kebijakan dukungan seperti fleksibilitas waktu belajar, bantuan sosial, atau program pemberdayaan mahasiswa perempuan.

4. Optimalisasi Proses Seleksi Masuk:
Pertimbangkan kembali kriteria seleksi masuk agar lebih mencerminkan kesiapan akademik calon mahasiswa, misalnya dengan menyeimbangkan bobot admission grade dan previous qualification grade.

5. Penanganan Dini terhadap Mahasiswa Berpotensi Menunggak:
Meski sebagian besar dropout bukan karena hutang, tetap perlu dipastikan bahwa sistem bantuan keuangan tersedia bagi mahasiswa yang berisiko.
