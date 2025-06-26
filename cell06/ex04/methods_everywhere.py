#!/usr/bin/env python3
import sys

def shrink(word):
    print(word[:8])

def enlarge(word):
    disp = word + "Z"*(8-len(word))
    print(disp)

param = len(sys.argv) -1
if param < 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)