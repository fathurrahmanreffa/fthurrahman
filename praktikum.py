# Program Menghitung Nilai Akhir Mahasiswa

# Input Nilai
tugas = float(input("Nilai Tugas: "))
uts = float(input("Nilai Uts: "))
uas = float(input("Nilai Uas: "))
kehadiran = float(input("Kehadiran(%): "))

# Menghitung Nilai Akhir
nilai_akhir = (0.20 * tugas ) + (0.30 * uts) + (0.50 * uas)

# Menentukan Status Kelulusan
if nilai_akhir >= 85 and kehadiran >= 98 and nilai_akhir % 2 == 0:
    status = "LULUS DENGAN PREDIKAT"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "LULUS"
else:
    status = "BELUM LULUS"

# Menampilkan Hasil
print("/nNilai Akhir: ", nilai_akhir)
print("Status:", status)