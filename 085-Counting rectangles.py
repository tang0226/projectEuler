def numRectangles(l, w):
	total = 0
	for subL in range(1, l + 1):
		for subW in range(1, w + 1):
			total += ((l - subL) + 1) * ((w - subW) + 1)
	return total
import math
smallest = 1000000
smallestNum = 0
for a in range(1, 100):
	for b in range(1, 100):
		add = [int(math.fabs(2000000 - numRectangles(a, b))), a * b]
		if add[0] < smallest:
			smallest = add[0]
			smallestNum = add[1]
		print(a, b, add[0], smallest, smallestNum)
