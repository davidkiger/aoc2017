file = open("18-1.in", "r")
# file = open("18-1.in.sample", "r")

inst = []
keys = set()
for line in file:
    pieces = line.strip().split()
    keys.add(pieces[1])
    if len(pieces) == 2:
        inst.append([pieces[0], pieces[1], ''])
    else:
        inst.append(pieces)

keys.remove('1')
registers = [
    {key: 0 for key in keys},
    {key: 0 for key in keys}
]
registers[1]['p'] = 1

count = 0
_next = [0, 0]
queue = [[], []]
rcv_queue = [[], []]
while True:
    if len(rcv_queue[0]) != 0 and len(rcv_queue[1]) != 0 and len(queue[0]) == 0 and len(queue[1]) == 0:
        print('Deadlocked. p1 sent {}'.format(count))
        break

    for i in [0, 1]:
        if len(rcv_queue[i]):
            if len(queue[i]) and len(rcv_queue[i]):
                registers[i][rcv_queue[i].pop(0)] = queue[i].pop(0)
            else:
                continue
        else:
            if _next[i] >= len(inst):
                print('{} out of instructions. p1 sent {}'.format(i, count))
                continue

            cmd, target, value = inst[_next[i]]

            if value != '':
                try:
                    value = int(value)
                except ValueError:
                    value = registers[i][value]

            if cmd == 'jgz':
                try:
                    t_val = int(target)
                except ValueError:
                    t_val = int(registers[i][target])
                if t_val > 0:
                    _next[i] += value
                else:
                    _next[i] += 1
            else:
                if cmd == 'snd':
                    queue[int(not i)].append(registers[i][target])
                    if i == 1:
                        count += 1
                elif cmd == 'set':
                    registers[i][target] = value
                elif cmd == 'add':
                    registers[i][target] += value
                elif cmd == 'mul':
                    registers[i][target] *= value
                elif cmd == 'mod':
                    registers[i][target] %= value
                elif cmd == 'rcv':
                    if len(queue[i]):
                        registers[i][target] = queue[i].pop(0)
                    else:
                        rcv_queue[i].append(target)

                _next[i] += 1
