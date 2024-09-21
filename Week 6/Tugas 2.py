nilai = set({3, 6, 9, 2, 5, 7})

print("Himpunan awal:", nilai)

for i in range(1, 11):
    nilai.add(i)

print("Himpunan setelah proses penambahan:", nilai)

nilai.discard(1)  
nilai.discard(4)  
nilai.discard(5) 
nilai.discard(8)  

print("Himpunan setelah proses penghapusan:", nilai)