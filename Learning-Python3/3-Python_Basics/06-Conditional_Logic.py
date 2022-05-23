
# Conditional Logic;
# -> Running the codes by certain conditions
True
False

user_age = False
user_licence = True

if user_age and user_licence:
    print("Ok")
elif user_licence:
    print("Unauthorised Access")
else:
    print("You are unauthorised")

# -Tabs & Spaces have a significance in python




# Truthy & Falsey;
True
False
bool

# True
print(bool('hello'))    # Any String
print(bool(5))          # Any Integer

# False
print(bool(''))     # Empty value
print(bool(0))      # 0
print(bool(None))   # None & False

username = "captain"
password = 123
if username and password:
    print("Ok, Go-On...")
elif password:
    print("Unauthorised Access")
else:
    print("You are unauthorised")



# Ternary Operator / Conditional Expressions;
True
False
water = True
other = "Take Water, Please!" if water else "Your cold coffee is on the way..."
print(other)

water = False
other = "Take Water, Please!" if water else "Your cold coffee is on the way..."
print(other)



# Short Circuiting;
True
False
starship = True
girlfriend = False
if starship and girlfriend:
    print("Have some fun between your work...")
elif starship or girlfriend:
    print("Not sure, Do what's more important!")
else:
    print("Hey! Wait & Focus on your work...")

starship = True
girlfriend = True
if starship and girlfriend:
    print("Have some fun between your work...")
elif starship or girlfriend:
    print("Not sure, Do what's more important!")
else:
    print("Hey! Wait & Focus your work...")




# Logical Operators;
bool
True
False
print(5 > 6)
print(6 > 5)

print(5 == 6)
print(5 != 6)

print('hello' == 'hello')
print('a' > 'b')
print('a' > 'A')
print('b' > 'a')

print(1 < 2 < 3 < 4)
print(1 < 2 > 3 < 4)

print(5 >= 6)
print(5 <= 6)

print(not(True))
print(not(False))



# Exercise_ Logical Operators;
bool
is_magician = True
is_expert = False
if is_expert and is_magician:
    print("you're a master magician ")
elif is_magician and not is_expert:
    print("At least you're getting there")
else:
    print("you need to learn magic!")


'''
# is v/s == ;
bool(1)
bool(0)     # Type conversion

# Equality ( == )
print(True == 1)
print(False == 0)
print(1 == '1')
print([] == 1)
print(10 == 10.0)
print([] == [])
print([1, 2, 3] == [1, 2, 3])
'''


"""
# Exactly same ( is )
print(True is 1)
print(False is 0)
print(1 is '1')
print([] is 1)
print(10 is 10.0)
print([] is [])
print([1, 2, 3] is [1, 2, 3])

print(True is True)
print(0 is 0)
print('1' is '1')
# False because, each new list always stored in a new memory location
print([1, 2, 3] is [1, 2, 3])
print(1 is 1)
print(False is False)
# False because, each new list always stored in a new memory location
print([] is [])

"""

