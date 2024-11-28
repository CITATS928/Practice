# https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true

import re
import sys

input_data = sys.stdin.read().splitlines()

for line in input_data[1:]:
    #print(line)
    print(bool(re.match(r'^[+-]?\d*\.\d+$',line)))

"""
^: 匹配字符串的开头。
[+-]：可选的正负号。
?: 代表前面的符号可以出现零次或一次。
\d*：零个或多个数字。
\.：小数点。
\d+：小数点后的数字部分，必须至少有一个数字。
$: 匹配字符串的结尾。
"""