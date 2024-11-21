"""
https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
"""

def swap_case(s):
    result =''
    for char in s:
        if char.islower():
            result+=char.upper()
        elif char.isupper():
            result+=char.lower()
        else:
            result+=char
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# improve function : 使用list生成式
def swap_case(s):
    return ''.join([char.upper() if char.islower() else char.lower() if char.isupper() else char for char in s])