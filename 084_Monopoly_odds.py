from random import randint
SQUARES = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']
COMMUNITY_CHEST = ['GO', 'JAIL'] + ([''] * 14)
CHANCE = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'NR', 'NR', 'NU', '-3'] + ([''] * 6)
DIE = 4
def roll():
	n1 = randint(1, DIE)
	n2 = randint(1, DIE)
	return (n1 + n2, n1 == n2)
def getCC():
	return COMMUNITY_CHEST[randint(0, 15)]
def getCH():
	return CHANCE[randint(0, 15)]
def newPos(i, r):
	return (i + r) % 40
posMap = {}
for i in range(40):
	posMap[SQUARES[i]] = i
results = {}
for i in SQUARES:
	results[i] = 0
results['GO'] = 1
currPos = 0
currSquare = 'GO'
def goTo(square):
	global currPos, currSquare
	currPos = posMap[square]
	currSquare = square
	results[square] += 1
def nextR(square):
	pos = posMap[square]
	while True:
		pos = (pos + 1) % 40
		square = SQUARES[pos]
		if square[0] == 'R':
			goTo(square)
			return
def nextU(square):
	pos = posMap[square]
	while True:
		pos = (pos + 1) % 40
		square = SQUARES[pos]
		if square[0] == 'U':
			goTo(square)
			return
doublesStreak = 0
for i in range(10 ** 5):
	r = roll()
	n = r[0]
	if r[1]:
		doublesStreak += 1
		if doublesStreak == 3:
			doublesStreak = 0
			goTo('JAIL')
			continue
	else:
		doublesStreak = 0
	newPos = (currPos + n) % 40
	newSquare = SQUARES[newPos]
	if newSquare == 'G2J':
		goTo('JAIL')
		continue
	elif newSquare[ : 2] == 'CC':
		CC = getCC()
		if CC:
			goTo(CC)
		else:
			goTo(newSquare)
		continue
	elif newSquare[ : 2] == 'CH':
		CH = getCH()
		if CH:
			if CH == 'NR':
				nextR(newSquare)
				continue
			elif CH == 'NU':
				nextU(newSquare)
				continue
			elif CH == '-3':
				goTo(SQUARES[(newPos - 3) % 40])
			else:
				goTo(CH)
		else:
			goTo(newSquare)
	else:
		goTo(newSquare)
newResults = []
for key in results.keys():
	newResults.append([results[key], key])
newResults.sort()
newResults.reverse()
answer = ''
for i in range(3):
	s = str(posMap[newResults[i][1]])
	s += '0' * (2 - len(s))
	answer += s
print(answer)