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
			print(i, n - i)
	return r

primes = primesUnder(1000000)

def isCircularPrime(n):
	s = str(n)
	l = len(s)
	for i in range(l - 1):
		s = s[1 : ] + s[0]
		if not(isPrime(int(s))):
			return False
	return True

total = 0
for i in primes:
	if isCircularPrime(i):
		total += 1
		print(i, total)
print(total)