import sys
import math
from itertools import chain

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

binary = ''.join('{:0>7b}'.format(ord(m)) for m in message)
print('binary', binary, file=sys.stderr)
prev = ""
result = []
for x in binary:
    if x != prev:
        result.append(x)
    elif x == prev:
        result[-1] += x
    prev = x

print(result, file=sys.stderr)
result_map = [('0' if x.startswith('1') else '00', len(x) * '0') for x in result]
print(result_map, file=sys.stderr)
print(' '.join(chain(*(result_map))))
