total = 0
upper = 10 ** 12
results = [1]
for b in range(2, round(upper ** (1 / 2))):
	n = b + 1
	e = 2
	while True:
		n += b ** e
		if n > upper:
			break
		results.append(n)
		e += 1
	if b % 1000 == 0:
		print(b)
results.sort()
results = list(dict.fromkeys(results))
print(sum(results))