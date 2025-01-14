# 1812. Determine Color of a Chessboard Square
# https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/?envType=problem-list-v2&envId=azgp9mnm

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in ['a','c','e','g']:
            if int(coordinates[1])%2==0:
                return True
            else:
                return False
        else:
            if int(coordinates[1])%2==0:
                return False
            else:
                return True
            
# 使用ord()，将字母转换为数字。再行列相加判断odd even

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col = ord(coordinates[0])-ord('a')+1
        row = int(coordinates[1])
        return (col+row)%2==1