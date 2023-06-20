import math
total = 0
def isPalindrome(num):
	return num == reverseNum(num)

def reverseNum(num):
	newText = ""
	text = str(num)
	length = len(text)
	for i in range(0, length):
		newText += text[length - i - 1]
	output = int(newText)
	return output

for i in range(1, 10000):
	done = False
	currNum = i
	for j in range(50):
		if not(done):
			num2 = reverseNum(currNum)
			currNum += num2
			if isPalindrome(currNum):
				done = True
	if not(done):
		total += 1
		print(i)
print()
print(total)
