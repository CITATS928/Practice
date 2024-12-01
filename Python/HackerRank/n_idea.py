# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

import sys

input_data = sys.stdin.read().splitlines()
array = list(map(int, input_data[1].split()))
set_A = set(map(int, input_data[2].split()))
set_B = set(map(int, input_data[3].split()))

# print(array)
# print(set_A)
# print(set_B)

happiness = 0

for item in array:
    if item in set_A:
        happiness+=1
    if item in set_B:
        happiness-=1
        
sys.stdout.write(f'{happiness}\n')