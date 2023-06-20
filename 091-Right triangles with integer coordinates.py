planeSize = 50
total = 0
for x1 in range(planeSize + 1):
    for y1 in range(planeSize + 1):
        for x2 in range(planeSize + 1):
            for y2 in range(planeSize + 1):
                if x1 == y1 == 0 or x2 == y2 == 0:
                    continue
                if x1 == x2 and y1 == y2:
                    continue
                squares = [x1 ** 2 + y1 ** 2, x2 ** 2 + y2 ** 2, (abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2)]
                squares.sort()
                if squares[0] + squares[1] == squares[2]:
                    total += 1
                    print(x1, y1, x2, y2)
total = int(total / 2)
print(total)