steps = 367

ring = [0]
index = 0

for i in range(0, 2017):
    index = (index + steps) % len(ring)
    index += 1
    ring.insert(index, i+1)

print(ring[ring.index(2017)+1])
