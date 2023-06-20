from math import comb
from time import time
start = time()
def p(n):
	r = 0
	for streak in range(1, n):
		sequences = comb(n, streak) - 1
		r += sequences * comb(26, n)
	return r
print(max(p(i) for i in range(3, 27)), time() - start)