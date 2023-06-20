from functions import sieve, isPalindrome, isSquare, isPrime
def isReversiblePrimeSquare(sq):
	if isPalindrome(str(sq)):
		return False
	sq2 = int(str(sq)[::-1])
	if isSquare(sq2):
		if isPrime(round(sq2 ** 0.5)):
			print(p, round(sq2 ** 0.5), sq, sq2, end=" ")
			return True
	return False
primes = sieve(10 ** 8)
total = 0
count = 0
target = 50
for p in primes:
	sq = p * p
	if isReversiblePrimeSquare(sq):
		total += sq
		count += 1
		print(total, count, end="\n")
		if count == target:
			break