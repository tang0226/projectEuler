import math
total = 0
for r in range(1, 101):
	for n in range(r, 101):
		num = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
		if num > 1000000:
			total += 1
print(total)