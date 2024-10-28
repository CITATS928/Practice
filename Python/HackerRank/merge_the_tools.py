"""
https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

Sample Input:
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output:
AB
CA
AD
"""

def merge_the_tools(string, k):
    substring=[string[i:i+k] for i in range(0, len(string), k)]
    
    for i in range(len(substring)):
        seen=set()
        temp=''
        for j in range(k):
            if substring[i][j] not in seen:
                temp+=substring[i][j]
            seen.add(substring[i][j])
        print(temp)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

"""
# improved version:
减少for循环数量，使用dict保持substring中的字符的顺序并去重

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        # 将string拆分成长度为k的substring
        substring = string[i:i+k]

        # 使用字典保持substring中的字符的顺序并去重
        result = ''.join(dict.fromkeys(substring))

        print(result)
"""
