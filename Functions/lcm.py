# Python Program to Find LCF


def calculate_hcf(x, y):
    if y > x:
        x, y = y, x

    while y:
        x, y = y, x % y
    return x


def calculate_lcm(x, y):
    lcm = (x * y) // calculate_hcf(x, y)
    return lcm


num1 = 54
num2 = 24

print(calculate_lcm(num2, num1))
