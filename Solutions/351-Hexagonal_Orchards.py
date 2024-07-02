n = 10 ** 8

blocked_count = [0] * (n + 1)
for l in range(1, n):
  unblocked = l - blocked_count[l]
  for i in range(l * 2, n + 1, l):
    blocked_count[i] += unblocked
  if l % 10000 == 0:
    print(l)
s = sum(blocked_count)
print(s, s * 6)