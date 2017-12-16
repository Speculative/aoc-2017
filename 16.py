steps = []
with open('16.in', 'r') as f:
    steps = f.read().strip().split(',')

start = 'abcdefghijklmnop'
progs = [c for c in start]

cache = {}

def dance(p, s):
    p = list(p)
    for d in s:
        if d[0] == 's':
            spin = int(d[1:])
            p = p[-spin:] + p[:-spin]
        elif d[0] == 'x':
            a, b = [int(i) for i in d[1:].split('/')]
            p[a], p[b] = p[b], p[a]
        elif d[0] == 'p':
            a, b = [p.index(i) for i in d[1:].split('/')]
            p[a], p[b] = p[b], p[a]
    return p

# Part 1: End positions of programs after 1 round of the dance
print(''.join(dance(progs, steps)))

# Part 2: End positions after 1,000,000,000 rounds of the dance
cycle = 1
cache[0] = progs
cache[1] = dance(progs, steps)
# Find the cycle length
while ''.join(cache[cycle]) != start:
    cycle += 1
    cache[cycle] = dance(cache[cycle - 1], steps)
# Since we repeat every cycle length, just take the remainder
print(''.join(cache[1000000000 % cycle]))
