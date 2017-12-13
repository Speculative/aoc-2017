fw = {}

with open('13.in', 'r') as f:
    for line in f:
        line = line.split(': ')
        fw[int(line[0])] = int(line[1])

# range: 1 2 3 4 5
# cycle: 1 2 4 6 8
# Cycles are 2*(r-1)

def cross(off=0):
    sev = 0
    caught = False
    for l, r in fw.items():
        if (l + off) % ((r - 1) * 2) == 0:
            sev += l * r
            caught = True
    return (sev, caught)

# Part 1: severity from crossing without delay
print(cross()[0])

# Part 2: minimum delay to cross without being caught
delay = 1
while cross(delay)[1]:
    delay += 1

print(delay)
