# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import OrderedDict

input_data = sys.stdin.read().splitlines()
N = int(input_data[0])
items = input_data[1:]

order = OrderedDict()

for item in items:
    *name, price = item.rsplit(' ', 1)
    name = ' '.join(name)
    price = int(price)

    if name in order:
        order[name] += price
    else:
        order[name] = price

for name, price in order.items():
    print(name, price)
