"""
File: Steeplechase.py
Name: Daisy
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    """
    Pre-condition: Karel is on the left side of the wall, facing East
    Post-condition: Karel is on the right side of the wall
    """
    up()
    move()
    down()


def up():
    """
    Pre-condition: Karel is on the left side of the wall, facing East
    Post-condition: Karel is on the left side of the wall, facing North
    """
    while not front_is_clear():
        turn_left()
        # Facing North
        move()
        turn_right()
        # Facing East


def down():
    """
    Pre-condition: Karel is on the top of the wall, facing East
    Post-condition: Karel is on the ground, facing East
    """
    turn_right()
    # Facing South
    while front_is_clear():
        move()
    turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
