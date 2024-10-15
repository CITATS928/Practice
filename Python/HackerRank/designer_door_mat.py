"""
https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Sample Input
9 27

Sample Output
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

input_size = sys.stdin.read().split()
N=int(input_size[0])
M=int(input_size[1])

design='.|.'
pattern='---'

for i in range(0, (N//2)):
    print((pattern*((N//2)-i))+(design*(1+i*2))+(pattern*((N//2)-i)))
    
print(('-'*((M-7)//2))+'WELCOME'+('-'*((M-7)//2)))

for i in range((N//2)-1, -1,-1):
    print((pattern*((N//2)-i))+(design*(1+i*2))+(pattern*((N//2)-i)))
"""
improved version:
#use str.center() method to center the string

import sys
input_size = sys.stdin.read().split()
N=int(input_size[0])
M=int(input_size[1])

for i in range(1, N, 2):
    print(('.|.'*i).center(M, '-'))

print('WELCOME'.center(M, '-'))

for i in range(N-2, -1, -2):
    print(('.|.'*i).center(M, '-'))
"""