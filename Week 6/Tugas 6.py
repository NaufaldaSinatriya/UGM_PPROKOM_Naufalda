
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}
C = set()  

A_B = A.difference(B)
B_A = B.difference(A)
A_C = A.difference(C)
B_C = B.difference(C)

print("A - B:", A_B)
print("B - A:", B_A)
print("A - C:", A_C)
print("B - C:", B_C)
