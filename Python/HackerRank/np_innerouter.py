import sys
import numpy as np

input_data = sys.stdin.read().splitlines()

A = np.array(list(map(int, input_data[0].split())))
B = np.array(list(map(int, input_data[1].split())))

inner_product = np.inner(A, B)
outer_product = np.outer(A, B)

print(inner_product)
print(outer_product)
