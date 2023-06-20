import math
total = 0
length = 50
for red in range((length // 2) + 1):
	for green in range((length // 3) + 1):
		for blue in range((length // 4) + 1):
			if (red * 2) + (green * 3) + (blue * 4) > length:
				break
			grey = length - (2 * red) - (3 * green) - (4 * blue)
			add = math.factorial(red + green + blue + (grey))
			add /= math.factorial(red) * math.factorial(green) * math.factorial(blue)
			add /= math.factorial(grey)
			total += add
		if (red * 2) + (green * 3) > length:
			break
total = int(total)
print(total)