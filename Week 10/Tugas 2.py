rows = 2
col = 3

matriks = []

for i in range(rows):
    row = []
    for j in range(col):
        value = int(input(f"Masukkan nilai ke-[{i}][{j}]: "))
        row.append(value)
        if (i == 0 and j == col - 1) or (i == 1 and j == col - 1):
            print(" -" * 15)
    matriks.append(row)

print("Matriks yang dimasukkan:")
for row in matriks:
    for element in row:
        print(element, end=' ')
    print()
