from functools import reduce

# Hex math thanks to:
# http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/
hex_move = {
    'n' : lambda c: (c[0] - 1, c[1] + 1, c[2]    ),
    'ne': lambda c: (c[0]    , c[1] + 1, c[2] - 1),
    'se': lambda c: (c[0] + 1, c[1]    , c[2] - 1),
    's' : lambda c: (c[0] + 1, c[1] - 1, c[2]    ),
    'sw': lambda c: (c[0]    , c[1] - 1, c[2] + 1),
    'nw': lambda c: (c[0] - 1, c[1]    , c[2] + 1)
}

def dist(c):
    return max(abs(c[0]), abs(c[1]), abs(c[2]))

moves = []
with open('11.in', 'r') as f:
    moves = f.read().strip().split(',')

dmax = 0
c = (0, 0, 0)
for m in moves:
    c = hex_move[m](c)
    d = dist(c)
    if d > dmax:
        dmax = d

# Part 1: Final hex distance
print(dist(c))

# Part 2: Greatest hex distance seen
print(dmax)
