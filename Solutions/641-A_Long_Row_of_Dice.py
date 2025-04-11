"""
All dice start at 1
turn every 2nd die, then every 3rd die, increasing the value by one or resetting to 1 each time
how many dice end at 1?

The number of times a die is turned must be a multiple of 6 for it to end as a 1

This is a question of number of divisors, i.e. if a die's position is divisible by
a number, it will be turned at that step.

Also, we start with turning every 2nd die, so 1 is not counted as a divisor

in summary, we must count the number of dice for which the position number
has 6n+1 factors

die 1 also always ends at 1

7, 13, 19, 25, 31, 37, 43, 49, 55, 61

Given a number's prime factorization p1^a * p2^b * p3^c * . . . .
the number of divisors is (a + 1) * (b + 1) * (c + 1) * . . . .

So, to find numbers for which the number of divisors is of the form d = 6n+1,
use d's factorization to find every combination of numbers whose product is d

each combination represents A * B * C . . . where A = a + 1.
What we're doing here is finding the possible component powers of the prime
factorization of a number with d divisors.

For each combination, subtract 1 from each number, and the result is a set of
powers in prime factorizations p1^a * p2^b . . .
since a = A - 1, the number of factors for this number, no matter which primes we
pick, will be A * B * C * . . ., which equals d

Theoretical requirements:
the sum of the p.f.'s of d must be less than log_2(upper), since
minimum possible factorizations would involve powers of at least 2
For the problem's limit of 10^36, this is approx. 119.589

This is also the ceiling for any individual power in a candidate's p.f.


Values of d will never be divisible by 2 or 3, so the minimum possible
prime factor of d is 5
This is perfect, because that means that all primes involved in the factorizations
of die IDs will have at least an exponent of 4, so they must be lower than the 
4th root of upper.

(in the max case, this will be 10 ** 9, which we can realistically sieve. The upper was very carefully chosen for this problem!)

How to find all possible combos of factors whose product is d?

Start with basic case, where every factor in d's p.f.
corresponds to an A = a + 1 where a is a prime exponent.
For this case, unique terms in d's p.f. can be treated independently, but
repeated terms in d's p.f. (i.e. exponents > 1) must be ordered,
e.g. d = 25, pf=[5, 5], can't include 2^4 * 3^4 AND 3^4 * 2^4
but, d = 55, pf=[5, 11], you can use any combo of prime bases, since the powers are different

On the other hand, we can also combine terms in d's p.f. by multiplying them together,
e.g. d=325, pf=[5, 5, 13]. We can count p.f.'s with exponents 4, 4, 12, but
we can also count p.f.'s with, for example, exponents 24 (5*5-1) and 12
All that matters is that the product ABC... = d is preserved, we are simply
redefining A, B, C, etc. so that they produce the same d.

Good news: the min. power in a d's p.f. is 5. To see how many of pf_d's terms we can combine:
taking the series of minimums:
5*5 = 25, 25 - 1 = 24
5*5*5 = 125, 125 - 1 = 124 > 119.589
This means that combining three terms of any d's p.f. is impossible, since
the prime power that results will always exceed our upper bound.

Therefore, we only need to worry about combining pairs of terms in d's p.f.. Woohoo!

Rules for combining pairs:
pairwise = 00, 01, 02, . . . 10, 11, 12
inner loop:
 - skip if the prime is the same as the prev. one


High-level algorithm:
Find pfactors of possible d
Get all unique exponent combinations by merging pairs of d's pfactors
for each combo [e1, e2, e3, . . .] find count of factorizations with unique primes:
p1^e1 * p2^e2 * p3^e3 . . . = n < upper


every large exponent calculation you can save / prune is worth a lot

"""

from functions import sieve
import math

def prod(arr):
  res = 1
  for i in arr:
    res *= i
  return res

def primeFactorizations(n, primes):
  factorizations = list([] for i in range(n + 1))
  # Different from functions utility because it reverses the order of the factors
  for i in primes[::-1]:
      exp = i
      while exp <= n:
        for j in range(exp, n + 1, exp):
          factorizations[j].append(i)
        exp *= i
  return factorizations


