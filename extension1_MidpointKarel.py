"""
File: extension1_MidpointKarel.py
Name: Chang Yen-Yu
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition:Karel is at (1,1), facing East.
    Post-condition:Karel is in the middle of the 1st street, facing South.
    """
    go_up_to_the_middle()
    go_down_to_the_middle()


def go_up_to_the_middle():
    # function_1: Karel goes up to the middle of the highest street.
    """
    Pre-condition:Karel is at (1,1), facing East.
    Post-condition:Karel is in the middle of the highest street, facing North.
    """
    turn_left()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            turn_right()
            move()
            turn_left()


def go_down_to_the_middle():
    # function_2: Karel goes down to the middle of the 1st street.
    """
    Pre-condition:Karel is in the middle of the highest street, facing North.
    Post-condition:Karel is in the middle of the 1st street, facing South.
    """
    turn_around()
    while front_is_clear():
        move()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
