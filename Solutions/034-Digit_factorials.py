import math

factorialDigits = []
for i in range(10):
	factorialDigits.append(math.factorial(i))

def digitFactorialSum(n):
	return sum(list(factorialDigits[int(i)] for i in str(n)))

total = 0
for i in range(10, 100000):
	if i == digitFactorialSum(i):
		total += i
		print(i, total)