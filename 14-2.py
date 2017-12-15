def fill_neighbors(region_marks, next_mark, x, y):
    region_marks[x][y] = next_mark
    if y-1 >= 0 and region_marks[x][y-1] == -1:
        fill_neighbors(region_marks, next_mark, x, y-1)
    if x+1 < 128 and region_marks[x+1][y] == -1:
        fill_neighbors(region_marks, next_mark, x+1, y)
    if y+1 < 128 and region_marks[x][y+1] == -1:
        fill_neighbors(region_marks, next_mark, x, y+1)
    if x-1 >= 0 and region_marks[x-1][y] == -1:
        fill_neighbors(region_marks, next_mark, x-1, y)


base_key = 'ljoxqyyw'
hash_keys = []

for i in range(128):
    hash_keys.append("{}-{}".format(base_key, i))

total = 0
region_marks = []
for key in hash_keys:
    arr = [x for x in range(256)]
    pos = 0
    skip_size = 0
    lengths = [ord(x) for x in list(key)]

    lengths += [17, 31, 73, 47, 23]

    for r in range(64):
        for span in lengths:
            for i in range(span//2):
                swap_pos = (pos + (span-i-1)) % len(arr)
                swap_val = arr[swap_pos]
                new_pos = (pos + i) % len(arr)
                arr[swap_pos] = arr[new_pos]
                arr[new_pos] = swap_val
            pos = (pos + span + skip_size) % len(arr)
            skip_size += 1

    hex_digits = []
    for block in range(16):
        new_hex = 0
        for num in range(16):
            new_hex ^= arr[block*16+num]
        hex_digits.append(new_hex)

    hex_str = ''
    for num in hex_digits:
        hex_str += '{:02x}'.format(num)

    region_marks.append(
        [int(x) for x in list(str(bin(int(hex_str, 16))[2:].zfill(128)))]
    )

for x in range(128):
    for y in range(128):
        if region_marks[x][y] == 1:
            region_marks[x][y] = -1

region_count = 0
for x in range(128):
    for y in range(128):
        if region_marks[x][y] == -1:
            region_count += 1
            fill_neighbors(region_marks, region_count, x, y)

print(region_count)
