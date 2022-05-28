'''
Comprehension Test:  Find duplicates

'''

list_one = ['a', 'b', 'c', 'd', 'b', 'n', 'm', 'n', 'a']


# Odinary way...
duplicates = []
for char in list_one:
    if list_one.count(char) > 1:        #  .methods() & functions() are two different things, don't ever try messing with them ;)
        if char not in duplicates:
            duplicates.append(char)

print(duplicates)



# Using comprehensions for this task...
duplicates_two = list(set([char for char in list_one if list_one.count(char) > 1]))
duplicates_two.sort()
print(duplicates_two)


