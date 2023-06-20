import math

def isPrime(n):
  if n < 2:
    return False
  if n < 4:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  return True

def primesUnder(n):
	r = [2]
	for i in range(3, n, 2):
		if isPrime(i):
			r.append(i)
	return r

def nextPrime(n):
	i = n + (n % 2) - 1
	while True:
		i += 2
		if isPrime(i):
			return i

def phis(n):
	phis = list(range(n + 1))
	currPrime = 2
	while currPrime < n:
		for i in range(1, math.floor(n / currPrime) + 1):
			phis[currPrime * i] = int(phis[currPrime * i] * ((currPrime - 1) / currPrime))
		print(currPrime, n - currPrime)
		currPrime = nextPrime(currPrime)
	return phis

print(sum(phis(1000000)) - 1)