from functions import digitSum
counts = []

for i in range(100):
	if digitSum(i) <= 9:
		counts.append(9 - digitSum(i))
	else:
		counts.append(0)

digits = 20

for i in range(digits - 3):
	new = [0] * 100
	for j in range(100):
		for k in range(9 - digitSum(j) + 1):
			new[int(str(j)[-1] + str(k))] += counts[j]
	counts = new
print(counts, sum(counts))