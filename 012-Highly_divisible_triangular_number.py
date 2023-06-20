import math
def factorCount(n):
	if n == 1:
		return 1
	factors = 2
	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if n % i == 0:
			factors += 1
			if n / i != i:
				factors += 1
	return factors

tri = 1
change = 2
target = 500
while True:
	if factorCount(tri) > target:
		print(tri)
		break
	tri += change
	change += 1