factors = [16807, 48271]
divisor = 2147483647

judging = [[], []]

numbers = [699, 124]
# numbers = [65, 8921]

score = 0
a_length = 0
b_length = 0
while min(a_length, b_length) < 5000000:
    new_numbers = [
        (numbers[0]*factors[0]) % divisor,
        (numbers[1]*factors[1]) % divisor,
    ]
    numbers = [new_numbers[0], new_numbers[1]]

    if numbers[0] % 4 == 0:
        judging[0].append(numbers[0])
        a_length += 1

    if numbers[1] % 8 == 0:
        judging[1].append(numbers[1])
        b_length += 1

for i in range(5000000):
    if (judging[0][i] & 65535) == (judging[1][i] & 65535):
        score += 1

print(score)
