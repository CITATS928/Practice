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