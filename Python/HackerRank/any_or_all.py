"""
https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
"""

import sys

# Check if a number is palindromic
def palindromic(num):
    strn=str(num)
    for i in range(0,len(strn)):
        if strn[i]!=strn[len(strn)-i-1]:
            return False
    return True


input_data = sys.stdin.read().split('\n')
ls=input_data[1].split()

# 把ls裡的string变成int
intls=list(map(int,ls))


# Check if all numbers are positive，如果list里的所有元素都是positive，那么all()返回True
all_positive = all(num>0 for num in intls)

# Check if any number is palindromic，如果list里有任何一个元素是palindromic，那么any()返回True
any_palindromic = any(palindromic(num) for num in intls)

print(all_positive and any_palindromic)

