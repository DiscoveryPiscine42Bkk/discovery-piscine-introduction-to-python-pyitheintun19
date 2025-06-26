#!/usr/bin/env python

def adds_one(param):
    param += 1
    return param

var = 19
print(f"Initialized variable: {var} ")

var = adds_one(var)
print(f"Adding from the function: {var}")