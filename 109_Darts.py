total = 0
scores = [25, 50]
for i in range(1, 21):
    scores += [i, i * 2, i * 3]
doubles = list(i * 2 for i in range(1, 21)) + [50]
maxScore = 99
for double in doubles:
    if double <= maxScore:
        total += 1
    for s1 in range(len(scores)):
        if double + scores[s1] <= maxScore:
            total += 1
        for s2 in range(s1, len(scores)):
            if double + scores[s1] + scores[s2] <= maxScore:
                total += 1
print(total)