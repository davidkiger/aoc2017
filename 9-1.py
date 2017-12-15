file = open("9-1.in", "r")

for line in file:
    score = 0
    group_depth = 0
    in_cancel = False
    in_garbage = False
    for char in line:
        if in_cancel:
            in_cancel = False
        elif char == '!' and not in_cancel:
            in_cancel = True
        elif char == '<':
            in_garbage = True
        elif char == '>' and in_garbage:
            in_garbage = False
        elif char == '{' and not in_garbage:
            group_depth += 1
        elif char == '}' and not in_garbage and group_depth > 0:
            score += group_depth
            group_depth -= 1

print(score)
