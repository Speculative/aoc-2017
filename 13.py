fw = {}

with open('13.in', 'r') as f:
    for line in f:
        line = line.split(': ')
        fw[int(line[0])] = int(line[1])

# range: 1 2 3 4 5
# cycle: 1 2 4 6 8
# Cycles are 2*(r-1)

def cross(off=0):
    for l, r in fw.items():
        if (l + off) % ((r - 1) * 2) == 0:
            yield(l * r, True)
        else:
            yield(0, False)

# Part 1: severity from crossing without delay
print(sum(sev for sev, _ in cross()))

# Part 2: minimum delay to cross without being caught
delay = 0
# Combining any with cross() generator lets us fail fast to reduce # of calculations
while any(caught for _, caught in cross(delay)):
    delay += 1

print(delay)
