# Name -> (weight, below, [above])
programs = {}

# Convenience accessors
def weight(node):
    return programs[node][0] if node in programs else 0

def below(node):
    return programs[node][1] if node in programs else None

def above(node):
    return programs[node][2] if node in programs else []

def above_weights(node):
    return list(map(tree_weight, above(node)))

# Recursively determine the weight of a subtree
def tree_weight(node):
    return programs[node][0] + sum(map(tree_weight, programs[node][2]))

# Find the singular unique item in the list if one exists
def unique_index(l):
    singles = [x for x in l if l.count(x) == 1]
    return l.index(singles[0]) if len(singles) == 1 else None

# Really ugly string and map fiddling to populate the tree map
with open('7.in', 'r') as f:
    for line in f:
        # bleeehhhh
        parts = line.split('->')
        n = parts[0][:parts[0].index(' ')]
        w = int(parts[0][parts[0].index('(')+1:parts[0].index(')')])
        a = []
        if (len(parts) == 2):
            a = list(map(lambda s: s.strip(), parts[1].split(',')))

        # Record this node (taking the below node if it's already known
        programs[n] = (w, below(n), a)

        for p in a:
            # Mark node n as the one below each above node p
            # (taking their weight/above values if they're already known
            programs[p] = (weight(p), n, above(p))

# Part 1: Root of the tree
# Just start searching from some node. This is the first one in the input.
root = 'qgcmjz'
while (below(root)):
    root = below(root)
print(root)

# Part 2: Single unbalanced node
n = root
# We want to keep descending through the tree, following the path of unbalanced subtrees
unbalanced = True
while unbalanced:
    aw = above_weights(n)
    # When the set of above weights is length 1, we've found a balanced subtree
    # Therefore the current node must be the unbalanced one
    if len(set(aw)) == 1:
        unbalanced = False
    else:
        # Traverse to the unbalanced node above
        n = above(n)[unique_index(aw)]

# n is now the node at which the bad weight occurs
parent_weights = above_weights(below(n))
unbalanced_index = unique_index(parent_weights)

# How much heavier this node is than its peers
# Subtracting 1 always works since python lists support negative indexing! :^)
diff = parent_weights[unbalanced_index] - parent_weights[unbalanced_index - 1]

# And take that off of the unbalanced node's weight
print(weight(n) - diff)

