def isBouncy(n):
	string = str(n)
	seq = []
	valid = False
	for i in range(0, len(string) - 1):
		if int(string[i]) > int(string[i + 1]):
			seq.append(False)
		elif int(string[i]) < int(string[i + 1]):
			seq.append(True)
	if seq.count(True) > 0 and seq.count(False) > 0:
		valid = True
	return valid
bouncy = 0
num = 99
density = 0
done = False
while not(done):
	num += 1
	if isBouncy(num):
		bouncy += 1
	density = bouncy / num
	if density == 0.99:
		done = True
	print(num, density)
print(num)