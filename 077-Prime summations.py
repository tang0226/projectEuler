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

def numberOfWays(n,values):
    table = [0] *(n+1)
    table[0] = 1
    for value in values:
        for i in range(value, n+1): 
            table[i] += table[i-value]            
    return table[n]
primes = []
upper = 100
for i in range(upper):
	if isPrime(i):
		primes.append(i)

for i in range(100):
	n = numberOfWays(i, primes)
	if n > 5000:
		print(i)
		break