import math

def isPrime(n):
	if n < 2:
		return False
	if n < 4:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while(i * i <= n):
		if (n % i == 0 or n % (i + 2) == 0):
			return False
		i = i + 6
	return True

def primeFactorization(n):
	currNum = n
	factorization = []
	if isPrime(currNum):
		return [currNum]
	while not(isPrime(currNum)):
		for i in range(2, math.ceil(math.sqrt(n)) + 1):
			if currNum % i == 0:
				currNum = int(currNum / i)
				factorization.append(i)
				break
	factorization.append(currNum)
	factorization.sort()
	return factorization

upper = 12000
factors = [0, 0, 0, 0, 0]
for i in range(5, upper + 1):
	factors.append(list(dict.fromkeys(primeFactorization(i))))

total = 0
for i in range(5, len(factors)):
	nums = list(range(1, i + 1))
	for j in factors[i]:
		nums = list(k for k in nums if k % j != 0)
	for j in nums:
		if 1 / 3 < j / i < 1 / 2:
			total += 1
	print(i, total)
print(total)