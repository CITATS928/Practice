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


#优化
#去除不必要的循环：直接访问字典中的value
#避免硬编码：使用len()获取长度
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    #获取指定学生的成绩
    scores = student_marks[query_name]
    #计算平均成绩
    result = sum(scores) / len(scores)
    print(f"{average:.2f}")
"""