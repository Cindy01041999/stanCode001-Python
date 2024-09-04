"""
File: extension3_triangular_checker.py
Name: Chang Yen Yu
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    n != EXIT
    n == x * (x + 1) / 2 -> n is a triangular num
    n < x * (x + 1) / 2 -> n is not a triangular num
    """
    print('Welcome to the triangular number checker!')
    while True:
        n = int(input('n: '))
        x = 1
        T = x * (x + 1) / 2
        if n == EXIT:
            break
        while True:
            if n > T:
                x += 1
                T = x * (x + 1) / 2
            elif n < T:
                print(str(n) + ' is not a triangular number.')
                break
            else:  # n == T
                print(str(n) + ' is a triangular number.')
                break
    print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
