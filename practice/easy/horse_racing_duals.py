n = int(input())
h = sorted(int(input()) for _ in range(n))
print(min(map(lambda x, y: abs(x-y), h, h[1:])))
