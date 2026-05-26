import random


# Fungsi untuk Roulette Wheel Selection
def roulette_wheel_selection(populasi, fitness_populasi):
    """
    Memilih individu sebagai parent berdasarkan probabilitas proporsional dengan fitness.
    
    Args:
        populasi (list): List individu dalam populasi
        fitness_populasi (list): List nilai fitness masing-masing individu
    
    Returns:
        tuple: (individu terpilih, indeks individu)
    """
    total_fitness = sum(fitness_populasi)
    
    # Jika total fitness 0, pilih secara acak
    if total_fitness == 0:
        idx = random.randrange(len(populasi))
        return populasi[idx], idx
    
    # Menghitung probabilitas untuk setiap individu
    probabilitas = [fitness / total_fitness for fitness in fitness_populasi]
    
    # Menghitung probabilitas kumulatif
    kumulatif_prob = []
    kumulatif = 0
    for p in probabilitas:
        kumulatif += p
        kumulatif_prob.append(kumulatif)
    
    # Menghasilkan bilangan acak dan menentukan individu terpilih
    r = random.random()
    for i, kum_prob in enumerate(kumulatif_prob):
        if r <= kum_prob:
            return populasi[i], i
    
    # Jika tidak ada yang memenuhi, kembalikan individu terakhir
    return populasi[-1], len(populasi)-1


# Fungsi untuk Tournament Selection
def tournament_selection(populasi, fitness_populasi, k=3):
    """
    Memilih individu dengan cara membandingkan beberapa individu yang dipilih acak.
    
    Args:
        populasi (list): List individu dalam populasi
        fitness_populasi (list): List nilai fitness masing-masing individu
        k (int): Jumlah individu yang dibandingkan dalam turnamen
    
    Returns:
        tuple: (individu terpilih, indeks individu)
    """
    # Memastikan k tidak lebih besar dari populasi
    if len(populasi) < k:
        k = len(populasi)
    
    # Memilih k individu secara acak
    peserta_indices = random.sample(range(len(populasi)), k)
    peserta = [(populasi[i], fitness_populasi[i], i) for i in peserta_indices]
    
    # Mengurutkan berdasarkan fitness (menurun)
    peserta.sort(key=lambda x: x[1], reverse=True)
    
    # Mengembalikan individu dengan fitness tertinggi
    return peserta[0][0], peserta[0][2]


# Contoh penggunaan
if __name__ == "__main__":
    # Definisikan populasi awal dan fitness_populasi
    populasi_awal = ['individu1', 'individu2', 'individu3', 'individu4']
    fitness_populasi = [10, 20, 30, 40]

    # Membuat salinan populasi dan fitness untuk dimodifikasi
    available_populasi = populasi_awal.copy()
    available_fitness = fitness_populasi.copy()

    # Memilih Parent 1 menggunakan Roulette Wheel Selection
    parent1, idx1 = roulette_wheel_selection(available_populasi, available_fitness)
    
    # Menghapus parent1 dari daftar available_populasi dan available_fitness
    del available_populasi[idx1]
    del available_fitness[idx1]

    # Memilih Parent 2 menggunakan Tournament Selection
    parent2, idx2 = tournament_selection(available_populasi, available_fitness)
    
    # Menghapus parent2 dari daftar available_populasi dan available_fitness
    del available_populasi[idx2]
    del available_fitness[idx2]

    print("\nParent Terpilih:")
    print(f"Parent 1: {parent1}")
    print(f"Parent 2: {parent2}")
