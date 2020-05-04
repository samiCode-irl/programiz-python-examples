# Python Program to Print the Fibonacci sequence

# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
# The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.
# This means to say the nth term is the sum of (n-1)th and (n-2)th term.

num = int(input('How many term: '))

n1 = 0
n2 = 1
count = 0

while count < num:
    print(n1)
    nth = n1 + n2

    n1 = n2
    n2 = nth
    count += 1
