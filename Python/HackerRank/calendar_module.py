# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import calendar

month, day, year = map(int, sys.stdin.read().strip().split())

weekday_num = calendar.weekday(year, month, day)

weekday_name = calendar.day_name[weekday_num].upper()

print(weekday_name)
