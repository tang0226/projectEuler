from math import factorial, comb
def listPerms(l):
    r = factorial(len(l))
    for i in list(dict.fromkeys(l)):
        r /= factorial(l.count(i))
    return int(r)
total = 0
for d1 in range(12, 0, -1):
    for d2 in range(d1, 0, -1):
        t2 = d1 + d2
        for d3 in range(d2, 0, -1):
            print(d1, d2, d3)
            t3 = t2 + d3
            for d4 in range(d3, 0, -1):
                t4 = t3 + d4
                for d5 in range(d4, 0, -1):
                    t5 = t4 + d5
                    for d6 in range(d5, 0, -1):
                        t6 = t5 + d6
                        if t6 > 66:
                            continue
                        if t6 < 22:
                            break
                        for d7 in range(d6, 0, -1):
                            t7 = t6 + d7
                            if t7 > 67:
                                continue
                            if t7 < 34:
                                break
                            for d8 in range(d7, 0, -1):
                                t8 = t7 + d8
                                if t8 > 68:
                                    continue
                                if t8 < 46:
                                    break
                                for d9 in range(d8, 0, -1):
                                    t9 = t8 + d9
                                    if t9 > 69:
                                        continue
                                    if t9 < 58:
                                        break
                                    for d10 in range(d9, 0, -1):
                                        t10 = t9 + d10
                                        if t10 > 70:
                                            continue
                                        if t10 < 70:
                                            break
                                        topDice = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]
                                        if d10 == 1:
                                            total += listPerms(topDice + ([1] * 10))
                                        else:
                                            for match in range(11):
                                                notMatch = 10 - match
                                                total += listPerms(topDice + ([d10] * match) + ([0] * notMatch)) * ((d10 - 1) ** notMatch)

print(total)