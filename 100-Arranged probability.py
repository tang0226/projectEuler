import math
from decimal import Decimal
upper = 10 ** 12
b = 85
r = 35
increment = 5
while True:
	t = b + r
	p = (Decimal(b) / Decimal(t)) * (Decimal(b - 1) / Decimal(t - 1))
	if p < 0.5:
		b += increment
	elif p > 0.5:
		r += increment
	else:
		print(b, r)
		increment = int(b / increment)
		r -= r % increment
		if t > upper:
			print(b)
			break