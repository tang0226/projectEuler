total = 0
for i in range(2, 10000000):
	currTotal = i
	while currTotal != 1 and currTotal != 89:
		store = currTotal
		currTotal = 0
		string = str(store)
		length = len(string)
		for j in range(length):
			currTotal += int(string[j]) ** 2
	if currTotal == 89:
		total += 1
		print(i, total)
	