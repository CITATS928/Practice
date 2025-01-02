import sys
import numpy as np

input_data = sys.stdin.read().splitlines()

coefficients = list(map(float, input_data[0].split()))

x = float(input_data[1])
result = np.polyval(coefficients, x)
print(result)