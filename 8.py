regs = {}
largest = 0

comp_ops = {
    '==': (lambda x, y: x == y),
    '!=': (lambda x, y: x != y),
    '>':  (lambda x, y: x > y ),
    '<':  (lambda x, y: x < y ),
    '>=': (lambda x, y: x >= y),
    '<=': (lambda x, y: x <= y),
}

ops = {
    'inc': (lambda x, y: x + y),
    'dec': (lambda x, y: x - y)
}

def get(r):
    if not r in regs:
        regs[r] = 0
    return regs[r]

with open('8.in', 'r') as f:
    for line in f:
        r1, op, diff, _, r2, comp_op, comp = line.split()
        diff = int(diff)
        comp = int(comp)
        
        r1_val = get(r1)
        r2_val = get(r2)
        if comp_ops[comp_op](r2_val, comp):
            r1_new = ops[op](r1_val, diff)
            regs[r1] = r1_new
            if r1_new > largest:
                largest = r1_new

# Part 1: Largest value after execution
print(max(regs.values()))

# Part 2: Largest value ever encountered
print(largest)

