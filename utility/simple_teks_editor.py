# list to do (fitur):
# membuat file/tulis baru
# baca isi file
# menambahkan teks ke isi file
# hapus isi file

import os

def buat_file():
    nama = input("masukan nama file yang ingin dibuat: ")
    path = f"teks_editor/{nama}.txt"
    with open(path, "w") as file:
        file.write("")
        return
    
def list_folder():
        files = os.listdir("teks_editor")
        print("File yang tersedia:")
        for nomor, file in enumerate(files, 1):
            print(f"{nomor}. {file}")

def baca_file():
    try:
        list_folder()
        pilih = input("masukan nama file yang mau dibaca: ")
        path = f"teks_editor/{pilih}.txt"
        with open(path, "r") as file:
            isi = file.read()
            file.read()    
            print(f"---{isi}---")
    except:
        print("masukan nama file yang benar !")
        print("pakai nama file bukan nomor ya..")

def tambah_isi():
    list_folder()
    pilih = input("masukan nama file yang mau dibaca: ")
    path = f"teks_editor/{pilih}.txt"
    with open(path, "a") as file:
        file.write(input("apa yang mau ditambahkan: "))

def hapus_file():
    # menghapus sebuah file 
    pass

def menu():
    while True:
        print("selamat datang !")
        print("-- simple teks editor --")
        print("1. Buat/Tulis File")
        print("2. Baca File")
        print("3. Tambah Teks")
        print("4. Hapus isi Teks")
        print("5. Keluar")
        pilihan = int(input('masukan nomor: '))
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
menu()
