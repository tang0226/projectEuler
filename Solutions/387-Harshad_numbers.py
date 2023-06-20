import math

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
 
def digitSum(n):
	return sum(list(int(i) for i in str(n)))

def isHarshad(n):
	return n % digitSum(n) == 0

def isTruncatable(n):
	if not(isHarshad(n)):
		return False
	s = str(n)
	s = s[0 : len(s) - 1]
	if s == "":
		return True
	if not(isHarshad(int(s))):
		return False
	return isTruncatable(int(s))

def isStrong(n):
	return isPrime(n / digitSum(n))

total = 0

for a in range(10, 100):
	if isHarshad(a):
		if isTruncatable(a) and isStrong(a):
			for x in [1, 3, 7, 9]:
				b = a * 10 + x
				if isPrime(b):
					total += b
					print(b, total)
		for b in range(10):
			a1 = a * 10 + b
			if isHarshad(a1):
				if isTruncatable(a1) and isStrong(a1):
					for x in [1, 3, 7, 9]:
						b1 = a1 * 10 + x
						if isPrime(b1):
							total += b1
							print(b1, total)
				for c in range(10):
					a2 = a1 * 10 + c
					if isHarshad(a2):
						if isTruncatable(a2) and isStrong(a2):
							for x in [1, 3, 7, 9]:
								b2 = a2 * 10 + x
								if isPrime(b2):
									total += b2
									print(b2, total)
						for d in range(10):
							a3 = a2 * 10 + d
							if isHarshad(a3):
								if isTruncatable(a3) and isStrong(a3):
									for x in [1, 3, 7, 9]:
										b3 = a3 * 10 + x
										if isPrime(b3):
											total += b3
											print(b3, total)
								for e in range(10):
									a4 = a3 * 10 + e
									if isHarshad(a4):
										if isTruncatable(a4) and isStrong(a4):
											for x in [1, 3, 7, 9]:
												b4 = a4 * 10 + x
												if isPrime(b4):
													total += b4
													print(b4, total)
										for f in range(10):
											a5 = a4 * 10 + f
											if isHarshad(a5):
												if isTruncatable(a5) and isStrong(a5):
													for x in [1, 3, 7, 9]:
														b5 = a5 * 10 + x
														if isPrime(b5):
															total += b5
															print(b5, total)
												for g in range(10):
													a6 = a5 * 10 + g
													if isHarshad(a6):
														if isTruncatable(a6) and isStrong(a6):
															for x in [1, 3, 7, 9]:
																b6 = a6 * 10 + x
																if isPrime(b6):
																	total += b6
																	print(b6, total)
														for h in range(10):
															a7 = a6 * 10 + h
															if isHarshad(a7):
																if isTruncatable(a7) and isStrong(a7):
																	for x in [1, 3, 7, 9]:
																		b7 = a7 * 10 + x
																		if isPrime(b7):
																			total += b7
																			print(b7, total)
																for i in range(10):
																	a8 = a7 * 10 + i
																	if isHarshad(a8):
																		if isTruncatable(a8) and isStrong(a8):
																			for x in [1, 3, 7, 9]:
																				b8 = a8 * 10 + x
																				if isPrime(b8):
																					total += b8
																					print(b8, total)
																		for j in range(10):
																			a9 = a8 * 10 + j
																			if isHarshad(a9):
																				if isTruncatable(a9) and isStrong(a9):
																					for x in [1, 3, 7, 9]:
																						b9 = a9 * 10 + x
																						if isPrime(b9):
																							total += b9
																							print(b9, total)
																				for k in range(10):
																					a10 = a9 * 10 + k
																					if isHarshad(a10):
																						if isTruncatable(a10) and isStrong(a10):
																							for x in [1, 3, 7, 9]:
																								b10 = a10 * 10 + x
																								if isPrime(b10):
																									total += b10
																									print(b10, total)
																						for l in range(10):
																							a11 = a10 * 10 + l
																							if isHarshad(a11):
																								if isTruncatable(a11) and isStrong(a11):
																									for x in [1, 3, 7, 9]:
																										b11 = a11 * 10 + x
																										if isPrime(b11):
																											total += b11
																											print(b11, total)
print(total)