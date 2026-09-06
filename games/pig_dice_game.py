# pseudo teks untuk membuat game pig dice game
# fitur bermain player vs player (1 vs 1)
# fitur roll dadu player
# fitur hold dadu player
# kalau dapat angka 1 = skor giliran hangus, giliran pindah
# menggunakan kocokan dadu random
# target skor untuk menang = 100
# skor disimpan dalam list of dictionary (nama, skor_total, skor_giliran)
# giliran berpindah kalau: dapat 1 atau hold

# buat struktur data
# buat kerangka gameplay

import random

# struktur data
players = [
    {"nama": "Player 1", "skor_total": 0, "skor_giliran": 0},
    {"nama": "Player 2", "skor_total": 0, "skor_giliran": 0},
]

def play():
    while True:
        user_input = input("roll the dice? (y/n): ").lower()
        if user_input == "y":
            dice1 = random.randint(1, 6)
            if dice1 == 1:
                print("u dont get any point nigga")
                break
            result = dice1
            print(result)
        elif user_input == "n":
            print("thank you for playing!")
            break
        else:
            print("wrong input!!")
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

    Contoh:
    --------------------------------------------------------------------------------
    Player 1 roll -> dapat 5 (skor giliran: 5)
    Player 1 roll -> dapat 3 (skor giliran: 8)
    Player 1 roll -> dapat 1 (skor giliran hangus! giliran pindah)

    Player 2 roll -> dapat 6 (skor giliran: 6)
    Player 2 hold -> skor total: 6, giliran pindah ke Player 1
    --------------------------------------------------------------------------------
    """
        print(rules_text)
        user = input("selesai membaca? (y/n): ").lower()
        balik = user
        if user == "y":
            break
        elif user == "n":
            print("silahkan baca kembali aturan diatas")
        else:
            print("pilihan tidak valid")
def menu():
    while True:
        print("\nselamat datang!")
        print("-- pig dice game --")
        print("1. Rules bermain")
        print("2. Mulai bermain")
        print("3. Keluar")
        pilihan = int(input("masukan nomor: "))
        if pilihan == 1:
            rules()
        elif pilihan == 2:
            pass
        else:
            print("Terimakasih sudah bermain !")
            break
menu()