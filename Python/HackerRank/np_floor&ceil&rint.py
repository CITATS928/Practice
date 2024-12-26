# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true

import sys
import numpy as np 

np.set_printoptions(legacy='1.13')

input_data = sys.stdin.read().split()
my_array = np.array(list(map(float, input_data)))

result_floor = np.floor(my_array)
result_ceil = np.ceil(my_array)
result_rint = np.rint(my_array)

sys.stdout.write(str(result_floor) + '\n' + str(result_ceil) + '\n' + str(result_rint) + '\n')
