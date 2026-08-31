# 1. DATA KURS
KURS = {"USD": 1.0, "IDR": 16000.0, "EUR": 0.92}

# 2. FUNCTION VALIDASI NOMINAL
def input_angka(angka):
    # while True, try/except, cek > 0, return kalau valid
    while True:
        try:
            nilai = int(input(angka))
            if nilai <= 0:
                print('tidak bisa angka 0')
            else:
                return nilai
        except ValueError:
            print('masukan angka !!')
# 3. FUNCTION VALIDASI KURS
def input_kurs(kurs):
    # while True, cek apakah ada di KURS, return kalau valid
    while True:
        nilai = input(kurs).upper()
        if nilai not in KURS:
            print('masukan kurs yang tersedia!')
        else:
            return nilai

# 4. FUNCTION HITUNG KONVERSI
def hitung_konversi(nominal, kurs_asal, kurs_tujuan):
    # rumus: (nominal / KURS[kurs_asal]) * KURS[kurs_tujuan]
    hasil = (nominal / KURS[kurs_asal]) * KURS[kurs_tujuan]
    return hasil
# 5. PROGRAM UTAMA
while True:
    nominal = input_angka('masukan nilai uang: ')
    kurs_awal = input_kurs('masukan kurs asal (IDR/USD/EUR): ')
    kurs_akhir = input_kurs('masukan kurs tujuan (IDR/USD/EUR): ')
    
    hasil = hitung_konversi(nominal, kurs_awal, kurs_akhir)
    print(f'hasil konversi: {hasil}')
    
    # tanya play again
    play_again = input("play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Terimakasih sudah bermain!")
        break