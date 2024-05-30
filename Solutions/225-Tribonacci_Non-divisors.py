def divides_trib(n):
  tn_3 = 1
  tn_2 = 1
  tn_1 = 1
  while True:
    tn = (tn_3 + tn_2 + tn_1) % n
    if tn == 0:
      return True
    tn_3 = tn_2
    tn_2 = tn_1
    tn_1 = tn
    if tn_1 == tn_2 == tn_3 == 1:
      return False

n = 3
count = 0
target = 124
while True:
  if not divides_trib(n):
    count += 1
    print(count, n)
    if count == target:
      break
  n += 2
print(n)