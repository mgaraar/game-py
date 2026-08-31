daftar_nama = []

def ToDo():
    while True:
        daftar = input('Masukan List To Do nya (ketik quit jika sudah): ')
        if daftar.lower() == 'quit':
            break
        daftar_nama.append({'tugas': daftar, 'selesai': False})

def TampilkanTugas():
    if len(daftar_nama) == 0:
        print("belum ada tugas !")
        return
    for item in daftar_nama:
        if item['selesai']: # == True
            print(f"[✅] {item['tugas']}")
        else:
            print(f"[❌] {item['tugas']}")                  

def TugasSelesai():
    if len(daftar_nama) == 0:
        print("belum ada tugas !")
        return
    try:
        selesai = int(input('masukan nomor tugas yang selesai: '))
        final = selesai - 1
        daftar_nama[final]['selesai'] = True
        TampilkanTugas()
    except:
        print("nomor tidak valid !")

def LoopsTugas():
    if len(daftar_nama) == 0:
        print("belum ada tugas !")
        return
    for item in daftar_nama:
        if item['selesai']:
            print(f"{item['tugas']} sudah selesai!")

def MenuUtama():
    while True:
        print("== To Do List ==")
        print("1. tambahkan tugas")
        print("2. tampilkan semua tugas")
        print("3. selesaikan tugas")
        print("4. tampilkan tugas selesai")
        print("5. keluar")
        menu = int(input("masukan nomor: "))
        if menu == 1:
            ToDo()
        elif menu == 2:
            TampilkanTugas()
        elif menu == 3:
            TugasSelesai()
        elif menu == 4:
            LoopsTugas()
        elif menu == 5:
            break
        else:
            print("masukan angka yang benar !")

MenuUtama()