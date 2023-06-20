from functions import primeFactorization
factorizations = list(primeFactorization(i) for i in range(2, 21))
max2 = 0
max3 = 0
max5 = 0
max7 = 0
max11 = 0
max13 = 0
max17 = 0
max19 = 0
for i in factorizations:
	c2 = i.count(2)
	c3 = i.count(3)
	c5 = i.count(5)
	c7 = i.count(7)
	c11 = i.count(11)
	c13 = i.count(13)
	c17 = i.count(17)
	c19 = i.count(19)
	if c2 > max2:
		max2 = c2
	if c3 > max3:
		max3 = c3
	if c5 > max5:
		max5 = c5
	if c7 > max7:
		max7 = c7
	if c11 > max11:
		max11 = c11
	if c13 > max13:
		max13 = c13
	if c17 > max17:
		max17 = c17
	if c19 > max19:
		max19 = c19
x = 2 ** max2
x *= 3 ** max3
x *= 5 ** max5
x *= 7 ** max7
x *= 11 ** max11
x *= 13 ** max13
x *= 17 ** max17
x *= 19 * max19
print(x)