# Python Program to Print all Prime Numbers in an Interval
# In this program, you'll learn to print all prime numbers within an interval using for loops and display it.

upper = 1000
lower = 900

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
