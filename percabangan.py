# variable dan tipe data
nama_mhs = "Fathur"
kelas = "C1"

nalgoritma = 90
nagama = 90
nbasisdata = 90

# print(rata_rata)
nilaialgo = int(input("Masukkan Nilai Algoritma : "))
nagama = int(input("Masukan Nilai Agama : "))
nbasisdata = int(input("Masukan Nilai  Basis data : "))
nkimia = int(input("Masukan Nilai Kimia : "))
nfisika = int(input("Masukan Nilai  Fisika : "))
nbahasainggris = int(input("Masukan Nilai Bahasa Inggris : "))
nolahraga = int(input("Masukan Nilai Olahraga: "))

rata_rata = (nalgoritma + nagama + nbasisdata + nkimia + nfisika + nbahasainggris + nolahraga) / 7

# penentuan lulus dan tidak
if   rata_rata >=80 and rata_rata <=100:
     # kondisi jika terpenuhi
     # maka
     print("Nilai : A")
elif rata_rata >=78 and rata_rata <=80:
     print("Nilai : 8")
elif rata_rata >=50 and rata_rata <=70:
     print("Nilai : C")
elif rata_rata >=30 and rata_rata <=50:
     print("Nilai : D")
elif rata_rata >=0 and rata_rata <=20:
     print ("Nilai :E")
else :
     # cukup menampilkan hasil
     # maka
     print("Nilai Lebih dari 100 atau dibawah 50")