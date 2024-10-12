"""
https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

list_sum=[]
input_data = sys.stdin.read().split('\n')

for i in range(1, len(input_data)):
    list_sum.append(max(map(int, input_data[i].split())))

total=0
for num in list_sum:
    total+=num*num
M=(input_data[0].split())[1]
result=total%int(M)
print(result)