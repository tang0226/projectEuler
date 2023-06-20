from Solutions.functions import sieve
from math import *

def primesBetween(lower, upper, sievePrimes):
    Range = upper - lower
    length = Range + 1
    isPrime = []
    if lower % 2 == 0:
        isPrime = ([0, 1] * ((length // 2) + 1))[ : length]
    else:
        isPrime = ([1, 0] * ((length // 2) + 1))[ : length]
    primeLimit = upper ** 0.5
    for p in sievePrimes:
        i = 0
        if lower % p != 0:
            i = p - (lower % p)
        while i < length:
            isPrime[i] = 0
            i += p
    p = lower
    r = []
    for i in isPrime:
        if i:
            r.append(p)
        p += 1
    return r
    

def segmentedTotients(lower, upper, primes):
    Range = upper - lower
    length = Range + 1
    totients = list(range(lower, upper + 1))
    for l in primes:
        for p in l:
            i = 0
            if lower % p != 0:
                i = p - (lower % p)
            while i < length:
                totients[i] = int(totients[i] * (p - 1) / p)
                i += p
    return totients
    

intervalSize = 10 ** 8
primeUpperBound = floor(intervalSize ** 0.5) + 1
sievePrimes = sieve(primeUpperBound)[1 : ]
primes = [sieve(intervalSize)]

lowerBound = intervalSize + 1
upperBound = intervalSize * 2

target = 15499 / 94744
lowestR = 1

while True:
    print("Range:", lowerBound, "to", upperBound)
    newPrimeUpperBound = floor(upperBound ** 0.5) + 1
    sievePrimes += primesBetween(primeUpperBound + 1, newPrimeUpperBound, sievePrimes)
    primeUpperBound = newPrimeUpperBound
    primes.append(primesBetween(lowerBound, upperBound, sievePrimes))
    print("prime sieves done, sieving for totients...")
    totients = segmentedTotients(lowerBound, upperBound, primes)
    print("totient sieve done, finding resilience")
    n = lowerBound
    for t in totients:
        R = t / (n - 1)
        if R < lowestR:
            lowestR = R
            print(n, R, target)
        n += 1
    lowerBound += intervalSize
    upperBound += intervalSize
    print()
#5761455