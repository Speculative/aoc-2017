from math import sqrt, ceil
from grid_utils import empty, look, R, U, L, D, ALL

p = 325489

# Part 1: Manhattan distance integer square

# 17 16 15 14 13
# 18 5  4  3  12
# 19 6  1  2  11
# 20 7  8  9  10
# 21 22 23 24 25

# 4  3  2  3  4
# 3  2  1  2  3
# 2  1  0  1  2
# 3  2  1  2  3
# 4  3  2  3  4

# Corner of the square will be... a perfect square
side = ceil(sqrt(p))
corner = side ** 2
# adding side - 1 keeps the offset from the corner the same, as if "rotating"
bottom_place = p
while (bottom_place + (side - 1) < corner):
    bottom_place += side - 1
# Distance to the middle of this side + distance from there to the center
# the middle of the side is at manhattan distance half the side length
dist = abs(corner - (side // 2) - bottom_place) + side // 2
print(dist)

# Part 2: Cumulative spiral sum
# The order of this sequence gives the shape of the spiral
sequence = [R, U, L, D]
direction = 0

# I have no idea how large this grid actually needs to be
grid = empty(side, side, 0)
v = 1
x = side // 2
y = side // 2
while (v < p):
    grid[x][y] = v
    next_direction = (direction + 1) % 4
    if (look(grid, (x, y), sequence[next_direction]) == 0):
        direction = next_direction
    x += sequence[direction][0]
    y += sequence[direction][1]
    v = sum(look(grid, (x,  y), d) for d in ALL)

print(v)
