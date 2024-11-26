# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

import sys
import itertools

input_data = sys.stdin.read().splitlines()

l=[]
for data in input_data:
   l.append(map(int, data.split()))

s=''
for item in tuple(itertools.product(*l)):
    s+=''.join(str(item))+' '
    
print(s)

