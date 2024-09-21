A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

irisan_A_D = A.intersection(D)
irisan_B_D = B.intersection(D)
irisan_C_D = C.intersection(D)
irisan_A_B_C_D = A.intersection(B).intersection(C).intersection(D)

print("A ∩ D:", irisan_A_D)
print("B ∩ D:", irisan_B_D)
print("C ∩ D:", irisan_C_D)
print("A ∩ B ∩ C ∩ D:", irisan_A_B_C_D)