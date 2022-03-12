largestIndex = 0
largestBase = 519432
largestExp = 525806
filepath = "Input_files/099-base_exp.txt"
with open(filepath) as fp:
	line = fp.readline()
	currIndex = 1
	while line:
		line = line.strip()
		base = ""
		exp = ""
		mode = True
		for i in range(0, len(line)):
			if line[i] == ",":
				mode = False
				continue
			if mode:
				base += line[i]
			else:
				exp += line[i]
		base = int(base)
		exp = int(exp)
		newBase = base ** (exp / largestExp)
		if newBase > largestBase:
			largestBase = base
			largestExp = exp
			largestIndex = currIndex
			print(currIndex)
		currIndex += 1
		line = fp.readline()
fp.close()
