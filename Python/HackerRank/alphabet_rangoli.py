"""
https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

"""

def print_rangoli(size):
    size_in_scaii=97+size-1
    print('letter is '+ chr(size_in_scaii))
    first_half=[]
    for i in range(size_in_scaii, 97-1,-1):
        first_half.append(chr(i))
    second_half=first_half[:-1][::-1]
    print(first_half)
    print(second_half)
    full_list=first_half+second_half
    mid_line='-'.join(full_list)
    print(mid_line)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)