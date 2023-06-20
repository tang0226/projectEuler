from Solutions.functions import isSquare
from math import floor

def nextTerm(D, term):
    a = term[0]
    i = term[1]
    d = term[2]
    # Second phase
    coeff = d
    integer = -i
    denom = D - (i ** 2)
    # Third phase
    denom //= coeff
    newA = int((D ** 0.5 + integer) / denom)
    integer -= denom * newA
    return [newA, integer, denom]

def solve(D):
    sqrt = floor(D ** 0.5)
    a = [sqrt]
    t0 = [sqrt, -sqrt, 1]
    t = nextTerm(D, t0)
    while True:
        a.append(t[0])
        n = a[-1]
        d = 1
        for i in range(len(a) - 2, -1, -1):
            n, d = d, n
            n += d * a[i]
        if n ** 2 - D * d ** 2 == 1:
            return n
        t = nextTerm(D, t)

upper = 1000
maxX = 0
maxD = 0
for D in range(2, upper + 1):
    if not isSquare(D):
        x = solve(D)
        if x > maxX:
            maxX = x
            maxD = D
    print(D)
print()
print(maxD)