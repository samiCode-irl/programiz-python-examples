# Python Program to Check Armstrong Number

# abcd... = an + bn + cn + dn + ...
# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

number = 153
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
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
