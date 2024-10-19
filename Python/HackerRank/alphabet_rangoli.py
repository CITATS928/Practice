"""
https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

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
    print(mid_line)
    width_full_list=len(mid_line)
    # print('list length = '+ str(width_full_list))
    for i in range(size-1):
        remove_middle(full_list)
        remove_middle(full_list)
        line='-'.join(full_list).center(width_full_list,'-')
        print(line)
    ###### sudo for upper half
    #when adding line, add a copy to a list, then print the list in reverse order

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)