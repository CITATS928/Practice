# https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true

import numpy

def arrays(arr):
    return numpy.array(arr[::-1],float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)