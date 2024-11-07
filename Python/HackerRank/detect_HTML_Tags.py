"""
https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true
"""


import re
import sys

def remove_comment(string):
    return re.sub(r'<!--.*?-->','',string).strip()
    
input_data = sys.stdin.read().split('\n')
line_count = input_data[0]

input_data = remove_comment('\n'.join(input_data[1:])).splitlines()

print(input_data)

merged_line = []
temp=''
    
for line in input_data:
    temp+=line.strip()
    if temp.endswith('>'):
        merged_line.append(temp)
        temp=''
    else:
        temp+=' '