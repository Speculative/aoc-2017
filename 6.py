p = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]

# Map list to step count when first seen
seen = {}
steps = 0

while not str(p) in seen:
    seen[str(p)] = steps
    i = p.index(max(p))
    d = p[i]
    p[i] = 0
    while d > 0:
        i = (i + 1) % 16
        p[i] += 1
        d -= 1
    steps += 1

# Part 1: time until the first repeated state
print(steps)

# Part 2: cycle length
print(steps - seen[str(p)])

