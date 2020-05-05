# Python Program to Find Sum of Natural Numbers Using Recursion


def sum(x):
    if x <= 1:
        return x
    else:
        return(x + sum(x - 1))


print(sum(16))
