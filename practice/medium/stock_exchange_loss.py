output = []
base = None
_min = None
n = int(input())
for i in input().split():
    v = int(i)
    if base is None or v > base:
        base = v
    else:
        _min = min(base, v)
        output.append((base, _min))

try:
    result = min(output, key=lambda x: x[1] - x[0])
    print(result[1] - result[0])
except ValueError:
    print(0)


# Best Solution
n = int(input())
prices = map(int, input().split())

loss = 0
high = next(prices)

for p in prices:
    high = max(high, p)
    loss = min(loss, p - high)

print(loss)
