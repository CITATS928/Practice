# https://www.hackerrank.com/challenges/py-check-subset/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

input_data = sys.stdin.read().splitlines()

T = int(input_data[0])
results = []

index = 1
for _ in range(T):
    nA = int(input_data[index])
    A = set(input_data[index + 1].split())
    
    nB = int(input_data[index + 2])
    B = set(input_data[index + 3].split())
    
    results.append(A.issubset(B))
    
    index += 4

for result in results:
    print(result)
