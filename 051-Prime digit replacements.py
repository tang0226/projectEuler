def isPrime(n):
	if n < 2:
		return False
	if n < 4:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while(i * i <= n):
		if (n % i == 0 or n % (i + 2) == 0):
			return False
		i = i + 6
	return True

def insert(strIn, ins, index):
	return strIn[0 : index] + ins + strIn[index : ]

replaceDigits = []

for numDigits in range(2, 7):
	newSet = []
	for replace in range(1, 2 ** numDigits - 1):
		s = bin(replace)
		s = s[2 : ]
		for i in range(numDigits - len(s)):
			s = "0" + s
		new = []
		for i in s:
			if i == "0":
				new.append(False)
			else:
				new.append(True)
		
		newSet.append(new)
	replaceDigits.append(newSet)




#generate fixed digits, insert same digit, check

for numDigits in range(2, 7):
	for i in replaceDigits[numDigits - 2]:
		fCount = i.count(False)
		for digits in range(10 ** fCount):
			s = str(digits)
			for j in range(fCount - len(s)):
				s = "0" + s
			count = 0
			primes = []
			for digit in range(10):
				new = ""
				sUse = s
				for k in range(len(i)):
					if i[k]:
						new += str(digit)
					else:
						new += sUse[0]
						sUse = sUse[1 : ]
				if isPrime(int(new)) and new[0] != "0":
					count += 1
					primes.append(int(new))
			if len(primes) > 5:
				print(primes, count, numDigits, digits)