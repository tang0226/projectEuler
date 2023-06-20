import math

def isPrime(n):
  if n < 2:
    return False
  if n < 4:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
  return True

def primesUnder(n):
	r = []
	for i in range(2, math.ceil(n)):
		if isPrime(i):
			r.append(i)
	return r

upper = 50000000
nums = [0] * upper

squares = primesUnder(int(upper ** (1 / 2)))
cubes = primesUnder(int(upper ** (1 / 3)))
fourths = primesUnder(int(upper ** (1 / 4)))

total = 0

for i in squares:
	for j in cubes:
		for k in fourths:
			num = (i ** 2) + (j ** 3) + (k ** 4)
			if num < upper and nums[num] == 0:
				total += 1
				nums[num] = 1
				print(i, j, k, num, total, squares[len(squares) - 1])
print(total)