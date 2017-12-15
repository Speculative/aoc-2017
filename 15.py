a = 703
b = 516
af = 16807
bf = 48271
div = 2147483647

def seq(x, f):
    while True:
        x = (x * f) % div
        yield x

def take(g, n):
    return (v for v, _ in zip(g, range(n)))

def lower(x):
    return x & 0xFFFF

# Part 1: Number of pairs with matching lower 16 bits out of 40,000,000 pairs
print(sum(
    # sum of booleans gives us an integer count of True
    lower(ap) == lower(bp)
    for ap, bp in
        # take restricts the number of pairs we generate
        take(
            # zip the two generators to iterate over them simultaneously
            zip(seq(a, af), seq(b, bf)),
            40000000
        )
    )
)


# Part 1: Number of pairs with matching lower 16 bits out of 5,000,000 pairs in filtered sequences
print(sum(
    lower(ap) == lower(bp)
    for ap, bp in
        take(
            zip(
                # Same deal as before, but now each generator is further filtered
                filter(lambda v: v % 4 == 0, seq(a, af)),
                filter(lambda v: v % 8 == 0, seq(b, bf))
            ),
            5000000
        )
    )
)

