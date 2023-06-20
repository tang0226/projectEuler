from functions import isPalindrome
nums = []
for i in range(100, 999):
	for j in range(i + 1, 1000):
		x = i * j
		if isPalindrome(x):
			nums.append(x)
print(max(nums))