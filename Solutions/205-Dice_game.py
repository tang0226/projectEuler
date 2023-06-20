amounts4 = []
amounts6 = []
for i in range(0, 37):
	amounts4.append(0)
	amounts6.append(0)
for i in range(1, 5):
	for j in range(1, 5):
		for k in range(1, 5):
			for l in range(1, 5):
				for m in range(1, 5):
					for n in range(1, 5):
						for o in range(1, 5):
							for p in range(1, 5):
								for q in range(1, 5):
									amounts4[i + j + k + l + m + n + o + p + q] += 1
for i in range(1, 7):
	for j in range(1, 7):
		for k in range(1, 7):
			for l in range(1, 7):
				for m in range(1, 7):
					for n in range(1, 7):
						amounts6[i + j + k + l + m + n] += 1
for i in range(len(amounts4)):
	amounts4[i] /= 4 ** 9
for i in range(len(amounts6)):
	amounts6[i] /= 6 ** 6


probability = 0


for i in range(0, len(amounts4)):
	currTotal = 0
	for j in range(0, i):
		currTotal += amounts6[j]
	probability += amounts4[i] * currTotal
print(probability)