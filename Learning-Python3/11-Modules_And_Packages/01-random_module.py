# Using random module...

import random
from tkinter.tix import ListNoteBook


print(dir(random))
# print(help(random))

print(random.random())
print(random.randint(1, 100))

print(random.choice([1, 2, 3, 4, 5, 6]))

list_one = [3, 6, 9, 33, 66, 99]
random.shuffle(list_one)
print(list_one)


print(random)