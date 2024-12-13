import numpy
import sys

def reshape(arr):
    int_arr = list(map(int, arr))
    return numpy.reshape(int_arr,(3,3))
    
if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    result = reshape(input_data)
    sys.stdout.write(str(result))