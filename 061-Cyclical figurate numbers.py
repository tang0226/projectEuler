figurates = []
for change in range(1, 7):
	n = 1
	new = []
	add = change + 1
	while len(str(n)) < 5:
		if len(str(n)) == 4:
			new.append(n)
		n += add
		add += change
	figurates.append(new)
for i in range(len(figurates)):
	for j in figurates[i]:
		s = str(j)
		if s[2] == "0":
			figurates[i].remove(j)
organize = []
for i in range(90):
	organize.append([[], [], [], [], [], []])
def prefix(n):
	return int(str(n)[ : 2])
def suffix(n):
	return int(str(n)[2 : ])
for i in range(len(figurates)):
	for j in figurates[i]:
		organize[prefix(j) - 10][i].append(j)

for i in range(len(figurates)):
	for start in figurates[i]:
		available = [0, 1, 2, 3, 4, 5]
		available.remove(i)
		suf = suffix(start)
		chain = [start]
		for index in available:
			if len(organize[suf - 10][index]) != 0:
				for a in organize[suf - 10][index]:
					if suf == prefix(a):
						available1 = list(x for x in available)
						available1.remove(index)
						suf1 = suffix(a)
						chain1 = list(x for x in chain)
						chain1.append(a)
						for index1 in available1:
							if len(organize[suf1 - 10][index1]) != 0:
								for b in organize[suf1 - 10][index1]:
									if suf1 == prefix(b):
										available2 = list(x for x in available1)
										available2.remove(index1)
										suf2 = suffix(b)
										chain2 = list(x for x in chain1)
										chain2.append(b)
										for index2 in available2:
											if len(organize[suf2 - 10][index2]) != 0:
												for c in organize[suf2 - 10][index2]:
													if suf2 == prefix(c):
														available3 = list(x for x in available2)
														available3.remove(index2)
														suf3 = suffix(c)
														chain3 = list(x for x in chain2)
														chain3.append(c)
														for index3 in available3:
															if len(organize[suf3 - 10][index3]) != 0:
																for d in organize[suf3 - 10][index3]:
																	if suf3 == prefix(d):
																		available4 = list(x for x in available3)
																		available4.remove(index3)
																		suf4 = suffix(d)
																		chain4 = list(x for x in chain3)
																		chain4.append(d)
																		for index4 in available4:
																			if len(organize[suf4 - 10][index4]) != 0:
																				for e in organize[suf4 - 10][index4]:
																					if suf4 == prefix(e):
																						available5 = list(x for x in available4)
																						available5.remove(index4)
																						suf5 = suffix(e)
																						chain5 = list(x for x in chain4)
																						if suffix(e) == prefix(start):
																							chain5.append(e)
																							print(chain5, sum(chain5))