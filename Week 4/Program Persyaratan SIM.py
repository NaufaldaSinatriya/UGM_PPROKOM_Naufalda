# Program Persyaratan SIM
umur = int(input("Masukan Umur Anda = "))
nilai = int(input("Masukan Nilai Tes Anda = "))
lulus = "Selamat Anda Berhak Mendapatkan SIM Anda"
gagal = "Maaf, Anda tidak berhak mendapatkan SIM Anda\nSilahkan coba lagi bulan atau tahun depan"

if umur > 17:
    if nilai < 60:
        print()
        print(gagal)
    else:
        print()
        print(lulus)
else:
    print()
    print(gagal)