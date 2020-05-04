# Python Program to Find the Largest Among Three Numbers

num1 = 10
num2 = 100
num3 = 1000

if (num1 >= num2) and (num1 >= num3):
    print(num1)
elif (num2 >= num1) and (num2 >= num3):
    print(num2)
else:
    print(num3)
