"""
https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    strings=s.split(' ')
    for i in range(len(strings)):
        strings[i]=strings[i].capitalize()
    return ' '.join(strings)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
