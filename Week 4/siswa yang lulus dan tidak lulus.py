nilai_siswa = [0] * 5 

urutan = 1
for data in range(5):
    nilai_siswa[data] = int(input(f"Masukkan nilai siswa ke-{urutan}: "))
    urutan+= 1

urutan = 1

for nilai in nilai_siswa:
    if nilai >= 70:
        print(f"Siswa ke-{urutan} lulus")
    else:
        print(f"Siswa ke-{urutan} tidak lulus")
    urutan += 1