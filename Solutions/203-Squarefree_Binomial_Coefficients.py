import math
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

def isSquarefree(n):
	f = primeFactorization(n)
	if f == list(dict.fromkeys(f)):
		return True
	return False

pascal = [[1]]
rows = 51
for length in range(2, rows + 1):
	new = []
	l = len(pascal)
	for i in range(len(pascal[l - 1]) + 1):
		if i != 0 and i != len(pascal[l - 1]):
			new.append(pascal[l - 1][i - 1] + pascal[l - 1][i])
		else:
			new.append(1)
	pascal.append(new)

distinct = []
for i in pascal:
	for j in i:
		distinct.append(j)
distinct = list(dict.fromkeys(distinct))
distinct.sort()
total = 1
m = max(distinct)
distinct.pop(0)
print(1, total, m - 1)
for i in distinct:
	if isSquarefree(i):
		total += i
		print(i, total, m - i)
print(total)