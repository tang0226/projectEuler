from math import factorial
factorials = list(factorial(i) for i in range(19))

def numbers(digitCounts):
	if digitCounts[-1] == 0:
		return 0
	nums = 0
	for i in range(1, len(digitCounts)):
		temp = list(j for j in digitCounts)
		temp[i] -= 1
		add = factorials[17]
		for j in temp:
			add = int(add / factorials[j])
		nums += add
	return nums

total = 0

for count0 in range(4):

	for count1 in range(4):

		for count2 in range(4):

			for count3 in range(4):

				for count4 in range(4):

					for count5 in range(4):

						digitCounts1 = [count0, count1, count2, count3, count4, count5]
						numDigits1 = sum(digitCounts1)

						if numDigits1 == 18:
							x = numbers(digitCounts1)
							if x:
								total += x
								print(digitCounts1, x, total, 1)

						for count6 in range(4):

							digitCounts2 = digitCounts1 + [count6]
							numDigits2 = numDigits1 + count6

							if numDigits2 > 18:
								break

							if numDigits2 == 18:
								x = numbers(digitCounts2)
								if x:
									total += x
									print(digitCounts2, x, total, 2)

							for count7 in range(4):

								digitCounts3 = digitCounts2 + [count7]
								numDigits3 = numDigits2 + count7

								if numDigits3 > 18:
									break

								if numDigits3 == 18:
									x = numbers(digitCounts3)
									if x:
										total += x
										print(digitCounts3, x, total, 3)

								for count8 in range(4):

									digitCounts4 = digitCounts3 + [count8]
									numDigits4 = numDigits3 + count8

									if numDigits4 > 18:
										break

									if numDigits4 == 18:
										x = numbers(digitCounts4)
										if x:
											total += x
											print(digitCounts4, x, total, 4)

									for count9 in range(4):

										digitCounts5 = digitCounts4 + [count9]
										numDigits5 = numDigits4 + count9
										
										if numDigits5 > 18:
											break

										if numDigits5 == 18:
											x = numbers(digitCounts5)
											total += x
											print(digitCounts5, x, total, 5)

print(total)