def no_dup(line):
    return all(list(map(lambda w: line.count(w) == 1, line)))

def split_words(line):
    return line.strip().split()

def sort_words(line):
    return list(map(lambda w: ''.join(sorted(w)), line))

def solve(count_line, lines):
    print(sum(map(count_line, lines)))

with open('4.in', 'r') as f:
    # Lambdas in place of a way to compose functions...
    # Part 1: No duplicates
    solve(lambda line: no_dup(split_words(line)), f)
    
    # Part 2: No anagrams
    f.seek(0)
    solve(lambda line: no_dup(sort_words(split_words(line))), f)

