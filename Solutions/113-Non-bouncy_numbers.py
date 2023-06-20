decreasing = [[], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
increasing = [[], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

maxDigits = 100

def recurseDecreasing():
	if len(decreasing) > maxDigits:
		return False
	new = [1]
	for i in range(1, 10):
		new.append(sum(decreasing[-1][ : i + 1]))
	decreasing.append(new)
	recurseDecreasing()

def recurseIncreasing():
	if len(increasing) > maxDigits:
		return False
	new = [0]
	for i in range(1, 10):
		new.append(sum(increasing[-1][i : ]))
	increasing.append(new)
	recurseIncreasing()


recurseDecreasing()
recurseIncreasing()
total = sum(list(sum(i) for i in decreasing)) + sum(list(sum(i) for i in increasing))
total -= 9 * maxDigits
total -= maxDigits + 1

print(total)
print(decreasing)
print(increasing)