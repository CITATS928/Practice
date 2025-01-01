
# https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy as np
import sys

input_data = sys.stdin.read().splitlines()

N = int(input_data[0])

A = np.array([list(map(int, input_data[i + 1].split())) for i in range(N)])
B = np.array([list(map(int, input_data[i + 1 + N].split())) for i in range(N)])

result = np.dot(A, B)

print(result)
