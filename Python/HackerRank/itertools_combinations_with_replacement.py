"""
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true

itertools.combinations_with_replacement(iterable, r)
This tool returns r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import itertools

in_put = sys.stdin.read().split()
length = int(in_put[1])
iterable= sorted(in_put[0])

combi = itertools.combinations_with_replacement(iterable,length)
for element in combi:
    print(''.join(element))
