#         APLIKASI KASIR RESTORAN
#===========================================
print("=" * 45)
print("         SELAMAT DATANG DI RESTORAN")
print("=" * 45)
# Daftar menu makanan
menu = {
    1: ["Nasi Goreng", 25000],
    2: ["Mie Ayam", 15000],
    3: ["Ayam Geprek", 20000],
    4: ["Sate Ayam", 30000],
    5: ["Bakso", 18000]
}
# Inisialisasi variabel
total = 0
pesanan = []
# Perulangan pemesanan
while True:
    print("\n========== MENU MAKANAN ==========")
    for nomor, data in menu.items():
        print(f"{nomor}. {data[0]:15} - Rp{data[1]:,}")
    print("0. Selesai Memilih")
    print("=" * 35)
    pilihan = input("Pilih menu (0-5): ")
    # Cek pilihan selesai
    if pilihan == "0":
        break
    # Validasi pilihan menu
    if not pilihan.isdigit():
        print("Input harus berupa angka!")
        continue
    pilihan = int(pilihan)
    if pilihan not in menu:
        print("Menu tidak tersedia!")
        continue
    # Input jumlah pesanan
    jumlah = int(input("Masukkan jumlah pesanan: "))
    if jumlah <= 0:
        print("Jumlah pesanan harus lebih dari 0!")
        continue
    # Menghitung subtotal
    nama = menu[pilihan][0]
    harga = menu[pilihan][1]
    subtotal = harga * jumlah
    # Menambahkan ke total
    total += subtotal
    # Menyimpan pesanan
    pesanan.append([nama, jumlah, harga, subtotal])
    print(f"{nama} berhasil ditambahkan!")
    print(f"Subtotal: Rp{subtotal:,}")
# ==========================================
#             PERHITUNGAN DISKON
# ==========================================
print("\n========== PEMBAYARAN ==========")
diskon = 0
if total > 200000:
    diskon = 0.20
    print("Selamat! Anda mendapatkan diskon 20%")
else:
    print("Anda tidak mendapatkan diskon.")
potongan = total * diskon
total_bayar = total - potongan
# ==========================================
#             STRUK PEMBAYARAN
# ==========================================
print("\n" + "=" * 45)
print("             STRUK PEMBAYARAN")
print("=" * 45)
for item in pesanan:
    print(f"{item[0]}")
    print(f"  {item[1]} x Rp{item[2]:,} = Rp{item[3]:,}")
print("-" * 45)
print(f"Total Belanja : Rp{total:,.0f}")
print(f"Diskon        : {diskon * 100:.0f}%")
print(f"Potongan      : Rp{potongan:,.0f}")
print("-" * 45)
print(f"TOTAL BAYAR   : Rp{total_bayar:,.0f}")
print("=" * 45)
print(        "TERIMA KASIH TELAH BERKUNJUNG")
print("=" * 45)