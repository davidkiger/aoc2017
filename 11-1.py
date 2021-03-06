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
for step in steps:
    x, y = move(x, y, step)

count = 0
while not (x == 0 and y == 0):
    if x == 0:
        if y > 0:
            x, y = move(x, y, 'n')
        else:
            x, y = move(x, y, 's')
    elif x >= 0 and y >= 0:
        x, y = move(x, y, 'nw')
    elif x >= 0 and y < 0:
        x, y = move(x, y, 'sw')
    elif x < 0 and y >= 0:
        x, y = move(x, y, 'ne')
    elif x < 0 and y < 0:
        x, y = move(x, y, 'se')

    count += 1

print(count)
