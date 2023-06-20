def digitSum(n):
	return sum(int(i) for i in str(n))
results = []
for e in range(15):
	for b in range(100):
		n = b ** e
		if digitSum(n) == b and len(str(n)) > 1:
			results.append(n)
results.sort()
print(results[29])