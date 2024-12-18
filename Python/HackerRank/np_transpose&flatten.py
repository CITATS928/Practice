import numpy
import sys

input_data = sys.stdin.read().splitlines()
array = [list(map(int, data.split())) for data in input_data[1:]]

transpose_result = numpy.transpose(array)
sys.stdout.write(str(transpose_result)+'\n')

np_array = numpy.array(array)
flatten_result = np_array.flatten()
sys.stdout.write(str(flatten_result))


# 先转换为数组：
array = numpy.array([list(map(int, data.split())) for data in input_data[1:]])

# 转置：
transpose_result = numpy.transpose(array)

# 展平：
flatten_result = transpose_result.flatten()