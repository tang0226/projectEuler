import math
factorials = [1]
for i in range(1, 11):
	factorials.append(math.factorial(i))

def fds(n):
	return sum(factorials[int(i)] for i in str(n))

total = 0

for start in range(10 ** 6):
	chain = [start]
	while True:
		chain.append(fds(chain[-1]))
		if chain.count(chain[-1]) > 1:
			chain.pop(-1)
			break
	if len(chain) == 60:
		total += 1
		print(chain, total)
print(total)