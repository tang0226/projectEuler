from math import factorial
from Solutions.functions import nCr
total = 0
days = 30
for streak2 in range(days // 2):
	for streak1 in range(days):
		aTotal = (streak2 * 2) + streak1
		streaks = streak2 + streak1
		if aTotal + streaks - 1 > days:
			continue
		other = days - aTotal
		total +=  nCr(other + 1, streaks) * nCr(streaks, streak1) * (other + 1)
print(total)