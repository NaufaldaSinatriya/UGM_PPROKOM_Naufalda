def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num) ):
        if num % i == 0:
            return False
    return True

angka = [4, 5, 11, 12, 14, 16, 16, 19]
bilangan_prima = [num for num in angka if is_prime(num)]

jumlah_prima = len(bilangan_prima)
total_prima = sum(bilangan_prima)

print("Array:", angka)
print("Bilangan prima dalam array:", bilangan_prima)
print("Jumlah bilangan prima:", jumlah_prima)
print("Penjumlahan semua bilangan prima:", total_prima)

