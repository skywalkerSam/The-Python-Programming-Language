# Functional Programming...

'''
# What is it ?
        >_  Unlike OOP where It's all about combining data & functions, It's about separating data & functions.

        >_  A function() shouldn't mess up with the outside codebase ..        (A Guideline :)

        >_  Pure functions() ...

'''


# Data
wizard = {
    "name": "Harry Potter",
    "power": "Mindset & The Wand",
    "isgood": True
}


# Function
def attack(power=0):
    feedback = input("Should I increase the power ability?: ")

    if (feedback == "y"):
        power += 10

    elif (feedback == "Y"):
        power += 10

    else:
        "Okay, \n"

    out = f"Attacking by the wand with {power}% of ability..."

    return out


print(attack(75))
