import sys
import itertools

input_data = sys.stdin.read().split()
size = int(input_data[1])

string_s = sorted(input_data[0])

for item in itertools.permutations(string_s,size):
    print(''.join(item))