import sys

w, h = [int(i) for i in input().split()]
n = int(input())
x0, y0 = [int(i) for i in input().split()]

print('w', w, 'h', h, 'n', n, 'x0', x0, 'y0', y0, file=sys.stderr)

min_x, min_y, max_x, max_y = 0, 0, w, h

# game loop
while True:
    bomb_dir = input()
    print('bomb_dir', bomb_dir, file=sys.stderr)
    print(min_x, min_y, max_x, max_y, x0, y0, file=sys.stderr)

    for direct in bomb_dir:
        if 'U' == direct:
            max_y = y0
        elif 'D' == direct:
            min_y = y0
        elif 'L' == direct:
            max_x = x0
        elif 'R' == direct:
            min_x = x0

    x0 = (min_x + max_x) >> 1
    y0 = (min_y + max_y) >> 1

    print(x0, y0)
