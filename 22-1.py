file = open("22-1.in", "r")
# file = open("22-1.in.sample", "r")

grid = {}
x = 0
y = 0
for line in file:
    nodes = list(line.strip())
    if not grid:
        min_x = len(nodes)//2
        min_y = min_x

    for i in range(len(nodes)):
        grid[(i - min_x, y - min_y)] = nodes[i]
    y += 1

directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
direction = 0
virus = [0, 0]
infections = 0
for i in range(10000):
    loc = tuple(virus)
    if loc not in grid or grid[loc] == '.':
        direction = (direction - 1) % len(directions)
        grid[loc] = '#'
        infections += 1
    else:
        direction = (direction + 1) % len(directions)
        grid[loc] = '.'
    virus = [virus[0] + directions[direction][0], virus[1] + directions[direction][1]]

print(infections)
