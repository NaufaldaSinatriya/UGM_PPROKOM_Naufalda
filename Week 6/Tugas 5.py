A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}
C = set()  

selisih_simetris_A_B = A.symmetric_difference(B)
selisih_simetris_B_A = B.symmetric_difference(A)
selisih_simetris_A_C = A.symmetric_difference(C)
selisih_simetris_B_C = B.symmetric_difference(C)

print("A Δ B:", selisih_simetris_A_B)
print("B Δ A:", selisih_simetris_B_A)
print("A Δ C:", selisih_simetris_A_C)
print("B Δ C:", selisih_simetris_B_C)
