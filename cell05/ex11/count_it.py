import sys

param = sys.argv[1:]  

if not param:
    print("none")
else:
    print("parameters: ", len(param))
    for arg in sys.argv[1:]:
        print(f"{arg} ({len(arg)})", end=" ")
        print()