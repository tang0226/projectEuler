N = 7
P = 2 ** N
D = []
for y in range(P - 1, -1, -1):
	row = ""
	for x in range(P):
		if (x - 2 ** (N - 1)) ** 2 + (y - 2 ** (N - 1)) ** 2 <= 2 ** (2 * N - 2):
			row += "0"
		else:
			row += "1"
	D.append(row)
for i in D:
	print(i)
print(len(D), len(D[0]))