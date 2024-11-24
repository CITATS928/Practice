# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

import sys
import collections

input_data = sys.stdin.read().splitlines()

l = list(map(int, input_data[1].split()))


# Counter 会生成一个字典，每个房间号是key，出现的次数是value。
# 只需找到出现次数为 1 的房间号
rooms = collections.Counter(l)

for key, values in rooms.items():
    if values == 1:
        print(key)


# Another solution
# 用set()去重，然后乘以k，再减去原来的和，这样剩余的数就是比船长多k-1倍的数，再除以k-1，就是captain的房间号
input_data = sys.stdin.read().splitlines()

l = list(map(int, input_data[1].split()))
k=int(input_data[0])

exc = sum(l)

act = sum(set(l))*k

print(int((act-exc)/(k-1)))