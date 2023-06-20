from functions import isPrime, primesUnder
from itertools import permutations

def noRepeats(n):
	digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in str(n):
		digits[int(i)] += 1
		if max(digits) > 1:
			return False
	return True

def no0(n):
	return str(n).count("0") == 0

primes = list(i for i in primesUnder(10000) if noRepeats(i) and no0(i))

total = 0
for i in primes:
	digits = "123456789"
	for j in str(i):
		digits = digits.replace(j, "")
	for j in ["".join(p) for p in permutations(digits)]:
		if isPrime(int(j)):
			total += 1
			print(i, int(j), total)

for i in range(len(primes) - 1):
	for j in range(i + 1, len(primes)):
		digits = "123456789"
		p1 = primes[i]
		p2 = primes[j]
		digitCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		valid = True
		for k in str(p1) + str(p2):
			digitCounts[int(k)] += 1
			if max(digitCounts) > 1:
				valid = False
				break
		if not(valid):
			continue
		for k in str(p1) + str(p2):
			digits = digits.replace(k, "")
		for k in ["".join(p) for p in permutations(digits)]:
			if isPrime(int(k)) and int(k) > p2:
				total += 1
				print(p1, p2, int(k), total)

for i in range(len(primes) - 2):
	for j in range(i + 1, len(primes) - 1):
		for k in range(j + 1, len(primes)):
			p1 = primes[i]
			p2 = primes[j]
			p3 = primes[k]
			if len(str(p1)) + len(str(p2)) + len(str(p3)) > 8:
				break
			digitCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			valid = True
			for l in str(p1) + str(p2) + str(p3):
				digitCounts[int(l)] += 1
				if max(digitCounts) > 1:
					valid = False
					break
			if not(valid):
				continue
			digits = "123456789"
			for l in str(p1) + str(p2) + str(p3):
				digits = digits.replace(l, "")
			for l in ["".join(p) for p in permutations(digits)]:
				if isPrime(int(l)) and int(l) > p3:
					total += 1
					print(p1, p2, p3, int(l), total)

for i in range(len(primes) - 3):
	for j in range(i + 1, len(primes) - 2):
		for k in range(j + 1, len(primes) - 1):
			for l in range(k + 1, len(primes)):
				p1 = primes[i]
				p2 = primes[j]
				p3 = primes[k]
				p4 = primes[l]
				if len(str(p1)) + len(str(p2)) + len(str(p3)) + len(str(p4)) > 8:
					break
				digitCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
				valid = True
				for m in str(p1) + str(p2) + str(p3) + str(p4):
					digitCounts[int(m)] += 1
					if max(digitCounts) > 1:
						valid = False
						break
				if not(valid):
					continue
				digits = "123456789"
				for m in str(p1) + str(p2) + str(p3) + str(p4):
					digits = digits.replace(m, "")
				for m in ["".join(p) for p in permutations(digits)]:
					if isPrime(int(m)) and int(m) > p4:
						total += 1
						print(p1, p2, p3, p4, int(m), total)

primes3Digit = []
for i in primes:
	if len(str(i)) < 3:
		primes3Digit.append(i)
	else:
		break

for i in range(len(primes3Digit) - 4):
	for j in range(i + 1, len(primes3Digit) - 3):
		for k in range(j + 1, len(primes3Digit) - 2):
			for l in range(k + 1, len(primes3Digit) - 1):
				for m in range(l + 1, len(primes3Digit)):
					p1 = primes3Digit[i]
					p2 = primes3Digit[j]
					p3 = primes3Digit[k]
					p4 = primes3Digit[l]
					p5 = primes3Digit[m]
					if len(str(p1)) + len(str(p2)) + len(str(p3)) + len(str(p4)) + len(str(p5)) > 8:
						break
					digitCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					valid = True
					for n in str(p1) + str(p2) + str(p3) + str(p4) + str(p5):
						digitCounts[int(n)] += 1
						if max(digitCounts) > 1:
							valid = False
							break
					if not(valid):
						continue
					digits = "123456789"
					for n in str(p1) + str(p2) + str(p3) + str(p4) + str(p5):
						digits = digits.replace(n, "")
					for n in ["".join(p) for p in permutations(digits)]:
						if isPrime(int(n)) and int(n) > p5:
							total += 1
							print(p1, p2, p3, p4, p5, int(n), total)

print(total)