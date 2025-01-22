# https://www.hackerrank.com/challenges/python-mod-divmod/problem

import sys

input_data = sys.stdin.read().splitlines()
a = int(input_data[0])
b = int(input_data[1])

integer_division = a // b
modulo_result = a % b
divmod_result = divmod(a, b)

print(integer_division)
print(modulo_result)
print(divmod_result)