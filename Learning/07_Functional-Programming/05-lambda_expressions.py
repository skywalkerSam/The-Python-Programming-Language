# Lambda Function Expressions...

"""
lambda usage:

    >_ To create anonymous functions which doesn't get stored in memory.

    >_ Pattern -  lambda param: function

"""

# 1 - Normal Expression
from random import randint
from functools import reduce
my_list = [3, 6, 9]

out = list(map(lambda item: item*2, my_list))
print(out)


# 2 - Random Implementation

random_list = [randint(0, 100), randint(0, 100), randint(0, 100)]
print(list(map(lambda stuff: stuff*2, random_list)))


# 3 - Filter Implementation (Odds)
random_list_two = [randint(0, 100), randint(0, 100), randint(0, 100)]
print(list(filter(lambda stuff: stuff % 2 != 0, random_list_two)))


# 4 - Reduce Implementation
list_three = [1, 2, 3, 4]


def reduce_one(acc, item):      # Stock reduce
    print(acc, item)
    return acc + item


print(reduce(reduce_one, list_three, 10))

# Simple & sweet reduce()
print(reduce(lambda acc, item: acc + item, list_three, 10))


# 5 - Lambda Expression Exercise: Squares
ultimate_list = [2, 4, 6]
print(list(map(lambda item: item**2, ultimate_list)))


# 6 - Lambda Expression Exercise: Sort
tuple_one = [(4, 3), (0, 2), (10, -1), (9, 9)]

tuple_one.sort()    # Simple sort() method
print(tuple_one)


# Sorting based on second element using lambda
tuple_one.sort(key=lambda item: item[1])
print(tuple_one)
