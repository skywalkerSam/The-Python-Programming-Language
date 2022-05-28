# Performance Check

from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        time1 = time()
        outcome = func(*args, **kwargs)
        time2 = time()
        print(f"Took {time2 - time1} sec.")
        return outcome
    return wrapper


@performance
def calculation():
    for num in range(10000000):
        num**2


calculation()

