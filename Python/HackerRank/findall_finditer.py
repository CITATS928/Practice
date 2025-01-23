# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

input_data = sys.stdin.read().strip()
pattern = r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])'

matches = re.findall(pattern, input_data)

if matches:
    for char in matches:
        print(char)
else:
    print(-1)