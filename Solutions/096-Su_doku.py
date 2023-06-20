affected = []
for y in range(9):
	row = []
	for x in range(9):
		area = []
		for pos in range(9):
			if not (pos == x and pos == y):
				area.append((x, pos))
				area.append((pos, y))
		regionX = (x // 3) * 3
		regionY = (y // 3) * 3
		for i in range(regionX, regionX + 3):
			if i == x:
				continue
			for j in range(regionY, regionY + 3):
				if j == y:
					continue
				area.append((i, j))
		area = list(dict.fromkeys(area))
		area.sort()
		row.append(area)
	affected.append(row)

def convert(grid):
	converted = []
	for y in range(9):
		row = []
		for x in range(9):
			if grid[y][x] != 0:
				row.append('Done')
			else:
				possible = list(range(1, 10))
				for coord in affected[y][x]:
					remove = grid[coord[1]][coord[0]]
					if remove in possible:
						possible.remove(remove)
				row.append(possible)
		converted.append(row)
	return converted

def solve(grid):
	converted = convert(grid)
	leastCoords = ()
	leastLength = 9
	for y in range(9):
		for x in range(9):
			test = converted[y][x]
			if test != 'Done':
				if len(test) < leastLength:
					leastLength = len(test)
					leastCoords = (x, y)
	x = leastCoords[0]
	y = leastCoords[1]
	possible = converted[y][x]
	for test in possible:
		gridCopy = list(i.copy() for i in grid)
		gridCopy[y][x] = test
		valid = True
		for i in gridCopy:
			for j in i:
				if j == 0:
					valid = False
					break
			if not valid:
				break
		if valid:
			nums = gridCopy[0][ : 3]
			return (nums[0] * 100) + (nums[1] * 10) + nums[2]
		result = solve(gridCopy)
		if result:
			return result
	return False

grids = []
with open('Input_files/096_sudoku.txt') as f:
	line = f.readline().strip()
	grid = []
	while line:
		if line[0] == 'G':
			grids.append(grid)
			grid = []
		else:
			grid.append(list(int(i) for i in line))
		line = f.readline().strip()
grids.append(grid)
grids = grids[1 : ]

total = 0
for i in range(50):
	solved = solve(grids[i])
	total += solved
	print(i, solved, total)