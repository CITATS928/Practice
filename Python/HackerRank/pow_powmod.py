# https://www.hackerrank.com/challenges/python-power-mod-power/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

input_data = sys.stdin.read().splitlines()

a = int(input_data[0])
b = int(input_data[1])
m = int(input_data[2])

print(pow(a,b))
print(pow(a,b,m))