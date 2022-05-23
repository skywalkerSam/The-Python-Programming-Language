"""
# Fibonacci Numbers:
                    >_ Starts from 0 & 1.

                    >_ a + b = c

"""

def fibonacci_nums(fib_index):
    a = 0
    b = 1
    for i in range(fib_index):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fibonacci_nums(2100):
    print(x)

