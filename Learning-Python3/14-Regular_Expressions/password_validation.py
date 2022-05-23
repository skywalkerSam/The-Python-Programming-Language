"""
Developer: Sam Skywalker
Purpose: A robust password validator
Date:
"""

import re
from pyfiglet import *


def ispassword_valid():
    print(figlet_format("Password Validator", "small"))
    user_pass = input("Enter a password: ")

    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$")

    if re.fullmatch(pattern, user_pass):
        print("\n\t Affirmative, It's a valid password :) \n")
    else:
        print("\n\t Failed! Please enter a strong password & Try Again :( \n")


if __name__ == "__main__":
    ispassword_valid()
    



