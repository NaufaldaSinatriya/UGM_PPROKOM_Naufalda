A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

gabungan_A_B = A.union(B)
gabungan_B_C = B.union(C)
gabungan_B_C_D = B.union(C).union(D)
gabungan_A_B_C_D = A.union(B).union(C).union(D)

print("A ∪ B:", gabungan_A_B)
print("B ∪ C:", gabungan_B_C)
print("B ∪ C ∪ D:", gabungan_B_C_D)
print("A ∪ B ∪ C ∪ D:", gabungan_A_B_C_D)