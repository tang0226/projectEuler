import math
import sys

def intToBase(n, b):
  n_b = []
  p = b ** math.floor(math.log(n) / math.log(b))
  x = n
  while p >= 1:
    d = x // p
    n_b.append(int(d))
    x -= p * d
    p /= b
  return n_b

def baseToInt(n, b):
  r = 0
  p = 1
  for i in range(len(n) - 1, -1, -1):
    r += p * n[i]
    p *= b
  return r

def isPandigital(n, b):
  found = [0] * b
  unique = 0
  for d in n:
    if found[d] == 0:
      unique += 1
      if unique == b:
        return True
    found[d] += 1

def is_11_super_pandigital(n):
  for b in range(11, 1, -1):
    if not isPandigital(intToBase(n, b), b):
      return False
  return True

def is_10_super_pandigital(n):
  for b in range(10, 1, -1):
    if not isPandigital(intToBase(n, b), b):
      return False
  return True

def get_perms(n):
  perms = [[i] for i in range(n)]
  for i in range(n - 1):
    new_perms = []
    for p in perms:
      for d in range(n):
        if d not in p:
          new_perms.append(p + [d])
    perms = new_perms
  return perms


# pre-calculate for efficiency
perms = get_perms(10)

# test with 10-super-pandigitals
"""total = 0
count = 0
for p in perms:
  if p[0] > 0:
    n = baseToInt(p, 10)
    if is_10_super_pandigital(n):
      total += n
      count += 1
      print(count, n, total)
      if count == 10:
        print(total)
        sys.exit()"""

total = 0
count = 0

for d1 in range(1, 12):
  left1 = [i for i in range(12) if i != d1]
  for d2 in left1:
    left2 = [i for i in left1 if i != d2]
    for p in perms:
      digs = [d1, d2] + [left2[i] for i in p]
      n = baseToInt(digs, 12)
      if is_11_super_pandigital(n):
        total += n
        count += 1
        print(count, n, total)
        if count == 10:
          print(total)
          sys.exit()
    print(d1, d2)
"""for d1 in range(1, 12):
  left1 = [i for i in range(12) if i != d1]
  for d2 in left1:
    left2 = [i for i in left1 if i != d2]
    for d3 in left2:
      left3 = [i for i in left2 if i != d3]
      for d4 in left3:
        left4 = [i for i in left3 if i != d4]
        for d5 in left4:
          left5 = [i for i in left4 if i != d5]
          for d6 in left5:
            left6 = [i for i in left5 if i != d6]
            for d7 in left6:
              left7 = [i for i in left6 if i != d7]
              for d8 in left7:
                left8 = [i for i in left7 if i != d8]
                for d9 in left8:
                  left9 = [i for i in left8 if i != d9]
                  for d10 in left9:
                    left10 = [i for i in left9 if i != d10]
                    for d11 in left10:
                      digs = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, [i for i in left10 if i != d11][0]]
                      n = baseToInt(digs, 12)
                      if is_11_super_pandigital(n):
                        total += n
                        count += 1
                        print(count, n, total)
                        if count == 10:
                          print(total)
                          sys.exit()
      print(d1, d2, d3)"""