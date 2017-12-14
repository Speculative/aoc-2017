def shift(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])

def look(grid, pos, direction):
    x, y = shift(pos, direction)
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        return grid[pos[0] + direction[0]][pos[1] + direction[1]]
    else:
        return None

def empty(rows, cols, fill=0):
    return [[fill for i in range(rows)] for j in range(cols)]

R = ( 1,  0)
U = ( 0,  1)
L = (-1,  0)
D = ( 0, -1)

UR = ( 1,  1)
UL = (-1,  1)
DR = ( 1, -1)
DL = (-1, -1)

CARDINAL = [R, U, L, D]
ALL = [R, U, L, D, UR, UL, DR, DL]

