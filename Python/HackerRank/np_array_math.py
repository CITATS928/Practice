import sys
import numpy as np 

input_data = sys.stdin.read().splitlines()
N, M = map(int, input_data[0].split())


array_a = np.array([list(map(int, row.split())) for row in input_data[1:N+1]])
array_b = np.array([list(map(int, row.split())) for row in input_data[N+1:]])

print(array_a+array_b)
print(array_a-array_b)
print(array_a*array_b)
print(array_a//array_b)
print(array_a%array_b)
print(array_a**array_b)