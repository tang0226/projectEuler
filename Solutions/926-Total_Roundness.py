from functions import sieve

"""
try w/ 20:
2^2 x 5
(2+1) * (1+1) = 6



2
3
2x2
5
2x3
7
2x2x2
3x3
2x5

BUT EXCLUDE THE 1 COMBINATION!!! (p1^0 x p2^0 x p3^0 etc.)
being divisible by 1, 1^2, 1^3, etc. should not be counted

exp 1
= 2^8 x 3^4 x 5^2 x 7
(8+1) * (4+1) * (2+1) * (1+1) = 270

exp 2
2^4 x 3^2 x 5
(4+1) x (2+1) x (1+1) = 30

exp 3
2^2 x 3
(2+1) x (1+1) = 6

exp 4
2^2 x 3
(2+1) x (1+1) = 6

n's roundness in base b is the same as the max e for which b^e divides n

count how many number are divisible by any b (1st power)

add how many numbers are divisible by b^2 (2nd power).
Add one because the "first zero" has already been counted, i.e. each number
divisible by b^2 is divisible by b^1 and has already been counted once

. . .

"""

fac = 10000000
mod = 10 ** 9 + 7

primes = sieve(fac)
l = len(primes)
numFactors = [0] * len(primes)
for i in range(l):
  p = primes[i]
  exp = p
  while exp <= fac:
    numFactors[i] += fac // exp
    exp *= p

power = 1
total = 0
while True:
  prod = 1
  for i in range(l):
    x = numFactors[i] // power
    if x == 0:
      break
    prod *= x + 1
    prod %= mod
  if prod == 1:
    break
  total += prod - 1
  if power % 10000 == 0:
    print(power)
  power += 1


print(total % mod)
