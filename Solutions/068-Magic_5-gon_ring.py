def cycle(array, amount):
	use = list(i for i in array)
	for i in range(amount):
		use.append(use.pop(0))
	return use

import itertools
perms = itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
largest = 0
for i in perms:
	if i.index(10) % 2 == 1:
		continue
	if i[0] + i[1] + i[3] == i[2] + i[3] + i[5] == i[4] + i[5] + i[7] == i[6] + i[7] + i[9] == i[8] + i[9] + i[1]:
		arms = [[i[0], i[1], i[3]], [i[2], i[3], i[5]], [i[4], i[5], i[7]], [i[6], i[7], i[9]], [i[8], i[9], i[1]]]
		arms = cycle(arms, arms.index(min(arms)))
		s = ""
		for j in arms:
			s += str(j[0]) + str(j[1]) + str(j[2])
		if int(s) > largest:
			largest = int(s)
			print(largest)