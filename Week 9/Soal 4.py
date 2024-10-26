
jumlah_elemen = int(input("Masukkan jumlah elemen dalam array: "))

array = list(range(1, jumlah_elemen + 1))
print("Data Array:", array)

kelipatan = int(input("Masukkan kelipatan yang ingin ditampilkan: "))
kelipatan_array = [elemen for elemen in array if elemen % kelipatan == 0]

if kelipatan_array:
    print("Elemen yang merupakan kelipatan dari", kelipatan, ":", kelipatan_array)
else:
    print("Tidak ada elemen yang merupakan kelipatan dari", kelipatan)
