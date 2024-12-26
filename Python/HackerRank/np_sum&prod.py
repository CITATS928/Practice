# https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true

import sys
import numpy as np

input_data = sys.stdin.read().splitlines()

N, M = map(int, input_data[0].split())

array = np.array([list(map(int, line.split())) for line in input_data[1:N+1]])

sum_result = np.sum(array, axis=0)
product_result = np.prod(sum_result)
print(product_result)