file = open("23-1.in", "r")

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

_next = 0
muls = 0
while True:
    try:
        cmd, target, value = inst[_next]
    except IndexError:
        break

    if value != '':
        try:
            value = int(value)
        except ValueError:
            value = registers[value]

    if cmd == 'jnz':
        try:
            t_val = int(target)
        except ValueError:
            t_val = int(registers[target])

        if t_val != 0:
            _next += value
        else:
            _next += 1
    else:
        if cmd == 'set':
            registers[target] = value
        elif cmd == 'sub':
            registers[target] -= value
        elif cmd == 'mul':
            registers[target] *= value
            muls += 1
        _next += 1

print(muls)
