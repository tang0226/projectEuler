import math
def isPrime(num):
	tot = 0
	prime = True
	for i in range(1, math.floor(math.sqrt(num)) + 1):
		if num % i == 0:
			if num / i == i:
				tot += 1
			else:
				tot += 2
		if tot > 2:
			prime = False
			break
	if prime:
		return True
	else:
		return False
primes = []
for i in range(2, 100000):
	if isPrime(i):
		primes.append(i)
num = 2
i = 0
while num < 1000000:
	i += 1
	num *= primes[i]
if num > 1000000:
	num = math.floor(num / primes[i])
print(num)