import pprint

pp = pprint.PrettyPrinter(indent=4)

file = open("21-1.in", "r")
# file = open("21-1.in.sample", "r")


def convert(pattern):
    if isinstance(pattern, str):
        return pattern.split('/')
    else:
        return '/'.join(pattern)


def chunk(pattern, length):
    return [pattern[0+x:length+x] for x in range(0, len(pattern), length)]

rules = {}
for line in file:
    rule, output = line.strip().split(' => ')
    for i in range(4):
        rules[rule] = output

        vflip = convert([x[::-1] for x in convert(rule)])
        rules[vflip] = output

        hflip = convert([x[::-1] for x in convert(rule[::-1])])
        rules[hflip] = output

        grid = [list(x) for x in convert(rule)]
        rotated = list(zip(*grid[::-1]))
        rule = '/'.join([''.join(x) for x in rotated])

pattern = '.#./..#/###'
# pattern = '.#.#.#.#/#.#.#.#./......../########/......../......../......../........'
# pattern = '.#.#.#.#./#.#.#.#.#/........./#########/........./........./........./........./.........'
for i in range(5):
    print(pattern)
    grid = convert(pattern)
    if len(grid) % 2 == 0:
        length = 2
    else:
        length = 3

    chunks = []
    for row in grid:
        chunks.append(chunk(row, length))

    # woo boy this is janky
    new_patterns = []
    if len(chunks) == length:
        new_patterns.append(pattern)
        new_grid_size = 1
    else:
        new_grid_size = 0
        for x in range(len(chunks)//length):
            new_grid_size += 1
            for y in range(len(chunks)//length):
                if length == 2:
                    new_patterns.append('/'.join([chunks[length*x][y], chunks[length*x+1][y]]))
                else:
                    new_patterns.append('/'.join([chunks[length*x][y], chunks[length*x+1][y], chunks[length*x+2][y]]))

    # print(new_patterns)

    transformed_patterns = []
    for i, p in enumerate(new_patterns):
        if p not in rules:
            print("OH SHIT: {}".format(p))
        else:
            # print("{} => {}".format(p, rules[p]))
            transformed_patterns.append(convert(rules[p]))

    # print('transformed:')
    # pp.pprint(transformed_patterns)

    new_lines = []
    for r in range(len(transformed_patterns)//new_grid_size):
        for c in range(len(transformed_patterns[0])):
            new_line = ''
            for i in range(new_grid_size):
                new_line += transformed_patterns[r*new_grid_size+i][c]
            new_lines.append(new_line)

    # pp.pprint(convert(new_lines))
    pattern = convert(new_lines)
    # print("==========")

print(pattern.count('#'))
