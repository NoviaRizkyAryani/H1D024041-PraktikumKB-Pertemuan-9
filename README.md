## Algoritma Genetika 1 - Praktikum KB Pertemuan 9

Proyek ini merupakan implementasi **Algoritma Genetika (AG)** untuk menyelesaikan **Knapsack Problem** (masalah pemilihan barang). Algoritma Genetika adalah metode pencarian dan optimasi berbasis populasi yang terinspirasi oleh proses evolusi biologis.

Program ini menggunakan operasi-operasi genetik seperti:
- **Seleksi (Selection)** - memilih individu terbaik
- **Penyilangan/Crossover** - menggabungkan dua parent
- **Mutasi (Mutation)** - mengubah individu untuk diversitas

untuk menemukan kombinasi barang terbaik yang memaksimalkan nilai tanpa melebihi kapasitas tas.

---

### Algoritma Genetika

Algoritma Genetika adalah teknik pencarian dan optimasi yang meniru proses evolusi alami. Konsep ini dikembangkan oleh **John Holland** pada tahun 1960-an.

**Langkah-langkah utama:**

1. **Inisialisasi** - Membuat populasi awal secara acak
2. **Evaluasi** - Menghitung fitness setiap individu
3. **Seleksi** - Memilih individu terbaik untuk reproduksi
4. **Crossover** - Menggabungkan dua parent untuk membuat offspring
5. **Mutasi** - Mengubah offspring untuk menjaga diversitas
6. **Pengulangan** - Ulangi langkah 2-5 sampai konvergen

### Knapsack Problem

Knapsack Problem adalah masalah optimasi klasik di mana kita harus memilih sejumlah barang dengan bobot dan nilai tertentu untuk dimasukkan ke dalam tas dengan kapasitas terbatas, dengan tujuan memaksimalkan total nilai tanpa melebihi kapasitas.

**Formulasi:**
- Maksimalkan: Σ(nilai_i × x_i)
- Batasan: Σ(bobot_i × x_i) ≤ kapasitas_tas
- x_i ∈ {0, 1} (barang dipilih atau tidak)

---

## Fitur Implementasi

### Metode Seleksi (2 jenis)

**1. Roulette Wheel Selection**
- Memilih individu berdasarkan probabilitas proporsional dengan fitness
- Individu dengan fitness tinggi memiliki peluang lebih besar dipilih

**2. Tournament Selection**
- Memilih k individu secara acak dan memilih yang terbaik
- Memberikan tekanan seleksi yang dapat dikontrol

### Metode Crossover (3 jenis)

**1. One-Point Crossover**
- Memotong kromosom di satu titik
- Menukar bagian setelah titik potong

**2. Two-Point Crossover**
- Memotong kromosom di dua titik
- Menukar segmen di antara kedua titik

**3. Uniform Crossover**
- Setiap gen dipilih secara acak dari salah satu parent
- Menggunakan mask untuk menentukan sumber gen

### Metode Mutasi (3 jenis)

**1. Swap Mutation**
- Menukar posisi dua gen dalam kromosom

**2. Inversion Mutation**
- Membalik urutan gen dalam segmen tertentu

**3. Uniform Mutation**
- Mengubah nilai gen dengan probabilitas tertentu

### Visualisasi

- **Grafik Perkembangan Fitness** menampilkan:
  - Fitness tertinggi (garis biru) - solusi terbaik setiap generasi
  - Fitness rata-rata (garis merah) - kualitas populasi rata-rata
  - Fitness terendah (garis kuning) - solusi terburuk setiap generasi
  - Scatter plot (titik abu-abu) - semua individu dalam populasi

---

## Instalasi

### Prasyarat
- Python 3.7 atau lebih tinggi
- pip (Python Package Manager)

### Langkah Instalasi

```bash
# Clone atau download repository
git clone https://github.com/NoviaRizkyAryani/H1D024041-PraktikumKB-Pertemuan-9.git
cd H1D024041-PraktikumKB-Pertemuan-9

# Install dependencies
pip install matplotlib numpy
```

---

## Cara Penggunaan

### Menjalankan Program Utama

```bash
python main.py
```

Program akan:
1. Membuat populasi awal secara acak
2. Mengevaluasi fitness setiap individu
3. Melakukan seleksi, crossover, dan mutasi selama 50 generasi
4. Menampilkan grafik perkembangan fitness
5. Menampilkan hasil optimasi terbaik

### Menjalankan Module Individual

**Inisialisasi Populasi:**
```bash
python InisiasiPopulasi.py
```

**Evaluasi Fitness:**
```bash
python EvaluasiFitness.py
```

**Seleksi:**
```bash
python selection.py
```

**Crossover:**
```bash
python crossover.py
```

**Mutasi:**
```bash
python mutation.py
```

