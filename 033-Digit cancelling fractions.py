nums = []
for i in range(10, 100):
	for j in range(i + 1, 100):
		strI = str(i)
		strJ = str(j)
		numerator = 0
		denominator = 0
		if int(strI[0]) > 0 and int(strI[1]) > 0 and int(strJ[0]) > 0 and int(strJ[1]) > 0:
			if strI[0] != strI[1] and strJ[0] != strJ[1]:
				valid = True
				if strI[0] == strJ[1]:
					numerator = int(strI[1])
					denominator = int(strJ[0])
				elif strI[1] == strJ[0]:
					numerator = int(strI[0])
					denominator = int(strJ[1])
				else:
					valid = False
				if valid:
					if numerator / denominator == i / j:
						print(i, j)
						nums.append([numerator, denominator])
numerator = 1
denominator = 1
for i in range(0, 4):
	numerator *= nums[i][0]
	denominator *= nums[i][1]
print(numerator, denominator)