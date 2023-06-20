def last10(n):
	s = str(n)
	l = len(s)
	return int(s[l - 10 : ])
n = 28433
for i in range(7830457):
	n *= 2
	if len(str(n)) >= 10:
		n = last10(n)
n = last10(n + 1)
print(n)