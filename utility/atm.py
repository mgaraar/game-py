users = {
    "1234": {"pin": "1234", "saldo": 1000000, "nama": "Rey"},
    "0000": {"pin": "0000", "saldo": 500000, "nama": "Guest"}
}

def show_demo_accounts():
    print("\n=== Akun Demo ===")
    for uid, data in users.items():
        print(f"User ID: {uid} | PIN: {data['pin']} | Nama: {data['nama']}")
    print("Catatan: PIN terlihat di sini cuma untuk nyoba, di ATM beneran jangan!")
    print()

def login():
    show_demo_accounts()
    
    while True:
        print("1. Login")
        print("2. Buat akun baru")
        print("3. Keluar")
        pilih = input("Pilih (1-3): ")
        
        if pilih == '1':
            for _ in range(3):
                user_id = input("Masukkan user ID: ")
                pin = input("Masukkan PIN: ")
                
                if user_id in users and users[user_id]["pin"] == pin:
                    print(f"\nLogin berhasil! Selamat datang, {users[user_id]['nama']}!")
                    return user_id
                
                print("User ID atau PIN salah!\n")
            
            print("Terlalu banyak percobaan. Keluar...")
            return None
        
        elif pilih == '2':
            nama = input("Masukkan nama: ").strip()
            while True:
                user_id = input("Buat User ID: ").strip()
                if not user_id:
                    print("User ID tidak boleh kosong!")
                elif user_id in users:
                    print("User ID sudah dipakai!")
                else:
                    break
            
            while True:
                pin = input("Buat PIN: ").strip()
                if len(pin) < 4:
                    print("PIN minimal 4 digit!")
                else:
                    break
            
            users[user_id] = {"pin": pin, "saldo": 0, "nama": nama}
            print(f"Akun {nama} berhasil dibuat! Silakan login.")
            print()
        
        elif pilih == '3':
            print("Keluar...")
            return None
        
        else:
            print("Pilihan tidak valid!")

def show_menu():
    print("\n=== MENU ATM ===")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Keluar")

def cek_saldo(saldo):
    print(f"\nSaldo kamu: Rp {saldo:,}")

def tarik_tunai(saldo):
    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Masukkan angka!")
        return saldo
    
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0!")
    elif jumlah > saldo:
        print("Saldo tidak cukup!")
    else:
        saldo -= jumlah
        print(f"Berhasil menarik Rp {jumlah:,}")
        print(f"Sisa saldo: Rp {saldo:,}")
    
    return saldo

def setor_tunai(saldo):
    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Masukkan angka!")
        return saldo
    
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0!")
    else:
        saldo += jumlah
        print(f"Berhasil setor Rp {jumlah:,}")
        print(f"Saldo sekarang: Rp {saldo:,}")
    
    return saldo

def main():
    user_id = login()
    if not user_id:
        return
    
    saldo = users[user_id]["saldo"]
    
    while True:
        show_menu()
        pilih = input("Pilih menu (1-4): ")
        
        if pilih == '1':
            cek_saldo(saldo)
        elif pilih == '2':
            saldo = tarik_tunai(saldo)
        elif pilih == '3':
            saldo = setor_tunai(saldo)
        elif pilih == '4':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
