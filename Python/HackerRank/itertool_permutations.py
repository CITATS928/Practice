# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
import sys
import itertools

input_data = sys.stdin.read().split()
size = int(input_data[1])

string_s = sorted(input_data[0])

for item in itertools.permutations(string_s,size):
    print(''.join(item))


# 所使用的方法是先对要排列的string进行sort，然后使用itertools.permutations()方法进行排列，最后输出结果

# 但是如果想先对string进行排列，然后再进行sort。 因为permutation方法会返还一个迭代器，所以我们可以先将迭代器转换为list，然后再进行sort
string_s = input_data[0]
permutations = itertools.permutations(string_s,size)
sorted_permutations = sorted([''.join(item) for item in permutations])

for item in sorted_permutations:
    print(item)


# 优化获取input
input_data = sys.stdin.read().split()
string_s, size = sorted(input_data[0]), int(input_data[1])
