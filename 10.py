from knot_hash import knot_hash, dense_hash

p = '31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33'

# Part 1: product of first two values of knot hash
p1, _, _ = knot_hash(list(range(256)), list(map(int, p.split(','))))
print(p1[0] * p1[1])

# Part 2: Hex dense hash of the ASCII length values
print(dense_hash(p))

