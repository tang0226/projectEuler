factorSums = [0]
upper = 1000000
for i in range(upper):
	factorSums.append(1)
import math
for i in range(2, int(upper / 2) + 1):
	for j in range(2, math.floor(upper / i) + 1):
		factorSums[i * j] += i
	print(i)

longest = 0
smallestOfLongest = 0

for i in range(1, upper + 1):
	chain = [i]
	index = 0
	valid = True
	while True:
		s = factorSums[chain[index]]
		if s > upper:
			valid = False
			break
		if chain.count(s) == 1:
			chain = chain[chain.index(s) : ]
			break
		chain.append(s)
		index += 1
	if not(valid):
		continue
	if len(chain) > longest:
		longest = len(chain)
		smallestOfLongest = min(chain)
	print(i, len(chain), longest, smallestOfLongest)