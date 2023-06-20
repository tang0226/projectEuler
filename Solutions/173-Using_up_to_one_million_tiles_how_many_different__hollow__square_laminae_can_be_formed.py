from math import sqrt, ceil
def tiles(s, t):
	return 4 * t * (s + t)
x = 1000000
maxS = ceil(x / 4 + 1)
maxT = ceil((-4 + sqrt(16 * (x + 1))) / 8)
total = 0
for s in range(1, maxS + 1):
	for t in range(1, maxT + 1):
		if tiles(s, t) > x:
			break
		total += 1
print(total)