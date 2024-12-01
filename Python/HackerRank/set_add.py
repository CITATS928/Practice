# https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

import sys

input_data = sys.stdin.read().splitlines()

s = set()

for line in input_data[1:]:
    s.add(line)
    # print(line)
    
# print(len(s))
sys.stdout.write(f'{len(s)}')


######################

# 注意事项：sys.stdout.write()方法不会自动换行，需要手动添加换行符
sys.stdout.write(f'{len(s)}\n')

# another way, 直接导入set，不需要循环
s = set(input_data[1:])