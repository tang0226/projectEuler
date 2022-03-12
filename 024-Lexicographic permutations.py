def permutation(digits, permNum):
	import math
	currFact = len(digits) - 1
	perm = ""
	permNum1 = permNum - 1
	for i in range(0, len(digits)):
		fact = math.factorial(currFact)
		perm += str(digits.pop(math.floor(permNum1 / fact)))
		if permNum1 - fact * math.floor(permNum1 / fact) >= 0:
			permNum1 -= fact * math.floor(permNum1 / fact)
		currFact -= 1
	return perm
print(permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000))