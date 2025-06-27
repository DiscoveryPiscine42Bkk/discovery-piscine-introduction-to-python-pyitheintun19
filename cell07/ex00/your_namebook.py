#!/usr/bin/env python3

def array_of_names(dict):
    
    arraynames = []
    for first_name, last_name in dict.items():
        full_name = first_name.capitalize() + " " + last_name.capitalize()
        arraynames.append(full_name)
    return arraynames
    

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
