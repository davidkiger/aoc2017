file = open("8-1.in", "r")

registers = {}
for line in file:
    reg, opp, val, _, check_reg, cond, cond_val = line.strip().split(" ")
    val = int(val)
    cond_val = int(cond_val)

    if reg not in registers:
        registers[reg] = 0
    if check_reg not in registers:
        registers[check_reg] = 0

    do_opp = False
    if cond == '>' and registers[check_reg] > cond_val: do_opp = True
    elif cond == '>=' and registers[check_reg] >= cond_val: do_opp = True
    elif cond == '<' and registers[check_reg] < cond_val: do_opp = True
    elif cond == '<=' and registers[check_reg] <= cond_val: do_opp = True
    elif cond == '==' and registers[check_reg] == cond_val: do_opp = True
    elif cond == '!=' and registers[check_reg] != cond_val: do_opp = True

    if do_opp and opp == 'inc':
        registers[reg] += val
    elif do_opp and opp == 'dec':
        registers[reg] -= val

print(registers[max(registers, key=registers.get)])
