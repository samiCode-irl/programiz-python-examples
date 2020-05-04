# Python Program to Calculate the Area of a Triangle
# In this program, you'll learn to calculate the area
# of a triangle and display it

import math

a = 5
b = 6
c = 7

s = (a+b+c) / 2
area = math.sqrt((s * (s - a) * (s - b) * (s - c)))

print('Area of triangle: %0.3f' % (area))
