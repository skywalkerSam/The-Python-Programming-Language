# Error Handling -  II

from pyfiglet import *


def Intro():
    print(figlet_format("Division . . .", "script"))


def division():
    input_one = float(input("\t Enter first number: "))
    input_two = float(input("\t Enter second number: "))
    
    print("\t Result: ", input_one / input_two)


while (True):
    try:
        Intro()
        division()
        break

    except ZeroDivisionError:
        print("You can't just divide anything with ZERO :(")
        continue

    except TypeError:
        print("Enter the numbers in decimal, not in words!!!")
        continue

    except ValueError:
        print("Please enter the numbers carefully...")
        continue

    else:
        print("Please, Try Again!")
        continue



   