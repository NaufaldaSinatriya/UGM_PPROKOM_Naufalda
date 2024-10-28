rows = 2
col = 3

matriks = []

for i in range(rows):
    row = []
    for j in range(col):
        value = int(input(f"Masukkan nilai ke-[{i}][{j}]: "))
        row.append(value)
    matriks.append(row)

print("Matriks asli:")
for row in matriks:
    for element in row:
        print(element, end=' ')
    print()

transpose = [[0] * rows for _ in range(col)]

for i in range(rows):
    for j in range(col):
        transpose[j][i] = matriks[i][j]

print("Matriks transpose:")
for row in transpose:
    for element in row:
        print(element, end=' ')
    print()
