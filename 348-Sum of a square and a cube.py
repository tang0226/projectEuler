import math
# isPalindrome function
def isPalindrome(n):
	s = str(n)
	n = len(s) / 2
	if s[ : math.ceil(n)] == (s[math.floor(n) : ])[math.ceil(n) :: -1]:
		return True
	return False

results = []
print("generating palindromic sums...")
squareUpper = 30000
cubeUpper = 3000
# produce valid numbers
for s in range(1, squareUpper):
	odd = 0
	if s % 2 == 0:
		odd = 1
	else:
		odd = 2
	for c in range(odd, cubeUpper, 2):
		n = (s * s) + (c * c * c)
		if isPalindrome(n):
			results.append(n)
	print(s, squareUpper - s)
print("sorting..")
# after producing the numbers, sort
results.sort()
print("checking")
# find the first 5 that appear exactly 4 times
total = 0
for i in range(len(results) - 5):
	if results[i] == results[i + 1] == results[i + 2] == results[i + 3] != results[i + 4]:
		total += results[i]
		print(results[i], total)
