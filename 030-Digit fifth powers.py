digitFifths = []
for i in range(10):
	digitFifths.append(i ** 5)

def digitFifthSum(n):
	return sum(list(digitFifths[int(i)] for i in str(n)))

total = 0
for i in range(10, 1000000):
	if digitFifthSum(i) == i:
		total += i
		print(i, total)