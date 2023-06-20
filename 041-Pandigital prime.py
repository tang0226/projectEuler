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

from itertools import permutations

validDigits = [4, 7]
maximum = 0

for digits in validDigits:
	for p in list(permutations(list(range(1, digits + 1)))):
		x = list(str(i) for i in p)
		x = int("".join(x))
		if isPrime(x):
			if x > maximum:
				maximum = x
			print(x, maximum)