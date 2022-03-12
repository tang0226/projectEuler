i = 1010101030
lastAdd = 60
while True:
	if lastAdd == 40:
		i += 60
		lastAdd = 60
	elif lastAdd == 60:
		i += 40
		lastAdd = 40
	s = str(i ** 2)
	if s[0] == "1" and s[2] == "2" and s[4] == "3" and s[6] == "4" and s[8] == "5" and s[10] == "6" and s[12] == "7" and s[14] == "8" and s[16] == "9" and s[18] == "0":
		break
print(i)