from math import *
from Solutions.functions import *
upper = 10 ** 8
primes = sieve(floor(upper / 2) + 1)
total = 0
for i in range(len(primes) - 1):
    for j in range(i, len(primes)):
        if primes[i] * primes[j] < upper:
            total += 1
        else:
            break
    print(primes[i])
print(total)