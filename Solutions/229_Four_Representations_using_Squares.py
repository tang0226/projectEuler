"""
500000000 3032922
550000000 3320168
600000000 3606591
650000000 3890941
700000000 4174506
750000000 4457082
800000000 4738915
850000000 5019798
900000000 5299686
950000000 5579031
1000000000 5857994
1050000000 6136019
1100000000 6413223
1150000000 6690283
1200000000 6966819
1250000000 7242368
1300000000 7517245
1350000000 7792159
1400000000 8066082
1450000000 8339679
1500000000 8613052
1550000000 8886106
1600000000 9158476
1650000000 9430727
1700000000 9702827
1750000000 9974012
1800000000 10245299
1850000000 10515958
1900000000 10785886
1950000000 11055541
2000000000 11325263
"""
from math import floor, ceil
coeffs = [1, 2, 3, 7]
numCoeffs = len(coeffs)
upper = 2 * 10 ** 9
interval = 5 * 10 ** 7
count = 8613052
beginAt = 1500000000 + 1
for start in range(beginAt, upper, interval):
    end = start + interval - 1
    conditions = list(([0] * numCoeffs) for i in range(interval))
    for i in range(numCoeffs):
        c = coeffs[i]
        for b in range(1, floor(((end - 1) / c) ** 0.5) + 1):
            cbSquared = c * b * b
            aMin = 0
            if cbSquared >= start:
                aMin = 1
            else:
                aMin = ceil((start - cbSquared) ** 0.5)
            for a in range(aMin, floor((end - cbSquared) ** 0.5) + 1):
                n = a * a + cbSquared
                conditions[(n - 1) % interval][i] = 1
        print(end, c, count)
    target = [1] * numCoeffs
    for i in conditions:
        if i == target:
            count += 1
    print(end, count)