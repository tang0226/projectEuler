import math
def isPrime(n):
	if n < 2:
		return False
	if n < 4:
		return True
	if n % 2 == 0:
		return False
	if n % 3 == 0:
		return False
	for i in range(5, math.floor(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def factorArray(n):
	factors = [1, n]
	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if n % i == 0:
			if n / i == i:
				factors.append(i)
			else:
				factors.append(int(n / i))
				factors.append(i)
	factors.sort()
	return factors

def rad(n):
	r = 1
	if isPrime(n):
		return n
	for i in factorArray(n):
		if isPrime(i):
			r *= i
	return r

data = []
for i in range(1, 100001):
	data.append([rad(i), i])
	print(i)
data.sort()
print(data[9999][1])