from functions import isPrime, nChooseK

digits = 10

bins = []
for i in range(1, 2 ** digits - 1):
    b = bin(i)[2 : ]
    b = ('0' * (digits - len(b))) + b
    bins.append(b)
combos = list([] for i in range(digits - 1))
for i in bins:
    combos[i.count('0') - 1].append(i)

def getPrimes(combo, digit):
    countDigit = combo.count('1')
    countOther = combo.count('0')
    primes = []
    for i in range(10 ** countOther):
        s = str(i)
        s = ('0' * (countOther - len(s))) + s
        if s.count(str(digit)) > 0:
            continue
        index = 0
        n = ''
        for j in range(len(combo)):
            if combo[j] == '1':
                n += str(digit)
            else:
                n += s[index]
                index += 1
        if n[0] == '0':
            continue
        if isPrime(int(n)):
            primes.append(int(n))
    return primes

total = 0
for d in range(10):
    for i in range(digits - 1):
        primes = []
        for combo in combos[i]:
            primes += getPrimes(combo, d)
        if primes != []:
            total += sum(primes)
            break
print(total)
