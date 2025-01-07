# https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

import sys
import cmath

z = complex(sys.stdin.read().strip())


r = abs(z)
phi = cmath.phase(z)

sys.stdout.write(f"{r:.3f}\n")
sys.stdout.write(f"{phi:.3f}\n")