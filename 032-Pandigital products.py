import time
start = time.time()
products = []
total = 0
for i in range(1, 10001):
	for j in range(1, 10000):
		num = i * j
		text = str(i) + str(j) + str(num)
		if len(text) == 9:
			ints = [text[0], text[1], text[2], text[3], text[4], text[5], text[6], text[7], text[8]]
			valid = True
			for k in range(1, 10):
				if ints.count(str(k)) != 1:
					valid = False
			if valid:
				 if products.count(num) != 1:
					 products.append(num)
					 total += num
					 print(i, j, num, total)
print(total)
end = time.time() - start
print("time taken: " + str(end) + " sec")