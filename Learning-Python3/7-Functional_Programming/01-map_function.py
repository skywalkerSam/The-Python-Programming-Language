# Map function...

list_one = [1, 2, 3]

# function()


def multiply_by2(item):
    return item*2


list_two = list(map(multiply_by2, list_one))        # map()
print(list_two)

print(list_one)     # Original list is still the same...
