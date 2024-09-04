"""
File: CollectNewspaperKarel.py
Name: Chang Yen Yu
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition:Karel is at the North-western corner of the house, facing East.
    Post-condition:Karel is at the North-western corner of the house, with a beeper, facing East.
    """
    pick_newspaper()
    move_back_to_home()
    put_beeper()


def pick_newspaper():
    # function_1: move to the newspaper
    """
    Pre-condition:Karel is at the North-western corner of the house, facing East.
    Post-condition:Karel is at the outside of the house, with a beeper, facing East.
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def move_back_to_home():
    # function_2: go back to the initial place
    """
    Pre-condition:Karel is at the outside of the house, with a beeper, facing East.
    Post-condition:Karel is at the North-western corner of the house, with a beeper, facing East.
    """
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
