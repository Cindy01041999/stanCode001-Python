"""
File: hailstone.py
Name: Chang Yen Yu
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    n % 2 == 0 -> take half
    n % 2 == 1 -> 3 * n + 1
    Count how many steps will the number become 1.
    """
    print('This program computes Hailstone sequences.')
    number = int(input('Enter a number: '))
    count = 0
    while True:
        if number == 1:
            break
        elif number % 2 == 0:
            print(str(number) + ' is even, so I take half: ' + str(number / 2))
            number = number / 2
            count += 1
        else:
            print(str(number) + ' is odd, so I make 3n+1: ' + str(number * 3 + 1))
            number = number * 3 + 1
            count += 1
    print('It took ' + str(count) + ' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
