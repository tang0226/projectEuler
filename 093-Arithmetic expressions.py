from functions import *
import math
def operation(n1, n2, op):
	if op == "+":
		return n1 + n2
	elif op == "-":
		return n1 - n2
	elif op == "*":
		return n1 * n2
	else:
		if n2 == 0:
			return False
		x = n1 / n2
		return x
def output(digits, ops, order):
	if order[ : 2] == "02" or order[ : 2] == "20":
		o1 = operation(int(digits[0]), int(digits[1]), ops[0])
		o2 = operation(int(digits[2]), int(digits[3]), ops[2])
		x = operation(o1, o2, ops[1])
		if isInt(x):
			return int(x)
		return False
	else:
		n1 = int(digits[0])
		n2 = int(digits[1])
		n3 = int(digits[2])
		n4 = int(digits[3])
		r = 0
		if order[0] == "0":
			r = operation(n1, n2, ops[0])
			r = operation(r, n3, ops[1])
			r = operation(r, n4, ops[2])
		elif order[0] == "1":
			r = operation(n2, n3, ops[1])
			if order[1] == "0":
				r = operation(n1, r, ops[0])
				r = operation(r, n4, ops[2])
			else:
				r = operation(r, n4, ops[2])
				r = operation(n1, r, ops[0])
		else:
			r = operation(n3, n4, ops[2])
			r = operation(n2, r, ops[1])
			r = operation(n1, r, ops[0])
		if isInt(r):
			return int(r)
		return False
			

digits = "123456789"
ops = "+-*/"
import itertools
perms = ["".join(p) for p in itertools.permutations("012")]
longest = 0
longestDigits = ""
for a in range(len(digits) - 3):
	for b in range(a + 1, len(digits) - 2):
		for c in range(b + 1, len(digits) - 1):
			for d in range(c + 1, len(digits)):
				results = []
				for perm in ["".join(p) for p in itertools.permutations(digits[a] + digits[b] + digits[c] + digits[d])]:
					for x in ops:
						for y in ops:
							for z in ops:
								for order in perms:
									o = output(perm, x + y + z, order)
									if o and o > 0:
										results.append(o)
				results = list(dict.fromkeys(results))
				results.sort()
				if results[0] != 1:
					continue
				length = 0
				for i in range(len(results) - 1):
					if results[i + 1] - results[i] == 1:
						length += 1
					else:
						length += 1
						break
				if length > longest:
					longest = length
					longestDigits = digits[a] + digits[b] + digits[c] + digits[d]
				print(a + 1, b + 1, c + 1, d + 1, length, longest, longestDigits)