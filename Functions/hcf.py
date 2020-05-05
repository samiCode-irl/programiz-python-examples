# Python Program to Find HCF or GCD

# The highest common factor (H.C.F) or greatest common divisor (G.C.D) of two numbers
# is the largest positive integer that perfectly divides the two given numbers.
# For example, the H.C.F of 12 and 14 is 2.

# With Loops


# def calculate_hcf(num1, num2):
#     if num1 > num2:
#         smaller = num2
#     else:
#         smaller = num1

#     for i in range(1, smaller + 1):
#         if (num1 % i == 0) and (num2 % i == 0):
#             hcf = i
#     return(hcf)


# num1 = 54
# num2 = 24
# print(calculate_hcf(num1, num2))


# Euclidean algorithm
# (32, 12) => (12, 8) => (8, 4) => 4

def calculatehcf(x, y):
    if y > x:
        x, y = y, x

    while y:
        x, y = y, x % y
    return x


num1 = 54
num2 = 24

hcf = calculatehcf(num2, num1)
print(hcf)