### Mengubah Parameter

Edit file `main.py` bagian bawah:

```python
run_ga(
    jumlah_generasi=50,      # Ubah jumlah generasi
    jumlah_populasi=20,      # Ubah ukuran populasi
    prob_crossover=0.8,      # Ubah probabilitas crossover
    prob_mutasi=0.1,         # Ubah probabilitas mutasi
    kapasitas_tas=50         # Ubah kapasitas tas
)
```

---

## Struktur File

```
H1D024041-PraktikumKB-Pertemuan-9/
├── main.py                 # Program utama (jalankan ini)
├── InisiasiPopulasi.py     # Inisialisasi populasi awal
├── EvaluasiFitness.py      # Evaluasi fitness kromosom
├── selection.py            # Metode seleksi (Roulette Wheel & Tournament)
├── crossover.py            # Metode crossover (One-Point, Two-Point, Uniform)
├── mutation.py             # Metode mutasi (Swap, Inversion, Uniform)
├── .gitignore              # File yang diabaikan Git
├── __pycache__/            # Cache Python (otomatis dibuat)
└── README.md               # Dokumentasi ini
```

---

## Output Program
### Grafik Perkembangan Fitness

Ketika program dijalankan, akan menampilkan grafik dengan:
- **Garis Biru**: Fitness tertinggi - menunjukkan solusi terbaik yang ditemukan
- **Garis Merah**: Fitness rata-rata - menunjukkan kualitas populasi secara umum
- **Garis Kuning**: Fitness terendah - menunjukkan solusi terburuk
- **Titik Abu-abu**: Semua individu dalam populasi - menunjukkan diversitas

### Output Terminal

```
==================================================
HASIL OPTIMASI KNAPSACK DENGAN ALGORITMA GENETIKA
==================================================
Nilai Fitness Terbaik: 329
Total Bobot: 50
Kapasitas Tas: 50
Barang Terpilih:
- Barang2
- Barang5
- Barang6
- Barang8
==================================================
```

---

## Penjelasan Hasil

### Data Barang (Default)

| No | Nama | Nilai | Bobot |
|----|------|-------|-------|
| 1  | Barang1 | 60  | 10 |
| 2  | Barang2 | 100 | 20 |
| 3  | Barang3 | 120 | 30 |
| 4  | Barang4 | 90  | 25 |
| 5  | Barang5 | 69  | 11 |
| 6  | Barang6 | 70  | 9  |
| 7  | Barang7 | 80  | 15 |
| 8  | Barang8 | 90  | 10 |
| 9  | Barang9 | 25  | 3  |

**Kapasitas Tas:** 50 kg

### Interpretasi Hasil

**Nilai Fitness Terbaik: 329**
- Ini adalah total nilai barang yang dipilih
- Berarti kombinasi barang menghasilkan nilai maksimal 329

**Total Bobot: 50**
- Total bobot barang yang dipilih
- Sama dengan kapasitas tas (menggunakan kapasitas penuh)

**Barang Terpilih: Barang2, Barang5, Barang6, Barang8**
- Barang2: nilai 100, bobot 20
- Barang5: nilai 69, bobot 11
- Barang6: nilai 70, bobot 9
- Barang8: nilai 90, bobot 10
- Total: nilai 329, bobot 50

---

## Catatan Penting
### Hasil Berbeda Setiap Kali Jalankan

Nilai hasil bisa berbeda setiap kali menjalankan program karena:
- Populasi awal dibuat secara acak
- Seleksi parent bersifat probabilistik
- Crossover dan mutasi memiliki elemen keacakan

Ini adalah **sifat normal Algoritma Genetika** yang memungkinkan eksplorasi ruang solusi yang luas.

### Grafik Tidak Selalu Monoton Naik

Fitness tertinggi (garis biru) mungkin tidak selalu naik karena:
- Populasi dapat kehilangan best solution melalui proses seleksi dan crossover
- Mutasi dapat menghasilkan solusi yang lebih buruk
- Ini adalah trade-off antara eksplorasi dan eksploitasi

### Cara Meningkatkan Hasil

1. **Tingkatkan jumlah generasi** - lebih banyak iterasi, lebih baik
2. **Tingkatkan jumlah populasi** - lebih banyak kandidat, lebih baik
3. **Sesuaikan probabilitas crossover dan mutasi** - eksperimen dengan nilai
4. **Jalankan berkali-kali** - ambil hasil terbaik dari beberapa run

---
## 📚 Referensi

- Holland, J. H. (1975). "Adaptation in Natural and Artificial Systems"
- [Wikipedia - Genetic Algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm)
- [Wikipedia - Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem)

---

**Terakhir diperbarui:** 26 Mei 2026  
**Status:** ✅ Selesai dan Teruji
