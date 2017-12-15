file = open("5-1.in", "r")
# file = open("5-1.in.sample", "r")

inst = []
for line in file:
    inst.append(int(line))

idx = 0
counter = 0
while idx < len(inst) and idx >= 0:
    counter += 1
    new_idx = idx + inst[idx]
    inst[idx] += 1
    idx = new_idx

print(counter)
