# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

import sys
import collections

input_data = sys.stdin.read().splitlines()

l = list(map(int, input_data[1].split()))

rooms = collections.Counter(l)

for key, values in rooms.items():
    if values == 1:
        print(key)