import math
def fCount(num):
	tot = 0
	for i in range(1, math.floor(math.sqrt(num)) + 1):
		if num % i == 0:
			if num / i == i:
				tot += 1
			else:
				tot += 2
	return tot

def primeFCount(num):
	tot = 0
	for i in range(1, math.floor(math.sqrt(num)) + 1):
		if num % i == 0:
			if num / i == i:
				if fCount(num / i) == 2:
					tot += 1
			else:
				if fCount(num / i) == 2:
					tot += 1
				if fCount(i) == 2:
					tot += 1
	return tot


done = False
a = 0
while not(done):
	a += 1
	nums = [a, a + 1, a + 2, a + 3]
	done = True
	for i in nums:
		if primeFCount(i) != 4:
			done = False
	print(a)
print()
print(a)