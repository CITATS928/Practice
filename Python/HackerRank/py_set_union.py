# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true

import sys

input_data = sys.stdin.read().splitlines()
set_a = set(map(int, input_data[1].split()))
set_b = set(map(int, input_data[3].split()))

new_set = set_a.union(set_b)
result = len(new_set)
sys.stdout.write(str(result))