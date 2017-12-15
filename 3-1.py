def calc_number(n, i, j):
    if i <= j:
        x = min(i, n-1-j)
        number = (n-2*x)**2 + 2*x - i - j
    else:
        x = min(j, n-1-i)
        number = (n-2*x-2)**2 - 2*x + i + j
    return number

n = 5
for i in range(n):
    for j in range(n):
        print("{:>6} ".format(calc_number(n, i, j)), end='')
    print("")
