def first(n):
	digits = []
	for i in str(n)[ : 9]:
		digits.append(i)
	digits.sort()
	if digits == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
		return True
	return False

def last(n):
	digits = []
	for i in str(n)[-9 : ]:
		digits.append(i)
	digits.sort()
	if digits == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
		return True
	return False

fs = [0, 1]
target = 314313
i = 1
for j in range(target - 2):
	fs.append(fs[0] + fs[1])
	fs.pop(0)
	i += 1
while True:
	x = fs[0] + fs[1]
	fs.append(x)
	fs.pop(0)
	i += 1
	print(i)
	if first(x) and last(x):
		print(i)
		break