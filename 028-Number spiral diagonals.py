import math


nums = []
side = 1001
for i in range(side):
  nums.append([])
  for j in range(side):
    nums[i].append(0)



x = math.floor(side / 2)
y = math.floor(side / 2)
currNum = 1
direction = 0
total = side * side



def move():
  global x
  global y
  global direction
  if direction == 0:
    x += 1
  elif direction == 1:
    y += 1
  elif direction == 2:
    x -= 1
  else:
    y -= 1



def changeDirection():
  global direction
  direction += 1
  if direction == 4:
    direction = 0



for i in range(side):
  for j in range(2):
    for k in range(i + 1):
      if currNum != side * side:
        nums[y][x] = currNum
        currNum += 1
        move()
    changeDirection()



for i in range(side):
  for j in range(side):
    if i == j or i + j == side - 1:
      total += nums[i][j]
print(total)