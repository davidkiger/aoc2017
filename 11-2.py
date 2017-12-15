file = open("11-1.in", "r")


def move(x, y, direction):
    if x % 2:
        if direction == 'n':
            return (x, y-1)
        elif direction == 's':
            return (x, y+1)
        elif direction == 'ne':
            return (x+1, y)
        elif direction == 'se':
            return (x+1, y+1)
        elif direction == 'sw':
            return (x-1, y+1)
        elif direction == 'nw':
            return (x-1, y)
    else:
        if direction == 'n':
            return (x, y-1)
        elif direction == 's':
            return (x, y+1)
        elif direction == 'ne':
            return (x+1, y-1)
        elif direction == 'se':
            return (x+1, y)
        elif direction == 'sw':
            return (x-1, y)
        elif direction == 'nw':
            return (x-1, y-1)


for line in file:
    steps = [x for x in line.strip().split(",")]

x = 0
y = 0
max_dist = 0
for step in steps:
    x, y = move(x, y, step)

    count = 0
    dist_x = x
    dist_y = y
    while not (dist_x == 0 and dist_y == 0):
        if dist_x == 0:
            if dist_y > 0:
                dist_x, dist_y = move(dist_x, dist_y, 'n')
            else:
                dist_x, dist_y = move(dist_x, dist_y, 's')
        elif dist_x >= 0 and dist_y >= 0:
            dist_x, dist_y = move(dist_x, dist_y, 'nw')
        elif dist_x >= 0 and dist_y < 0:
            dist_x, dist_y = move(dist_x, dist_y, 'sw')
        elif dist_x < 0 and dist_y >= 0:
            dist_x, dist_y = move(dist_x, dist_y, 'ne')
        elif dist_x < 0 and dist_y < 0:
            dist_x, dist_y = move(dist_x, dist_y, 'se')

        count += 1

    if count > max_dist:
        max_dist = count

print(max_dist)
