#!/usr/bin/env python
import escc

def main():
    tc = escc.escapeColors()

    tc.textcolor(fg="YELLOW")
    print("Text-color!")
    tc.reset()

    tc.textcolor(bg="BLUE")
    print("Background-color!")
    tc.reset()

    tc.textcolor(bgmode="DIM", fg="BLUE", bg="YELLOW")
    print("We even have mixed-mode!")
    tc.reset()

if __name__ == "__main__":
    main()
