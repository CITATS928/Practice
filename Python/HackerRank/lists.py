"""
https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

"""

import sys

test_list=[]
def insert(i,e):
    return test_list.insert(i,e)
    
def remove(e):
    return test_list.remove(e)
    
def append(e):
    return test_list.append(e)



if __name__ == '__main__':
    N = int(input())
    for i in range(0,N):
        lst=sys.stdin.readline().split()
        if lst[0]=='insert':
            insert(int(lst[1]),int(lst[2]))
        elif lst[0]=='print':
            print(test_list)
        elif lst[0]=='sort':
            test_list.sort()
            #print(testlist)
            #sortlst(lst)
        elif lst[0]=='pop':
            test_list.pop()
        elif lst[0]=='remove':
            remove(int(lst[1]))
        elif lst[0]=='append':
            append(int(lst[1]))
        elif lst[0]=='reverse':
            test_list.reverse()
