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
	r = []
	for i in range(2, n):
		if isPrime(i):
			r.append(i)
	return r

def isPrimePair(s1, s2):
	if isPrime(int(s1 + s2)) and isPrime(int(s2 + s1)):
		return True
	return False

upper = 10000
primes = primesUnder(upper)
target = 5
print(len(primes))
for i in range(1, len(primes) - 5):
	currSet = [primes[i]]
	s1 = str(currSet[0])
	valid = True
	for j in range(i + 1, len(primes) - 4):
		s2 = str(primes[j])
		if isPrimePair(s1, s2):
			currSet = currSet[0 : 1]
			currSet.append(primes[j])
			for k in range(j + 1, len(primes) - 3):
				s3 = str(primes[k])
				if isPrimePair(s1, s3) and isPrimePair(s2, s3):
					currSet = currSet[0 : 2]
					currSet.append(primes[k])
					for l in range(k + 1, len(primes) - 2):
						s4 = str(primes[l])
						if isPrimePair(s1, s4) and isPrimePair(s2, s4) and isPrimePair(s3, s4):
							currSet = currSet[0 : 3]
							currSet.append(primes[l])
							for m in range(l + 1, len(primes) - 1):
								currSet = currSet[0 : 4]
								s5 = str(primes[m])
								if isPrimePair(s1, s5) and isPrimePair(s2, s5) and isPrimePair(s3, s5) and isPrimePair(s4, s5):
									currSet.append(primes[m])
									print(currSet, sum(currSet))