import random

SYMBOLS = ["🍒", "🍋", "🍊", "🍇", "🔔", "💎"]

def spin():
    return [random.choice(SYMBOLS) for _ in range(3)]

def check_win(reels):
    a, b, c = reels
    
    if a == b == c:
        multipliers = {
            "🍒": 5,
            "🍋": 8,
            "🍊": 10,
            "🍇": 15,
            "🔔": 25,
            "💎": 50
        }
        return True, f"3x {a}", multipliers.get(a, 5)
    
    elif a == b or b == c or a == c:
        matched = a if a == b or a == c else b
        return True, f"2x {matched}", 2
    
    return False, "", 0

def play_slot():
    saldo = 100000  # saldo awal
    print("=== SLOT MACHINE ===")
    print(f"Saldo awal kamu: Rp {saldo:,}")
    print("3 simbol sama = hadiah besar, 2 simbol sama = 2x taruhan\n")
    
    while saldo > 0:
        print(f"\nSaldo kamu: Rp {saldo:,}")
        
        try:
            bet = int(input("Masukkan taruhan (atau 0 untuk keluar): "))
        except ValueError:
            print("Masukkan angka!")
            continue
        
        if bet == 0:
            print(f"\nTerima kasih! Sisa saldo: Rp {saldo:,}")
            break
        
        if bet < 0:
            print("Taruhan tidak boleh negatif!")
            continue
        
        if bet > saldo:
            print(f"Taruhan melebihi saldo! Saldo kamu: Rp {saldo:,}")
            continue
        
        print(f"\nTaruhanmu: Rp {bet:,}")
        input("Tekan Enter untuk spin...")
        
        reels = spin()
        print(f"\n {' | '.join(reels)}")
        
        win, desc, multiplier = check_win(reels)
        
        if win:
            prize = bet * multiplier
            saldo += prize
            print(f"Kamu dapat {desc}! Multiplier: {multiplier}x")
            print(f"Hadiah: +Rp {prize:,}")
            print(f"Saldo sekarang: Rp {saldo:,}")
        else:
            saldo -= bet
            print(f"Tidak menang. -Rp {bet:,}")
            print(f"Saldo sekarang: Rp {saldo:,}")
    
    else:
        print("\n💸 KAMU BANKRUT!")
        print("Saldo kamu habis. Game over!")

if __name__ == "__main__":
    play_slot()
