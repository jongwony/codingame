import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
print(light_x, light_y, initial_tx, initial_ty, file=sys.stderr)

x, y = initial_tx, initial_ty
maps = (40, 18)

direction = {
    (0, 1): 'S',
    (0, -1): 'N',
    (1, 0): 'E',
    (1, -1): 'NE',
    (1, 1): 'SE',
    (-1, 0): 'W',
    (-1, -1): 'NW',
    (-1, 1): 'SW',
}

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # A single line providing the move to be made: N NE E SE S SW W or NW
    vx = (light_x - x) / maps[0]
    vy = (light_y - y) / maps[1]
    v = math.copysign(math.ceil(abs(vx)), vx), math.copysign(math.ceil(abs(vy)), vy)
    print(v, file=sys.stderr)
    print(direction[v])
    x, y = x + v[0], y + v[1]
