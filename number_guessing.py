''''''
# feature that i used for the program :
# random nomor generator (random.radint)
# max attempt for player (5 attempt)
# if player input beside of int in the program, the program will give a warning to guess in number not string (try/except ValueError)
# program give a hint if player guess is to high or low (ilif/else)
# The program displays the number of remaining guessing attempts. (remaining variabel)
# win detection 
# lose detection
# best score system 
# new record
# feature to play again
''''''
import random

best_score = None

while True:                                    
    random_number = random.randint(1, 10)
    max_attempts = 5

    for attempt_number in range(1, max_attempts + 1):   
        remaining = max_attempts - attempt_number
        try:
            guess = int(input("come on take a guess the number between 1 - 10: "))
        except ValueError:
            print(f"That's not a number!, you have {remaining} attempt again")
            continue

        if guess == random_number:
            print(f"woah you get it in {attempt_number} attempt, cool!")
            if best_score is None or attempt_number < best_score:
                best_score = attempt_number
                print("new record!")
            break
        elif guess > random_number:
            print(f"too high !, you have {remaining} attempt again")
        else:
            print(f"too low !, you have {remaining} attempt again")
    else:
        print(f"You've run out of chances. The number correct is {random_number}")

    if best_score is not None:
        print(f"your best score so far is in {best_score} attempt")

    play_again = input("play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break

