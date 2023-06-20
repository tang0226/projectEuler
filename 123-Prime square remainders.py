from functions import *
p = 2
n = 1
upper = 10 ** 10
while True:
	x = (((p - 1) ** n) + ((p + 1) ** n)) % (p * p)
	if n % 100 == 1:
		print(n, p, x)
	if x > upper:
		print(n)
		break
	p = nextPrime(nextPrime(p))
	n += 2