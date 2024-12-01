# 3216. Lexicographically Smallest String After a Swap
# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/description/

class Solution:
    def getSmallestString(self, s: str) -> str:

        s = list(s)
        print(s)
        
        for i in range(len(s)-1):
            if s[i] > s[i+1] and ((int(s[i])%2==0 and int(s[i+1])%2==0) or (int(s[i])%2==1 and int(s[i+1])%2==1)):
                temp = s[i]
                s[i] = s[i+1]
                s[i+1] = temp
                break
        return ''.join(s)
    
