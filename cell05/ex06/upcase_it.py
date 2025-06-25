import sys

param = sys.argv[1:]  

if not param:
    print("none")
else:
    print(sys.argv[1].upper())