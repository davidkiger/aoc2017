file = open("20-1.in", "r")

particles = []
for line in file:
    p, v, a = line.strip()[:-1].split('>, ')
    _, p = p.split('=<')
    _, v = v.split('=<')
    _, a = a.split('=<')
    particles.append({'p': [int(x) for x in p.split(',')], 'v': [int(x) for x in v.split(',')], 'a': [int(x) for x in a.split(',')]})

check = 0
closest = -1
last_closest = -1
dist = 1000000000
while True:
    if closest == last_closest:
        check += 1
        if check > 500:
            break
    else:
        check = 0

    last_closest = closest
    closest = -1
    dist = 1000000000

    for i, p in enumerate(particles):
        p = particles[i]
        p['v'][0] += p['a'][0]
        p['v'][1] += p['a'][1]
        p['v'][2] += p['a'][2]

        p['p'][0] += p['v'][0]
        p['p'][1] += p['v'][1]
        p['p'][2] += p['v'][2]

        this_dist = sum([abs(x) for x in p['p']])
        if this_dist < dist:
            dist = this_dist
            closest = i

print(dist)
print(closest)
