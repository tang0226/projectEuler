def F(m, n):
    combos = []
    for i in range(n - m + 1):
        add = n - i - m + 1
        if add < 0:
            add = 0
        combos.append(add)
    total = 1
    while True:
        total += sum(combos)
        newCombos = [0] * len(combos)
        for space in range(m + 1, len(combos)):
            for gap in range(1, space - m + 1):
                for tile in range(m, space - gap + 1):
                    newCombos[space - gap - tile] += combos[space]
            combos[space] = 0
        combos = newCombos
        if sum(combos) == 0:
            break
    return total

m = 50
n = m
target = 10 ** 6
while True:
    if F(m, n) > target:
        print(m, n)
        break
    n += 1