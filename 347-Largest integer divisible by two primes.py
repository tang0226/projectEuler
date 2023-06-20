from functions import isPrime, primesUnder
import math
def M(p, q, N):
	largest = 0
	for powerP in range(1, math.floor(math.log(N, p)) + 1):
		for powerQ in range(1, math.floor(math.log(N, p)) + 1):
			x = (p ** powerP) * (q ** powerQ)
			if x > N:
				break
			if x > largest:
				largest = x
	return largest

upper = 10 ** 7
primes = primesUnder(math.ceil(upper / 2) + 1)
total = 0
for p in range(len(primes) - 1):
	for q in range(p + 1, len(primes)):
		if primes[p] * primes[q] > upper:
			break
		total += M(primes[p], primes[q], upper)
	print(p)
print(total)