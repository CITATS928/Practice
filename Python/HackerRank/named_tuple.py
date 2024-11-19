import sys
from collections import namedtuple

input_data = sys.stdin.read().splitlines()
num_stud = int(input_data[0])

Mark = namedtuple('students_info',input_data[1].split())

students = [Mark(*lines.split()) for lines in input_data[2:]]

sums = 0
for student in students:
    sums+=float(student.MARKS)

print(f'{sums/num_stud:.2f}')
