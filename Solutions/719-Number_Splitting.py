from Solutions.functions import cleanBin
from math import floor, sqrt
def isSNumber(base, square):
    p = []
    s = str(square)
    l = len(s)
    b = list(cleanBin(i, l - 1) for i in range(1, 2 ** (l - 1)))
    for currB in b:
        currPartition = []
        currStart = 0
        for index in range(len(currB)):
            if currB[index] == "1":
                currPartition.append(int(s[currStart : index + 1]))
                currStart = index + 1
        currPartition.append(int(s[currStart : ]))
        if sum(currPartition) == base:
            return True
    return False
    return p
upper = 10 ** 12
total = 0
for base in range(4, floor(sqrt(upper)) + 1):
    square = base * base
    if isSNumber(base, square):
        total += square
        print(base, square, total)
print(total)