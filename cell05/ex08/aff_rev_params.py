import sys

param = sys.argv[1:]  

if not param:
    print("none")
else:
    for arg in reversed(param):
        print(arg)