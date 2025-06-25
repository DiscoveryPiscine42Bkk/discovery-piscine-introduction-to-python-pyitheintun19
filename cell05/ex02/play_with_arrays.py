original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for new in range(len(original_array)):
    if original_array[new] >=5:
        new_array.append(original_array[new]+2)

print(f"Original array: {original_array}")
print(f"New array: {new_array}")