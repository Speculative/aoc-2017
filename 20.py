from copy import deepcopy

p = []

with open('20.in', 'r') as f:
    for line in f:
        line = line.strip().split(', ')
        p.append([[int(c) for c in line[i][3:-1].split(',')] for i in range(3)])

def simulate(particles, rounds, collide=False):
    # Deep copy because we're directly modifying nested lists
    particles = deepcopy(particles)

    for _ in range(rounds):
        spaces = {}
        for n in range(len(particles)):
            pos, vel, acc = particles[n]
            vel = [vel[c] + acc[c] for c in range(3)]
            pos = [pos[c] + vel[c] for c in range(3)]
            particles[n][0] = pos
            particles[n][1] = vel

            pos = tuple(pos)
            if not pos in spaces:
                spaces[pos] = [n]
            else:
                spaces[pos].append(n)

        # After each tick, remove colliding particles
        if collide:
            collided = []
            for p in spaces.values():
                if len(p) > 1:
                    collided += p
            particles = [particles[n] for n in range(len(particles)) if not n in collided]

    return particles

# Part 1: Closest particle
p1 = simulate(p, 1000)
closest = None
dist = 0
for n in range(len(p1)):
    d = sum(abs(c) for c in p1[n][0])
    if d < dist or closest == None:
        closest = n
        dist = d

print(closest)

# Part 2: Number of remaining particles after collisions
p2 = simulate(p, 1000, True)
print(len(p2))
