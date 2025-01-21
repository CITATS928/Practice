# https://www.hackerrank.com/challenges/find-angle/problem

import math
import sys

input_data = sys.stdin.read().splitlines()
AB = int(input_data[0])
BC = int(input_data[1])


AC = math.sqrt(AB**2 + BC**2)

theta = str(int(round(360*math.asin(AB/AC)*(1/(2*math.pi))))) + chr(176)

print(theta)