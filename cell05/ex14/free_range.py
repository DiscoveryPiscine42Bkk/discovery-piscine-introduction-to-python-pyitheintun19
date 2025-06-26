import sys

param = sys.argv

if len(param) - 1 !=2:
    print("none")
else:
    num =  []
    numb1 = int(param[1])
    numb2 = int(param[2])
    for i in range(numb1, numb2 + 1):
        num.append(i)
    print(num)