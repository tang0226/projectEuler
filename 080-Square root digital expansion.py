from decimal import *
getcontext().prec = 102
total = 0
upper = 100
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81]
for i in range(2, upper):
	if squares.count(i) == 1:
		continue
	s = str(Decimal(i) ** Decimal(1	/ 2))
	count = 0
	for j in range(len(s) - 2):
		if s[j] != ".":
			total += int(s[j])
print(total)