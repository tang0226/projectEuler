from functions import sieve
hammingType = 100
upper = 10 ** 9
primes = sieve(upper)
for i in range(len(primes)):
    if primes[i] > hammingType:
        primes = primes[i : ]
        break
hamming = list(1 for i in range(upper + 1))
for i in primes:
    for j in range(i, upper, i):
        hamming[j] = 0
    print(i)
print(hamming.count(1) - 1)