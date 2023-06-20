from math import *
from functions import nextPrime, isPrime
upper = 10 ** 9
admissible = list(2 ** i for i in range(1, floor(log(upper, 2)) + 1))
def pseudoFortunate(n):
    test = n + 3
    while not isPrime(test):
        test += 2
    return test - n
pf = list(pseudoFortunate(a) for a in admissible)
currPrime = 3
while admissible:
    newAdmissible = []
    mul = currPrime
    while True:
        found = False
        for check in admissible:
            new = check * mul
            if new < upper:
                pf.append(pseudoFortunate(new))
                newAdmissible.append(new)
                found = True
        if not found:
            break
        mul *= currPrime
    admissible = newAdmissible
    print(currPrime)
    currPrime = nextPrime(currPrime)
print(sum(list(dict.fromkeys(pf))))