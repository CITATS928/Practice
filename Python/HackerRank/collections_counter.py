"""
https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
"""

from collections import Counter
import sys

input_data = sys.stdin.read().split('\n')
Raghu = 0
num_shoes = list(map(int, input_data[1].split()))
num_costomer = input_data[2]

shoe_list = Counter(num_shoes)

for i in range(3, len(input_data)):
    size, price = map(int, input_data[i].split())
    
    if shoe_list[size] > 0:
        Raghu+=price
        shoe_list[size]-=1
        
print(Raghu)