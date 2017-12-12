pipes = {}

with open('12.in', 'r') as f:
    for line in f:
        line = line.split(" <-> ")
        p = int(line[0])
        r = list(map(lambda s: int(s.strip()), line[1].split(',')))
        pipes[p] = r

groups = {}
visited = []
pids = pipes.keys()
for p in pids:
    if p in visited:
        continue

    q = [p]
    g = []
    while len(q) > 0:
        pid = q.pop()
        visited.append(pid)
        unvisited = [r for r in pipes[pid] if not r in g]
        g = g + unvisited
        q = q + unvisited

    groups[p] = g


print(len(groups[0]))

print(len(groups.keys()))

