from grid_utils import shift, look, R, U, L, D, CARDINAL

net = []

with open('19.in', 'r') as f:
    for line in f:
        net.append(line.strip('\n'))

hor = [R, L]
ver = [U, D]

loc = (0, net[0].index('|'))
head = R
seen = []
steps = 0
moving = True
while moving:
    steps += 1
    loc = shift(loc, head)
    here = net[loc[0]][loc[1]]
    if here == '-' or here == '|':
        continue
    elif here == '+':
        # Inverted because grid_utils treats coordinates as (row, col)
        if head in hor:
            turn = [look(net, loc, d) for d in ver].index('-')
            head = ver[turn]
        else:
            turn = [look(net, loc, d) for d in hor].index('|')
            head = hor[turn]
    elif here == ' ':
        moving = False
    else:
        seen.append(here)

# Part 1: Seen letters
print(''.join(seen))

# Part 2: Steps taken
print(steps)
