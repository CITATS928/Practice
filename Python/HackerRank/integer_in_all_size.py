# https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
input_data = sys.stdin.read().splitlines()

a = int(input_data[0])
b = int(input_data[1])
c = int(input_data[2])
d = int(input_data[3])


print(pow(a,b)+pow(c,d))
