"""
x^2 + xy + 41y^2 <= N
let f(x, y) = x^2 + xy + 41y^2
f(x, y) = f(-x, -y) since x^2 = (-x)^2 (same with y) and xy = (-x)(-y)
therefore, every solution will have double: (x, y) and (-x, -y)

Take double the number of solutions with only positive x

loop through y, and count solutions for x:
x^2 + xy + 41y^2 = N
x^2 + yx + (41y^2 - N) = 0
( -b +- sqrt(b^2 - 4ac) ) / 2a
( -y +- sqrt(y^2 - 4*(41y^2 - N) ) ) / 2

round answers, check nums in vicinity to get exact solutions
think of these as bounding x's on a parabola
since the x^2 coeff is +1, the parabola will be downward facing.
therefore our bounds contain all solutions to f(x, y) <= N
"""

from Code.Solutions.functions import formatTime
import time
startTime = time.perf_counter()

def f(x, y):
  return x ** 2 + x * y + 41 * y ** 2

N = 10 ** 16


y = 0
total = 0
while True:
  # remember to double all solutions
  discriminant = y ** 2 - 4 * (41 * y ** 2 - N)
  if discriminant < 0:
    break
  
  sqrtD = discriminant ** 0.5

  sol1 = (-y + sqrtD) / 2
  sol2 = (-y - sqrtD) / 2

  # make sure sol1 is less than sol2
  if sol1 > sol2:
    temp = sol1
    sol1 = sol2
    sol2 = temp
  
  sol1 = round(sol1) - 2
  while f(sol1, y) > N:
    sol1 += 1
  
  sol2 = round(sol2) + 2
  while f(sol2, y) > N:
    sol2 -= 1
  if y != 0:
    count = (sol2 - sol1 + 1) * 2
  else:
    # don't add 1 because (0,0) does not count
    count = sol2 - sol1
  
  total += count

  if y % 1000000 == 0:
    print(y, sol1, sol2, count, total)

  y += 1

print(total, ";", formatTime(time.perf_counter() - startTime))