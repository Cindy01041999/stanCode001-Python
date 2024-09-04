"""
File: CheckerboardKarel.py
Name: Chang Yen Yu
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition:Karel is at (1,1), facing East.
    Post-condition:Karel is at (1,8), facing West.
    """
    while front_is_clear():
        put_beeper_in_line()
        go_back()
        turn_to_next_line()
    turn_left()
    while front_is_clear():
        put_beeper_in_line()


def put_beeper_in_line():
    # function_1: put beeper in line
    """
    Pre-condition:Karel is at (1,1), facing East.
    Post-condition:Karel is at (8,1), facing East.
    """
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():
            move()
    turn_around()
    move()
    if not on_beeper():
        turn_around()
        move()
        put_beeper()
    else:
        turn_around()
        move()


def go_back():
    # function_2: go back to the initial place
    """
    Pre-condition:Karel is at (8,1), facing East.
    Post-condition:Karel is at (1,1) facing West.
    """
    turn_around()
    while front_is_clear():
        move()


def turn_to_next_line():
    # function_3: turn to the next line
    """
    Pre-condition:Karel is at (1,1) facing West.
    Post-condition:Karel is at (1,2) or (2,2), facing East.
    """
    turn_right()
    if front_is_clear():
        if on_beeper():
            move()
            turn_right()
            move()
        else:
            move()
            turn_right()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
