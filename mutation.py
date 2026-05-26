import random


# Swap Mutation
def swap_mutation(kromosom):
    """
    Melakukan mutasi dengan menukar dua gen dalam kromosom.
    
    Args:
        kromosom (list): Kromosom yang akan dimutasi
    
    Returns:
        list: Kromosom setelah mutasi
    """
    # Pastikan kromosom adalah list
    kromosom = list(kromosom)
    
    # Pilih dua posisi untuk swap
    posisi1, posisi2 = random.sample(range(len(kromosom)), 2)
    
    # Melakukan swap
    kromosom[posisi1], kromosom[posisi2] = kromosom[posisi2], kromosom[posisi1]
    
    return kromosom


# Inversion Mutation
def inversion_mutation(kromosom):
    """
    Melakukan mutasi dengan membalik urutan gen dalam segmen tertentu.
    
    Args:
        kromosom (list): Kromosom yang akan dimutasi
    
    Returns:
        list: Kromosom setelah mutasi
    """
    kromosom = list(kromosom)
    
    posisi1 = random.randint(0, len(kromosom) - 2)
    posisi2 = random.randint(posisi1 + 1, len(kromosom) - 1)
    
    # Membalik segmen kromosom
    kromosom[posisi1:posisi2] = list(reversed(kromosom[posisi1:posisi2]))
    
    return kromosom


# Uniform Mutation
def uniform_mutation(kromosom, mutation_rate=0.1):
    """
    Melakukan mutasi dengan mengubah nilai gen dengan probabilitas tertentu.
    
    Args:
        kromosom (list): Kromosom yang akan dimutasi
        mutation_rate (float): Probabilitas mutasi untuk setiap gen
    
    Returns:
        list: Kromosom setelah mutasi
    """
    # Pastikan kromosom adalah list
    kromosom = list(kromosom)
    
    for i in range(len(kromosom)):
        if random.random() < mutation_rate:
            # Membalik nilai gen (0 menjadi 1, atau 1 menjadi 0)
            kromosom[i] = 1 - kromosom[i]
    
    return kromosom


# Contoh penggunaan
if __name__ == "__main__":
    anak1 = [0, 1, 1, 0, 1]  # Contoh kromosom
    
    # Swap Mutation
    mutasi_anak1 = swap_mutation(anak1.copy())
    print(f"Original: {anak1}")
    print(f"Swap Mutation: {mutasi_anak1}")
    
    # Inversion Mutation
    mutasi_anak2 = inversion_mutation(anak1.copy())
    print(f"Inversion Mutation: {mutasi_anak2}")
    
    # Uniform Mutation
    mutasi_anak3 = uniform_mutation(anak1.copy())
    print(f"Uniform Mutation: {mutasi_anak3}")
