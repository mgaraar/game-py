import os

def buat_file():
    nama = input("masukan nama file yang ingin dibuat: ")
    path = f"teks_editor/{nama}.txt"
    with open(path, "w") as file:
        file.write("")
    print(f"File '{nama}.txt' berhasil dibuat!")

def list_folder():
    files = os.listdir("teks_editor")
    print("File yang tersedia:")
    for nomor, file in enumerate(files, 1):
        print(f"{nomor}. {file}")
    return files  

def baca_file():
    try:
        files = list_folder()
        pilih = int(input("masukan nomor file yang mau dibaca: ")) - 1
        path = f"teks_editor/{files[pilih]}"
        with open(path, "r") as file:
            isi = file.read()
            print(f"---\n{isi}\n---")
    except:
        print("nomor tidak valid!")

def tambah_isi():
    try:
        files = list_folder()
        pilih = int(input("masukan nomor file yang mau ditambah: ")) - 1
        path = f"teks_editor/{files[pilih]}"
        teks = input("apa yang mau ditambahkan: ")
        with open(path, "a") as file:
            file.write(f"\n{teks}")
        print("teks berhasil ditambahkan!")
    except:
        print("nomor tidak valid!")

def hapus_file():
    try:
        files = list_folder()
        pilih = int(input("masukan nomor file yang mau dihapus: ")) - 1
        path = f"teks_editor/{files[pilih]}"
        os.remove(path)
        print(f"File '{files[pilih]}' berhasil dihapus!")
    except:
        print("nomor tidak valid!")

def menu():
    while True:
        print("\nselamat datang!")
        print("-- simple teks editor --")
        print("1. Buat File")
        print("2. Baca File")
        print("3. Tambah Teks")
        print("4. Hapus File")
        print("5. Keluar")
        try:
            pilihan = int(input('masukan nomor: '))
        except:
            print("masukan angka!")
            continue
        if pilihan == 1:
            buat_file()
        elif pilihan == 2:
            baca_file()
        elif pilihan == 3:
            tambah_isi()
        elif pilihan == 4:
            hapus_file()
        elif pilihan == 5:
            break
        else:
            print("pilihan tidak valid!")

menu()