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
    codes[] dictionary.

    Ex: import escc

        tc = escc.escapeColors()
        tc.textcolor(bg="BLUE", fgmode="BLINK", fg="GREEN")
        print("This is just another sample string")
        tc.reset() 

    This would print the sample string in green on a blue
    background, and it would also blink the text.

    """

    def __init__(self):
        self.esc = "["
        self.codes = {"RESET": 0,
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

    def textcolor(self, bgmode="RESET", fgmode="RESET", bg=False, fg="WHITE"):
        self.fgmode = self.codes[fgmode]
        self.fg = self.codes[fg] + 30
        self.bgcheck = bg

        if self.bgcheck == False:
            sys.stdout.write("{}{};{}m"
                .format(self.esc, self.fgmode, self.fg))
        else:
            self.bgmode = self.codes[bgmode]
            self.bg = self.codes[bg] + 40

            sys.stdout.write("{}{};{}m{}{};{}m"
                .format(self.esc, self.fgmode, self.fg, self.esc,
                        self.bgmode, self.bg))

    def reset(self):
        sys.stdout.write("{}{}m".format(self.esc, self.codes["RESET"]))
