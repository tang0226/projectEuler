results = []
for a in range(2, 101):
	for b in range(2, 101):
		results.append(a ** b)
print(len(list(dict.fromkeys(results))))