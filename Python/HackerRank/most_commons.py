import sys
from collections import Counter

s = sys.stdin.read().strip()

counter = Counter(s)

# -x[1] sorts by frequency in descending order
# x[0] sorts by character in ascending order
sorted_chars = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

for char, freq in sorted_chars[:3]:
    print(char, freq)
