from itertools import islice
a = 703
b = 516
af = 16807
bf = 48271
div = 2147483647

def seq(x, f):
    while True:
        x = (x * f) % div
        yield x

def lower(x):
    return x & 0xFFFF

def count_lower_match(seq_a, seq_b, n):
    print(sum(
        # sum of booleans gives us an integer count of True
        lower(ap) == lower(bp)
        for ap, bp in
            islice(
                # zip the two generators to iterate over them simultaneously
                zip(seq_a, seq_b),
                n
            )
        )
    )

# Part 1: Number of pairs with matching lower 16 bits out of 40,000,000 pairs
count_lower_match(seq(a, af), seq(b, bf), 40000000)

# Part 2: Number of pairs with matching lower 16 bits out of 5,000,000 pairs in filtered sequences
count_lower_match(
    # Same deal as before, but now each generator is further filtered
    filter(lambda v: v % 4 == 0, seq(a, af)),
    filter(lambda v: v % 8 == 0, seq(b, bf)),
    5000000
)

