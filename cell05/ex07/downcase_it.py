import sys

param=len(sys.argv) - 1

if param == 0:
    print("none")
else:
    print(sys.argv[1].lower())  