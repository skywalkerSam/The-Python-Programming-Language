# Collections module...

from collections import Counter, defaultdict, OrderedDict

list_one = [1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9]
line_one = "Starboy on Starbase"
print(Counter(list_one))
print(Counter(line_one))


dict_one = defaultdict(lambda: "It doesn't exists...", {"a": 1, "b": "Sam"})    # Give a callable object to show as default :)
print(dict_one.get("a"))
print(dict_one['c'])


# Normal Dictonary...
dict_two = {}
dict_two["a"] = 3
dict_two['b'] = 33

dict_three = {}
dict_three['b'] = 33
dict_three['a'] = 3

print(dict_two == dict_three)


# False OrderedDict...
'''
Recently, the Python has made Dictionaries ordered by default! So unless you need to maintain older version of Python (older than 3.7), you no longer need to use ordered dict, you can just use regular dictionaries!
'''
dict_five = OrderedDict()
dict_five["a"] = 3
dict_five['b'] = 33

dict_six = OrderedDict()
dict_six['b'] = 33
dict_six["a"] = 3

print(dict_five == dict_six)    # False bacause, OrderedDict must be in a proper order ;)


# True OrderedDict...
dict_seven = OrderedDict()
dict_seven['b'] = 33
dict_seven["a"] = 3

dict_eight = OrderedDict()
dict_eight['b'] = 33
dict_eight["a"] = 3

print(dict_seven == dict_eight)
