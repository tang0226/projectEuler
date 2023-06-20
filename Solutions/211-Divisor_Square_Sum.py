from math import sqrt, floor, ceil
def isSquare(n):
    return round(sqrt(n))**2 == n
upper = 64000000
sigma2 = [0, 1] + list((i * i) + 1 for i in range(2, upper))
for d in range(2, ceil(sqrt(upper))):
    square = d * d
    for i in range(square, upper, d):
        sigma2[i] += square
        if i != square:
            sigma2[i] += round(i / d) ** 2
    print(d)
total = 0
print()
print()
for i in range(1, upper):
    if isSquare(sigma2[i]):
        total += i
        print(i)
    if i % 1000000 == 0:
        print(i)
print()
print(total)
print(sigma2[ : 11])