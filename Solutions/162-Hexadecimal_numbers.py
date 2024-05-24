from math import comb
maxDigs = 16
total = 0
for digs in range(3, maxDigs + 1):
	for index0 in range(1, digs):
		for index1 in range(digs):
			if index1 == index0:
				continue
			for indexA in range(digs):
				if indexA == index0 or indexA == index1:
					continue
				combos = 1
				for dig in range(digs):
					if dig == index0 or dig == index1 or dig == indexA:
						continue
					multiply = (int(digs > 3) * 13) + int(dig > index0) + int(dig > index1) + int(dig > indexA)
					combos *= multiply
				total += combos
print(hex(total).upper()[2 : ])