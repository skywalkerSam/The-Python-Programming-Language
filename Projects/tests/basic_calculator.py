

# Basic Calculator;

"""
Author; Sam Skywalker
Purpose; Python Basic Calculator
Date; 15th October of 2020
"""

print('Enter First Number')
num1=int(input())
print('Enter The Operation [+, -, *, /, //, %, ]')
operator=input()
print('Enter Second Number')
num2=int(input())

if operator=='+':
    print('The answer is :- ', num1+num2)
    print('THANKS FOR COMING!')

elif operator=='-':
    print('The answer is :- ', num1-num2)
    print('THANKS FOR COMING!')

elif operator=='*':
    print('The answer is :- ', num1*num2)
    print('THANKS FOR COMING!')

elif operator=='/':
    print('The answer is :- ', num1/num2)
    print('THANKS FOR COMING!')

elif operator=='//':
    print('The answer is :- ', num1//num2)
    print('THANKS FOR COMING!')

elif operator=='%':
    print('The answer is :- ', num1%num2)
    print('THANKS FOR COMING!')

else:
    print('Enter a valid Operation!')
    print('THANKS FOR COMING!')
