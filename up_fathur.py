print("================================")
print("   APLIKASI TIKET BIOSKOP")
print("================================")

while True:
    # 1. Input nama pembeli
    nama = input("Masukkan nama pembeli: ")

    # 2. Input jenis dan jumlah tiket
    print("Jenis Tiket:")
    print("1. Reguler  - Rp35.000")
    print("2. VIP      - Rp50.000")
    print("3. Premium  - Rp75.000")

    jenis = input("Pilih jenis tiket (1/2/3): ")
    jumlah = int(input("Masukkan jumlah tiket: "))

    # 3. Jumlah harga tiket
    if jenis == "1":
        nama_tiket = "Reguler"
        harga = 35000
    elif jenis == "2":
        nama_tiket = "VIP"
        harga = 50000
    elif jenis == "3":
        nama_tiket = "Premium"
        harga = 75000
    else:
        print("Jenis tiket tidak valid!")
        continue

    # 4. Menghitung total harga
    total = harga * jumlah

    # 5. Mengecek diskon
    if jumlah > 3:
        diskon = total * 0.10
    else:
        diskon = 0

    pembayaran = total - diskon

    # 6. Menampilkan hasil transaksi
    print("================================")
    print("       STRUK PEMBELIAN")
    print("================================")
    print("Nama Pelanggan :", nama)
    print("Jenis Tiket    :", nama_tiket)
    print("Jumlah Tiket   :", jumlah)
    print("Harga Tiket    : Rp", harga)
    print("Total Harga    : Rp", total)
    print("Diskon         : Rp", int(diskon))
    print("Total Bayar    : Rp", int(pembayaran))
    print("================================")

    # 7. Menanyakan pelanggan berikutnya
    lanjut = input("Melayani pelanggan berikutnya? (y/t): ")

    if lanjut.lower != "y":
        print("Terima kasih telah menggunakan program!")
        break