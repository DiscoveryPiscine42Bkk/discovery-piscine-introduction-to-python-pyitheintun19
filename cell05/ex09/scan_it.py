import sys
import re

if len(sys.argv) < 2:
    print("none")

else:
    param1 = sys.argv[1]
    param2 = sys.argv[2]

    search = re.findall(param1, param2, re.IGNORECASE)
    if search:
        print(len(search))
    else:
        print("none")
    