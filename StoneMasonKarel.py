"""
File: StoneMasonKarel.py
Name: Chang Yen Yu
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition:Karel is at the south-western corner, facing East.
    Post-condition:Karel is at the south-eastern corner, facing East.
    """
    while front_is_clear():
        build_column()
        go_back()
        move_to_next_column()
    build_column()
    go_back()


def build_column():
    # function_1: build the column
    """
    Pre-condition:Karel is at the south-western corner, facing East.
    Post-condition:Karel is at the upper side of the column, facing North.
    """
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
    if not on_beeper():
        put_beeper()


def go_back():
    # function_2: go back to the initial place
    """
    Pre-condition:Karel is at the upper side of the column, facing North.
    Post-condition:Karel is at the south-western corner, facing East.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def move_to_next_column():
    # function_3: move to the next column
    """
    Pre-condition:Karel is at the south-western corner, facing East.
    Post-condition:Karel is at the south-eastern corner, facing East.
    """
    for i in range(4):
        move()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
