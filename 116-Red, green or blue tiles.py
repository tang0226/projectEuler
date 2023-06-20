import math
def choose(n, k):
	return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))

length = 50
total = 0
for tile in range(2, 5):
	for numTiles in range(1, math.floor(length / tile) + 1):
		total += choose(numTiles + (length - (tile * numTiles)), numTiles)
print(total)