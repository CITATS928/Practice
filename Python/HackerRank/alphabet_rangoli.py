"""
https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).

Function Description
- Complete the rangoli function in the editor below.
- rangoli has the following parameters:
    int size: the size of the rangoli

Returns
string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
"""

def remove_middle(lst):
    mid=len(lst)//2
    return lst.pop(mid)
    
def print_rangoli(size):
    size_in_scaii=97+size-1
    # print('letter is '+ chr(size_in_scaii))
    first_half=[]
    for i in range(size_in_scaii, 97-1,-1):
        first_half.append(chr(i))
    second_half=first_half[:-1][::-1]
    # print(first_half)
    # print(second_half)
    full_list=first_half+second_half
    mid_line='-'.join(full_list)
    #print(mid_line)
    width_full_list=len(mid_line)
    # print('list length = '+ str(width_full_list))
    upper=[]
    lower=[]
    for i in range(size-1):
        remove_middle(full_list)
        remove_middle(full_list)
        line='-'.join(full_list).center(width_full_list,'-')
        upper.append(line)
        lower.append(line)
        #print(line)
    upper= upper[::-1]
    for lst in upper:
        print(lst)
    print(mid_line)
    for lst in lower:
        print(lst)
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)