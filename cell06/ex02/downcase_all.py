#!/usr/bin/env python
def downcase_all(argument):
      return argument.lower()


import sys
param = sys.argv

if len(param) == 1:
    print("none")
else:
     for arg in range(1, len(param)):
         print(downcase_all(param[arg]), end=" ")
         print()