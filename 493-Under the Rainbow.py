from functions import hcf
prob = 1
for n in range(60, 40, -1):
	prob *= (n / (n + 10))
prob = 1 - prob
print(prob)
print(round(7 * prob, 9))