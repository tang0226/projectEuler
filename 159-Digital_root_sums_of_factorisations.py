from functions import digitalRoot, sieve
upper = 10 ** 6
primes = sieve(upper)
isPrime = {}
for n in range(upper):
	isPrime[n] = False
for p in primes:
	isPrime[p] = True
factorPairs = list([] for i in range(upper))
for n in range(2, upper):
	for factor in range(2, int(n ** (1 / 2)) + 1):
		if n % factor == 0:
			factorPairs[n].append((factor, round(n / factor)))
	if n % 10000 == 0:
		print(n)
mdrs = [0, 0]
print()
for n in range(2, upper):
	if isPrime[n]:
		mdrs.append(digitalRoot(n))
	else:
		m = digitalRoot(n)
		for pair in factorPairs[n]:
			t = mdrs[pair[0]] + mdrs[pair[1]]
			if t > m:
				m = t
		mdrs.append(m)
	if n % 10000 == 0:
		print(n)
print(sum(mdrs[i] for i in range(2, upper)))