state = 'A'
idx = 0
tape = {0: 0}

for i in range(12629077):
    if idx not in tape:
        tape[idx] = 0

    if state == 'A':
        if tape[idx] == 0:
            tape[idx], idx, state = (1, idx + 1, 'B')
        elif tape[idx] == 1:
            tape[idx], idx, state = (0, idx - 1, 'B')
    elif state == 'B':
        if tape[idx] == 0:
            tape[idx], idx, state = (0, idx + 1, 'C')
        elif tape[idx] == 1:
            tape[idx], idx, state = (1, idx - 1, 'B')
    elif state == 'C':
        if tape[idx] == 0:
            tape[idx], idx, state = (1, idx + 1, 'D')
        elif tape[idx] == 1:
            tape[idx], idx, state = (0, idx - 1, 'A')
    elif state == 'D':
        if tape[idx] == 0:
            tape[idx], idx, state = (1, idx - 1, 'E')
        elif tape[idx] == 1:
            tape[idx], idx, state = (1, idx - 1, 'F')
    elif state == 'E':
        if tape[idx] == 0:
            tape[idx], idx, state = (1, idx - 1, 'A')
        elif tape[idx] == 1:
            tape[idx], idx, state = (0, idx - 1, 'D')
    elif state == 'F':
        if tape[idx] == 0:
            tape[idx], idx, state = (1, idx + 1, 'A')
        elif tape[idx] == 1:
            tape[idx], idx, state = (1, idx - 1, 'E')

print(sum(tape.values()))
