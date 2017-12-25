import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


result = []

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    result.append(t)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print(result, file=sys.stderr)
try:
    value = min(result, key=abs)
except ValueError:
    value = 0
else:
    if abs(value) in result:
        value = abs(value)
print(value)