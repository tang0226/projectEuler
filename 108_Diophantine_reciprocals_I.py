n = 27720
maxSolutions = 473
while True:
    n += 20
    solutions = 0
    for x in range(n + 1, (n * 2) + 1):
        #y = (x * n) / (x - n)
        if (x * n) % (x - n) == 0:
            solutions += 1
    if solutions > maxSolutions:
        maxSolutions = solutions
        print(n, solutions)