"""
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""
if __name__ == '__main__':
    list1=[]
    list2=[]
    scores=[]
    result=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append(name)
        list1.append(score)
        list2.append(list1)
        list1=[]
        scores.append(score)
        
    scores=list(set(scores))
    scores.sort()
    for student in list2:
        if student[1]==scores[1]:
            result.append(student[0])
            
    result.sort()
    for name in result:
        print(name)
 