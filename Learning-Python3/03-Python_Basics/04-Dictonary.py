
# Dictionary;
    #-> Dictionary is an unordered key-value pairs.

dict

dictonary1 = {
    'a': [1, 2, 3],
    'b': 'hello',
    'c': True,
    'first_program': 'Hello World'
}
print(dictonary1)
print(dictonary1['a'])
print(dictonary1['b'])
print(dictonary1['c'])
print(dictonary1['first_program'])



# Typecasting dict into list for using index order
mylist = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'c': True,
        'first_program': 'Hello World'
    },
    {
        'num1': 1,
        'num2': 2,
        'num3': [1, 2, 3]
    }]

print(mylist)
print(mylist[0])
print(mylist[0]['first_program'])

print(mylist[1])
print(mylist[1]['num3'])




# Understanding Data Structures;
# Making data in a structure so that, user can access it through desired methods
# When, which data structure should use, Is a challenge !
# Different data Structures has it's own significance !



# Dictionary Keys;
# -> The key should be a immutable datatype
# -> Same key name will overwrite the previous value
# -> Strings are good for key names
dict
dictionary1 = {

    123: ['123', '321'],
    'hello': "Hello World",
    True: 'True',
    "False": False,
    True: [True, False, "Booleans"]  # overwriting

}
print(dictionary1)
print(dictionary1['hello'])
print(dictionary1[True])



# Dictionary Methods;
# -> Errors aren't good, try to avoid them !
dict
user = {
    "age": 16,
    "height": "168 cm",
    "weight": "97 kg"

}
print(user)
print(user["age"])
# print(user['name'])    #error

# get()
# -> Use get() because it never throws the error, it gives None

print(user.get('name'))  # None
# define default parameter, In case if it already defined it not gonna replace the actual value
print(user.get('name', "username"))

# Another way to creating dictionary
user2 = dict(name="CaptainMS")
print(user2)



# Dictionary Methods 2;
dict

# check
bool
print("age" in user)
print('class' in user)

# keys(), values(), items()
print("age" in user.keys())
print("age" in user.values())
print(user.items())
print('age' in user.items())

# clear()
user.clear()
print(user)

print(user.clear())

# copy()
user = user2.copy()
print(user)

print(user2)

# pop('key')
print(user.pop('name'))
print(user)

# popitem()   | removes any random item from list
print(user2.popitem())
print(user2)

# update({key:value})
print(user.update({"name": "Captian"}))
print(user)





