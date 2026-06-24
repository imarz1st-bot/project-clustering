# CLUSTERISASI PARTITIONING METHODS (K-MEANS DAN K-MEDOIDS)

## 1. Pendahuluan

Clustering merupakan salah satu teknik *unsupervised learning* yang digunakan untuk mengelompokkan data berdasarkan tingkat kemiripannya. Data yang memiliki karakteristik serupa akan ditempatkan dalam satu kelompok (*cluster*), sedangkan data yang berbeda akan berada pada cluster yang berbeda. Tujuan utama clustering adalah menghasilkan kelompok yang homogen di dalam cluster dan heterogen antar cluster.

Clustering banyak diterapkan dalam berbagai bidang, seperti pemasaran, perbankan, asuransi, serta pengelompokan berita dan sistem rekomendasi.

## 2. Jenis-Jenis Metode Clustering

Metode clustering secara umum dibagi menjadi tiga kelompok, yaitu:

1. **Partition-Based Clustering**

   * K-Means
   * K-Medoids
   * K-Medians
   * Fuzzy C-Means

2. **Hierarchical Clustering**

   * Agglomerative
   * Divisive

3. **Density-Based Clustering**

   * DBSCAN

## 3. Metode K-Means

K-Means adalah metode clustering yang membagi data ke dalam sejumlah cluster (K) yang telah ditentukan sebelumnya. Setiap data hanya dapat menjadi anggota satu cluster.

Karakteristik utama K-Means meliputi:

* Membagi data menjadi beberapa cluster yang tidak saling tumpang tindih.
* Meminimalkan jarak antara data dengan pusat cluster (centroid).
* Menghasilkan cluster yang homogen.

### Algoritma K-Means

Langkah-langkah K-Means adalah sebagai berikut:

1. Menentukan jumlah cluster (K).
2. Memilih centroid awal.
3. Menghitung jarak setiap data terhadap centroid.
4. Mengelompokkan data ke cluster dengan jarak terdekat.
5. Menghitung centroid baru berdasarkan rata-rata anggota cluster.
6. Mengulangi proses hingga posisi centroid tidak berubah lagi.

### Contoh Klasterisasi Pelanggan

Pada data pelanggan yang terdiri dari atribut umur (*Age*) dan pendapatan (*Income*), digunakan K = 2 dengan centroid awal:

* C1 = (41,19)
* C2 = (47,100)

Melalui beberapa iterasi, anggota cluster berubah hingga posisi centroid menjadi stabil. Proses berhenti pada iterasi keempat karena tidak terjadi perubahan centroid. Hal ini menunjukkan bahwa proses clustering telah konvergen.

## 4. Metode K-Medoids (PAM)

K-Medoids atau *Partitioning Around Medoids (PAM)* merupakan pengembangan dari K-Means. Perbedaan utama antara keduanya terletak pada pusat cluster yang digunakan.

* **K-Means** menggunakan centroid (nilai rata-rata).
* **K-Medoids** menggunakan medoid, yaitu salah satu data asli yang memiliki total jarak minimum terhadap data lain dalam cluster.

Karena menggunakan data aktual sebagai pusat cluster, K-Medoids lebih tahan terhadap pengaruh data ekstrem (*outlier*).

### Algoritma K-Medoids

Tahapan K-Medoids meliputi:

1. Menentukan jumlah cluster.
2. Memilih medoid awal.
3. Menghitung jarak antar data.
4. Membentuk cluster.
5. Menghitung nilai biaya (*cost*).
6. Menukar medoid dengan objek lain (*swap*).
7. Memilih medoid baru jika menghasilkan cost yang lebih kecil.
8. Mengulangi proses hingga tidak terjadi pertukaran medoid.

## 5. Pengaruh Outlier

Pada K-Means, keberadaan data ekstrem dapat menggeser posisi centroid karena pusat cluster dihitung berdasarkan rata-rata. Akibatnya, hasil clustering dapat menjadi kurang representatif.

Sebaliknya, K-Medoids memilih pusat cluster dari data aktual sehingga pengaruh outlier lebih kecil dan hasil cluster menjadi lebih stabil.

## 6. Perbandingan K-Means dan K-Medoids

| Karakteristik                 | K-Means  | K-Medoids               |
| ----------------------------- | -------- | ----------------------- |
| Pusat Cluster                 | Centroid | Medoid                  |
| Sensitivitas terhadap Outlier | Tinggi   | Lebih rendah            |
| Kecepatan Proses              | Cepat    | Lebih lambat            |
| Jenis Data                    | Numerik  | Numerik dan kategorikal |
| Interpretasi                  | Sedang   | Lebih mudah             |
| Kompleksitas                  | Rendah   | Lebih tinggi            |

## 7. Penggunaan K-Medoids

K-Medoids lebih cocok digunakan ketika:

* Dataset mengandung banyak outlier.
* Pusat cluster harus berupa data aktual.
* Dibutuhkan hasil clustering yang lebih stabil.
* Data yang digunakan berupa data numerik maupun kategorikal.

## 8. Kesimpulan

Clustering merupakan teknik pengelompokan data yang bertujuan menghasilkan kelompok dengan tingkat kemiripan tinggi di dalam cluster dan perbedaan yang jelas antar cluster. K-Means merupakan metode clustering yang cepat dan sederhana dengan menggunakan centroid sebagai pusat cluster, namun sensitif terhadap outlier. Sementara itu, K-Medoids menggunakan medoid sebagai pusat cluster sehingga lebih tahan terhadap data ekstrem dan menghasilkan cluster yang lebih stabil. Pemilihan metode yang digunakan bergantung pada karakteristik data dan kebutuhan analisis.
