"""
https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true
"""


import re
import sys

def remove_comment(string):
    return re.sub(r'<!--.*?-->','',string).strip()
    
input_data = sys.stdin.read().split('\n')
line_count = input_data[0]

input_data = [remove_comment(line) for line in input_data[1:] if remove_comment(line)]
print(input_data)