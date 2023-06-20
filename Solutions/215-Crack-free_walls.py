def cleanBin(n, l):
	r = bin(n)[2 : ]
	return "0" * (l - len(r)) + r

# this function returns all possible layers of length n using 2x1 and 3x1 bricks
def getRows(n):
	r = []
	bins = list(cleanBin(i, n // 2) for i in range(2 ** (n // 2)))
	for i in bins:
		currPos = 0
		cracks = []
		for j in i:
			if currPos == n - 2 or currPos == n - 3:
				break
			if currPos == n - 4:
				cracks.append(currPos + 2)
				break
			brick = int(j) + 2
			if currPos == n - 5:
				cracks.append(currPos + brick)
				break
			currPos += brick
			cracks.append(currPos)
		r.append(cracks)
	index = 0
	while index < len(r) - 1:
		if r[index] == r[index + 1]:
			r.pop(index)
			index -= 1
		index += 1
	return r

# a function that determines if two layers produce any running cracks
def valid(r1, r2):
	combine = r1 + r2
	return combine == list(dict.fromkeys(combine))

# define the length and height of all walls here
l = 32
h = 10

layers = getRows(l)

compatible = []

for i in range(len(layers)):
	compatible.append([])

# find which layers are compatible with which (formatted by index)
for i in range(len(layers) - 1):
	for j in range(i + 1, len(layers)):
		if valid(layers[i], layers[j]):
			compatible[i].append(j)
			compatible[j].append(i)
	print(i, len(layers))

# walls[i] = number of valid walls that "start" with the layer layers[i]
walls = list(1 for i in range(len(layers)))
for level in range(1, h):
	
	# make a new array
	new = []
	for i in range(len(walls)):
		new.append(0)
	
	for i in range(len(walls)):
		for j in compatible[i]:
			new[j] += walls[i]
	walls = new

print(sum(walls))