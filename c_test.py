#!/usr/bin/env python
import escc

def main():
    tc = escc.escapeColors()

    tc.textcolor(FG="YELLOW")
    print("FÄRG!")
    tc.reset()

    tc.textcolor(BG="BLUE")
    print("BAKGRUND!")
    tc.reset()

if __name__ == "__main__":
    main()
