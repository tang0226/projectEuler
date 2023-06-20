t1 = float(input("First term: "))
d = float(input("Common difference: "))
n = int(input("Number of terms: "))
x = t1
for i in range(n):
	print("Term {}: {}".format(i + 1, x))
	x += d