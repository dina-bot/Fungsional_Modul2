database_peserta = []

def tambah_peserta(nama, nilai):
    hasil = "Lolos" if nilai >= 75 else "Tidak Lolos"
    data_peserta = {"ID": len(database_peserta), "Nama": nama, "Nilai": nilai, "Hasil Akhir": hasil}
    database_peserta.append(data_peserta)
    return "Data peserta berhasil ditambahkan!"

def edit_nilai(id_peserta, nilai_baru):
    if 0 <= id_peserta < len(database_peserta):
        database_peserta[id_peserta]["Nilai"] = nilai_baru
        database_peserta[id_peserta]["Hasil Akhir"] = "Lolos" if nilai_baru >= 75 else "Tidak Lolos"
        return "Nilai peserta berhasil diubah!"
    else:
        return "ID peserta tidak valid."

def tampilkan_nilai_peserta(id_peserta):
    if 0 <= id_peserta < len(database_peserta):
        peserta = database_peserta[id_peserta]
        return f"Nama: {peserta['Nama']}\nNilai: {peserta['Nilai']}\nHasil Akhir: {peserta['Hasil Akhir']}"
    else:
        return "ID peserta tidak valid."

cari_peserta = lambda nama: [peserta for peserta in database_peserta if peserta["Nama"] == nama]

while True:
    print("\nSelamat datang di Sistem Informasi Peserta")
    print("1. Admin - Tambah Peserta")
    print("2. Admin - Edit Nilai Peserta")
    print("3. Peserta - Tampilkan Nilai")
    print("4. Cari Peserta")
    print("5. Keluar")
    
    pilihan = input("Pilih tindakan (1/2/3/4/5): ")
    
    if pilihan == "1":
        if input("Anda yakin ingin menambahkan peserta? (y/n): ").lower() == "y":
            nama = input("Masukkan Nama Peserta: ")
            nilai = int(input("Masukkan Nilai Peserta: "))
            print(tambah_peserta(nama, nilai))
    elif pilihan == "2":
        id_peserta = int(input("Masukkan ID Peserta yang akan diubah: "))
        nilai_baru = int(input("Masukkan Nilai Baru: "))
        print(edit_nilai(id_peserta, nilai_baru))
    elif pilihan == "3":
        id_peserta = int(input("Masukkan ID Peserta Anda: "))
        print(tampilkan_nilai_peserta(id_peserta))
    elif pilihan == "4":
        nama_cari = input("Masukkan Nama Peserta yang akan dicari: ")
        hasil_cari = cari_peserta(nama_cari)
        if hasil_cari:
            print(f"Data ditemukan:\n{hasil_cari[0]}")
        else:
            print("Peserta tidak ditemukan.")
    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih tindakan yang sesuai.")
