prog = []

with open('18.in', 'r') as f:
    for line in f:
        prog.append(line.split())

def get_arg(regs, a):
    try:
        return int(a)
    except ValueError:
        return regs[a] if a in regs else 0

def run_thread(regs, ip, pipe, part1=False):
    if ip > len(prog):
        return (regs, ip, [], True)

    ins = prog[ip][0]
    args = prog[ip][1:]
    send = []
    wait = False

    if ins == 'set':
        regs[args[0]] = get_arg(regs, args[1])
    elif ins == 'add':
        regs[args[0]] = get_arg(regs, args[0]) + get_arg(regs, args[1])
    elif ins == 'mul':
        regs[args[0]] = get_arg(regs, args[0]) * get_arg(regs, args[1])
    elif ins == 'mod':
        regs[args[0]] = get_arg(regs, args[0]) % get_arg(regs, args[1])
    elif ins == 'snd':
        send = [get_arg(regs, args[0])]
    elif ins == 'rcv':
        # Gross per-part logic
        if part1:
            if regs[args[0]] != 0:
                pipe.pop(0)

        # Part 2's rcv behavior
        elif len(pipe) == 0:
            wait = True
        else:
            regs[args[0]] = pipe.pop(0)

    if ins == 'jgz' and get_arg(regs, args[0]) > 0:
        ip += get_arg(regs, args[1])
    elif not wait:
        # if waiting, don't move. Next cycle we'll retry the rcv
        ip += 1

    return (regs, ip, send, wait)

# Part 1: Single thread waiting for the first non-zero rcv
r = {}
ip = 0
q = []
sent = None
while sent == None:
    send_val = q[0] if len(q) > 0 else None
    res = run_thread(r, ip, q, True)
    if len(q) == 0 and send_val != None:
        # We know something was taken from the input queue
        sent = send_val
    r = res[0]
    ip = res[1]
    if len(res[2]) > 0:
        q = res[2]
print(send_val)

# Part 2: threading
r1 = { 'p': 0 }
ip1 = 0
q1 = []

r2 = { 'p': 1 }
ip2 = 0
q2 = []

progress = True
sends = 0

while progress:
    # step each thread
    out1 = run_thread(r1, ip1, q1)
    out2 = run_thread(r2, ip2, q2)

    r1 = out1[0]
    r2 = out2[0]

    ip1 = out1[1]
    ip2 = out2[1]

    # IPC
    q1 = q1 + out2[2]
    q2 = q2 + out1[2]
    
    if len(out2[2]) > 0:
        sends += 1

    # check for deadlock
    progress = not out1[3] or not out2[3]

print(sends)

