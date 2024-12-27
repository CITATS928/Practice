# https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true

import sys
import numpy as np

input_data = sys.stdin.read().splitlines()
N, M = map(int, input_data[0].split())

array = np.array([list(map(int, input_data[i + 1].split())) for i in range(N)])

min_values = np.min(array, axis=1)
max_of_min = np.max(min_values)

sys.stdout.write(str(max_of_min) + '\n')