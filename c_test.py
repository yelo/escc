#!/usr/bin/env python
# Just some nasty examples of how to use it.
import escc
from random import choice

def main():
    tc = escc.escapeColors()

    colors = ["BLACK", "RED", "GREEN", "YELLOW",
              "BLUE", "MAGENTA", "CYAN", "WHITE"]

    modes = ["RESET", "BRIGHT", "DIM", "UNDERLINE",
             "BLINK", "REVERSE", "HIDDEN"]

    for item in colors:
        tc.textcolor(fgmode="RESET", fg=item)
        print("{0}".format(item))
        tc.reset()

    for item in colors:
        tc.textcolor(bgmode="RESET", bg=item)
        print("{0}".format(item))
        tc.reset()

    tc.textcolor(bgmode=choice(modes), fgmode=choice(modes),
                 fg="RED", bg="BLACK")
    print("Happy happy fun mixed mode!")
    tc.reset()

if __name__ == "__main__":
    main()
