#!/usr/bin/env python
# A simple wrapper for linux (POSIX?) color escape sequences
# to-do: exceptions, make it failsafe
# yelo@yaoi.se
import sys

class escapeColors:
    """Get colored output with escape sequences.

    This is just a small utility to get
    colored output with the aid of escape sequences,
    the available modes and colors hides inside the
    CODES[] array.

    Ex: import escc

        tc = escc.escapeColors()
        tc.textcolor(BG="BLUE", FGMODE="BLINK", FG="GREEN")
        print("This is just another sample string")
        tc.reset() 

    This would print the sample string in green on a blue
    background, and it would also blink the text.

    """

    def __init__(self):
        self.ESC = "["
        self.CODES = {"RESET": 0,
                      "BRIGHT": 1,
                      "DIM": 2,
                      "UNDERLINE": 3,
                      "BLINK": 4,
                      "REVERSE": 5,
                      "HIDDEN": 8,

                      "BLACK": 0,
                      "RED": 1,
                      "GREEN": 2,
                      "YELLOW": 3,
                      "BLUE": 4,
                      "MAGENTA": 5,
                      "CYAN": 6,
                      "WHITE": 7}

    def textcolor(self, BGMODE="RESET", FGMODE="RESET", BG=False, FG="WHITE"):
        self.FGMODE = self.CODES[FGMODE]
        self.FG = self.CODES[FG] + 30
        self.BGCHECK = BG
        if self.BGCHECK == False:
            sys.stdout.write("{}{};{}m"
                .format(self.ESC, self.FGMODE, self.FG))
        else:
            self.BGMODE = self.CODES[BGMODE]
            self.BG = self.CODES[BG] + 40
            sys.stdout.write("{}{};{}m{}{};{}m"
                .format(self.ESC, self.FGMODE, self.FG, self.ESC,
                        self.BGMODE, self.BG))

    def reset(self):
        sys.stdout.write("{}{}m".format(self.ESC, self.CODES["RESET"]))
