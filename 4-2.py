file = open("4-1.in", "r")

count = 0
for line in file:
    words = line.strip().split(" ")
    chars = ["".join(sorted(list(chars))) for chars in words]
    if len(chars) == len(set(chars)):
        count += 1

print(count)
