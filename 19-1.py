file = open("19-1.in", "r")

grid = []
for line in file:
    grid.append(list(line.strip('\n\r')))

move = [1, 0]
letters = ''
pos = [0, grid[0].index('|')]
continuing = True
steps = 0

while continuing:
    steps += 1
    if grid[pos[0]][pos[1]].isalpha():
        letters += grid[pos[0]][pos[1]]

    check_pos = [pos[0]+move[0], pos[1]+move[1]]

    other_moves = []
    if move[0]:
        other_moves = [[0, 1], [0, -1]]
    elif move[1]:
        other_moves = [[1, 0], [-1, 0]]

    continuing = False
    try:
        if grid[check_pos[0]][check_pos[1]] != ' ':
            pos = check_pos
            continuing = True
        else:
            raise IndexError
    except IndexError:
        for new_move in other_moves:
            try:
                new_check_pos = [pos[0]+new_move[0], pos[1]+new_move[1]]
                if grid[new_check_pos[0]][new_check_pos[1]] != ' ':
                    pos = new_check_pos
                    move = new_move
                    continuing = True
                    break
            except IndexError:
                pass

print(letters)
print(steps)
