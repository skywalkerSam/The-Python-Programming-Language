"""
Developer: Sam Skywalker
Purpose: Guessing game for testing purposes
Date: 12022.04.10.13:09
"""

from random import randint
from pyfiglet import figlet_format
import pdb


# Integration
attempt = 0
current_number = randint(0, 10)
while (attempt <= 10):
    try:
        print(figlet_format("The Guessing Game", "small"))
        print("""
                # Rules:

            1. Enter a number between 0 ~ 10.
            2. You have only 10 attempts
        """)
        # pdb.set_trace()
        user_guess = int(input("Enter your guess: "))
        attempt = attempt + 1
        
        if attempt <= 10 and user_guess == current_number:
            print("\n Damm, You're a genius ;) \n")
            break
        else:
            print(f"{10 - attempt} attempts left...")

    except KeyboardInterrupt:
        print("\n\n Operation cancelled by the user :( \n")
        break

    except ValueError:
        print("\n\n You must enter a number/integer, Ok! \n")
