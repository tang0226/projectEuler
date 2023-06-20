cubes = []
target = 5
for i in range(465, 10000):
	cubes.append(i * i * i)
digits = []
for i in cubes:
	digits1 = []
	for j in str(i):
		digits1.append(int(j))
	digits1.sort()
	digits.append([digits1, i])
digits.sort()
same = 1
last = digits[0][0]
lastNum = 0
for i in range(1, len(digits)):
	if digits[i][0] == last:
		same += 1
	else:
		last = digits[i][0]
		lastNum = digits[i][1]
		same = 1
	if same == target:
		print(lastNum)
		break