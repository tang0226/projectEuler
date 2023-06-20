from functions import sieve
from math import floor, log
n = 20000000
k = 15000000
factorizations = list([] for i in range(n + 1))
for prime in sieve(n):
    divisor = prime
    while divisor < n:
        index = divisor
        while index <= n:
            factorizations[index].append(prime)
            index += divisor
        divisor *= prime
    print(prime)
nFacSum = sum(sum(factorizations[i]) for i in range(len(factorizations)))
kFacSum = sum(sum(factorizations[i]) for i in range(2, k + 1))
nMinusKFacSum = sum(sum(factorizations[i]) for i in range(2, n - k + 1))
print(nFacSum - kFacSum - nMinusKFacSum)