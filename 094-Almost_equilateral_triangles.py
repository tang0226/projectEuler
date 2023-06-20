from math import sqrt
total = 0
def isSquare(n):
    return round(sqrt(n))**2 == n
for base in range(4, ((10 ** 9) // 3) + 2, 2):
    otherSide = base + 1
    heightSquared = (otherSide ** 2) - (int(base / 2) ** 2)
    if isSquare(heightSquared):
        total += base + (otherSide * 2)
        print("FOUND:", base, otherSide, otherSide, total)
    otherSide = base - 1
    heightSquared = (otherSide ** 2) - (int(base / 2) ** 2)
    if isSquare(heightSquared):
        total += base + (otherSide * 2)
        print("FOUND:", base, otherSide, otherSide, total)