def print_row(n, i):
    n2 = n**2
    m2 = (n - 1)**2

    if n % 2 == 0:
        if i == n - 1:
            for k in range(n2, n2-n, -1):
                print("{:>6} ".format(k), end='')
        else:
            print_row(n - 1, i)
            print("{:>6} ".format(m2 + 1 + i), end='')
    else:
        if i == 0:
            for k in range(m2+n, n2+1, 1):
                print("{:>6} ".format(k), end='')
        else:
            print("{:>6} ".format(m2 + n - i), end='')
            print_row(n - 1, i - 1)

n = 3
for i in range(n):
    print_row(n, i)
    print("")
