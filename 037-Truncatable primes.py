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
	r = n + (n % 2) - 1
	while True:
		r += 2
		if isPrime(r):
			return r

def isTruncatablePrime(n):
	s1 = str(n)
	s2 = str(n)
	for i in range(len(s1) - 1):
		s1 = s1[1 : ]
		if not(isPrime(int(s1))):
			return False
		s2 = s2[ : -1]
		if not(isPrime(int(s2))):
			return False
	return True

currPrime = 11
total = 0
count = 0
while count < 11:
	if isTruncatablePrime(currPrime):
		total += currPrime
		count += 1
		print(currPrime, count, total)
	currPrime = nextPrime(currPrime)