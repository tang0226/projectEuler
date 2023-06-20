import time
start = time.time()
num = str(2 ** 1000)
total = 0
for x in range(0, len(num)):
  total += int(num[x])
print(total)
end = time.time() - start
print("time: " + str(end))