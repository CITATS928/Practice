"""
https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #print(student_marks)
    sumN=0
    for key in student_marks:
        if key == query_name:
            #print('name = ' + key)
            for value in student_marks[key]:
                sumN += value
            result = format((sumN/3), '.2f')
            print(result)

