# https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true

import numpy
import sys

input_data = sys.stdin.read().splitlines()
N, M, P = map(int, (input_data[0].split()))

array1 = numpy.array([list(map(int, row.split())) for row in input_data[1:N+1]])

array2 = numpy.array([list(map(int, row.split())) for row in input_data[N+1:N+M+1]])

result = numpy.concatenate((array1,array2) ,axis=0)
sys.stdout.write(str(result))