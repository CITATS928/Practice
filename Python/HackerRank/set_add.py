# https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

import sys

input_data = sys.stdin.read().splitlines()

s = set()

for line in input_data[1:]:
    s.add(line)
    # print(line)
    
# print(len(s))
sys.stdout.write(f'{len(s)}')