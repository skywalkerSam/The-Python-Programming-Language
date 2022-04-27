"""
Developer: Sam Skywalker
Purpose: Email verification tool
Date: 12022.04.01.17:05

"""

# import "re" module
import re
from pyfiglet import *


# DRY implementation
def isemail_valid():
    print(figlet_format("Email Validator", "small"))

    # User's email
    user_email = input("Enter an Email address: ")

    # Email pattern
    pattern = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

    # Email validation
    if re.fullmatch(pattern, user_email):
        # Success message
        print("\n\t Affirmative, It's a valid Email address :) \n")
    else:
        # Failure message
        print("\n\t Failed! Please enter a valid Email address & Try Again :( \n")


# Test
if __name__ == "__main__":
    isemail_valid()




