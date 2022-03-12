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
primes = [2]
for i in range(3, 1000000, 2):
	if isPrime(i):
		primes.append(i)
		print(i)
longest = 0
longestNum = 0
for targetIndex in range(len(primes) - 1, -1, -1):
	start = 0
	while not(primes[start] > primes[targetIndex] / 2):
		currSum = primes[start]
		l = 1
		addIndex = start + 1
		while currSum < primes[targetIndex]:
			l += 1
			currSum += primes[addIndex]
			addIndex += 1
		if currSum == primes[targetIndex]:
			if l > longest:
				longest = l
				longestNum = currSum
				print(currSum, l, longestNum, longest)
		start += 1
