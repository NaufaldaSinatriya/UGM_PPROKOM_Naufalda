array_satu = [[4, 6],
          [1, 7]]
array_dua = [[2, 3],
          [5, 6]]

jumlah = [[0, 0],
          [0, 0]]
pengurangan = [[0, 0],
               [0, 0]]

for i in range(len(array_satu)):
    for j in range(len(array_satu[0])):
        jumlah[i][j] = array_satu[i][j] + array_dua[i][j]
        pengurangan[i][j] = array_satu[i][j] - array_dua[i][j]

print("Hasil Penjumlahan:")
for baris in jumlah:
    print(baris)

print("\nHasil Pengurangan:")
for baris in pengurangan:
    print(baris)
