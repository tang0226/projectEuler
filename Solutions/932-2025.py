"""
square of an n-digit number will always have 2n or 2n-1 digits
"""

n = 16
upper = 10 ** (n // 2)

pow10 = [10 ** i for i in range((n // 2) + 2)]

def checkPartition(ab, split):
  b = ab % pow10[split]
  if b < pow10[split - 1]:
    return False
  a = ab // pow10[split]
  return ab == (a + b) ** 2

aPlusB = 4
ab = 16
currDigs = 2
p1 = currDigs // 2
p2 = 0
nextDigThreshold = 100
total = 0
while currDigs <= n:
  if checkPartition(ab, p1):
    total += ab
    print(ab, total)
  if p2:
    if checkPartition(ab, p2):
      total += ab
      print(ab, total)
  aPlusB += 1
  ab = aPlusB ** 2
  if (ab > nextDigThreshold):
    currDigs += 1
    p1 = currDigs // 2
    if (currDigs % 2 == 1):
      p2 = p1 + 1
    else:
      p2 = 0
    nextDigThreshold *= 10
