# https://www.hackerrank.com/challenges/re-start-re-end/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

input_data = sys.stdin.read().splitlines()
S = input_data[0]
k = input_data[1]

pattern = f'(?={re.escape(k)})'
matches = list(re.finditer(pattern, S))

if matches:
    for char in matches:
        start = char.start()
        end = start + len(k) - 1
        print((start, end))
else:
    print((-1, -1))