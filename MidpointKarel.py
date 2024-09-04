"""
File: MidpointKarel.py
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
    Post-condition:Karel is in the middle of street 1, facing South.
    """
    put_beepers_in_street1()
    pick_up_beepers()


def put_beepers_in_street1():
    # put beepers in street_1
    """
    Pre-condition:Karel is at (1,1), facing East.
    Post-condition:Karel is at the end of street 1, facing East.
    """
    if not front_is_clear():
        put_beeper()
    while front_is_clear():
        move()
        put_beeper()


def pick_up_beepers():
    # function_2: pick up the beepers
    """
    Pre-condition:Karel is at the end of street 1, facing East.
    Post-condition:Karel is in the middle of street 1, facing South.
    """
    turn_around()
    if front_is_clear():
        pick_beeper()
    while front_is_clear():
        move()
        if not on_beeper():
            turn_around()
            move()
            if on_beeper():
                pick_beeper()
            else:
                if facing_east():
                    turn_right()
                else:
                    turn_left()
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
