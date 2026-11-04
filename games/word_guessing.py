import random

WORDS = {
    "Programming": [
        "python", "developer", "keyboard", "monitor", "program",
        "variable", "function", "class", "object", "loop"
    ],
    "Cloud & Network": [
        "cloud", "network", "server", "database", "api",
        "firewall", "router", "bandwidth", "protocol", "latency"
    ],
    "General": [
        "algorithm", "syntax", "compiler", "internet", "software",
        "hardware", "browser", "folder", "file", "screen"
    ]
}

def choose_word(category):
    return random.choice(WORDS[category])

def get_difficulty():
    print("\nPilih kesulitan:")
    print("1. Mudah   (8 kesempatan)")
    print("2. Sedang  (6 kesempatan)")
    print("3. Sulit   (4 kesempatan)")
    while True:
        pilih = input("Masukkan nomor (1-3): ").strip()
        if pilih == '1':
            return 8
        elif pilih == '2':
            return 6
        elif pilih == '3':
            return 4
        else:
            print("Pilihan tidak valid!")

def get_category():
    print("\nPilih kategori:")
    categories = list(WORDS.keys())
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    
    while True:
        pilih = input(f"Masukkan nomor kategori (1-{len(categories)}): ").strip()
        if pilih.isdigit():
            idx = int(pilih) - 1
            if 0 <= idx < len(categories):
                return categories[idx]
        print("Pilihan tidak valid!")

def display_word(word, guessed):
    return ' '.join([c if c in guessed else '_' for c in word])

def play_game():
    print("=== WORD GUESSING GAME ===")
    
    category = get_category()
    word = choose_word(category)
    max_attempts = get_difficulty()
    attempts = max_attempts
    guessed = set()
    used_letters = set()
    
    print(f"\nKategori: {category}")
    print(f"Panjang kata: {len(word)} huruf")
    print("Tebak kata yang tersembunyi!")
    
    while attempts > 0:
        print(f"\nKata: {display_word(word, guessed)}")
        print(f"Sisa kesempatan: {attempts}/{max_attempts}")
        if used_letters:
            print(f"Huruf yang dipakai: {', '.join(sorted(used_letters))}")
        
        guess = input("Masukkan 1 huruf atau kata lengkap: ").lower().strip()
        
        if not guess:
            print("Masukkan sesuatu!")
            continue
        
        if len(guess) == 1:
            if not guess.isalpha():
                print("Masukkan huruf!")
                continue
            
            if guess in used_letters:
                print("Huruf ini sudah dipakai!")
                continue
            
            used_letters.add(guess)
            
            if guess in word:
                guessed.add(guess)
                print("Benar!")
                
                if all(c in guessed for c in word):
                    print(f"\nSelamat! Kamu menang! Katanya: {word}")
                    break
            else:
                attempts -= 1
                print(f"Salah! Sisa kesempatan: {attempts}")
        
        elif len(guess) == len(word):
            if guess == word:
                print(f"\nSelamat! Kamu menang! Katanya: {word}")
                break
            else:
                attempts -= 1
                print(f"Salah! Sisa kesempatan: {attempts}")
        
        else:
            print(f"Masukkan tepat 1 huruf atau {len(word)} huruf!")
    
    else:
        print(f"\nKesempatan habis! Katanya adalah: {word}")

if __name__ == "__main__":
    play_game()
