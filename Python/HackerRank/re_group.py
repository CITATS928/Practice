import re
S = input()


m = re.search(r'([0-9A-Za-z])\1', S)
if m:
    print(m.group(1))
else:
    print(-1)