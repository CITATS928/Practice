"""
https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true

This tool returns the r length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import itertools

in_put = sys.stdin.read().split()
sorted_input0 = sorted(''.join(in_put[0]))

for n in range(1,int(in_put[1])+1):
    combi1 = itertools.combinations(sorted_input0,n)
    for element in combi1:
        print(''.join(element))


#优化
"""
import itertools
import sys

# 读取输入
input_data = sys.stdin.read().split()

#sort
sorted_input = sorted(input_data[0])

#get lenth
length = int(input_data[1])

#获取所有组合(1~length)
for i in range(1, length + 1):
    for combination in itertools.combinations(sorted_input, i):
        print("".join(combination))
"""