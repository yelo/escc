#!/usr/bin/env python
import escc

def main():
    tc = escc.escapeColors()

    tc.textcolor(fg="YELLOW")
    print("FÄRG!")
    tc.reset()

    tc.textcolor(bg="BLUE")
    print("BAKGRUND!")
    tc.reset()

if __name__ == "__main__":
    main()
