from functions import isPrime, digitSum

segments = ["1111110", "0110000", "1101101", "1111001", "0110011", "1011011", "1011111", "1110010", "1111111", "1111011"]
common = []
for i in range(10):
	new = []
	for j in range(10):
		add = 0
		for x in range(7):
			if segments[i][x] == "1" and segments[j][x] == "1":
				add += 1
		new.append(add)
	common.append(new)

def difference(n):
	r = 0
	lastNum = n
	x = digitSum(n)
	while len(str(lastNum)) > 1:
		temp = str(lastNum)
		temp = temp[0 - len(str(x)) : ]
		for a in range(len(temp)):
			r += common[int(str(x)[a])][int(temp[a])] * 2
		lastNum = x
		x = digitSum(x)
	return r

tot = 0

for a in range(10 ** 7 + 1, 2 * 10 ** 7, 2):
	if isPrime(a):
		d = difference(a)
		tot += d
		print(a, d, tot)
print(tot)