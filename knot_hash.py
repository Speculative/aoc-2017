from functools import reduce

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

def dense_hash(to_hash):
    l = list(range(256))
    i = 0
    s = 0
    v = list(map(ord, to_hash)) + knot_const
    for _ in range(64):
        l, i, s = knot_hash(l, v, i, s)
    dh = [reduce(lambda a, b: a ^ b, l[x*16:(x+1)*16]) for x in range(16)]
    return ''.join(map(lambda h: '%02x' % h, dh))

