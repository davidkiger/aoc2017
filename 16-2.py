chars = list('abcdefghijklmnop')

file = open("16-1.in", "r")
for line in file:
    moves = line.strip().split(",")

cache = []
while True:
    string = ''.join(chars)
    if string in cache:
        print(cache[1000000000 % len(cache)])
        break

    cache.append(string)

    for move in moves:
        step = move[0]
        details = move[1:]

        if step == 's':
            chars = chars[-int(details):] + chars[:-int(details)]
        elif step == 'x':
            x, y = details.split('/')
            x, y = int(x), int(y)
            chars[x], chars[y] = chars[y], chars[x]
        elif step == 'p':
            x, y = details.split('/')
            x, y = chars.index(x), chars.index(y)
            chars[x], chars[y] = chars[y], chars[x]
