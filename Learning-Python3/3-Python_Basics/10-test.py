"""
Developer: Sam Skywalker
Purpose: Revision stuff
Date: 12022.04.19.03:07
"""

for i, en in enumerate("Hello"):
    print(f"{i}, {en}")


f_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(f_list))

print(type(5E2))

print(5E2 + 10)

print(bin(3))

print(hex(38412))

print(abs(-24))

print(abs(-24))

print(round(24.234, 2))


def f_one():
    '''
    Just a simple function :)
    '''
    for i in range(10):
        i = i**2
        print(i)
    return i


f_one()


# lambda
list_f = [3, 6, 9, 33, 66, 99]
print(list(map(lambda num: num**3, list_f)))


print(f_one.__doc__)
