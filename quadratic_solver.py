"""
File: quadratic_solver.py
Name:Chang Yen Yu
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Count the roots of (a * x * x + b * x + c = 0)
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	discriminant = float(b * b - 4 * a * c)
	if discriminant > 0:
		math_sqrt = float(math.sqrt(discriminant))
		root1 = (-b + math_sqrt) / (2 * a)
		root2 = (-b - math_sqrt) / (2 * a)
		print('Two roots: ' + str(root1) + ", " + str(root2))
	elif discriminant == 0:
		root3 = -b / (2 * a)
		print('One root: ' + str(root3))
	else:
		print('No real roots')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
