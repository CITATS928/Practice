"""
https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

Given an integer, n, print the following values for each integer i from 1 to n:
Decimal
Octal
Hexadecimal (capitalized)
Binary
"""

def print_formatted(number):
    width = len(format(number, 'b'))

    for num in range(1, number+1):
        print(f'{num:>{width}} {num:>{width}o} {num:>{width}X} {num:>{width}b}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)