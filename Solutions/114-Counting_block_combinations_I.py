length = 50
minTile = 3
combos = []
for i in range(length - minTile + 1):
    add = length - i - minTile + 1
    if add < 0:
        add = 0
    combos.append(add)
total = 1
print(combos)
while True:
    total += sum(combos)
    newCombos = [0] * len(combos)
    for space in range(minTile + 1, len(combos)):
        for gap in range(1, space - minTile + 1):
            for tile in range(minTile, space - gap + 1):
                newCombos[space - gap - tile] += combos[space]
        combos[space] = 0
    combos = newCombos
    if sum(combos) == 0:
        break
print(total)