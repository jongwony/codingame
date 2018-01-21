import sys
import math
from pprint import pprint


class Bender:
    CITY = []
    RESULT = []
    
    def __init__(self, x=None, y=None, d='SOUTH', beer=False, inverted=False, prev=' ', break_block=0):
        self.x = x
        self.y = y
        self.d = d
        self.beer = beer
        self.inverted = inverted
        self.prev = prev
        
        self.order = ['SOUTH', 'EAST', 'NORTH', 'WEST']
        self.inverse = ['WEST', 'NORTH', 'EAST', 'SOUTH']
        self.temp = []
        self.teleport = []
        
        self.break_block = break_block
    
    def __repr__(self):
        return '<{0.x!r}, {0.y!r}>, D={0.d!r}, B={0.beer!r}, I={0.inverted!r}, break={0.break_block!r}'.format(self)
        
    def __eq__(self, other):
        return repr(self) == repr(other)
        
    def find_next(self, x, y):
        next_x, next_y = x, y
        next_direction = {
            'SOUTH': (next_x + 1, next_y),
            'NORTH': (next_x - 1, next_y),
            'EAST': (next_x, next_y + 1),
            'WEST': (next_x, next_y - 1),
        }
        return next_direction[self.d]
        
    def find_booth(self):
        next_x, next_y = self.find_next(self.x, self.y)
        next_ = self.CITY[next_x][next_y]
        cases = {
            'E': self.east,
            'N': self.north,
            'W': self.west,
            'S': self.south,
            'B': self.breaker,
            'I': self.inverter,
            'T': self.teleporter,
            'X': self.obstacle,
            ' ': self.moves,
            '$': self.moves,
            '#': self.wall,
        }
        cases[next_](next_x, next_y)
        
    def east(self, x, y):
        self.moves(x, y)
        self.d = 'EAST'
        
    def west(self, x, y):
        self.moves(x, y)
        self.d = 'WEST'
        
    def north(self, x, y):
        self.moves(x, y)
        self.d = 'NORTH'
        
    def south(self, x, y):
        self.moves(x, y)
        self.d = 'SOUTH'
        
    def breaker(self, x, y):
        self.moves(x, y)
        self.break_block += 1
        self.beer = not self.beer
    
    def inverter(self, x, y):
        self.moves(x, y)
        self.inverted = not self.inverted
    
    def moves(self, x, y):
        self.temp = []
        self.CITY[self.x][self.y] = self.prev
        self.prev = ' ' if self.CITY[x][y] == 'X' else self.CITY[x][y]
        self.RESULT.append(Bender(self.x, self.y, self.d, self.beer, self.inverted, self.prev, self.break_block))
        self.x = x
        self.y = y
        self.CITY[self.x][self.y] = '@'
        
    def obstacle(self, x, y):
        if self.beer:
            self.moves(x, y)
        else:    
            self.wall(x, y)
        
    def wall(self, x, y):
        direction = self.inverse if self.inverted else self.order
        if self.temp:
            self.d = direction[(direction.index(self.d) + 1) % 4]
        else:
            self.d = direction[0]
            self.temp.append(self.d)

    def teleporter(self, x, y):
        self.moves(x, y)
        target_idx = self.teleport.index([x, y])
        before_x, before_y = self.teleport[target_idx]
        self.CITY[before_x][before_y] = 'T'
        self.x, self.y = self.teleport[(target_idx + 1) % 2]

    
bender = Bender()

l, c = [int(i) for i in input().split()]
for i in range(l):
    row = input()
    if '@' in row:
        bender.x, bender.y = i, row.find('@')
    if 'T' in row:
        bender.teleport.append([i, row.find('T')])
    print(row, file=sys.stderr)
    bender.CITY.append(list(row))


while bender.prev != '$':
    if bender in bender.RESULT:
        print('LOOP')
        sys.exit(0)

    print(bender, file=sys.stderr)
    bender.find_booth()
    # pprint(bender.CITY)


for x in bender.RESULT:
    print(x.d)
