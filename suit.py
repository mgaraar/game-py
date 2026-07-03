import random
choices = ['r', 'p', 's']
emojis = {'r': '🪨', 'p': '📄', 's': '✂️'}

while True:
    user_choice = input('masukan input anda (r/p/s): ').lower().strip()
    computer_choice = random.choice(choices)
    if user_choice not in choices:
        print('you input the wrong option')
        continue
    print(f'kamu memilih {emojis[user_choice]}')
    print(f'komputer memilih {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('seri')
    elif user_choice == 'r' and computer_choice == 's' or user_choice == 's' and computer_choice == 'p' or user_choice == 'p' and computer_choice == 'r':
        print('kamu menang!')
    else:
        print('kamu kalah')

    play_again = input("play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Terimakasih sudah bermain!")
        break