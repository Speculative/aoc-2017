from functools import reduce

p = '31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33'
knot_const = [17, 31, 73, 47, 23]

def knot_hash(l, v, i=0, s=0):
    l = list(l)
    n = len(l)
    for r in v:
        if i + r < n:
            sl = l[i:i+r][::-1]
            l = l[:i] + sl + l[i+r:]
        else:
            # How much to take from the end
            d = n - i
            #  How much to take from the beginning
            off = r - d
            sl = (l[i:] + l[:off])[::-1]
            # [end of reversed] + [untouched part of original list] + [beginning of reversed]
            l = sl[len(sl)-off:] + l[off:i] + sl[:len(sl)-off]
        i = (i + r + s) % n
        s += 1
    return (l, i, s)

# Part 1: product of first two values of knot hash
p1, _, _ = knot_hash(list(range(256)), list(map(int, p.split(','))))
print(p1[0] * p1[1])

# Part 2: Hex dense hash of the ASCII length values
l = list(range(256))
i = 0
s = 0
v = list(map(ord, p)) + knot_const

# Cycle 64 knot hashes, preserving current index & skip
for _ in range(64):
    l, i, s = knot_hash(l, v, i, s)

# Reduce the sparsh hash: xor each block of 16
dense_hash = [reduce(lambda a, b: a ^ b, l[x*16:(x+1)*16]) for x in range(16)]

# Pad to 2 hex digits
print(''.join(map(lambda h: '%02x' % h, dense_hash)))
