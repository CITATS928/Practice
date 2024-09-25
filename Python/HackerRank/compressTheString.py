"""
https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true

In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

For a better understanding of the problem, check the explanation.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import itertools

input_data = sys.stdin.read()
gb = itertools.groupby(input_data)
result =''

for key,group in gb:
    result +='('+str(len(list(group)))+', '+str(key)+') '

print(result)


#优化
#1. 变量命名优化：gb 改为更有意义的名 -> grouped
#2. 使用.strip()去除多余的空格
#3. 使用List Comprehension, 提高效率
#4. 使用str.join() for String Concatenation

"""
import itertools
import sys

# 读取输入
input_data = sys.stdin.read().strip()

# 使用groupby函数
grouped = itertools.groupby(input_data)

# 使用List Comprehension
result = [(len(list(group)), key) for key, group in grouped]

# 使用str.join() for String Concatenation
print(" ".join(f"({count}, {key})" for count, key in result))
"""