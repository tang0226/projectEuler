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
def factorArray(num):
	factors = [1, num]
	for i in range(2, math.floor(math.sqrt(num)) + 1):
		if num % i == 0:
			if num / i == i:
				factors.append(i)
			else:
				factors.append(int(num / i))
				factors.append(i)
	factors.sort()
	return factors

def isPgi(n):
	if n % 10 == 6 or n % 10 == 4 or (n + 8) % 20 == 0 or n % 20 == 0 or (n - 8) % 20 == 0:
		return False
	if not(isPrime(n + 1)):
		return False
	l = len(factorArray(n))
	f = factorArray(n)
	valid = True
	for i in range(math.floor(l / 2) + 1):
		if not(isPrime(f[i] + f[l - i - 1])):
			return False
	return True
upper = 10 ** 8
total1 = 0
total2 = 1437218764559
last = 89997658
for i in range(last + 4, upper, 4):
	if isPgi(i):
		total1 += i
		last = i
total2 += total1
print(total2, last)