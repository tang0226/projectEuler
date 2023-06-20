from Solutions.functions import nextPrime
power = 1
n = 2
multiplyOptions = [(3, 3, 1), (4, 2, 2)]
def getNextPower():
    r = {1: 2}
    last = 2
    curr = 4
    for i in range(200):
        r[last] = curr
        last = curr
        curr *= 2
    return r
nextPowers = getNextPower()
currPrime = 3
while power < 500500:
    multiply = multiplyOptions[0]
    n *= multiply[0]
    n %= 500500507
    nextPower = nextPowers[multiply[2]]
    currBase = multiply[1]
    multiplyOptions.append((currBase ** nextPower, currBase, nextPower))
    if multiply[2] == 1:
        currPrime = nextPrime(currPrime)
        multiplyOptions.append((currPrime, currPrime, 1))
    del multiplyOptions[0]
    power += 1
    multiplyOptions.sort()
    if power % 1000 == 0:
        print(power)
print(n)