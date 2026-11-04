# Tic Tac Toe: Player (X) vs Computer (O)

import random

# Board: list of 9 cells, index 0-8
board = [' ' for _ in range(9)]

def print_board():
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner():
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # baris
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # kolom
        (0, 4, 8), (2, 4, 6)              # diagonal
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    if ' ' not in board:
        return 'Draw'
    return None

def computer_move():
    """Komputer coba menang, blokir, atau acak."""
    # Cek apakah komputer bisa menang
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner() == 'O':
                return
            board[i] = ' '
    
    # Blokir pemain
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner() == 'X':
                board[i] = 'O'
                return
            board[i] = ' '
    
    # Ambil posisi tengah jika kosong
    if board[4] == ' ':
        board[4] = 'O'
        return
    
    # Acak posisi kosong
    empty = [i for i in range(9) if board[i] == ' ']
    if empty:
        board[random.choice(empty)] = 'O'

def play_game():
    print("=== TIC TAC TOE ===")
    print("Kamu = X, Komputer = O")
    print("Pilih posisi 1-9 seperti contoh:\n")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")
    
    while True:
        print_board()
        
        # Giliran pemain
        while True:
            try:
                pilih = int(input("Pilih posisi (1-9): ")) - 1
                if 0 <= pilih <= 8 and board[pilih] == ' ':
                    board[pilih] = 'X'
                    break
                else:
                    print("Posisi tidak valid!")
            except ValueError:
                print("Masukkan angka!")
        
        # Cek pemenang
        winner = check_winner()
        if winner:
            print_board()
            if winner == 'X':
                print("Kamu menang!")
            elif winner == 'O':
                print("Komputer menang!")
            else:
                print("Seri!")
            break
        
        # Giliran komputer
        computer_move()
        
        # Cek pemenang setelah komputer
        winner = check_winner()
        if winner:
            print_board()
            if winner == 'X':
                print("Kamu menang!")
            elif winner == 'O':
                print("Komputer menang!")
            else:
                print("Seri!")
            break

if __name__ == "__main__":
    play_game()
