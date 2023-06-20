import math
def permutation(digits, permNum):
	import math
	digits1 = []
	for i in digits:
		digits1.append(i)
	currFact = len(digits1) - 1
	perm = ""
	permNum1 = permNum - 1
	for i in range(0, len(digits1)):
		fact = math.factorial(currFact)
		perm += str(digits1.pop(math.floor(permNum1 / fact)))
		if permNum1 - fact * math.floor(permNum1 / fact) >= 0:
			permNum1 -= fact * math.floor(permNum1 / fact)
		currFact -= 1
	return perm
def isPrime(num):
	tot = 0
	prime = True
	for i in range(1, math.floor(math.sqrt(num)) + 1):
		if num % i == 0:
			if num / i == i:
				tot += 1
			else:
				tot += 2
		if tot > 2:
			prime = False
			break
	if prime:
		return True
	else:
		return False


primes = []
for i in range(1000, 10000):
	if isPrime(i):
		primes.append(i)
for i in primes:
	string = str(i)
	perms = []
	nums = []
	for j in range(0, 4):
		nums.append(int(string[j]))
	for j in range(1, 25):
		p = permutation(nums, j)
		if isPrime(int(p)) and perms.count(p) == 0 and p[0] != "0":
			perms.append(p)
	perms.sort()
	for j in range(0, len(perms) - 2):
		test = [perms[j : j + 3]]
		print(test)
		test.sort()
		if int(test[0][2]) - int(test[0][1]) == int(test[0][1]) - int(test[0][0]):
			print(int(test[0][2]) - int(test[0][1]), int(test[0][1]) - int(test[0][0]), int(test[0][2]) - int(test[0][1]) == int(test[0][1]) - int(test[0][0]))
			print(test)
			break
		