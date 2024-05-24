total = 0
for a1 in range(5):
  for b1 in range(a1 + 1, 6):
    for c1 in range(b1 + 1, 7):
      for d1 in range(c1 + 1, 8):
        for e1 in range(d1 + 1, 9):
          for f1 in range(e1 + 1, 10):
            for a2 in range(5):
              for b2 in range(a2 + 1, 6):
                for c2 in range(b2 + 1, 7):
                  for d2 in range(c2 + 1, 8):
                    for e2 in range(d2 + 1, 9):
                      for f2 in range(e2 + 1, 10):
                        x = [a1, b1, c1, d1, e1, f1]
                        y = [a2, b2, c2, d2, e2, f2]
                        if (
                          ((0 in x and 1 in y) or (0 in y and 1 in x)) and
                          ((0 in x and 4 in y) or (0 in y and 4 in x)) and
                          ((0 in x and (9 in y or 6 in y)) or (0 in y and (9 in x or 6 in x))) and
                          ((1 in x and (6 in y or 9 in y)) or (1 in y and (6 in x or 9 in x))) and
                          ((2 in x and 5 in y) or (2 in y and 5 in x)) and
                          ((3 in x and (6 in y or 9 in y)) or (3 in y and (6 in x or 9 in x))) and
                          ((4 in x and (9 in y or 6 in y)) or (4 in y and (9 in x or 6 in x))) and
                          (((6 in x or 9 in x) and 4 in y) or ((6 in y or 9 in y) and 4 in x)) and
                          ((8 in x and 1 in y) or (8 in y and 1 in x))
                        ):
                          total += 1
                          
print(total, total / 2)
