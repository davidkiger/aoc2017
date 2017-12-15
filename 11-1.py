file = open("11-1.in", "r")

for line in file:
    steps = [x for x in line.strip().split(",")]

n_s = 0
ne_sw = 0
nw_se = 0

for step in steps:
    if step == 'n': n_s += 1
    elif step == 's': n_s -= 1
    elif step == 'ne': ne_sw += 1
    elif step == 'sw': ne_sw -= 1
    elif step == 'nw': nw_se += 1
    elif step == 'se': nw_se -= 1

print("n_s: {} | ne_sw: {} | nw_se: {}".format(n_s, ne_sw, nw_se))
