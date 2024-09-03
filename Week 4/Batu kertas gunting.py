import random

choices = ['batu', 'kertas', 'gunting']

pilihan_pemain = input("Masukkan pilihanmu (batu/kertas/gunting): ").lower()

if pilihan_pemain not in choices:
    print("Pilihan tidak valid. Silakan pilih 'batu', 'kertas', atau 'gunting'.")
else:
    
    pilihan_komputer = random.choice(choices)
    print(f"Komputer memilih: {pilihan_komputer}")

    if pilihan_pemain == pilihan_komputer:
        print("Seri!")
    elif pilihan_pemain == 'batu':
        if pilihan_komputer == 'gunting':
            print("Kamu menang!")
        else:
            print("Komputer menang!")
    elif pilihan_pemain == 'kertas':
        if pilihan_komputer == 'batu':
            print("Kamu menang!")
        else:
            print("Komputer menang!")
    elif pilihan_pemain == 'gunting':
        if pilihan_komputer == 'kertas':
            print("Kamu menang!")
        else:
            print("Komputer menang!")