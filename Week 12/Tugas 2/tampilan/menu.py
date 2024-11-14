from rumus.persegi import persegi as ps
from rumus.segitiga import segitiga as sg
from rumus.lingkaran import lingkaran as lg

def menu():
    print("Pilih Bentuk 2D")
    print()
    print("1. Persegi Panjang")
    print("2. Lingkaran")
    print("3. Segitiga")
    print("4. Keluar")
    
    while True:
        try:
            pilihan = int(input('Masukkan Pilihan : '))
            if pilihan not in range(1, 5):
                print('Pilihan tidak valid')
            else:
                break
        except ValueError:
            print('Pilihan tidak valid')
        
    if pilihan == 1:
        ps()
    elif pilihan == 2:
        lg()
    elif pilihan == 3:
        sg()
    else:
        exit()