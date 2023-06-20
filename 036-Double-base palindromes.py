def isPalindrome(n):
	s = str(n)
	if s == s[ :: -1]:
		return True
	return False

total = 0
for i in range(1, 1000000):
	b = int(bin(i)[2 : ])
	if isPalindrome(i) and isPalindrome(b):
		total += i
		print(i, total)