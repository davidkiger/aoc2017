file = open("22-1.in", "r")
# file = open("22-1.in.sample", "r")

grid = {}
x = 0
y = 0
states = ['.', 'w', '#', 'f']
for line in file:
    nodes = list(line.strip())
    if not grid:
        min_x = len(nodes)//2
        min_y = min_x

    for i in range(len(nodes)):
        val = states.index(nodes[i])
        grid[(i - min_x, y - min_y)] = val
    y += 1

directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
direction = 0
virus = [0, 0]
infections = 0
for i in range(10000000):
    loc = tuple(virus)
    # clean
    if loc not in grid or grid[loc] == 0:
        direction = (direction - 1) % len(directions)
        grid[loc] = 1
    # weakened
    elif grid[loc] == 1:
        infections += 1
        grid[loc] = 2
    # infected
    elif grid[loc] == 2:
        direction = (direction + 1) % len(directions)
        grid[loc] = 3
    # flagged
    elif grid[loc] == 3:
        direction = (direction + 2) % len(directions)
        grid[loc] = 0
    virus = [virus[0] + directions[direction][0], virus[1] + directions[direction][1]]

print(infections)
