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
#print(in_put)
sorted_input0 = sorted(''.join(in_put[0]))
#combi=itertools.combinations(sorted_input0,int(in_put[1]))
for n in range(1,int(in_put[1])+1):
    combi1 = itertools.combinations(sorted_input0,n)
    for element in combi1:
        print(''.join(element))
