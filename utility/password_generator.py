import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    
    if not chars:
        return "Pilih minimal satu opsi!"
    
    return ''.join(random.choice(chars) for _ in range(length))

def get_int(prompt, min_val, max_val):
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
            print(f"Masukkan angka {min_val}-{max_val}!")
        except ValueError:
            print("Masukkan angka!")

def main():
    print("=== PASSWORD GENERATOR ===")
    
    while True:
        length = get_int("Panjang password (6-32): ", 6, 32)
        
        upper = input("Gunakan huruf besar? (y/n): ").lower() == 'y'
        digits = input("Gunakan angka? (y/n): ").lower() == 'y'
        symbols = input("Gunakan simbol? (y/n): ").lower() == 'y'
        
        password = generate_password(length, upper, digits, symbols)
        print(f"\nPassword: {password}")
        
        lagi = input("Buat lagi? (y/n): ").lower()
        if lagi != 'y':
            print("Keluar...")
            break

if __name__ == "__main__":
    main()
