file = open("13-1.in", "r")
# file = open("13-1.in.sample", "r")

layers = [0 for i in range(91)]
# layers = [0 for i in range(7)]
scanners = {}
for line in file:
    depth, _range = line.strip().split(": ")
    depth = int(depth)
    layers[depth] = int(_range)
    scanners[depth] = {"pos": 0, "dir": 1}

searching = True
delay = 0
while searching:
    searching = False
    for depth in scanners.keys():
        if (delay+depth) % (2*layers[depth]-2) == 0:
            searching = True
            break

    if searching:
        delay += 1

print(delay)
