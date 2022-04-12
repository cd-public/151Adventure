# File: Adventure.py

"""This program plays the a text-based Adventure game."""

from AdvGame import AdvGame

# Constants

DATA_FILE_PREFIX = "Crowther"

# Main program

def adventure():
    game = AdvGame(DATA_FILE_PREFIX)
    game.run()

# Startup code

if __name__ == "__main__":
    adventure()
