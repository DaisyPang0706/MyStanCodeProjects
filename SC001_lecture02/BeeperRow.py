"""
File: BeeperRow.py
Name: Daisy
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()


def main():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
pass


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
