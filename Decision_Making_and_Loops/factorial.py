# Python Program to Find the Factorial of a Number

# The factorial of a number is the product of all the integers from 1 to that number.
# For example, the factorial of 6 is 1*2*3*4*5*6 = 720. Factorial is not defined for negative numbers,
# and the factorial of zero is one, 0! = 1.

num = 7

factorial = 1

if num > 0:
    for i in range(1, num + 1):
        factorial *= i
    print(f'The factorial of {num} is {factorial}.')
elif num == 0:
    print(num, 'factorial is 1.')
else:
    print('Factorial doesn\'t exist.')
