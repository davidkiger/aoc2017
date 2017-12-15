file = open("4-1.in", "r")

count = 0
for line in file:
    words = line.strip().split(" ")
    if len(words) == len(set(words)):
        count += 1

print(count)
