# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

import sys
import itertools

input_data = sys.stdin.read().splitlines()

l=[]
for data in input_data:
   l.append(map(int, data.split()))

s=''
for item in tuple(itertools.product(*l)):
    s+=''.join(str(item))+' '
    
print(s)

# 优化
# 使用List Comprehension，一步完成数据处理并且为每一行的数据转换为list
# 使用str.join() for String Concatenation

input_data = [list(map(int, line.split()) for line in sys.stdin.read().splitlines())]

result = ' '.join(str(item) for item in itertools.product(*input_data))
print(result)