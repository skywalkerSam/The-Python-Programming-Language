"""
# Generators:
             >_ It's all about calculating and doing stuff efficiently or, performance.

             >_ You've a simple program & it takes much time, junk!

"""

from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Took:  {t2 - t1} Sec.")
        return result
    return wrapper


@performance
def test1():
    for num in range(100000000):    # range() is also a generator :)
        num**2


@performance
def test2():
    for num in list(range(100000000)):
        num**2


# test1()
# test2()


# A Generator
def general_function(num):
    for i in range(num):
        yield i
        

for i in general_function(100):
    print(i)


last_num = general_function(100)
next(last_num)
print(next(last_num))
