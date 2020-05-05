# Python Program to Find the Factors of a Number


def find_factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)


num = 320
find_factors(num)
