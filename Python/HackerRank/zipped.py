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
