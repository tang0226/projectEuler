import math
CHAR = "0123456789abcd"
def toBase14(n):
    if(n == 0):
        return "0"
    x = n
    e = 14 ** math.floor(math.log(x, 14))
    s = ""
    while e > 2:
        s += CHAR[int(x // e)]
        x %= e
        e //= 14
    s += CHAR[x]
    return s

steadySquares = [
    {"dec": 1, "b14": "1"},
    {"dec": 7, "b14": "7"},
    {"dec": 8, "b14": "8"}
]

e = 14
n = 2
total = 16
while n <= 9:
    newSteadySquares = []
    for sq in steadySquares:
        for d in range(1, 14):
            newDec = sq["dec"] + d * e
            #print(sq["dec"], e, newDec)
            newB14 = CHAR[d] + sq["b14"]
            newB14Sq = toBase14(newDec ** 2)
            if len(newB14) < n:
                continue
            if(newB14 == "c37"):
                pass
            if newB14Sq[-len(newB14)] == newB14:
                newSteadySquares.append({
                    "dec": newDec,
                    "b14": newB14
				})
                print(newB14)
                total += d
    steadySquares = newSteadySquares
    print(newSteadySquares)
    e *= 14
    n += 1
print(total)