#!/usr/bin/env python
# Just some nasty sample output
import escc as tc

def main():
    colors = ["BLACK", "RED", "GREEN", "YELLOW",
              "BLUE", "MAGENTA", "CYAN", "WHITE"]

    print("text-colors:\n")
    for item in colors:
        tc.textcolor(fg=item)
        print("\t{0} ".format(item.capitalize()))
    tc.reset()

    print("\n\nbackground-colors:\n")
    for item in colors:
        tc.textcolor(bg=item)
        print("\t {0} ".format(item.capitalize()))
    tc.reset()

    print("\n")

    tc.textcolor(fg="WHITE", text="I")
    tc.textcolor(fg="RED", text="HEART")
    tc.textcolor(bg="BLUE", fg="WHITE", text="ARCH")
    tc.textcolor(bgmode="DIM", bg="WHITE", fg="BLACK", text="LINUX\n")
    tc.reset()

if __name__ == "__main__":
    main()
