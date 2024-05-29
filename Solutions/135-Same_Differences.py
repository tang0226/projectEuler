import math

def quadratic(a, b, c):
  num = -b
  denom = 2 * a
  pm = (b * b - 4 * a * c) ** 0.5
  return ((num + pm) / denom, (num - pm) / denom)

def high_quadratic(a, b, c):
  return (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a)

def d_lower_bound(x):
  return high_quadratic(3, 2 * x, -(x ** 2))

def d_upper_bound(x, L):
  return high_quadratic(3, 2 * x, - (x ** 2 + L))

def diff(x, d):
  return -(x ** 2) + 2 * x * d + 3 * d ** 2

upper = 10 ** 6 - 1
solutions = [0] * (upper + 1)
x = 1
while True:
  d_lower = math.floor(d_lower_bound(x))
  d_upper = math.floor(d_upper_bound(x, upper))
  if d_lower > d_upper:
    break
  for d in range(d_lower, d_upper + 1):
    n = diff(x, d)
    if n < 0: continue
    solutions[n] += 1
  if x % 100000 == 0: print(x, d_lower, d_upper, solutions.count(10))
  x += 1

print(solutions.count(10))