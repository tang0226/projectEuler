import math
def isPalindrome(n):
	s = str(n)
	if s == s[ :: -1]:
		return True
	return False
total = 0
upper = 10 ** 8
results = []
for start in range(1, round(math.sqrt(upper)) - 1):
	n = start * start
	if n > upper:
		break
	for square in range(start + 1, round(math.sqrt(upper))):
		n += square * square
		if n < upper:
			if isPalindrome(n):
				total += n
				results.append(n)
		else:
			break
results = list(dict.fromkeys(results))
print(sum(results))