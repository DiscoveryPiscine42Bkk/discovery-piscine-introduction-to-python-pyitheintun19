#!/usr/bin/env python3

def find_the_redheads(family):
    
    redheads = []
    for name, hair_color in family.items():
        if hair_color.lower() == "red":
            redheads.append(name)
    return redheads

family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red",
}

print(find_the_redheads(family))