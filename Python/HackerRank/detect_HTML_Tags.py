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

#print(input_data)

merged_line = []
temp=''
    
for line in input_data:
    temp+=line.strip()
    if temp.endswith('>'):
        merged_line.append(temp)
        temp=''
    else:
        temp+=' '

tag_pattern = r'<(\w+)(.*?)>'
attr_pattern = r'(\w+)="(.*?)"'

for line in merged_line:
    for tag_match in re.findall(tag_pattern, line):
        tag_name = tag_match[0]
        tag_attr = tag_match[1]
        print(tag_name)

        attr_list = re.findall(attr_pattern, tag_attr)

        for name, value in attr_list:
            print(f'-> {name} > {value}')