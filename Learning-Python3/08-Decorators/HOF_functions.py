"""
Higher order functions(HOF):
                        >_ A function() that takes a function as parameter or, returns a function to enhance it.

                        >_ map(), filter(), reduce() & stuff which takes a function as parameter are termed as HOF..

"""


# Here's an example:
def machine_learning():
    return "I teach machines or, machines learn through me"


def deep_learning():
    return ""


# HOF
def artificial_intelligence(method1):
    return method1


print(artificial_intelligence(machine_learning()))


# ex-Two
def ai(machine_learning):
    return machine_learning


print(ai(machine_learning()))


# ex-Three
dumb_list = [num for num in range(0, 32)]

stuff = list(map(lambda num: num**2, dumb_list))
print(stuff)

stuff_two = list(num**3 for num in range(0, 100) if num%2 != 0)
print(stuff_two)
    