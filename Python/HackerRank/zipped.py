"""
https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true
"""


import sys

input_data = sys.stdin.read().split('\n')

N, X = map(int, input_data[0].split())

input_data=input_data[1:len(input_data)]
ls=[]

for line in input_data:
    ls.append(list(map(float, line.split())))

#print(ls)
zipped = zip(*ls)

for score in zipped:
    print(sum(score)/X)

"""
improved version:
import sys
input_data = sys.stdin.read().split('\n')
N, X = map(int, input_data[0].split())

# 读取学生的分数
ls=[list(map(float, line.split())) for line in input_data[1:]]

# 计算每个学生的平均分
for score in zip(*ls):
    print(sum(score)/X)
"""