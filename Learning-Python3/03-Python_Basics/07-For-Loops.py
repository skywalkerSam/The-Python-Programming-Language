
# for loops;
for item in "Captain Skywalker":    # it creates a variable - item
    print(item)

for item in '1234567890':
    print(item)

for item in [369, "hello", True, 1319]:     # works with different datatypes also
    print(item)

for item in {369: "hello", True: 1319}:
    print(item)

for item in (369, "hello", True, 1319):
    print(item)

    # Matrix / loop under loop
for item in [369, "hello", True, 1319]:
    for x in [1, 2, 3, 4]:
        print(x, item)



# Iterables / Iterate;
    # -> Could be Strings, list[], tuple(), set{}, dict{:}
    # -> Goes one by one to check every item in collection

    # Iterate over dict{:}
user1 = {
    "name": "Unknown",
    'age': "Whatever",
    'is_concious': True
}

for keys in user1:
    print(keys)

   # .items()
for item in user1.items():
    print(item)

    # .keys()
for key in user1.keys():
    print(key)

    # .values()
for value in user1.values():
    print(value)

   # key, value
for key, value in user1.items():
    print(key, value)

   # key-value, f-string
for key, value in user1.items():
    print(f"{key}-{value}")



# Exercise: Tricky Counter ;
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
counter = 0
for item in list1:
    counter = counter + item
print("The sum is", counter)



# range() ;
range

for numbers in range(1, 101):     # ( _ ) represents a variable for instant use
    print(numbers)

for _ in range(1, 11):     # ( _ ) represents a variable for instant use
    print(_)

for _ in range(1, 11, 2):       # Structure;  start : stop : jump/skip
    print(_)

# If you wanna reverse it, give it the reverse value.
for _ in range(11, 0, -1):
    print(_)

for _ in range(11, 0, -2):
    print(_)

for _ in range(3):              # Repeating value
    print(list(range(1, 11)))       # type conversion & using range()

for _ in range(1):
    print(list(range(0, 22)))


# Totaling program
E = 0
for numbers in range(1, 101):
    E = E + numbers
print(f"Total(E) sum is, {E}")



# enumerate() ;
enumerate

for char in enumerate("Hellooo"):       # Represents with Index
    print(char)

# Works with list, tuple & more
for index, character in enumerate(["Hello", '123', 'captain']):
    print(index, "-", character)

    # Exercise, find & print the index of 50 ;
for i, c in enumerate(list(range(100))):        # Means, 0 to 99
    # print(i, c)
    if c == 50:
        print(f'Index of 50 is, {i}')











