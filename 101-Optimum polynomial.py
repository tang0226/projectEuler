def u(n):
	return 1 - n + (n ** 2) - (n ** 3) + (n ** 4) - (n ** 5) + (n ** 6) - (n ** 7) + (n ** 8) - (n ** 9) + (n ** 10)

def getMatrix(degree):
	r = []
	for i in range(1, degree + 2):
		new = []
		for p in range(degree, -1, -1):
			new.append(i ** p)
		r.append(new)
	return r

def polynomial(x, coefficients):
	r = 0
	for i in range(len(coefficients)):
		r += coefficients[i] * (x ** (len(coefficients) - i - 1))
	return r

import numpy as np
from scipy.linalg import solve
terms = list(u(i) for i in range(1, 11))

total = 1

for degree in range(1, 10):
	a = getMatrix(degree)
	b = terms[ : degree + 1]
	c = list(int(round(i)) for i in solve(a, b))
	x = polynomial(degree + 2, c)
	total += x
	print(x, total)
print(total)