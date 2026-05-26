# Data barang: (nama, harga, bobot)
barang = [
    ("Barang1", 60, 10),
    ("Barang2", 100, 20),
    ("Barang3", 120, 30),
    ("Barang4", 90, 25),
    ("Barang5", 70, 15)
]

kapasitas_tas = 50  # Kapasitas maksimum tas


# Fungsi untuk menghitung nilai fitness
def hitung_fitness(kromosom, barang, kapasitas_tas):
    """
    Menghitung nilai fitness untuk sebuah kromosom dalam Knapsack Problem.
    
    Args:
        kromosom (list): List berisi 0 dan 1 yang merepresentasikan pilihan barang
        barang (list): List tuple berisi (nama, harga, bobot) setiap barang
        kapasitas_tas (int): Kapasitas maksimum tas
    
    Returns:
        int: Nilai fitness (total harga jika valid, 0 jika melebihi kapasitas)
    """
    total_harga = 0
    total_bobot = 0
    
    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_harga += barang[i][1]
            total_bobot += barang[i][2]
    
    # Penalti jika melebihi kapasitas
    if total_bobot > kapasitas_tas:
        return 0
    else:
        return total_harga


# Contoh penggunaan
if __name__ == "__main__":
    # Definisi contoh populasi awal
    populasi_awal = [
        [1, 0, 1, 0, 1],  # Contoh kromosom individu
        [0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1],
        # Tambahkan lebih banyak individu sesuai kebutuhan
    ]

    # Menghitung fitness untuk setiap individu
    fitness_populasi = [hitung_fitness(individu, barang, kapasitas_tas) for individu in populasi_awal]

    # Menampilkan nilai fitness
    print("\nNilai Fitness:")
    for idx, fitness in enumerate(fitness_populasi):
        print(f"Individu {idx+1}: Fitness = {fitness}")
