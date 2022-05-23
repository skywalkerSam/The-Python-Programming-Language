
# Graphical User Interface ;
# Exercise;
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!

image = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


# Iterate over
for row in image:
    for box in row:
        # conditions
        if (box == 0):
            print(" ", end="")     # because, default == \n
        else:
            print("*", end="")
    # Out the image
    print("")   # For new line everytime


print("\n")


# Reverse
for row in image:
    for box in row:
        if (box == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print("")


print("\n")





# Better-Way;
fill = "*"
empty = " "
for row in image:
    for box in row:
        if (box):
            print(fill, end="")
        else:
            print(empty, end="")
    print("")




# What is good code? ;
    # Clean
    # Readability
    # Predictability
    # DRY (Don't Repeat Yourself) - Making code reusable




# Exercise - Find Duplicates;
list1 = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
originals = set(list1)

for values in list1:
    if (list1.count(values) > 1):
        if (values not in duplicates):
            duplicates.append(values)

print(f"The Actual list; {list1}")
print(f"The duplicates are; {duplicates}")
print(f"The originals ate; {originals}")







