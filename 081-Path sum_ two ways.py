data = []
layers = []
filepath = "Input_files/081_082_083_matrix.txt"
with open(filepath) as fp:
	line = fp.readline()
	while line:
		line = line.strip()
		add = ""
		new = []
		for i in line:
			if i == ",":
				new.append(int(add))
				add = ""
			else:
				add += i
		new.append(int(add))
		data.append(new)
		line = fp.readline()
fp.close()
for startY in range(80):
	new = []
	x = 0
	for y in range(startY, -1, -1):
		new.append(data[y][x])
		x += 1
	layers.append(new)
for startX in range(1, 80):
	new = []
	y = 79
	for x in range(startX, 80):
		new.append(data[y][x])
		y -= 1
	layers.append(new)
while len(layers) > 80:
	l0 = len(layers[0]) - 1
	l1 = len(layers[1]) - 1
	for i in range(l1 + 1):
		if i == 0:
			layers[1][0] += layers[0][0]
		elif i == l1:
			layers[1][l1] += layers[0][l0]
		elif layers[0][i - 1] < layers[0][i]:
			layers[1][i] += layers[0][i - 1]
		else:
			layers[1][i] += layers[0][i]
	layers.pop(0)
layers.reverse()
for i in range(len(layers) - 2, -1, -1):
	for j in range(0, len(layers[i])):
		if layers[i + 1][j] < layers[i + 1][j + 1]:
			layers[i][j] += layers[i + 1][j]
		else:
			layers[i][j] += layers[i + 1][j + 1]
	layers.pop(-1)
print(layers[0][0])

		