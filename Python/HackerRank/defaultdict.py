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






# Improved version:

#简化输入的读取部分。用 splitlines() 来一次性获取所有行
input_data = sys.stdin.read().splitlines()

# 提高代码的可读性，更改变量名称
# 获取group a和group b的长度
num_words_in_a, num_words_in_b = map(int, input_data[0].split())

# 分别获取group a和group b的内容
group_a = input_data[1:num_words_in_a + 1]
group_b = input_data[num_words_in_a + 1:]

# 使用 defaultdict 来存储group a中的单词和它们的位置
positions_record = defaultdict(list)

# 避免硬编码，使用enumerate来获取单词的位置
for index, word in enumerate(group_a):
    positions_record[word].append(index+1)

# 输出 Group B 中每个单词在 Group A 中的所有出现位置
for word in group_b:
    if word in positions_record:
        print(' '.join(map(str, positions_record[word])))
    else:
        print(-1)