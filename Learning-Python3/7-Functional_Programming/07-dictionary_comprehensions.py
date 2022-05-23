
"""
Dictionary Comprehensions...

"""

# Being Overcleaver isn't good, code should be readable and, understandable...

my_dictionary = {key: value**2 for key, value in {"a": 1, "b": 2}.items()}
print(my_dictionary)


simple_dict = {
    "a": 1,
    "b": 2
}
dict_one = {key: value**2 for key, value in simple_dict.items() if value %2 == 0}
print(dict_one)



# An exercise_
my_dict = {num:num*2 for num in [1, 2, 3]}
print(my_dict)
