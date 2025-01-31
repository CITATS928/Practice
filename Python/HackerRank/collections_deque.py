# Enter your code here. Read input from STDIN. Print output to STDOUT# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import deque

input_data = sys.stdin.read().splitlines()
N = int(input_data[0])
d = deque()

for i in range(1, N + 1):
    operation = input_data[i].split()
    command = operation[0]

    if command == "append":
        d.append(int(operation[1]))
    elif command == "appendleft":
        d.appendleft(int(operation[1]))
    elif command == "pop":
        d.pop()
    elif command == "popleft":
        d.popleft()

print(" ".join(map(str, d)))
