"""
https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true
"""

import sys

input_data = sys.stdin.read().split()

# 建立四个空列表，分别用来存储小写字母、大写字母、奇数和偶数
cap=[]
low=[]
odd=[]
even=[]

# 遍历输入的字符串，根据字符的ASCII码值判断是小写字母、大写字母、奇数还是偶数
for i in range(0, len(input_data[0])):
    # 判断是否为小写字母
    if ord(input_data[0][i])>96 and ord(input_data[0][i])<123:
        low.append(input_data[0][i])
    # 判断是否为大写字母
    elif ord(input_data[0][i])>64 and ord(input_data[0][i])<91:
        cap.append(input_data[0][i])
    else:
        # 判断是否为偶数
        if int(input_data[0][i]) % 2 ==0:
            even.append(input_data[0][i])
        # 判断是否为奇数
        else:
            odd.append(input_data[0][i])

# 对四个列表进行排序
cap.sort()
low.sort()
even.sort()
odd.sort()

# 打印排序后的结果
print(''.join(low+cap+odd+even))

"""
improved version:

import sys

def sort_key(char):
    # 根据char的类型来决定优先级
    if char.islower():
        type_priority = 0
    elif char.isupper():
        type_priority = 1
    elif char.isdigit():
        type_priority = 2

    # 当是数字的时候，根据奇偶性来决定优先级
    if char.isdigit():
        dig_priority = 0 if int(char) % 2 != 0 else 1
    else:
        dig_priority = 0

    # 返回一个元组，元组的第一个元素是type_priority，第二个元素是dig_priority，第三个元素是char
    return (type_priority, dig_priority, char)

# 读取输入
input_data = sys.stdin.read().strip()

# 使用sort_key函数来排序
sorted_string = ''.join(sorted(input_data, key=sort_key))

print(sorted_string)



解释：

当排序的key是一个tuple的时候，会按照以下规则来排序：
1. 按照tuple的第一个元素tuple[0]来排序
2. 如果第一个元素相同，再按照第二个元素tuple[1]来排序
3. 如果第二个元素相同，再按照第三个元素tuple[2]来排序
.....

在这道题中,tuple返回的是一个三元组，分别是：
1. type_priority：先比较字符的类型（小写字母、大写字母、数字）。
2. digit_priority：在数字类型中，再比较奇偶性（奇数排在偶数前）。
3. char：如果前两个优先级相同，则按字符的字母顺序或数字大小排序。

如果string是Sorting1234， 那么sorted(input_data, key=sort_key)会返回一系列的tuple，如下：
对每个字符应用 sort_key
[
    sort_key('S'),     # (1, 0, 'S')
    sort_key('o'),     # (0, 0, 'o')
    sort_key('r'),     # (0, 0, 'r')
    sort_key('t'),     # (0, 0, 't')
    sort_key('i'),     # (0, 0, 'i')
    sort_key('n'),     # (0, 0, 'n')
    sort_key('g'),     # (0, 0, 'g')
    sort_key('1'),     # (2, 0, '1')
    sort_key('2'),     # (2, 1, '2')
    sort_key('3'),     # (2, 0, '3')
    sort_key('4')      # (2, 1, '4')
]

"""