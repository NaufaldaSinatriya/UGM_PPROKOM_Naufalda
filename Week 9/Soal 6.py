angka = [1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]
genap = []
ganjil = []

for num in angka:
    if num % 2 == 0:
        genap.append(num)
    else:
        ganjil.append(num)

print("Daftar angka:", angka)
print("Ini adalah angka genap:", genap)
print("Jumlah angka genap:", len(genap), "angka")
print("Ini adalah angka ganjil:", ganjil)
print("Jumlah angka ganjil:", len(ganjil), "angka")
