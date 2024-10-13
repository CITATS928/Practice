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