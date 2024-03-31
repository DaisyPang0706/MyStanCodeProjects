"""
File: PotholeFilling.py
Name: Daisy
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    #algorithm
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def put_99_beepers():
    """
    Karel will put 99 beepers
    """
    for i in range(99):
        put_beeper()

         
def go_in():
    """
    Pre-condition: Karel is at the upper left of the pothole, facing East
    Post-condition: Karel is in the pothole, facing South
    """
    move()
    turn_right()
    move()


def go_out():
    """
    Pre-condition: Karel is in the pothole, facing South
    Post-condition: Karel is at the upper left of the pothole, facing East
    """
    turn_around()
    move()
    turn_right()
    move()
    

def turn_around():
    """
    Karel will face the opposite direction
    """
    turn_left()
    turn_left()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
