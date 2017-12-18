file = open("18-1.in", "r")
# file = open("18-1.in.sample", "r")

inst = []
registers = {}
for line in file:
    pieces = line.strip().split()
    if pieces[1] not in registers:
        registers[pieces[1]] = 0
    if len(pieces) == 2:
        inst.append([pieces[0], pieces[1], ''])
    else:
        inst.append(pieces)

played = 0
_next = 0
while True:
    cmd, target, value = inst[_next]

    if value != '':
        try:
            value = int(value)
        except ValueError:
            value = registers[value]

    if cmd == 'jgz':
        try:
            t_val = int(target)
        except ValueError:
            t_val = int(registers[target])

        if t_val > 0:
            _next += value
        else:
            _next += 1
    else:
        if cmd == 'snd':
            played = registers[target]
        elif cmd == 'set':
            registers[target] = value
        elif cmd == 'add':
            registers[target] += value
        elif cmd == 'mul':
            registers[target] *= value
        elif cmd == 'mod':
            registers[target] %= value
        elif cmd == 'rcv':
            if registers[target] > 0:
                print('{}'.format(played))
                break
        _next += 1
