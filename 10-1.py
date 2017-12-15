file = open("10-1.in", "r")

arr = [x for x in range(256)]
pos = 0
skip_size = 0
for line in file:
    lengths = [int(x) for x in line.strip().split(",")]

for span in lengths:
    for i in range(span//2):
        swap_pos = (pos + (span-i-1)) % len(arr)
        swap_val = arr[swap_pos]
        new_pos = (pos + i) % len(arr)
        arr[swap_pos] = arr[new_pos]
        arr[new_pos] = swap_val
    pos = (pos + span + skip_size) % len(arr)
    skip_size += 1

print(arr)
