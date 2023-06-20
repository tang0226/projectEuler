def area(x1, y1, x2, y2, x3, y3):
	return abs((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))) / 2

def containsOrigin(x1, y1, x2, y2, x3, y3):
	a = area(x1, y1, x2, y2, x3, y3)
	a1 = area(0, 0, x2, y2, x3, y3)
	a2 = area(x1, y1, 0, 0, x3, y3)
	a3 = area(x1, y1, x2, y2, 0, 0)
	return a == a1 + a2 + a3

total = 0
filepath = "Input_files/102-triangles.txt"
with open(filepath) as fp:
	line = fp.readline()
	while line:
		line = line.strip()
		triangle = []
		new = ""
		for i in line:
			if i == ",":
				triangle.append(int(new))
				new = ""
			else:
				new += i
		triangle.append(int(new))
		if containsOrigin(triangle[0], triangle[1], triangle[2], triangle[3], triangle[4], triangle[5]):
			total += 1
		line = fp.readline()
fp.close()
print(total)