upper = 10 ** 36
maxPower = math.log(upper) // math.log(2) # ~119.589 for 10**36 upper

# just set to high value for now
factorCountUpper = 1_00_000_000

print("sieving for potential prime factors of d...")
fcp = sieve(factorCountUpper)
print("getting d prime factorizations...")
fac = primeFactorizations(factorCountUpper, fcp)

targetFactorizations = []
for n in range(7, factorCountUpper, 6):
  targetFactorizations.append(fac[n])

del fcp
del fac

primeFactorUpper = math.ceil(upper ** (1 / 4)) + 1

print("sieving for candidate prime factors...")
primes = sieve(primeFactorUpper)

print("building primesUnder cache...")
primesUnder = [0, 0]
_lastPrime = 2
_currVal = 1
for pi in range(1, len(primes)):
  primesUnder += [_currVal] * (primes[pi] - _lastPrime)
  _currVal += 1
  _lastPrime = primes[pi]
primesUnder += [_currVal] * (primeFactorUpper - _lastPrime + 1)


print("building primePowers cache...")
primePowers = []
for p in primes:
  arr = [1, p]
  x = p * p
  while x <= upper:
    arr.append(x)
    x *= p

  primePowers.append(arr)

maxPrimePower = [len(i) - 1 for i in primePowers]

def getPrimePower(i, exp):
  if exp > maxPrimePower[i]:
    return primePowers[i][-1] * primes[i] ** (exp - maxPrimePower[i])
  return primePowers[i][exp]

# takes desc. sorted array and returns desc sorted
def combineAndSort(arr, i, j):
  res = []
  last = 1e100
  toAdd = arr[i] * arr[j]
  added = False
  k = 0

  while k < len(arr):

    el = arr[k]

    if toAdd <= last and toAdd >= el and not added:
      res.append(toAdd)
      added = True
      last = toAdd
      continue

    if k == i or k == j:
      last = el
      k += 1
      continue


    res.append(el)
    last = el
    k += 1
  if not added:
    res.append(toAdd)
  return res

def getAllFactorCombos(pf):
  powerCombos = [pf]
  currList = [pf]
  while currList:
    newList = []
    for combo in currList:
      lastStart = None

      l = len(combo)
      if l == 1:
        continue
     
      for i in range(l - 1):
        
        if combo[i] == lastStart:
          continue
        
        lastCompare = None
        
        for j in range(i + 1, l):
          if combo[j] == lastCompare:
            continue

          toAdd = combineAndSort(combo, i, j)
          if sum(toAdd) <= maxPower:
            repeated = False
            for check in newList:
              if toAdd == check:
                repeated = True
                break
            if not repeated:
              newList.append(toAdd)

          lastCompare = combo[j]
        lastStart = combo[i]
    if len(newList):
      powerCombos += newList
    currList = newList
  return powerCombos

