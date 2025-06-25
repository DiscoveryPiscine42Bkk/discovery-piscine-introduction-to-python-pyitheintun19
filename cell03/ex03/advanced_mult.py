import sys

if len(sys.argv) > 1:
    print("none")
    sys.exit()
    
for multiplicand in range(0, 11):
        print(f"Table de {multiplicand}: ", end="")
        for multiplier in range(0, 11):
            product = multiplicand * multiplier
            print(f"{product} ", end="")
        print()