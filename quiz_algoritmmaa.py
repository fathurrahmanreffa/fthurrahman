# program nilai remedial siswa
print(" == Program Nilai Siswa ==")

print(" 1. Andi")
print(" 2. Budi")
print(" 3. Citra")


nama = int(input("Pilih mahasiswa (1-3): "))

if nama == 1 :
    target = 70
    print ("Andi")
    print("Target nilai:", target)

elif nama == 2:
    target = 75
    print("Budi")
    print("Target nilai", target)

elif nama == 3:
    target = 80
    print("Citra")
    print("Target nilai", target)

else:
    target= 0
    print("Pilihan Tidak Tersedia")

if target!=0:
    percobaan = 1 

    while percobaan <= 3:
        nilai = int(input("Masukan Nilai Ujian: "))

        if nilai >= target:
            print("Selamat kamu berhasil lulus")
            percobaan = 4

        else:
            if percobaan < 3:
                print("Nilai belum mencapai target")
            else:
                print("Kamu dinyatakan tidak lulus!")
            percobaan = percobaan +1