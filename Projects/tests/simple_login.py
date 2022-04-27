"""
Dev: Starboy
Aim: Just testing...
Log: 12022.01.31.04:35
"""

def credentials():
    username = input("Enter Your Username:\t")
    password = input("Enter Your Password:\t")
    encrypted_password = len(password) * "X"
    #out
    print("Please Confirm Your Credentials:\n")
    print(f"You're {username} & Your Password is {encrypted_password}")
    return username and password and encrypted_password


while (True):
    credentials()
    confirmation = input("Is This Ok! [ Y/N ]:\t")
    if (confirmation == "Y" or "y"):
        print("Thanks For Your Confirmation :)")
        break
    elif (confirmation == "N" or "n"):
        print("Ok, Let's Try Again!\n")
        continue
    else:
        print("Try Again! Something went wrong at our end :( ")
        continue






