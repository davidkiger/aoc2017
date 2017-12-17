steps = 367

index = 0
length = 1

for i in range(1, 50000000):
    index = ((index + steps) % length) + 1
    length += 1
    if index == 1:
        print("Inserting {}".format(i))
