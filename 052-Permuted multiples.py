done = False
n = 0
while not(done):
	n += 1
	text = str(n)
	done = True
	for i in range(2, 7):
		testNum = n * i
		testText = str(testNum)
		numCountsN = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		numCountsTest = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		for i in range(0, len(text)):
			numCountsN[int(text[i])] += 1
		
		for i in range(0, len(testText)):
			numCountsTest[int(testText[i])] += 1
		
		if numCountsN != numCountsTest:
			done = False
	print(n)
print()
print(n)
