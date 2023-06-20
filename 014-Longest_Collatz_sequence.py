import math

def collatz(n):
	if n % 2 == 0:
		return n // 2
	else:
		return 3 * n + 1

def is2Power(n):
	log = math.log(n, 2)
	if log == log // 1:
		return True
	return False

longestStart = 0
longestLength = 0

for i in range(999999, 1, -1):
	length = 1
	currNum = i
	while currNum > 1:
		if is2Power(currNum):
			length += int(math.log(currNum, 2))
			break
		currNum = collatz(currNum)
		length += 1
	if length > longestLength:
		longestLength = length
		longestStart = i
	print(i, length, longestLength, longestStart)