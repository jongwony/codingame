from collections import deque
from itertools import groupby

r = int(input())
l = int(input())

result = deque([[r]], maxlen=2)
for _ in range(l):
    temp = []
    for i, g in groupby(result[-1]):
        temp += [len(list(g)), i]
    result.append(temp)

print(*result[0])
