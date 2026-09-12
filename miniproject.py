# List untuk menyimpan data line-up
lineup = []

while True:
    print("\n--- SISTEM MANAJEMEN LINE-UP KONSER ---")
    print("1. Tambah Line-Up")
    print("2. Lihat Semua Line-Up")
    print("3. Ubah Line-Up")
    print("4. Hapus Line-Up")
    print("5. Keluar")

    pilihan = input("\nMasukkan pilihan (1-5): ")

    # Tambah data
    if pilihan == "1":

        print("\n--- TAMBAH LINE-UP ---")

        band = input("Masukkan nama band: ")
        lagu = input("Masukkan judul lagu: ")
        jam = input("Masukkan jam tampil: ")

        if band == "" or lagu == "" or jam == "":
            print("\nData tidak boleh kosong")

        else:
            data = (band, lagu, jam)

            lineup.append(data)

            print("\nData line-up berhasil ditambahkan")
            print("Band:", band)
            print("Lagu:", lagu)
            print("Jam:", jam)

    # LIHAT DATA
    elif pilihan == "2":

        print("\n--- DAFTAR LINE-UP KONSER ---")

        if len(lineup) == 0:
            print("Belum ada data line-up")

        else:
            nomor = 1

            for band in lineup:

                print("\nLine-Up ke-", nomor)
                print("Nama Band:", band[0])
                print("Judul Lagu:", band[1])
                print("Jam Tampil:", band[2])

                nomor += 1

    # UBAH DATA
    elif pilihan == "3":

        print("\n--- UBAH LINE-UP ---")

        if len(lineup) == 0:
            print("Data line-up masih kosong")

        else:
            print("\nData Line-Up:")

            nomor = 1

            for band in lineup:
                print(nomor, ".", band[0], "-", band[1])
                nomor += 1

            while True:
                ubah = input("\nMasukkan nomor line-up yang ingin diubah: ")

                if ubah.isdigit():
                    ubah = int(ubah)

                    if ubah >= 1 and ubah <= len(lineup):
                        break
                    else:
                        print("Nomor line-up tidak tersedia")

                else:
                    print("Input harus berupa angka")

            print("\nMasukkan data baru:")

            band = input("Nama band: ")
            lagu = input("Judul lagu: ")
            jam = input("Jam tampil: ")

            if band == "" or lagu == "" or jam == "":
                print("\nData tidak boleh kosong")

            else:
                lineup[ubah - 1] = (
                    band,
                    lagu,
                    jam
                )

                print("\nData line-up berhasil diubah")

    # HAPUS DATA
    elif pilihan == "4":

        print("\n--- HAPUS LINE-UP ---")

        if len(lineup) == 0:
            print("Data line-up masih kosong")

        else:
            print("\nDaftar Line-Up:")

            nomor = 1

            for band in lineup:
                print(nomor, ".", band[0], "-", band[1])
                nomor += 1

            while True:
                hapus = input(
                    "\nMasukkan nomor line-up yang ingin dihapus: "
                )

                if hapus.isdigit():
                    hapus = int(hapus)

                    if hapus >= 1 and hapus <= len(lineup):
                        break
                    else:
                        print("Nomor line-up tidak tersedia")

                else:
                    print("Input harus berupa angka")

            data_dihapus = lineup.pop(hapus - 1)

            print("\nData line-up berhasil dihapus")
            print("Band yang dihapus:", data_dihapus[0])
            print("Lagu yang dihapus:", data_dihapus[1])

    # KELUAR
    elif pilihan == "5":

        print("\n======================================")
        print("Terima kasih telah menggunakan")
        print("Sistem Manajemen Line-Up Konser")
        print("======================================")
        break

    # PILIHAN SALAH
    else:
        print("\nPilihan tidak valid")
        print("Silakan masukkan angka 1 sampai 5")