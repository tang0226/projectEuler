"""
+-*/()
"""
from Solutions.functions import padBin
from time import time
start = time()
    
def toFloat(f):
    return f[0] / f[1]

def add(f1, f2):
    return (f1[0] * f2[1] + f2[0] * f1[1], f1[1] * f2[1])

def sub(f1, f2):
    return (f1[0] * f2[1] - f2[0] * f1[1], f1[1] * f2[1])

def mul(f1, f2):
    return (f1[0] * f2[0], f1[1] * f2[1])

def div(f1, f2):
    return (f1[0] * f2[1], f1[1] * f2[0])

def toFloat(f):
    return f[0] / f[1]

operations = [lambda x, y: add(x, y), lambda x, y: sub(x, y), lambda x, y: mul(x, y), lambda x, y: div(x, y)]

def getResults(terms):
    results = []
    for i in range(1, len(terms)):
        for o in range(4):
            if (terms[i][0] == 0 or terms[i][1] == 0) and o == 3:
                continue
            newTerms = terms[ : i - 1] + [operations[o](terms[i - 1], terms[i])] + terms[i + 1 : ]
            if len(newTerms) == 1:
                results += newTerms
            else:
                results += getResults(newTerms)
    return list(dict.fromkeys(results))

digs = 9
gaps = digs - 1
bin = list(padBin(i, gaps) for i in range(2 ** gaps))
bin.reverse()
nums = []
for b in bin:
    terms = []
    currTerm = "1"
    for i in range(gaps):
        if b[i] == "0":
            terms.append((int(currTerm), 1))
            currTerm = ""
        currTerm += str(i + 2)
    terms.append((int(currTerm), 1))
    if len(terms) == 1:
        nums.append(int(toFloat(terms[0])))
        continue
    r = getResults(terms)
    for f in r:
        val = toFloat(f)
        if f[0] % f[1] == 0 and val > 0:
            nums.append(int(val))
    print(b, terms, len(nums))
nums = list(dict.fromkeys(nums))
nums.sort()
print(sum(nums), time() - start, "s")
"""
2: 17
3: 255
4: 4179
5: 74689
6: 1486063
"""