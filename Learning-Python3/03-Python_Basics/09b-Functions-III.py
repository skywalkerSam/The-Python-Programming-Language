
# *args & **kwargs ;

def function1(*args):
    return sum(args)


print(function1(3, 6, 9))


def function2(**kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return total


print(function2(num1=33, num2=66))


def function3(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(function3(3, 6, 9, num1=33, num2=66))




# Rule; params, *args, default parameters, **kwargs

def function4(name, *number, iq=369, **age):
    return name, number, iq, age


print(function4("captain", 3, 6, 9, started_year=15, current_age=17))




#Exercise; Functions;

# - My code;
def highest_even(*number):
    highest = max(number)
    if (highest % 2 == 0):
        return highest


print(highest_even(3, 6, 9, 30, 60, 90))




# Other Method;
def highest_even2(numbers):
    even = []
    for item in numbers:
        if (item % 2 == 0):
            even.append(item)
    return max(even)


print(highest_even(3, 6, 9, 30, 60, 90, 306090))


"""
# Walrus Operator ( := )

    -> It's focus is that, how to learn about new features of python.
        -> just search, what's new in Python 3.X
        -> Learn the feature now...

"""

a = "hellooo000"

while ((i := len(a)) > 5):
    print(i)
    a = a[:-1]

print(a)













