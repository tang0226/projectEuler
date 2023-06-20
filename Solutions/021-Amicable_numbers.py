import math

# my d function
def d(n):
	if n == 1:
		return 1
	factors = 1
	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if n % i == 0:
			factors += i
			if n / i != i:
				factors += int(n / i)
	return factors

total = 0

# find amicable number pairs
for a in range(1, 10000):
	b = d(a)
	if b != a and d(b) == a:
		total += a + b
		print(a, b)

# don't count repeats
total = int(total / 2)

# print the result
print(total)