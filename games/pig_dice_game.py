import random

players = [
    {"nama": "Player 1", "skor_total": 0, "skor_giliran": 0},
    {"nama": "Player 2", "skor_total": 0, "skor_giliran": 0},
]

def nama():
    players[0]["nama"] = input("masukan nama player 1: ")
    players[1]["nama"] = input("masukan nama player 2: ")

def play():
    nama()
    giliran = 0  # ← di luar loop!

    while True:
        player_sekarang = players[giliran]
        print(f"\n🎲 Giliran: {player_sekarang['nama']}")
        print(f"Skor total: {player_sekarang['skor_total']} | Skor giliran: {player_sekarang['skor_giliran']}")

        user_input = input("roll (r) atau hold (h)?: ").lower()

        if user_input == "r":
            dice = random.randint(1, 6)
            print(f"Dadu: {dice}")

            if dice == 1:
                print("Dapat angka 1! Skor giliran hangus, giliran pindah!")
                player_sekarang["skor_giliran"] = 0  # ← reset skor giliran
                giliran = 1 - giliran  # ← pindah giliran
            else:
                player_sekarang["skor_giliran"] += dice
                print(f"Skor giliran: {player_sekarang['skor_giliran']}")

        elif user_input == "h":
            player_sekarang["skor_total"] += player_sekarang["skor_giliran"]  # ← tambah ke total
            print(f"{player_sekarang['nama']} hold! Skor total: {player_sekarang['skor_total']}")
            
            if player_sekarang["skor_total"] >= 100:  # ← cek menang
                print(f"🏆 {player_sekarang['nama']} MENANG!")
                break
            
            player_sekarang["skor_giliran"] = 0  # ← reset skor giliran
            giliran = 1 - giliran  # ← pindah giliran

        else:
            print("input tidak valid!")

def rules():
    while True:
        rules_text = """
    🎲 ATURAN PIG DICE GAME
    Tujuan: Jadilah pemain pertama yang mencapai 100 poin!
    Cara main:
    1. Setiap giliran, pemain bisa Roll dadu sebanyak mungkin
    2. Angka yang keluar ditambahkan ke skor giliran (temporary)
    3. Pemain bisa Hold — skor giliran ditambahkan ke skor total, lalu giliran pindah ke lawan
    4. Kalau dapat angka 1 — skor giliran hangus (0), giliran langsung pindah ke lawan
    5. Pemain pertama yang mencapai 100 poin menang! 🏆
    """
        print(rules_text)
        user = input("selesai membaca? (y/n): ").lower()
        if user == "y":
            break
        elif user == "n":
            print("silahkan baca kembali!")
        else:
            print("pilihan tidak valid!")

def menu():
    while True:
        print("\nselamat datang!")
        print("-- pig dice game --")
        print("1. Rules bermain")
        print("2. Mulai bermain")
        print("3. Keluar")
        try:
            pilihan = int(input("masukan nomor: "))
        except:
            print("masukan angka!")
            continue
        if pilihan == 1:
            rules()
        elif pilihan == 2:
            play()
        elif pilihan == 3:
            print("Terimakasih sudah bermain!")
            break
        else:
            print("pilihan tidak valid!")

menu()