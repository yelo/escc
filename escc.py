#!/usr/bin/env python
# A simple wrapper for linux (POSIX?) color escape sequences
# To-do: check up error handling guidelines, if there's anything like it.
# yelo@yaoi.se
import sys

class escapeColors:
    """Get colored output with escape sequences.

    This is just a small utility to get
    colored output with the aid of escape sequences,
    the available modes and colors hides inside the
    codes-dictionary.

    Example:
        #!/usr/bin/env python
        import escc

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

    def textcolor(self, bgmode="RESET", fgmode="RESET", bg=False, fg="WHITE"):
        self.bgmode = bgmode
        self.fgmode = fgmode
        self.bg = bg
        self.fg = fg

        # I don't know if this is a good way to handle invalid
        # colors and modes, maybe it's prefered to let the user
        # handle exceptions themselves? I Have to check this up somewhere.
        #
        # if self.fgmode in self.codes:
        #     pass
        # else:
        #     escapeColors().fail(self.fgmode)
        #
        # if self.bgmode in self.codes:
        #     pass
        # else:
        #     escapeColors().fail(self.bgmode)
        #
        # if self.fg in self.codes:
        #   pass
        # else:
        #     escapeColors().fail(self.fg)
        #
        # if self.bg:
        #     if self.bg in self.codes:
        #         pass
        #     else:
        #         escapeColors().fail(self.bg)

        self.bgmode = self.codes[bgmode]
        self.fgmode = self.codes[self.fgmode]
        self.fg = self.codes[self.fg] + 30

        if bg:
            self.bg = self.codes[bg] + 40
            sys.stdout.write("{0}{1};{2}m{3}{4};{5}m"
            .format(self.esc, self.fgmode, self.fg, self.esc,
                    self.bgmode, self.bg))
        else:
            sys.stdout.write("{0}{1};{2}m"
            .format(self.esc, self.fgmode, self.fg))

    def reset(self):
        sys.stdout.write("{0}{1}m".format(self.esc, self.codes["RESET"]))

    def fail(self, error):
        self.error = error
        print("{0} is not a valid option.".format(self.error))
        sys.exit()
