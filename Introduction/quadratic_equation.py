# Python Program to Solve Quadratic Equation
# This program computes roots of a quadratic equation
# when coefficients a, b and c are known.

import math

a = 1
b = 5
c = 6

disc = (b ** 2) - (4 * a * c)

sol1 = (-b+math.sqrt(disc)) / (2 * a)
sol2 = (-b-math.sqrt(disc)) / (2 * a)

print(f'The solutions are {sol1} and {sol2}')
