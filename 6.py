from itertools import cycle, islice
p = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
n = 16

# Map list to step count when first seen
seen = {}
steps = 0

# Trying much too hard to be clever
def distribute(blocks, t):
    blocks = list(blocks)
    v = blocks[t]
    blocks[t] = 0
    acc = [0] * n
    # sum current value + distributed amount
    return [ b + d for b, d in
        zip(
            # Current values
            blocks,

            # Count the occurrences of each list index in the incremented list
            (sum
                # Each occurrence of the list index means increment it once
                (1
                    # Generate a sequence of list indices that should be incremented:
                    # cycle(range(n)) produces something like [0, 1, ... 15, 0, 1, ...]
                    for i in islice(cycle(range(n)),
                        # Take a slice of that cycle starting from the index after the element being distributed
                        t + 1,
                        # And take the next v indices in the cycle (the number of distribution steps)
                        t + 1 + v)
                    # And only count the occurrences of the current list index we're considering
                    if i == j)
                # And consider each list index individually
                for j in range(n))
        )
    ]

while not str(p) in seen:
    seen[str(p)] = steps
    i = p.index(max(p))
    p = distribute(p, i)
    steps += 1

    # This was the original iterative solution. Just distribute in a loop.
    # d = p[i]
    # p[i] = 0
    # while d > 0:
    #    i = (i + 1) % n
    #    p[i] += 1
    #    d -= 1

# Part 1: time until the first repeated state
print(steps)

# Part 2: cycle length
print(steps - seen[str(p)])

