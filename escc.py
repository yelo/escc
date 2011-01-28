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

    except KeyError:
        pass

def reset():
    """ Reset output to normal """
    sys.stdout.write("{0}{1}m".format(esc, codes["RESET"]))
