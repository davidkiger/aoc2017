base_key = 'ljoxqyyw'
hash_keys = []

for i in range(128):
    hash_keys.append("{}-{}".format(base_key, i))

total = 0
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

    # print(bin(int(hex_str, 16))[2:].zfill(128))
    total += str(bin(int(hex_str, 16))[2:].zfill(128)).count('1')

print(total)
