# Python Program to Display Fibonacci Sequence Using Recursion


def fibonacci(terms):

    if terms <= 1:
        return terms
    else:
        return(fibonacci(terms - 1) + fibonacci(terms - 2))


for i in range(10):
    print(fibonacci(i))
