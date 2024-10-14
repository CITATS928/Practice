"""
https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

Problem Overview:
You are given a string S and a width w. Your task is to wrap the string into a paragraph, such that each line has exactly w characters, except for possibly the last line which may contain fewer than w characters if the string length is not a perfect multiple of w.

Key Points:
You are given a string S (a long string) and an integer w (the maximum width for wrapping).
You need to break the string into segments of length w, and insert a newline character ('\n') after each segment.
The output should be a string that is formatted as multiple lines, where each line has up to w characters.
Input Format:
The first line contains a string S, which is the string you need to wrap.
The second line contains an integer w, which is the width of each wrapped line.
Output:
A single string with newline characters inserted to create lines of length w.

Example:
Input:
ABCDEFGHIJKLMNOPQRSTUVWXYZ
4

Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

import textwrap

def wrap(string, max_width):
    strings=''
    lists=[string[i:i+max_width] for i in range(0,len(string),max_width)]
    for ls in lists:
        strings+=ls+'\n'
    return strings.strip()

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


"""
improved version:
added join() method to join the list of strings into a single string

def wrap(string, max_width):
    chunks = [string[i:i+max_width] for i in range(0, len(string), max_width)]

    return '\n'.join(chunks)
"""