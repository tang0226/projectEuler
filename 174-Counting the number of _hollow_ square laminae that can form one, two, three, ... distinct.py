# my tiles function
def tiles(side, thickness):
	return 4 * thickness * (side + thickness)

# find the maximum side and thickness
maxSide = 0
maxThickness = 0
upper = 1000000
while True:
	maxSide += 1
	if tiles(maxSide, 1) > upper:
		break
while True:
	maxThickness += 1
	if tiles(1, maxThickness) > upper:
		break

# find the amount of laminae that use a certain number of tiles
nums = [0] * (upper + 1)
for s in range(1, maxSide):
	for t in range(1, maxThickness):
		x = tiles(s, t)
		if x > upper:
			break
		nums[x] += 1
	print(s, maxSide - s)

# define our N function
def N(n):
	r = 0
	for i in nums:
		if i == n:
			r += 1
	return r

# find the answer
print(sum(list(N(i) for i in range(1, 11))))