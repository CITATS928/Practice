# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import deque

def can_stack_blocks(blocks):
    dq = deque(blocks)
    top = float('inf')
    
    while dq:
        if dq[0] >= dq[-1]:
            chosen = dq.popleft()
        else:
            chosen = dq.pop()
        
        if chosen > top:
            return "No"
        
        top = chosen
    
    return "Yes"


input_data = sys.stdin.read().splitlines()
T = int(input_data[0])

index = 1
results = []
for _ in range(T):
    n = int(input_data[index])
    blocks = list(map(int, input_data[index + 1].split()))
    results.append(can_stack_blocks(blocks))
    index += 2

sys.stdout.write("\n".join(results) + "\n")
