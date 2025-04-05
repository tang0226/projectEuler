matrix = []
layers = []
filepath = "Code/Input_files/081_082_083_matrix.txt"

with open(filepath) as fp:
	line = fp.readline()
	while line:
		matrix.append([int(i) for i in line.strip().split(",")])
		line = fp.readline()
fp.close()


"""matrix = [
  [131, 673, 234, 103, 18],
  [201, 96, 342, 965, 150],
  [630, 803, 746, 422, 111],
  [537, 699, 497, 121, 956],
  [805, 732, 524, 37, 331]
]"""

w = len(matrix[0])
h = len(matrix)
print(w, h)



minSum = [[1e10] * w for i in range(h)]

minSum[0][0] = matrix[0][0]

while True:
  # up
  for y in range(1, h):
    for x in range(w):
      val = minSum[y - 1][x] + matrix[y][x]
      if val < minSum[y][x]:
        minSum[y][x] = val
  # down
  for y in range(h - 1):
    for x in range(w):
      val = minSum[y + 1][x] + matrix[y][x]
      if val < minSum[y][x]:
        minSum[y][x] = val
  # left
  for x in range(1, w):
    for y in range(h):
      val = minSum[y][x - 1] + matrix[y][x]
      if val < minSum[y][x]:
        minSum[y][x] = val
  # right
    for x in range(w - 1):
      for y in range(h):
        val = minSum[y][x + 1] + matrix[y][x]
        if val < minSum[y][x]:
          minSum[y][x] = val
  
  print(minSum[-1][-1])