# File error handling...

from distutils.log import error
from io import FileIO


with open("test.txt") as file1:
    print(file1.read())


# Using try-except exception handling :)
try:
    with open("test0.x") as file1:
        print(file1.read())

except FileNotFoundError as err:
    print("Sorry, File not found :(")
    # raise err


# File IO error :(
try:
    with open("test.xy") as file1:
        print(file1.read())

except IOError as error:
    print("Sorry, IOError :(")
    # raise error


