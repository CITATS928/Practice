# https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true

import numpy as np 
import sys


np.set_printoptions(legacy='1.13')


input_data = sys.stdin.read().split()
N,M = map(int, input_data)
print(np.eye(N,M))