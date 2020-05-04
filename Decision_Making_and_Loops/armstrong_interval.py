# Python Program to Check Armstrong Number

lower = 100
upper = 2000

for number in range(lower, upper + 1):
    num = number
    n = len(str(number))
    count = 0
    arm = 0

    while count < n:
        letter = int(num % 10)
        arm += (letter ** n)
        count += 1
        num = num / 10

    if number == arm:
        print(number)
