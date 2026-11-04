import random

def generate_secret(length):
    """Generate digit angka rahasia yang unik sesuai kesulitan."""
    digits = list('0123456789')
    random.shuffle(digits)
    return ''.join(digits[:length])

def count_bulls_cows(secret, guess):
    """Hitung jumlah bulls dan cows."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def give_clue(secret, guess, bulls, cows):
    """Beri satu clue acak berdasarkan tebakan sebelumnya."""
    clues = []
    
    # Clue dari bulls: ada yang benar posisinya
    for i, (s, g) in enumerate(zip(secret, guess)):
        if s == g:
            clues.append(f"Digit {s} ada di posisi ke-{i + 1}")
    
    # Clue dari cows: ada yang benar tapi posisi salah
    for d in set(guess):
        if d in secret and secret[secret.index(d)] != d:
            clues.append(f"Digit {d} ada di angka ini tapi posisinya bukan {guess.index(d) + 1}")
    
    # Clue negatif: digit yang tidak ada sama sekali
    wrong_digits = [d for d in guess if d not in secret]
    for d in wrong_digits:
        clues.append(f"Digit {d} tidak ada di angka ini")
    
    if clues:
        return random.choice(clues)
    return "Belum ada digit yang bisa dijadikan clue."

def get_difficulty():
    """Tanya pilihan kesulitan dan return panjang digit."""
    print("\nPilih kesulitan:")
    print("1. Mudah   (3 digit)")
    print("2. Sedang  (4 digit)")
    print("3. Sulit   (5 digit)")
    while True:
        pilih = input("Masukkan nomor kesulitan (1-3): ").strip()
        if pilih == '1':
            return 3
        elif pilih == '2':
            return 4
        elif pilih == '3':
            return 5
        else:
            print("Pilihan tidak valid!")

def play_game():
    length = get_difficulty()
    secret = generate_secret(length)
    attempts = 0
    
    print(f"\n=== GAME COWS AND BULLS ===")
    print(f"Tebak {length} digit angka yang benar!")
    print("Bulls = digit benar + posisi benar")
    print("Cows  = digit benar tapi posisi salah")
    print("Clue akan muncul setiap 3 percobaan gagal\n")
    
    while True:
        guess = input(f"Masukan tebakan {length} digit: ").strip()
        
        if len(guess) != length or not guess.isdigit():
            print(f"Input tidak valid! Masukkan tepat {length} digit angka.")
            continue
        
        if len(set(guess)) != length:
            print("Digit tidak boleh duplikat!")
            continue
        
        attempts += 1
        bulls, cows = count_bulls_cows(secret, guess)
        
        print(f"Bulls: {bulls} | Cows: {cows}")
        
        if bulls == length:
            print(f"\nSelamat! Kamu menebak dengan benar dalam {attempts} percobaan!")
            break
        
        # Beri clue setiap 3 percobaan gagal
        if attempts % 3 == 0:
            print(f"💡 Clue: {give_clue(secret, guess, bulls, cows)}")

if __name__ == "__main__":
    play_game()
