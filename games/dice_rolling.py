import random
while True:
    user_input = input('roll the dice? (y/n): ').lower()
    if user_input == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        result = dice1, dice2
        print(result)
    elif user_input == 'n':
        print("thank you for playing!")
        break
    else:
        print("wrong input!!")