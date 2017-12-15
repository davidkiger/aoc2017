import pprint


def calc_number(n, i, j):
    x = min(i, j, n-1-i, n-1-j)

    if i <= j:
        number = (n-2*x)**2 + 2*x - i - j
    else:
        number = (n-2*x-2)**2 - 2*x + i + j
    return number

pp = pprint.PrettyPrinter(indent=4)

n = 5
numbers = []
for i in range(n):
    new_row = []
    for j in range(n):
        new_row.append(calc_number(n, i, j))
    numbers.append(new_row)

pp.pprint(numbers)

sums = []
for i in range(n):
    sums.append([])
    for j in range(n):
        sum_of_neighbors = 0
        if i > 0 and j > 0 and numbers[i-1][j-1] < numbers[i][j]:
            sum_of_neighbors += numbers[i-1][j-1]
        if i > 0 and numbers[i-1][j] < numbers[i][j]:
            sum_of_neighbors += numbers[i-1][j]
        if i > 0 and j < n-1 and numbers[i-1][j+1] < numbers[i][j]:
            sum_of_neighbors += numbers[i-1][j+1]
        if j > 0 and numbers[i][j-1] < numbers[i][j]:
            sum_of_neighbors += numbers[i][j-1]
        if j < n-1 and numbers[i][j+1] < numbers[i][j]:
            sum_of_neighbors += numbers[i][j+1]
        if i < n-1 and j > 0 and numbers[i+1][j-1] < numbers[i][j]:
            sum_of_neighbors += numbers[i+1][j-1]
        if i < n-1 and numbers[i+1][j] < numbers[i][j]:
            sum_of_neighbors += numbers[i+1][j]
        if i < n-1 and j < n-1 and numbers[i+1][j+1] < numbers[i][j]:
            sum_of_neighbors += numbers[i+1][j+1]
        if sum_of_neighbors == 0:
            sum_of_neighbors = 1

        sums[i].append(sum_of_neighbors)

pp.pprint(sums)
