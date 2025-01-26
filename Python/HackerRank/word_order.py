# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import OrderedDict

input_data = sys.stdin.read().splitlines()
n = int(input_data[0])
words = input_data[1:]

word_counts = OrderedDict()

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(len(word_counts))
print(' '.join(map(str, word_counts.values())))
