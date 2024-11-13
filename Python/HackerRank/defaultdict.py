"""
https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
"""

from collections import defaultdict
import sys

input_data = sys.stdin.read().split('\n')

word_length, contain_lenth = map(int, input_data[0].split())

word_list = input_data[1:1+word_length]
contain_list = input_data[1+word_length:]

position_record = defaultdict(list)

for i in range(0,len(word_list)):
    position_record[word_list[i]].append(i+1)

for word in contain_list:
    if word in position_record:
        print(' '.join(map(str, position_record[word])))
    else:
        print('-1')

