from Solutions.functions import *
upper = 40000001
chainTarget = 25
primes = sieve(upper)
totients = list(range(upper))
for prime in primes:
	multiply = (prime - 1) / prime
	index = prime
	while index < upper:
		totients[index] = int(totients[index] * multiply)
		index += prime
	print(prime)
print()
total = 0
for prime in primes:
	length = 2
	currNum = prime - 1
	while currNum > 1:
		currNum = totients[currNum]
		length += 1
		if length > chainTarget:
			break
	if length == chainTarget:
		total += prime
		print(prime, total)
print(total)