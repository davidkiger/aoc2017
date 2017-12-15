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

pos = 0
severity = 0
while pos < len(layers):
    if (pos in scanners and scanners[pos]["pos"] == 0):
        severity += pos * layers[pos]

    for depth in scanners.keys():
        scanners[depth]["pos"] += scanners[depth]["dir"]
        if scanners[depth]["pos"] == (layers[depth]-1) or scanners[depth]["pos"] == 0:
            scanners[depth]["dir"] *= -1

    pos += 1

print(severity)
