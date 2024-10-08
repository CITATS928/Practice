"""
https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Here, 0<=i<=x; 0<=j<=y; 0<=k<=z. Please use list comprehensions rather than multiple loops, as a learning exercise.
"""


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result1=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
    """
    for x in range(x+1):
        for y in range(y+1):
            for z in range(z+1):
                if (x+y+z)!=n:
                    result.append([x,y,z])
        """
    print(result1)

