# 2283. Check if Number Has Equal Digit Count and Digit Value
# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/?envType=problem-list-v2&envId=azgp9mnm

class Solution:
    def digitCount(self, num: str) -> bool:

        for i in range(len(num)):
            # print(f'this time i is {i}')
            if num.count(str(i)) != int(num[i]):
                # print(f'numi is {num[i]}')
                # print(f'count i is {num.count(str(i))}')
                return False
        return True
    

# with collection.Counter()

import collections
class Solution:
    def digitCount(self, num: str) -> bool:
        counter = collections.Counter(num)

        print(counter)
        for i in range(len(num)):
            if int(num[i])!=int(counter.get(str(i),0)):
                print(num[i])
                print(counter[i])
                return False
        return True