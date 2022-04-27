# Error Handling

from pyfiglet import *


def Intro():
    print(figlet_format("Starbike . . .", "script"))


try_limit = 0
while (try_limit <= 3):
    Intro()
    try:
        user_age = int(input("\t Enter your age: "))
        if (user_age >= 18):
            print("Cool, You can drive :) \n \t Powering On The Engine...")
            break

    except ValueError:
        print("Please enter your age! Not your username!!!")
        continue

    # except ZeroDivisionError:
    #     print("Age can't be ZERO :(")
    #     continue

    else:
        print("Oops! Looks like you can't drive today :(")
        continue

    finally:
        # print("I can still run after everything...")
        try_limit = try_limit + 1















