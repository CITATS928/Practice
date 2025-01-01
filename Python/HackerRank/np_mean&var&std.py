# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import sys
import numpy as np


input_data = sys.stdin.read().splitlines()
N, M = map(int, input_data[0].split())

array = np.array([list(map(int, input_data[i + 1].split())) for i in range(N)])

mean_result = np.mean(array, axis=1)
var_result = np.var(array, axis=0)
std_result = np.std(array, axis=None)

print(mean_result)
print(var_result)
print(round(std_result,11))
