# https://www.hackerrank.com/challenges/np-linear-algebra/problem

import sys
import numpy as np

input_data = sys.stdin.read().splitlines()
N = int(input_data[0])

matrix = np.array([list(map(float, input_data[i + 1].split())) for i in range(N)])

determinant = np.linalg.det(matrix)
sys.stdout.write(f"{round(determinant, 2)}\n")