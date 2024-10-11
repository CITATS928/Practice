"""
https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true

Problem Overview:
You are given a list of N lowercase English letters, and you need to select K indices from this list. The task is to find the probability that at least one of the K selected indices contains the letter 'a'.

Input Format:
1. The first input line contains an integer N, which is the length of the list.
2. The second line contains N space-separated lowercase English letters.
3. The third line contains an integer K, which is the number of indices to be selected.

Output Format:
You need to output the probability that at least one of the K selected indices contains the letter 'a'. The result must be accurate to three decimal places.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
import sys

input_data = sys.stdin.read().split('\n')
line1 = input_data[0]
line2 = list(input_data[1].split())
line3 = int(input_data[2])
counter=0

iterators_list = itertools.combinations(line2, line3)
length_of_list = len(list(itertools.combinations(line2,line3)))
for element in iterators_list:
    if 'a' in element:
        counter+=1
    
result = counter/length_of_list
print(result)