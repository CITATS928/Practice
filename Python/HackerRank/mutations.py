"""
https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
"""

def mutate_string(string, position, character):
    l=list(string)
    l[position] = character
    return ''.join(l)
    
def mutate_string2(string, position, character):
    return string[:position]+character+string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)