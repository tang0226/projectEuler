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

density = 1
sideLength = 3
primes = 3
diagonals = 5
currNum = 9

i = 0
while density > 0.1:
	for i in range(0, 4):
		currNum += sideLength + 1
		if f(currNum) == 2:
			primes += 1
	sideLength += 2
	diagonals += 4
	density = primes / diagonals
	print(sideLength, density)
print(sideLength)