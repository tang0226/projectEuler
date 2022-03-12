"""

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

"""
total = 0
newData = []
numerals = ["I", "V", "X", "L", "C", "D", "M"]
numeralValues = [1, 5, 10, 50, 100, 500, 1000]


filepath = "Input_files/089-roman.txt"
with open(filepath) as fp:
	line = fp.readline()
	cnt = 1
	while line:
		line = line.strip()
		lengthRoman = len(line)
		currTotal = 0
		for j in range(lengthRoman):
			currTotal += numeralValues[numerals.index(line[j])]
		latestCharValue = numeralValues[numerals.index(line[0])]
		for j in range(1, lengthRoman):
			currCharValue = numeralValues[numerals.index(line[j])]
			if currCharValue > latestCharValue:
				currTotal -= latestCharValue * 2
			latestCharValue = numeralValues[numerals.index(line[j])]



		string = str(currTotal)
		lengthTotal = len(string)
		new = ""
		digits = []
		for i in range(lengthTotal):
			digits.append(int(string[i]))
		if lengthTotal == 4:
			for i in range(int(string[0])):
				new += "M"
			

			if digits[1] == 9:
				new += "CM"
			elif digits[1] == 4:
				new += "CD"
			elif digits[1] > 4:
				new += "D"
				for i in range(digits[1] - 5):
					new += "C"
			else:
				for i in range(digits[1]):
					new += "C"
			

			if digits[2] == 9:
				new += "XC"
			elif digits[2] == 4:
				new += "XL"
			elif digits[2] > 4:
				new += "L"
				for i in range(digits[2] - 5):
					new += "X"
			else:
				for i in range(digits[2]):
					new += "X"
			

			if digits[3] == 9:
				new += "IX"
			elif digits[3] == 4:
				new += "IV"
			elif digits[3] > 4:
				new += "V"
				for i in range(digits[3] - 5):
					new += "I"
			else:
				for i in range(digits[3]):
					new += "I"
		

		
		elif lengthTotal == 3:


			if digits[0] == 9:
				new += "CM"
			elif digits[0] == 4:
				new += "CD"
			elif digits[0] > 4:
				new += "D"
				for i in range(digits[0] - 5):
					new += "C"
			else:
				for i in range(digits[0]):
					new += "C"
			

			if digits[1] == 9:
				new += "XC"
			elif digits[1] == 4:
				new += "XL"
			elif digits[1] > 4:
				new += "L"
				for i in range(digits[1] - 5):
					new += "X"
			else:
				for i in range(digits[1]):
					new += "X"
			

			if digits[2] == 9:
				new += "IX"
			elif digits[2] == 4:
				new += "IV"
			elif digits[2] > 4:
				new += "V"
				for i in range(digits[2] - 5):
					new += "I"
			else:
				for i in range(digits[2]):
					new += "I"
		


		elif lengthTotal == 2:


			if digits[0] == 9:
				new += "XC"
			elif digits[0] == 4:
				new += "XL"
			elif digits[0] > 4:
				new += "L"
				for i in range(digits[0] - 5):
					new += "X"
			else:
				for i in range(digits[0]):
					new += "X"
			

			if digits[1] == 9:
				new += "IX"
			elif digits[1] == 4:
				new += "IV"
			elif digits[1] > 4:
				new += "V"
				for i in range(digits[1] - 5):
					new += "I"
			else:
				for i in range(digits[1]):
					new += "I"
		else:
			if digits[0] == 9:
				new += "IX"
			elif digits[0] == 4:
				new += "IV"
			elif digits[0] > 4:
				new += "V"
				for i in range(digits[0] - 5):
					new += "I"
			else:
				for i in range(digits[0]):
					new += "I"
		gain = lengthRoman - len(new)
		total += gain
		print("Id: {},Decimal: {},Start: {},End: {},Gain: {},Total gain: {}".format(cnt, currTotal, line, new, gain, total))
		cnt += 1
		line = fp.readline()
fp.close()
print(total)