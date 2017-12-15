factors = [16807, 48271]
divisor = 2147483647

numbers = [699, 124]
# numbers = [65, 8921]

score = 0
for i in range(40000000):
# for i in range(5):
    new_numbers = [
        (numbers[0]*factors[0]) % divisor,
        (numbers[1]*factors[1]) % divisor,
    ]
    numbers = [new_numbers[0], new_numbers[1]]

    if (numbers[0] & 65535) == (numbers[1] & 65535):
        score += 1

print(score)
