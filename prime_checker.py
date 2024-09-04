"""
File: prime_checker.py
Name: Chang Yen Yu
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
import math
EXIT = -100


def main():
	"""
	1. Check if n == EXIT or not.
	2. Check if n % m == 0
	"""
	print('Welcome to the prime checker!')
	n = int(input('n: '))
	m = n - 1
	while n != EXIT:
		if n == 2:
			print(str(n) + ' is a prime number.')
			n = int(input('n: '))
			m = n - 1
		elif n % m == 0:  # n可以被m整除 -> 餘數==0
			print(str(n) + ' is not a prime number.')
			n = int(input('n: '))
			m = n - 1
		elif m > 1:  # n不可以被m整除 -> 餘數!=0
			m = m - 1
		else:
			print(str(n) + ' is a prime number.')
			n = int(input('n: '))
			m = n - 1


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
