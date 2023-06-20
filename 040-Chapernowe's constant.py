text = "."
i = 1
num = 1
while len(text) < 1000000:
	text += str(i)
	i += 1
for j in range(6):
	num *= int(text[10 ** j])
print(num)