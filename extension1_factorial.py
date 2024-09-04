"""
File: extension1_factorial.py
Name: Chang Yen Yu
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	n! = 1*2*3*4...*n
	0! = 1
	1! = 1
	n! = n * (n-1)!
	"""
	print('Welcome to stanCode factorial master!')
	n = int(input('Give me a number, and I will list the answer of factorial: '))
	while True:
		if n == EXIT:
			break
		elif n == 0 or n == 1:
			print('Answer: 1')
			n = int(input('Give me a number, and I will list the answer of factorial: '))
		else:
			print('Answer: ' + str(factorial(n)))
			n = int(input('Give me a number, and I will list the answer of factorial: '))
	print('------See ya!------')


def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n-1)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()
