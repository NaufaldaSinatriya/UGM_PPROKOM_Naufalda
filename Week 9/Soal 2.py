
sebuah_angka = []

for i in range(5):
    nilai = float(input(f"Masukkan angka ke-{i + 1}: "))
    sebuah_angka.append(nilai)
    
    print(sebuah_angka)

total = sum(sebuah_angka)

while True:
    pilihan = input("Ingin melihat hasil 'jumlah' atau 'rata-rata'? ").lower()
    
    if pilihan == "jumlah":
        print("Jumlah total dari nilai datanya adalah:", total)
        break
    elif pilihan == "rata-rata":
        rata_rata = total / len(sebuah_angka)
        print("Rata-rata dari nilai datanya adalah:", round(rata_rata, 2))  
        break
    else:
    
        print("Kesalahan, Harap masukkan 'jumlah' atau 'rata-rata'.")