# get count of numbers under upper that have a prime factorization with the exponents exps
def getCount(exps):

  l = len(exps)

  lastExp = exps[-1]
  lastExpPow2 = 2 ** lastExp

  if l == 1:
    # return primes below pf[0]th root of upper
    primeThreshold = math.ceil(upper ** (1 / lastExp)) + 1
    _pi = primesUnder[primeThreshold]
    while primes[_pi] ** lastExp > upper:
      _pi -= 1
    #print("length 1:", primes[_pi], _pi + 1, primes[_pi] ** lastExp)
    return _pi + 1

  # not needed any more
  lastFactorDependent = exps[-1] == exps[-2]


  # array that will store the current indices of primes being raised to the exponents of pf
  indices = list(range(l - 1))

  # init array of current prime powers
  currPrimePowers = []
  for i in range(l - 1):
    exp = exps[i]
    primeI = indices[i]
    if exp > maxPrimePower[primeI]:
      return 0
    currPrimePowers.append(getPrimePower(primeI, exp))

  # progressive product of the prime powers, i.e. [ pow[0], pow[0] * pow[1], . . . etc. ]
  # this array will be kept consistent with currPrimePowers
  progProd = [currPrimePowers[0]]
  for i in range(1, l - 1):
    progProd.append(progProd[i - 1] * currPrimePowers[i])

  # Last incremented index
  incrIndex = 0

  toIncr = 0

  # running total
  count = 0

  while True:
    #print(indices, incrIndex, currPrimePowers, progProd)

    # check if the new exponents are too large
    if progProd[-1] * lastExpPow2 > upper:
      # if we just incremented the first index, the rest is at minimum, so we are always going to be over threshold
      if incrIndex == 0:
        return count
      toIncr = incrIndex - 1

    else:
      primeThreshold = math.ceil((upper / progProd[-1]) ** (1 / lastExp))
      _pi = primesUnder[primeThreshold]
      while getPrimePower(_pi, lastExp) * progProd[-1] > upper:
        _pi -= 1
      # subtract one for each previous factor with the same exponent (i.e. for sets of the same exponent, primes must be ordered)
      toAdd = _pi + 1
      if lastFactorDependent:
        toAdd -= indices[-1] + 1
        for _i in range(l - 1):
          if indices[_i] > indices[-1] and indices[_i] <= _pi:
            toAdd -= 1
      else:
        for _i in range(l - 1):
          if indices[_i] <= _pi:
            toAdd -= 1
      toAdd = max(toAdd, 0)
      count += toAdd
      #print(exps, indices, currPrimePowers, progProd, (upper / progProd[-1]) ** (1 / lastExp), _pi + 1, toAdd)

      toIncr = l - 2


    # Macro-step: get next valid combo of indices ()
    # increment the index and update power arrays
    while True:
      indices[toIncr] += 1
      repeated = False
      for i in range(toIncr):
        if i != toIncr:
          if indices[i] == indices[toIncr]:
            repeated = True
            break
      if not repeated:
        break

    # once the target index has been incremented, set all lower-level indices to min possible values
    for i in range(toIncr + 1, l - 1):
      # if this index is the same exponent as prev. one, set it to the next available value
      if exps[i] == exps[i - 1]:
        indices[i] = indices[i - 1] + 1
      else:
        # default to 0
        indices[i] = 0
      
      # increment this index until it does not match any previous indices
      while True:
        repeated = False
        for j in range(i):
          if indices[i] == indices[j]:
            repeated = True
            break
        if not repeated:
          break
        indices[i] += 1
      
      # update the corresponding prime power value
      currPrimePowers[i] = getPrimePower(indices[i], exps[i])

    incrIndex = toIncr
    
    pi = indices[incrIndex]
    currPrimePowers[incrIndex] = getPrimePower(pi, exps[incrIndex])

    if incrIndex == 0:
      progProd[0] = currPrimePowers[0]

    for i in range(max(incrIndex, 1), l - 1):
      progProd[i] = progProd[i - 1] * currPrimePowers[i]
    
    #print(indices, currPrimePowers, progProd)

#def countPrimeCombos(expCombos)
total = 1
print("beginning main loop: here we go!")
d = 7
for factorization in targetFactorizations:
  if sum(factorization) - len(factorization) <= maxPower:
    # get all possible combinations of powers
    combos = [[j - 1 for j in i] for i in getAllFactorCombos(factorization)]
    count = sum(getCount(i) for i in combos)
    if count:
      total += count
      print("d:", d, ";", "count:", count, ";", "total:", total)
  d += 6

    # then for each combination, count possible prime combinations within limit
#print(total)

#last thing I checked: update currPrimePower along with index when resetting
# this checked out (f(100) = 2, f(10^8) = 69), so this is promising

"""
.
.
.
d: 3705625 ; count: 1 ; total: 793525364
d: 3859375 ; count: 1 ; total: 793525365
d: 5078125 ; count: 1 ; total: 793525366
First try: 793525366 (correct!)
"""
