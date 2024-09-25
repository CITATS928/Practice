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