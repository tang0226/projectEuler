N = 2022

# Build Pascal's Triangle for binomial coefficients
comb = [[1], [1, 1]]
while len(comb) < N:
	new = []
	for i in range(len(comb) + 1):
		if i == 0 or i == len(comb):
			new.append(1)
		else:
			new.append(comb[-1][i - 1] + comb[-1][i])
	comb.append(new)
print(comb[8])
total = 0
for digits in range(1, N + 1):
	for dominant in range((digits // 2) + 1, digits + 1):
		nonDominant = digits - dominant
		
		# starts with the dominant digit
		total += 9 * comb[digits - 1][dominant - 1] * (9 ** nonDominant)
		total %= 1000000007
		
		if nonDominant:
			# starts with a non-dominant digit
			total += 9 * comb[digits - 1][nonDominant - 1] * (9 ** nonDominant)
			total %= 1000000007
		
print(total)
