# Python Program to Convert Decimal to Binary Using Recursion


def binary(x):
    if x > 1:
        binary(x//2)
    print(x % 2, end='')


binary(34)
