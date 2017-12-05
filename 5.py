def count_cycles(maze, transform):
    maze = list(maze)
    ip = 0
    cycles = 0
    while 0 <= ip < len(maze):
        new_ip = ip + maze[ip]
        maze[ip] = transform(maze[ip])
        ip = new_ip
        cycles += 1
    print(cycles)

with open('5.in', 'r') as f:
    maze = list(map(int, f.readlines()))
    count_cycles(maze, lambda j: j + 1)
    count_cycles(maze, lambda j: j + 1 if j < 3 else j - 1)
