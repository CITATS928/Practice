"""

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

