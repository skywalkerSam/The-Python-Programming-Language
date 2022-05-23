# Guess the number game...

from random import *
from pyfiglet import *


def Intro():
    print(figlet_format("Guessing Game )", "big"))
    print("Guess a number between 1 & 10...")

right_guess = randint(0, 10)


attempt = 0
while (attempt <= 6):
    Intro()
    try:
        user_guess = int(input("\t Enter your guessed number: "))
        attempt += 1
        if (user_guess == right_guess):
            print("Well Done! You're a genius...")
            break
        elif (0 < user_guess > 10):
            print("Please enter a number between 1 & 10 :(")
            continue
        else:
            print("Wrong Guess :( Try Again!")
            continue

    except ValueError:
        print("Please enter a number!")
        continue

    except KeyboardInterrupt:
        print("\n Operation canceled by the user :( \n")
        break

    



