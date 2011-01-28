#!/usr/bin/env python
# A simple wrapper for linux (POSIX?) color escape sequences
# Author: Jimmy Kumpulainen <jimmy.kumpulainen@gmail.com>
#
# to-do: check up error handling guidelines, if there's anything like it.

import sys

esc = "\033["
codes = {"RESET": 0,
         "BRIGHT": 1,
         "DIM": 2,
         "UNDERLINE": 3,
         "BLINK": 5,
         "REVERSE": 7,
         "HIDDEN": 8,

         "BLACK": 0,
         "RED": 1,
         "GREEN": 2,
         "YELLOW": 3,
         "BLUE": 4,
         "MAGENTA": 5,
         "CYAN": 6,
         "WHITE": 7}

def textcolor(bgmode="RESET", fgmode="RESET", bg=False, fg="WHITE", text=False):
    """ Get colored output with escape sequences.

    Available modes: RESET, BRIGHT, DIM, UNDERLINE
                     BLINK, REVERSE, HIDDEN

    Available colors: BLACK, RED, GREEN YELLOW
                      BLUE, MAGENTA, CYAN, WHITE

    """

    bgmode = codes[bgmode]
    fgmode = codes[fgmode]
    fg = codes[fg] + 30

    # I don't know if this is a good way to handle invalid
    # colors and modes, maybe it's prefered to let the user
    # handle exceptions themselves? I Have to check this up somewhere.
    #
    # if fgmode in codes:
    #     pass
    # else:
    #     fail(fgmode)
    #
    # if bgmode in codes:
    #     pass
    # else:
    #     fail(bgmode)
    #
    # if fg in codes:
    #   pass
    # else:
    #     fail(fg)
    #
    # if bg:
    #     if bg in codes:
    #         pass
    #     else:
    #         fail(bg)

    if text:
        if bg:
            bg = codes[bg] + 40
            sys.stdout.write("{0}{1};{2}m{3}{4};{5}m{6}"
                             .format(esc, fgmode, fg, esc, bgmode, bg, text))
        else:
            sys.stdout.write("{0}{1};{2}m{3}".format(esc, fgmode, fg, text))
    else:
        if bg:
            bg = codes[bg] + 40
            sys.stdout.write("{0}{1};{2}m{3}{4};{5}m"
            .format(esc, fgmode, fg, esc, bgmode, bg))
        else:
            sys.stdout.write("{0}{1};{2}m".format(esc, fgmode, fg))

def reset():
    """ Reset output to normal """
    sys.stdout.write("{0}{1}m".format(esc, codes["RESET"]))

def fail(error):
    """ Print an error message if an invalid option is used. """
    print("{0} is not a valid option.".format(error))
    sys.exit()
