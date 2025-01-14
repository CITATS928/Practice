# 1247. Minimum Swaps to Make Strings Equal
# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/description/?envType=problem-list-v2&envId=azgp9mnm

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if (s1+s2).count('x') %2 ==1:
            return -1
        mode1=0
        mode2=0
        for i in range(len(s1)):
            if s1[i]!=s2[i] and s1[i]=='x':
                mode1+=1
            elif s1[i]!=s2[i] and s1[i]=='y':
                mode2+=1
        print(mode1)
        print(mode2)
        counter = mode1//2+mode2//2
        if mode1%2==1:
            counter+=2
        return counter