def isprime(n):
    """Returns True if n is prime."""
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


b = 106700
h = 0

for i in range(1001):
    if not isprime(b):
        h += 1
    b += 17

print(h)


"""
set b 67
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23


b = 106700
c = 123700
f = 1
d = 2
e = 2

h = 0
for _ = 0; _ <= 1001; _++:
    # this is finding factors. If there are none, f = 0
    for d++:
        for e++:
            g = (d * e) - b
            if g == 0:
                f = 0

    # if b is not prime, increment h
    if f != 0:
        h += 1

    b += 17
"""


"""file = open("23-1.in", "r")

inst = []
registers = {}
for line in file:
    pieces = line.strip().split()
    if pieces[1] not in registers:
        registers[pieces[1]] = 0
    if len(pieces) == 2:
        inst.append([pieces[0], pieces[1], ''])
    else:
        inst.append(pieces)

registers['a'] = 1
_next = 0
while True:
    print(registers)
    try:
        cmd, target, value = inst[_next]
    except IndexError:
        break

    if value != '':
        try:
            value = int(value)
        except ValueError:
            value = registers[value]

    if cmd == 'jnz':
        try:
            t_val = int(target)
        except ValueError:
            t_val = int(registers[target])

        if t_val != 0:
            _next += value
        else:
            _next += 1
    else:
        if cmd == 'set':
            registers[target] = value
        elif cmd == 'sub':
            registers[target] -= value
        elif cmd == 'mul':
            registers[target] *= value
        _next += 1
"""
