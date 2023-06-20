def isPandigital(n):
	digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in str(n):
		digits[int(i)] += 1
	if digits == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
		return True
	return False

largest = 0
for i in range(1, 1000000):
	s = ""
	add = i
	while len(s) < 9:
		s += str(add)
		add += i
	if len(s) != 9:
		continue
	s = int(s)
	if isPandigital(s):
		if s > largest:
			largest = s
		print(i, s, largest)