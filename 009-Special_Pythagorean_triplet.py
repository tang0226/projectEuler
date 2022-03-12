done = False
for a in range(3, 997):
	if done:
		break
	print(a)
	for b in range(a + 1, 998):
		if a + b > 1000:
			break
		if done:
			break
		for c in range(b + 1, 999):
			if a + b + c > 1000:
				break
			if a * a + b * b == c * c:
				if a + b + c == 1000:
					print(a, b, c, a * b * c)
					done = True
					break