
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true


import sys
from collections import namedtuple

"""
input:
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6
"""

input_data = sys.stdin.read().splitlines()

# 学生人数
num_stud = int(input_data[0])

# 第二行是列名
# 创建 namedtuple 类型
Mark = namedtuple('students_info',input_data[1].split())

# # 将每一行数据转化为 namedtuple 实例
students = [Mark(*lines.split()) for lines in input_data[2:]]
#print(students)
# output: [students_info(ID='1', MARKS='97', NAME='Raymond', CLASS='7'), students_info(ID='2', MARKS='50', NAME='Steven', CLASS='4'), students_info(ID='3', MARKS='91', NAME='Adrian', CLASS='9'), students_info(ID='4', MARKS='72', NAME='Stewart', CLASS='5'), students_info(ID='5', MARKS='80', NAME='Peter', CLASS='6')]

sums = 0
for student in students:
    sums+=float(student.MARKS)

print(f'{sums/num_stud:.2f}')