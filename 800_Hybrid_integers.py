from functions import sieve
base = 800800
exp = 800800
def isValid(p, q, b, e):
	return (p ** (q / e)) * (q ** (p / e)) <= b
primes = sieve(16000000)
total = 0
for p in range(len(primes) - 1):
	for q in range(p + 1, len(primes)):
		if isValid(primes[p], primes[q], base, exp):
			total += 1
		else:
			break
	print(primes[p], total)