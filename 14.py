from knot_hash import dense_hash
from grid_utils import look, shift, CARDINAL

p = 'jzgqcdpd'

def bin_hex_digit(h):
    return bin(int(h, 16))[2:].rjust(4, '0')

s = 0
grid = [''.join([bin_hex_digit(h) for h in dense_hash(p + '-' + str(x))]) for x in range(128)]

# Part 1: Total filled cells
print(sum(sum(1 for b in row if b == '1') for row in grid))

# Part 2: Number of contiguous regions of '1'
visited = set()
regions = 0
for x in range(128):
    for y in range(128):
        if (x,y) in visited or grid[x][y] == '0':
            continue

        # BFS on the region
        q = [(x,y)]
        while len(q) > 0:
            c = q.pop()
            visited.add(c)
            q += [shift(c, d)
                    for d in CARDINAL
                    if not shift(c, d) in visited and look(grid, c, d) == '1']
        regions += 1

print(regions)
