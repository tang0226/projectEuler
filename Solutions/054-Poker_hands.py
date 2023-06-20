p1Wins = 0
values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
valuesInt = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
ranks = ["HC", "1P", "2P", "3K", "S", "F", "FH", "4K", "SF", "RF"]
def rank(ints, suits):
	if ints == [10, 11, 12, 13, 14] and suits.count(suits[0]) == 5:
		return ["RF", 0]
	
	if ints[0] + 1 == ints[1] and ints[1] + 1 == ints[2] and ints[2] + 1 == ints[3] and ints[3] + 1 == ints[4] and suits.count(suits[0]) == 5:
		return ["SF", ints[4]]
	
	if ints.count(ints[1]) == 4:
		return ["4K", ints[1]]
	
	if ints.count(ints[2]) == 3:
		if ints.count(ints[0]) == 2:
			return ["FH", ints[4]]
		if ints.count(ints[4]) == 2:
			return ["FH", ints[4]]
	
	if suits.count(suits[0]) == 5:
		return ["F", suits[4]]
	
	if ints[0] + 1 == ints[1] and ints[1] + 1 == ints[2] and ints[2] + 1 == ints[3] and ints[3] + 1 == ints[4]:
		return ["S", suits[4]]
	
	if ints.count(ints[2]) == 3:
		return ["3K", ints[2]]
	
	if ints.count(ints[1]) == 2 and ints.count(ints[3]) == 2:
		if ints[1] > ints[3]:
			return ["2P", ints[1]]
		else:
			return ["2P", ints[3]]
	
	for i in range(4):
		if ints.count(ints[i]) == 2:
			return ["1P", ints[i]]
	
	return ["HC", ints[4]]
last = 0
filepath = "Input_files/054-poker.txt"
with open(filepath) as fp:
	line = fp.readline()
	while line:
		line = line.strip()
		p1Hand = []
		p2Hand = []
		p1Ints = []
		p2Ints = []
		p1Suits = []
		p2Suits = []
		add = ""
		#initialize hands
		for i in line:
			if i == " ":
				if len(p1Hand) == 5:
					p2Hand.append(add)
				else:
					p1Hand.append(add)
				add = ""
			else:
				add += i
		p2Hand.append(add)
		for i in range(5):
			p1Ints.append(valuesInt[values.index(p1Hand[i][0])])
			p2Ints.append(valuesInt[values.index(p2Hand[i][0])])
			p1Suits.append(p1Hand[i][1])
			p2Suits.append(p2Hand[i][1])
		p1Ints.sort()
		p2Ints.sort()
		p1Rank = rank(p1Ints, p1Suits)
		p2Rank = rank(p2Ints, p2Suits)
		if ranks.index(p1Rank[0]) > ranks.index(p2Rank[0]):
			p1Wins += 1
		elif not(ranks.index(p2Rank[0]) > ranks.index(p1Rank[0])):
			if p1Rank[1] > p2Rank[1]:
				p1Wins += 1
			elif not(p2Rank[1] > p1Rank[1]):
				print(p1Ints, p2Ints, p1Rank)
		last = p1Wins
		line = fp.readline()
fp.close()
print(p1Wins)