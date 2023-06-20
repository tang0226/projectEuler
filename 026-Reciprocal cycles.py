import math
longest = 0
longestNum = 0
for i in range(2, 1000):
	done = False
	currLength = 0
	remainder = 1
	remainders = []
	while not(done):
		remainder = int(str(remainder % i) + "0")
		if remainders.count(remainder) == 1:
			done = True
		if not(done):
			currLength += 1
			remainders.append(remainder)
	if currLength > longest:
		longest = currLength
		longestNum = i
print(longestNum)