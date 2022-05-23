# Decorators-Two


def my_decorator(func):
    def wrap_function():
        print("##################### I'll override everything :) :) ;)")
        func()
        print("##################### I'll override everything :) :) ;)")
    return wrap_function


@my_decorator
def dumb():
    print("I'm a dumb function ;)")


dumb()


def hello():
    print("\n Hello Starboy... \n ")


hello()


# 2
def decorator_two(func):
    def override():
        print(
            "******************************* A mind full of *****************************")
        func()
        print(
            "******************************* A mind full of *****************************")
    return override


@decorator_two
def intro():
    print("I'm your workstation...")


intro()


@my_decorator
def intro_two():
    print("I'm StarbaseONE workstation...")


intro_two()


# Logic
hello_world = decorator_two(hello)
print(hello_world())


# Decorator Pattern...
def decorator_pattern(func):
    def wrap_func(*args, **kwargs):
        ''' Now it can take many arguments as you wish...'''
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        func(*args, **kwargs)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    return wrap_func


@decorator_pattern
def my_world(my_name):
    print(my_name)


my_world("Starboy")


# New World
@decorator_pattern
def new_world(my_name, wish):
    print(f"I'm {my_name} & I want {wish} ;)")


new_world("Starboy", "Starship")
