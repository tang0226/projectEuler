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

upper = 10000
count = 0
for D in range(2, upper + 1):
    if not isSquare(D):
        f = floor(D ** 0.5)
        t1 = nextTerm(D, [f, -f, 1])
        t = nextTerm(D, t1)
        diff = 1
        while t1 != t:
            t = nextTerm(D, t)
            diff += 1
        if diff % 2 == 1:
            count += 1
    print(D)
print()
print(count)