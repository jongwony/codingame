import sys
import math
import re
from functools import partial

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
regex = re.compile(r'[^a-zA-Z]')
new_t = [partial(re.sub, regex, '?')(x).upper() for x in t]
print(new_t, file=sys.stderr)
charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?'
find_idx = [charset.find(x) for x in new_t]

for _ in range(h):
    row = input()
    cut = lambda x: slice(x * l, x * l + l)
    print(''.join(row[cut(x)] for x in find_idx))
