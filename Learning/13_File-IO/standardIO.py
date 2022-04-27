# Standard way of I/O in python...  

'''
# File modes...
    >_ "r" = Read
            >_ "r+" = Read & write - Cursor always returns to zero.

    >_ "w" = override and write, also creates the file if, doesn't exists already..

    >_ "a" = Appends at the end & keeps appending...

            >_ "x" = Create
'''

# Standard Way...
from turtle import write_docstringdict


with open("test.txt") as a_file:    # It opens the file in 'read' mode by default.
    print(a_file.read())
    # no need to close the file here :)


with open("test0.txt", mode="w") as my_file:
    text = my_file.write("I'm happy")
    print(text)
    
with open("test0.txt", "a") as my_file:
    text = my_file.write(" :)")
    print(text)

with open("test0.txt") as my_file:
    print(my_file.read())


# You can create any type of file & perform operations...
with open("test00.py", "w") as py_file:
    py_file.write("print('Hello, I am a Robot')")
    
with open("test00.py") as py_file:
    print(py_file.read())

with open("test00.py", "a") as py_file:
    py_file.write("\nprint('Sorry, Just kidding :)')")

with open("test00.py") as py_file:
    print(py_file.read())
