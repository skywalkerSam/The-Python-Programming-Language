# filter function() ...

my_list = [1, 2, 3]


def only_odd(item):
    return item % 2 != 0


print(only_odd(1))
print(only_odd(2))

print(list(filter(only_odd, my_list)))

print(my_list)
