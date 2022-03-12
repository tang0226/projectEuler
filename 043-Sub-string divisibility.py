from itertools import permutations
import math
nums = list("".join(i) for i in permutations("0123456789"))[math.factorial(9) : ]
primes = [2, 3, 5, 7, 11, 13, 17]
total = 0
for i in nums:
	valid = True
	for j in range(7):
		if int(i[j + 1 : j + 4]) % primes[j] != 0:
			valid = False
			break
	if not(valid):
		continue
	total += int(i)
	print(i, total)
