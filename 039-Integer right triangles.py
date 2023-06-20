import math
def isPerfectSquare(n):
	sqrt = math.sqrt(n)
	return sqrt - math.floor(sqrt) == 0

results = []
for i in range(1000):
	results.append(0)
for a in range(500):
	for b in range(500):
		if isPerfectSquare((a * a) + (b * b)):
			n = a + b + int(math.sqrt((a * a) + (b * b)))
			if n < 1000:
				results[n] += 1
print(results.index(max(results)))