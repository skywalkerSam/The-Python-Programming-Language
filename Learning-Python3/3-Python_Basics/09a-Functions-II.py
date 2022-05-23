
# Methods vs Functions;

"""
    # Functions;

list()
print()
input()
str()
etc.


    # User-Defined Function;

def hello():
    print("Hello Sir...")


hello()



    # Methods

.count()
"string".captitalize()
.index()
.isalpha()
.isalnum()
.islower()
etc.

"""



# Docstrings;
def test(a):
    '''
    Info; Print the value given by the user...
    '''
    print(a)


test("hello")


# > See the documentation of the function()

help(test)

print(test.__doc__)




# Clean code;

def is_even(num):
    return (num % 2 == 0)


print(is_even(90))
print(is_even(91))


"""
#1
def is_even(num):
    if (num % 2 == 0):
        return True
    elif (num % 2 != 0):
        return False


print(is_even(20))
print(is_even(21))


#2
def is_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False


print(is_even(30))
print(is_even(31))


#3
def is_even(num):
    if (num % 2 == 0):
        return True


print(is_even(30))
print(is_even(31))


#4 - Clean & Best...

def is_even(num):
    return (num % 2 == 0)


print(is_even(90))
print(is_even(91))


"""







