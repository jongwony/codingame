import sys
import math


def path(x, y, pos, room):
    next_room = {
        1: (x, y + 1),
        2: (x + 1, y) if pos == 'LEFT' else (x - 1, y),
        3: (x, y + 1),
        4: (x - 1, y) if pos == 'TOP' else (x, y + 1),
        5: (x + 1, y) if pos == 'TOP' else (x, y + 1),
        6: (x + 1, y) if pos == 'LEFT' else (x - 1, y),
        7: (x, y + 1),
        8: (x, y + 1),
        9: (x, y + 1),
        10: (x - 1, y),
        11: (x + 1, y),
        12: (x, y + 1),
        13: (x, y + 1),
    }
    print(x, y, pos, room, file=sys.stderr)
    return next_room[room]

# w: number of columns.
# h: number of rows.
rooms = []
w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    rooms.append([int(i) for i in line.split()])
    
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    print(*path(xi, yi, pos, rooms[yi][xi]))
