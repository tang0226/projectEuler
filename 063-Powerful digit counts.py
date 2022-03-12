total = 0
for base in range(1, 100):
	for exp in range(1, 100):
		if len(str(base ** exp)) == exp:
			total += 1
			print(base ** exp, total)