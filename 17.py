p = 359

# Part 1: value following 2017
buf = [0]
i = 0
for n in range(1, 2018):
    i = ((i + p) % len(buf)) + 1
    buf = buf[:i] + [n] + buf[i:]

print(buf[(buf.index(2017) + 1) % len(buf)])

# Part 2: 0 never moves, so track what's in the cell next to it
v = 0
for n in range(1, 50000001):
    i = ((i + p) % (n)) + 1
    if i == 1:
        v = n
print(v)
