"""
# Generators:
            >_ It's all about generating numbers 'efficiently'.

            >_ All generators are iterable but, not all iterables are generators..

"""

def generator_function(num):
    for i in range(num):
        yield i             # It remembers the last value generated


for item in generator_function(100):
    print(item)
    

g = generator_function(10)
next(g)
next(g)         # A step forward...
print(next(g))

print(next(g))





