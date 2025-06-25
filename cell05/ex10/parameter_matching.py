import sys
import re

if len(sys.argv) < 2:
    print("none")

else:
    param = input("What was the parameter? ")
    if re.match(param, sys.argv[1]):
        print("Good job!")
    else:
        print("Nope, sorry...")