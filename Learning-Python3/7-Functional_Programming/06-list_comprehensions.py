'''
List Comprehensions...

'''

# Simple & easy
my_list = []

for char in "hello":
    print(char)
    my_list.append(char)


print(my_list)


# Using comprehensions...
list_one = [char for char in "hello"]
print(list_one)

list_two = [num for num in range(0, 100)]
print(list_two)

square_list = list(map(lambda num: num**2, list_two))       # lambda
print(square_list)

list_three = [num**2 for num in range(0, 100)]      # Comprehension
print(list_three)

# Filter odds with comprehensions
list_four = [num**2 for num in range(0, 100) if num % 2 == 0]
print(list_four)



'''
Set Comprehensions...

'''
my_set = {num for num in range(0, 100)}
print(my_set)






# list[], set{}, dictionary{:} Comprehensions...
