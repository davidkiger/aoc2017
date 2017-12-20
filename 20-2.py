file = open("20-1.in", "r")

particles = []
for line in file:
    p, v, a = line.strip()[:-1].split('>, ')
    _, p = p.split('=<')
    _, v = v.split('=<')
    _, a = a.split('=<')
    particles.append({'p': [int(x) for x in p.split(',')], 'v': [int(x) for x in v.split(',')], 'a': [int(x) for x in a.split(',')]})

num_left = len(particles)
last_left = num_left
check = 0
while True:
    if num_left == last_left:
        check += 1
        if check > 500:
            break
    else:
        check = 0

    positions = {}
    for i, p in enumerate(particles):
        p = particles[i]
        p['v'][0] += p['a'][0]
        p['v'][1] += p['a'][1]
        p['v'][2] += p['a'][2]

        p['p'][0] += p['v'][0]
        p['p'][1] += p['v'][1]
        p['p'][2] += p['v'][2]

        try:
            positions[tuple(p['p'])].append(i)
        except KeyError:
            positions[tuple(p['p'])] = [i]

    particles_to_remove = []
    for key, l in positions.items():
        if len(l) > 1:
            for i in l:
                particles_to_remove.append(i)

    for i in sorted(particles_to_remove, reverse=True):
        particles.pop(i)

print(len(particles))
