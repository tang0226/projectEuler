import math
def f(num):
	tot = 0
	for i in range(1, math.floor(math.sqrt(num)) + 1):
		if num % i == 0:
			if num / i == i:
				tot += 1
			else:
				tot += 2
	return tot
primes = []
for i in range(1, 10000):
	if f(i) == 2:
		primes.append(i)
done = False
a = 1
while not(done):
	a += 1
	if a % 2 == 1 and f(a) != 2:
		print("suspect", a)
		valid = True
		for i in primes:
			if a > i:
				for j in range(0, int(math.sqrt(a - i) * 2)):
					if (i + (2 * (j ** 2))) == a:
						valid = False
		if valid:
			print(a)
			done = True
	print(a)
print()
print(a)