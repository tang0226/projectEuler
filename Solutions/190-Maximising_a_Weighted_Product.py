from random import *

def evaluate(S):
  r = 1
  for i in range(len(S)):
    r *= S[i] ** (i + 1)
  return r


m = 15
mutations = 10
mutation_range = 0.00001

"""
2: 1.1851851851851896
3: 1.687499999922625
4: 2.899102922503863
5: 6.021364514993904
6: 15.135344116386584
7: 46.071013527056486
8: 169.89356236197358
9: 759.2063056366278
10: 4112.084964841912
11: 26998.957904864492
12: 214912.98822780215
13: 2074179.9583123412
14: 24273249.401645336
15: 344453832.4841585
"""

S = [1] * m
last_sum = 0
while True:
  max_sum_list = []
  max_sum = 0
  for i in range(mutations):
    new_list = S.copy()
    for j in range(m):
      mutate = random() * (mutation_range * 2) - mutation_range
      k = randint(0, m - 1)
      new_list[j] += mutate
      new_list[k] -= mutate
      e = evaluate(new_list)
      if e > max_sum:
        max_sum = e
        max_sum_list = new_list
  if max_sum > last_sum:
    S = max_sum_list
    last_sum = max_sum
    print(max_sum)