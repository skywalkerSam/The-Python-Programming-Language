
"""
# Scope;
    -> It just says, what variables do i have access to...

"""
hello = "hello world"

print(hello)

# print(hello2)   - error because, it's out of scope



def fun1():
    hello_ = "Dear Happs"
    print(hello_)


fun1()
# print(hello_)  - error because of scope, it's wrong indentation




"""
# Scope Rules;

"""

a = 1  # - Global Scope


# 1
def confusion():  # - It has it's own universe
    a = 5
    return a


print(a)
print(confusion())

print(confusion())
print(a)



# 2
b = 3


def confusion1():
    return a, b


print(confusion1())




"""
# Rules;

    1- Start with local
    2- Parent local
    3- Global
    4- built-in Python functions

"""

h = 1

def parent():
    a = 21

    def confusion3():
        return a
    return confusion1(), confusion3()


print(parent())
print(a)


def parent1():
    def confusion4():
        return sum
    return confusion4()


print(parent1())




"""
# global Keyword;

"""

total = 0

# 1


def count():
    global total    # global keyword
    total += 1
    return total


count()
count()
print(count())


total1 = 0
# 2


def count1(total1):
    total1 += 1
    return total1


print(count1(count1(count1(total1))))       # better way




"""
nonlocal Keyword;
    -> Redirects to parent local...(Remember Rules !)

"""


def outer():
    x = "outer"

    def inner():
        nonlocal x      # nonlocal Keyword
        x = "nonlocal"
        print("inner x ; ", x)

    inner()
    print("outer x ; ", x)


outer()




"""
Why do we need scope?
    -> Because, we don't have infinity hardware resources, they are limited that's why, we have to make efficient programs.
    -> To make code clean, efficient & reusable..

"""


"""
Python Exam;

    -> Test-1; 24/25

    -> Test-2; 

"""









