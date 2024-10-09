--https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true

/*
You are given two tables: Students and Grades. Students contains three columns ID, Name and Marks. Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. Ketty doesn't want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

Sample Output:
Maria 10 99
Jane 9 81
Julia 9 88 
Scarlet 8 78
NULL 7 63
NULL 7 68
*/

SELECT 
CASE 
    WHEN Grade<8 Then 'NULL'
    ELSE students.Name
END AS Name, grades.Grade, students.Marks FROM Students
INNER JOIN grades
ON Students.Marks BETWEEN grades.min_mark and grades.max_mark
ORDER BY grades.grade DESC,
CASE 
    WHEN grades.grade>=8 THEN students.name
    ELSE students.marks
    END;