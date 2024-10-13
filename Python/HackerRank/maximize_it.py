"""
https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import itertools

lists=[]
result=[]
input_data = sys.stdin.read().split('\n')

K = int((input_data[0].split())[0])
M = int((input_data[0].split())[1])

for ls in input_data[1:]:
    #因为每行第一个数字是这行的长度，所以要去掉第一个数字
    lists.append(list(map(int, ls[1:].split())))

combination = itertools.product(*lists)
for comb in combination:
    result.append(sum(x*x for x in comb)%M)
print(max(result))

"""
improved version:

import itertools
import sys

input_data = sys.stdin.read().split('\n')
K, M = map(int,input_data[0].split())

# Get the list of lists
lists = [list(map(int, line[1:].split())) for line in input_data[1:]]

max_result = 0

# 计算所有组合，找到最大值
for comb in itertools.product(*lists):
    current_result = sum(x**2 for x in comb)%M
    if current_result > max_result:
        max_result = current_result

print(max_result)
"""