from functions import factorial, decToBase

def nk(n, k):
	return factorial(n) / factorial(k) / factorial(n - k)

maxDigs = 16
total = 0

for digs in range(3, maxDigs + 1):
	for count0 in range(1, digs - 1):
		for count1 in range(1, digs - count0):
			for countA in range(1, digs - count0 - count1 + 1):
				other = digs - count0 - count1 - countA
				start1 = factorial(digs - 1) / factorial(count0) / factorial(count1 - 1) / factorial(countA) / factorial(other)
				startA = factorial(digs - 1) / factorial(count0) / factorial(count1) / factorial(countA - 1) / factorial(other)
				if other:
					startOther = factorial(digs - 1) / factorial(count0) / factorial(count1) / factorial(countA) / factorial(other - 1)
					total += startOther * (13 ** other)
				total += (start1 + startA) * (13 ** other)
	print(digs)
total = int(total)
print(total)
print(total, decToBase(total, 16))