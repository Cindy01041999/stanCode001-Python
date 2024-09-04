"""
File: extension2_number_checker.py
Name: Chang Yen Yu
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    n != EXIT
    m != n, m < n, n % m == 0
    calculate the sum of m, and check if the sum_m >, < or == n
    """
    print('Welcome to the number checker!')
    while True:
        n = int(input('n: '))
        m = 1
        sum_m = 0
        if n == EXIT:
            break
        while m != n and m < n:
            if n % m == 0:
                sum_m += m
                m += 1
            else:
                m += 1
        if sum_m == n:
            print(str(n) + ' is a perfect number.')
        elif sum_m > n:
            print(str(n) + ' is an abundant number.')
        else:  # sum_m < n
            print(str(n) + ' is a deficient number.')
    print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
