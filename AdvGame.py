# File: AdvGame.py

"""
This module is the starter file for the AdvGame class, which implements
the game and is therefore analogous to the TMCourse class in the
teaching machine.  The starter file contains the header lines for the
methods you need for Milestone #1.  As you move on to later milestones,
you will need to add a few more methods as described later in this
handout..  The AdvGame class is responsible for reading the various data
files and assembling the information in the internal data structure,
which consists primarily of AdvRoom and AdvObject values stored in
dictionaries that allow the application to find those values by name.
This class also exports the run method, which is called by the Adventure
function to start the game.necessary to play a game.
"""

from AdvRoom import AdvRoom
from AdvObject import AdvObject
from tokenscanner import TokenScanner

# Constants

MARKER = "-----"

class AdvGame:

    def __init__(self, prefix):
        """Reads the game data from files with the specified prefix."""
        # You complete this code and define any helper methods you need

    def run(self):
        """Plays the adventure game stored in this object."""
        # You complete this code and define any helper methods you need

# Constants

HELP_TEXT = [
    "Welcome to Adventure!",
    "Somewhere nearby is Colossal Cave, where others have found fortunes in",
    "treasure and gold, though it is rumored that some who enter are never",
    "seen again.  Magic is said to work in the cave.  I will be your eyes",
    "and hands.  Direct me with natural English commands; I don't understand",
    "all of the English language, but I do a pretty good job.",
    "",
    "It's important to remember that cave passages turn a lot, and that",
    "leaving a room to the north does not guarantee entering the next from",
    "the south, although it often works out that way.  You'd best make",
    "yourself a map as you go along.",
    "",
    "Much of my vocabulary describes places and is used to move you there.",
    "To move, try words like IN, OUT, EAST, WEST, NORTH, SOUTH, UP, or DOWN.",
    "I also know about a number of objects hidden within the cave which you",
    "can TAKE or DROP.  To see what objects you're carrying, say INVENTORY.",
    "To reprint the detailed description of where you are, say LOOK.  If you",
    "want to end your adventure, say QUIT."
]
