p = ''

with open('9.in', 'r') as f:
    p = f.read()

score = 0
garbage_score = 0
level = 0
garbage = False
skip = False

for c in p:
    if skip:
        skip = False
        continue

    if not garbage:
        if c == '<':
            garbage = True
        elif c == '{':
            level += 1
        elif c == '}':
            score += level
            level -= 1
    else:
        if c == '!':
            skip = True
        elif c == '>':
            garbage = False
        else:
            garbage_score += 1

# Part 1: Score of nested matched brace sets
print(score)

# Part 2: Score of garbage characters
print(garbage_score)
