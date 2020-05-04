# Python Program to Find the Sum of Natural Numbers

num = 16
sum = 0

if num > 0:
    for n in range(0, num + 1):
        sum += n
    print(sum)
else:
    print('enter positive num')
