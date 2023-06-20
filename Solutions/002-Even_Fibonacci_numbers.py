num1 = 0
num2 = 1
count = 1
total = 0
while num1 <= 4000000:
	count += 1
	store2 = num2
	num2 += num1
	num1 = store2
	if num1 % 2 == 0:
		total += num1
print(total)