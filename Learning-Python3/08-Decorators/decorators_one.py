'''
Decorators:
        >_ functions are like variables in python.

        >_ functions, first class citizens

        >_ @decorators supercharges the function()

'''


def hello():
    return "Hello..."


print(hello())

dumb = hello()
print(dumb)

del hello         # It deleted the hello() but, didn't ereased the memory of it. (Like, love ;)
# print(hello())
print(dumb)     # Because, It's still in memory
dumb = "I'm still here :)"

def dumb_function():
    return "I'm a dumb function ;)"


def make_function(func):
    return func()


print(make_function(dumb_function))

print(dumb)

