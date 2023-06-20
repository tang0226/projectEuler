import math

upper = 10 ** 7

phis = list(range(upper))

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

def nextPrime(n):
	i = n + (n % 2) - 1
	while True:
		i += 2
		if isPrime(i):
			return i

limit = math.ceil(upper / 2)

i = 2
while i < limit:
	for j in range(1, math.ceil(upper / i)):
		phis[i * j] = int(phis[i * j] * ((i - 1) / i))
	print(i, limit - i)
	i = nextPrime(i)

