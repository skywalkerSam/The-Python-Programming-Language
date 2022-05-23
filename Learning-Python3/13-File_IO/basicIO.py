# Basic File Operations...


my_file = open("test.txt")
'''
print(my_file.read())

print(my_file.read())   # not printed because the "cursor" is still there :(

my_file.seek(0)
print(my_file.read())
'''

# print(my_file.readline())
# print(my_file.readline())   # Read the file line-by-line...
# print(my_file.readline())


print(my_file.readlines()) 




my_file.close()    # It's always good to close the file when, you're done with it...
