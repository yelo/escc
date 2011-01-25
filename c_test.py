#!/usr/bin/env python
# just some nasty examples of how to use it
import escc

def main():
    tc = escc.escapeColors()

    tc.textcolor(fg="YELLOW")
    print("Text color!")
    tc.reset()

    tc.textcolor(bg="BLUE")
    print("Background color!")
    tc.reset()

    tc.textcolor(bgmode="DIM", fg="BLUE", bg="YELLOW")
    print("We even have a fancy mixed mode!")
    tc.reset()

    tc.modes()

if __name__ == "__main__":
    main()
