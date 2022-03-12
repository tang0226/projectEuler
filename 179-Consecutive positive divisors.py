from functions import factorCount
start = 9614014
new = 8
total = 948670
upper = 10 ** 7
# 5798194 576170 8
# 9614013 948670 8
for i in range(start, upper):
	f = factorCount(i + 1)
	if f == new:
		total += 1
		print(i, total, new)
	new = f
print(total)