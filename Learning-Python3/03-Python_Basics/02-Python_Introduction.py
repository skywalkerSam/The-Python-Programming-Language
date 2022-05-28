
print('Hello world')

# repl.it  | with google-acc.
# -> glot.io  | can code without signup



# First program;
name = input('Enter your name; ')
print('Hello ' + name)
print('Hello', name)



# Fundamental Data Types;
int
float
bool
str
list
tuple
set
dict
# Custom Data Types -> class
# Specialized Data Types
None   # noting
complex


# int & float;
# -> integer [whole numbers] and floating value [decimal containing numbers]
# -> float takes more memory than int
print(3 + 6)
print(type(3 + 6))
print(3 - 6)
print(3 * 6)
print(3 / 6)
print(type(3 / 6))

print(3 // 6)        # gives integer always
print(type(3 // 6))

print(3 % 6)   # remainder

print(9**2)   # Squre of 9
print(9**3)   # cube of 9

print(3.9 + 6.1)
print(type(3.9 + 6.1))



# Math Functions;
print(round(3.1))   # near value
print(round(3.5))
print(round(3.9))

print(abs(-21))   # absolute value



'''
Developer fundamentals ;
  -> Don't try to learn dictonary
  -> Programming is solving the problems, don't try to memorise everything
  -> Take help of google and other things as a reference
  -> Learn the concepts, they are grammar[OOP] for all programming languages 

'''



# Operator Precedence;
print((9-3)+30-2**2)

# Calculations follows the BODMAS rule
# -> Brackets, Of [Power Of (**)], Division, Multiplcation, Addition & Subtraction


# Complex and bin();
complex

# bin(), binary
print(5)
print(bin(5))   # Binary form of integer value, after 0b thats; 101
print(int('0b101', 2))
print(bin(3))
print(bin(6))
print(bin(9))
print(int('0b1001', 2))



# Variables;
iq = 199   # variable, must be descripted well
print(iq)

_iq = 133   # cvariables can start with letters and underscore (_)
print(_iq)

__iQ = 963   # can do this, but not a good practice
print(__iQ)

user_name_1 = 'star-wars'
print(user_name_1)

User_id1 = 'CaptainMS'
print(User_id1)

IQ = 166   # variables are case sensitive
print(IQ)

pc = 'Desktop'
print(pc)
pc = 'Laptop'   # Variable's value can be changed
print(pc)

# constants
PC = 'Laptop/Desktop'   # Value of this type of variables should not be changed
print(PC)

a, b, c = 3, 6, 9  # rapidly assign value to variable
print(a)
print(b)
print(c)

# Keywords must not be assigned as a variable name



# Expression & Statement;
iq = 199
user_age = iq // 6
      # Expression; iq // 6
      # Statement; user_age = iq // 6
print(iq)
print(user_age)



# Argumented Assignment Operator;
some_value = 3
some_value = 3 + 6
print(some_value)

some_value = 3
some_value = some_value + 6
print(some_value)

some_value = 3
some_value += 6   # best way, argumented assignment operator
print(some_value)

some_value -= 6
print(some_value)

some_value = 3
some_value *= 6
print(some_value)

some_value = 3
some_value /= 6
print(some_value)



# Strings;
str
' hello world '
" Hello World "
''' HELLO WORLD '''
""" HELLO WORLD """

mini_str = 'hello world'
micro_str = "Hello World"

large_str = '''

      WOW
      0 0
       ^
      ---
      
'''

long_str = """

HELLO WORLD,
            I'm Captain Murlidhar Singh

"""

print(mini_str)
print(micro_str)
print(large_str)
print(long_str)

first_name = 'Captain Murlidhar '
last_name = 'Singh'
full_name = first_name + last_name
print(full_name)
print(type(full_name))



# String Concatenation;
# -> Adding the strings
print('hello ' + 'world')   # only work with strings !



# Type Conversion;
int
float
str

a = 100

b = str(a)
print(b)
print(type(b))

c = type(int(b))
print(c)

print(type(int(str(99))))   # same as c



# Escape sequences;
print("today's weather ; ")
print('\ttoday\'s temperature ; 27 degree celcius, \"Mostly Sunny\", wishing \n\t You a great day\\')

# \'
# \"
# \n
# \t
# \\

# ' ' over " "


# Formatted Strings;

# f string
name1 = 'captain'
age1 = '15'
print(f"Hello {name1}, Your Age; {age1} years\n")

# .format()
name2 = 'CAPTAIN_MS'
age2 = '17'
print('Hello {}, Your Age; {} years\n'.format(name2, age2))

# Reverse value
name2 = 'CAPTAIN_MS'
age2 = '17'
print('Hello {1},\t Your Age; {0} years\n'.format(name2, age2))   # 0 & 1

# Assign new variables
print('Hello {name3}, Your Age; {age3} years\n'.format(name3='MS', age3='18'))

# odinary way;
name = "CaptianMS"
age = "16"   # same as; str(16)

print('Hello ' + name + ", " + 'Your age; ' +
      age, 'years\n')   # can use (+) or (,)


# String Indexes / Slicing;
# -> Index starts from 0

program1 = "Hello World"
# "012345678910"
print(program1)
print(program1[0])

# [start:stop:stepover]
print(program1[0:11:1])
print(program1[::])     # blank = default
print(program1[1:11:2])

# Reverse Index [-1, -2, -3, etc.]
print(program1[-1])
print(program1[::-1])   # Reverse whole String



# Immutability;
# -> Can't change / replace the value
program2 = 'hello captain'
print(program2)
# program2[0] = 'H'
# Can't change the value of string, we've to create a new one
program2 = program2 + 'MS'
print(program2)


# Built-In Functions & Methods;
# -> Don't memorise, see the python documentations or other resources as a reference
# -> Functions are also called Actions
int
str
float
print()
type(int)
len('hello')

mystr = 'hello world'
print(mystr[:])
print(len(mystr))

# Methods
print(mystr.capitalize())
print(mystr.upper())
print(mystr.lower())

print(mystr.find('world'))   # Index representation

print(mystr.replace('world', 'captain'))
# String is immutable, We can't change the value but we can re-assign the value
print(mystr)

mystr2 = mystr.replace('world', 'captain')
print(mystr2)   # We've re-assigned the value into another variable
print(mystr)



# Booleans;
bool
True
False

name = 'CaptainMS'
is_cool = False
is_hacker = True

print(bool(0))   # default False
print(bool(1))   # default True
print(bool(3))

print('\n')

print(bool(False))
print(bool(True))
print(bool('False'))   # ?
print(bool('True'))


#  # Exercise: Type Conversion;
# -> How facebook store user's data_

name = 'CaptainMS'
age = '16'
relationship_status = 'single'
print(name, age, relationship_status)

age = '18'
relationship_status = 'It\'s Complicated'
print(name, age, relationship_status)

# f string
print(f"Name; {name}\n Age; {age}\n Relationship Status; {relationship_status}\n")


# Program1; Find the user's age_
birth_year = input('Enter the Year when, you was born; ')
current_year = input('Enter Current year; ')
age2 = int(current_year) - int(birth_year)   # can also use float
print(f"Your age; {age2} Years")



# Commenting the code;
# -> Comment the code for understanding & for future reference
# -> Ctrl + /   ; To comment a whole line

print('hello world')   # Comment after code

'Refered as string comment'
"Refered as string comment"

'''
Refered
as
string
comment

'''

"""
Refered 
as
string
comment

 WOW
 0 0
  ^
 ---

"""

# docstring?


# Exercise: Password Checker
username = input('Enter Username; ')
password = input('Enter Password; ')
print(
    f"\nYour Username; {username}\nYour Password; {'X' * len(password)}\nYour Password Strength;", len(password))






