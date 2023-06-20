import math



def f(num):
  factors = 1
  for i in range(1, math.floor(num / 2)):
    if num % i == 0:
      if i == 1:
        factors += 1
      else:
        factors += 2
  return factors

data = []
biggest = 0
for a in range(-999, 1000):
  for b in range(-1000, 1001):
    length = 0
    n = 0
    valid = True
    while valid:
      testNum = (n ** 2) + (a * n) + b
      if f(testNum) == 2:
        length += 1
        n += 1
      else:
        valid = False
    if length > biggest:
      biggest = length
    add = [a, b, length]
    data.append(add)
    if b % 10 == 0:
      print(a, b, length, biggest)



biggest = 0
answer = 0



for i in range(0, len(data)):
  if data[i][2] > biggest:
    biggest = data[i][2]
    answer = data[i][0] * data[i][1]
print(answer)
