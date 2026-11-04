def check_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Minimal 8 karakter")
    
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Tambahkan huruf kecil")
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Tambahkan huruf besar")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Tambahkan angka")
    
    if any(not c.isalnum() for c in password):
        score += 1
    else:
        feedback.append("Tambahkan simbol (!@#$%&)")
    
    # Klasifikasi
    if score == 5:
        level = "Sangat Kuat"
    elif score == 4:
        level = "Kuat"
    elif score == 3:
        level = "Sedang"
    elif score == 2:
        level = "Lemah"
    else:
        level = "Sangat Lemah"
    
    return level, feedback

def main():
    print("=== PASSWORD STRENGTH CHECKER ===")
    
    while True:
        password = input("\nMasukkan password (atau 'q' untuk keluar): ")
        
        if password.lower() == 'q':
            print("Keluar...")
            break
        
        level, feedback = check_strength(password)
        print(f"\nKekuatan: {level}")
        
        if feedback:
            print("Saran perbaikan:")
            for item in feedback:
                print(f"- {item}")
        else:
            print("Passwordmu sudah bagus!")

if __name__ == "__main__":
    main()
