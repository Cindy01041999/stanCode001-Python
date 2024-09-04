"""
File: rocket.py
Name: Chang Yen Yu
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    Split the rocket into 6 parts, write the code for each part, and combine together.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end='')
        for j in range(i+1):
            print('/', end='')
        for j in range(i+1):
            print('\\', end='')
        print('')


def belt():
    print('+', end='')
    for i in range(1):
        for j in range(SIZE * 2):
            print('=', end='')
    print('+', end='')
    print('')


def upper():
    for i in range(SIZE):
        for j in range(1):
            print('|', end='')
        for j in range(SIZE-1-i):
            print('.', end='')
        for j in range(i+1):
            print('/' + '\\', end='')
        for j in range(SIZE-1-i):
            print('.', end='')
        for j in range(1):
            print('|', end='')
        print('')


def lower():
    for i in range(SIZE):
        for j in range(1):
            print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(SIZE-i):
            print('\\' + '/', end='')
        for j in range(i):
            print('.', end='')
        for j in range(1):
            print('|', end='')
        print('')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
