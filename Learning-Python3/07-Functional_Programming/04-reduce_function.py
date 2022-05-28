# reduce function() ...


from functools import reduce

list_one = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, list_one, 30))
