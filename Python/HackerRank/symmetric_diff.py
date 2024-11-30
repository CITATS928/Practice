# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

import sys

input_data = sys.stdin.read().splitlines()
set_a = set(map(int, input_data[1].split()))
set_b = set(map(int, input_data[3].split()))

set_union = set_a.union(set_b)
set_intersection = set_a.intersection(set_b)

set_final = sorted(set_union.difference(set_intersection))
for num in set_final:
    print(num)
