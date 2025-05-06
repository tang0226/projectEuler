import math

def sqDist(p1, p2):
  return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

mod = 50515093
s = [290797]
k = 2000000

while len(s) < k * 2:
  s.append((s[-1] ** 2) % mod)

P = [(s[n], s[n + 1]) for n in range(0, k * 2, 2)]

chunksPerAxis = 2000
chunkSize = math.ceil(mod / chunksPerAxis)

chunks = [[[] for i in range(chunksPerAxis)] for j in range(chunksPerAxis)]

for p in P:
  chunks[p[0] // chunkSize][p[1] // chunkSize].append(p)


minD = 1e100

for cx in range(chunksPerAxis):
  for cy in range(chunksPerAxis):
    p = chunks[cx][cy]

    l = len(p)
    for i in range(l - 1):
      for j in range(i + 1, l):
        d = sqDist(p[i], p[j])
        if d < minD:
          minD = d

    # compare with next / surrounding chunks if not last in row or col
    if cx < chunksPerAxis - 1 and cy < chunksPerAxis - 1:
      compare = chunks[cx + 1][cy] + chunks[cx][cy + 1] + chunks[cx + 1][cy + 1]
      for p1 in p:
        for p2 in compare:
          d = sqDist(p1, p2)
          if d < minD:
            minD = d
  print(cx)

print("Min distance:", minD)