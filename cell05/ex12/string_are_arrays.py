import sys

args = sys.argv[1:]

if not args:
    print("none")
else:
    count = 0
    for arg in args:
        count += sum(1 for ch in arg if ch == 'z')
    if count:
        print("z" * count)
    else:
        print("none")