
"""
Functions;
    -> We're not limited to the python's pre-build functions, We can create our own functions using ( def ).
    -> Code Reusability - Making code reusable, clean & easy to modify.

A Good Function;
    -> Should do one thing really well.
    -> Should return something.


"""


def say_hello():
    print("Hello my crtetor :)")


say_hello()



# Implementing Reusability;
image = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


def show_image():
    fill = "*"
    empty = " "
    for row in image:
        for box in row:
            if (box):
                print(fill, end="")
            else:
                print(empty, end="")
        print("")


show_image()
show_image()
show_image()



# Parameters & Arguments;

# Parameters;
def say(first_name, last_name):
    print(f"Hello my crtetor :) {first_name} {last_name}")

    # Positional Arguments;
say("Captain", "Skywalker")
say("Captain", "Murlidhar Singh")



# Default Parameters & Keyword Arguments;

# Default Parameters;
def users(username="user", password="root"):    # It sets the default arguments for parameters
    print(f"{username} - {password}")


print("\nDatabase-1\n")
users()
users("Root", "tooR")


# Keyword Arguments;
# It's not a good idea, Use the standard
users(username="user1", password="/home")


# Return;
def sum1(num1, num2):
    print("It can print but, can't give anything without asking for return something...")
    num1 + num2


print(sum1(2, 3))




# sum2
def sum2(num1, num2):
    return num1 + num2      # return
    # print("After returning the values, it exit() the function...")


print(9 + sum2(3, 9))
print(sum2(33, sum2(60, 6)))        # matrix

total = sum2(33, 66)
grand_total = (99 + total)
print(grand_total)


# sum3
def sum3(num1, num2):
    return num1 + num2


print(sum3(10, 20))




# Exercise; Tesla
def checkDriverAge():
    print("""
          ######### Tesla #########
                      #
                      #
                      #

          Welcome to Tesla Model X...
          """)

    age = int(input("Please Confirm Your Age; "))

    if (age > 18):
        print("\nEnjoy Your Ride, Powering On...\n")

    elif (age == 18):
        print("\nCongratulations on your first year of driving, Enjoy the ride, Powering On...\n")
    else:
        print("\nSorry, you are too young to drive this car. Powering off...\n")


checkDriverAge()


# With Default Parameter & without using input()
def checkDriverAge2(age=0):
    print("""
          ######### Tesla #########
                      #
                      #
                      #

          Welcome to Tesla Model X...
          """)

    if (age > 18):
        print("\nEnjoy Your Ride, Powering On...\n")

    elif (age == 18):
        print("\nCongratulations on your first year of driving, Enjoy the ride, Powering On...\n")
    else:
        print("\nSorry, you are too young to drive this car. Powering off...\n")


checkDriverAge2(45)











