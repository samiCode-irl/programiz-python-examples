# Python Program to Find Factorial of Number Using Recursion


def factorial(x):
    if x <= 1:
        return x
    else:
        return x * factorial(x - 1)


print(factorial(7))
