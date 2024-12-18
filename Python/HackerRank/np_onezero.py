import sys
import numpy as np

input_data = tuple(map(int, sys.stdin.read().split()))

print(np.zeros(input_data, dtype=np.int))

print(np.ones(input_data, dtype=np.int))
