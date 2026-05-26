import random


# One-Point Crossover
def one_point_crossover(parent1, parent2):
    """
    Melakukan crossover dengan satu titik potong.
    
    Args:
        parent1 (list): Kromosom parent pertama
        parent2 (list): Kromosom parent kedua
    
    Returns:
        tuple: (anak1, anak2) hasil crossover
    """
    titik_potong = random.randint(1, len(parent1)-1)
    anak1 = parent1[:titik_potong] + parent2[titik_potong:]
    anak2 = parent2[:titik_potong] + parent1[titik_potong:]
    return anak1, anak2


# Two-Point Crossover
def two_point_crossover(parent1, parent2):
    """
    Melakukan crossover dengan dua titik potong.
    
    Args:
        parent1 (list): Kromosom parent pertama
        parent2 (list): Kromosom parent kedua
    
    Returns:
        tuple: (anak1, anak2) hasil crossover
    """
    titik1 = random.randint(1, len(parent1)-2)
    titik2 = random.randint(titik1+1, len(parent1)-1)
    
    anak1 = parent1[:titik1] + parent2[titik1:titik2] + parent1[titik2:]
    anak2 = parent2[:titik1] + parent1[titik1:titik2] + parent2[titik2:]
    
    return anak1, anak2


# Uniform Crossover
def uniform_crossover(parent1, parent2):
    """
    Melakukan crossover dengan memilih gen secara acak dari setiap parent.
    
    Args:
        parent1 (list): Kromosom parent pertama
        parent2 (list): Kromosom parent kedua
    
    Returns:
        tuple: (anak1, anak2) hasil crossover
    """
    # Membuat mask acak
    mask = [random.randint(0, 1) for _ in range(len(parent1))]
    
    anak1 = []
    anak2 = []
    
    for i in range(len(parent1)):
        if mask[i] == 0:
            # Jika mask bernilai 0, ambil gen dari parent1 untuk anak1,
            # dan parent2 untuk anak2
            anak1.append(parent1[i])
            anak2.append(parent2[i])
        else:
            # Jika mask bernilai 1, ambil gen dari parent2 untuk anak1,
            # dan parent1 untuk anak2
            anak1.append(parent2[i])
            anak2.append(parent1[i])
    
    return anak1, anak2


# Contoh penggunaan
if __name__ == "__main__":
    parent1 = [1, 0, 1, 1, 0]  # Contoh parent1
    parent2 = [0, 1, 0, 0, 1]  # Contoh parent2
    
    # One-Point Crossover
    anak1_opc, anak2_opc = one_point_crossover(parent1, parent2)
    print("\nHasil One-Point Crossover:")
    print(f"Anak 1: {anak1_opc}")
    print(f"Anak 2: {anak2_opc}")
    
    # Two-Point Crossover
    anak1_tpc, anak2_tpc = two_point_crossover(parent1, parent2)
    print("\nHasil Two-Point Crossover:")
    print(f"Anak 1: {anak1_tpc}")
    print(f"Anak 2: {anak2_tpc}")
    
    # Uniform Crossover
    anak1_uc, anak2_uc = uniform_crossover(parent1, parent2)
    print("\nHasil Uniform Crossover:")
    print(f"Anak 1: {anak1_uc}")
    print(f"Anak 2: {anak2_uc}")
