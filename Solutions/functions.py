
from math import *

def formatTime(s):
  m = s // 60
  seconds = s % 60
  sStr = ("0" if seconds < 10 else "") + str(seconds)
  if m >= 60:
    minutes = m % 60
    mStr = ("0" if minutes < 10 else "") + minutes
    return f"{m // 60}:{mStr}:{sStr}"
  return f"{int(m)}:{sStr}"

def isPrime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  x = 3
  while x * x <= n:
    if n % x == 0:
      return False
    x += 2
  return True

def isInt(n):
  return n - floor(n) == 0

def isSquare(n):
  return isInt(sqrt(n))

def lcm(n1, n2):
  if n1 > n2:
    n = n1
    while True:
      if n % n1 == n % n2 == 0:
        return n
      n += n1
  elif n2 > n1:
    n = n2
    while True:
      if n % n1 == n % n2 == 0:
        return n
      n += n2
  else:
    return n1

def concat(n1, n2):
  return int(str(n1) + str(n2))

def cleanBin(n, l):
  r = bin(n)[2 : ]
  return "0" * (l - len(r)) + r
  
def hcf(x, y):
   while(y):
     x, y = y, x % y
   return x

def binToDec(strBin):
  currTotal = 0
  currPow = len(strBin) - 1
  for i in range(0, len(strBin)):
    if strBin[i] == "1":
      currTotal += 2 ** currPow
    currPow -= 1
  return currTotal

def bubbleSort(values):
  l = len(values)
  valuesUse = values
  for end in range(l - 1, 0, -1):
    for start2 in range(0, end):
      if valuesUse[start] > valuesUse[start + 1]:
        store = valuesUse[start]
        valuesUse[start] = valuesUse[start + 1]
        valuesUse[start + 1] = store
  return valuesUse

def choose(n, k):
  return int(factorial(n) / (factorial(k) * factorial(n - k)))

def digitSum(n):
  s = str(n)
  r = 0
  for i in s:
    r += int(i)
  return r

def factorArray(n):
  if n == 1:
    return [1]
  factors = [1, n]
  for i in range(2, floor(sqrt(n)) + 1):
    if n % i == 0:
      factors.append(i)
      if n / i != i:
        factors.append(int(n / i))
  factors.sort()
  return factors

def reducedFrac(n, d):
  h = hcf(n, d)
  return [int(n / h), int(d / h)]

def permutation(digits, permNum):
  digits1 = []
  for i in digits:
    digits1.append(i)
  currFact = len(digits1) - 1
  perm = ""
  permNum1 = permNum - 1
  for i in range(0, len(digits1)):
    fact = factorial(currFact)
    perm += str(digits1.pop(floor(permNum1 / fact)))
    if permNum1 - fact * floor(permNum1 / fact) >= 0:
      permNum1 -= fact * floor(permNum1 / fact)
    currFact -= 1
  return perm

def primeFactorization(n):
  currNum = n
  factorization = []
  if isPrime(currNum):
    return [currNum]
  while not(isPrime(currNum)):
    if currNum % 2 == 0:
      currNum = round(currNum / 2)
      factorization.append(2)
      continue
    for i in range(3, ceil(n / 2) + 1, 2):
      if currNum % i == 0:
        currNum = round(currNum / i)
        factorization.append(i)
        break
  factorization.append(currNum)
  factorization.sort()
  return factorization

def primeFactorizations(n, primes):
  factorizations = list([] for i in range(n + 1))
  for i in primes:
    exp = i
    while exp <= n:
      for j in range(exp, n + 1, exp):
        factorizations[j].append(i)
      exp *= i
  return factorizations

def addArray(a1, a2):
  return list(a1[i] + a2[i] for i in range(len(a1)))

def nextPrime(n):
  r = n + (n % 2) - 1
  while True:
    r += 2
    if isPrime(r):
      return r

def sieve(n):
  conditions = ([0, 0] + ([0, 1] * (((n - 1) // 2) + 1)))[ : n + 1]
  primes = [2, 3]
  currPrime = 3
  while currPrime < floor(sqrt(n)) + 1:
    print(currPrime)
    conditions[currPrime] = 0
    for x in range(currPrime ** 2, n + 1, currPrime):
      conditions[x] = 0
    while not conditions[currPrime]:
      currPrime += 1
    primes.append(currPrime)
  #print(conditions)
  for i in range(primes[-1] + 1, len(conditions)):
    if conditions[i] == 1:
      primes.append(i)
  return primes

def firstPrimes(n):
  r = [2]
  x = 3
  while len(r) < n:
    if isPrime(x):
      r.append(x)
      print(x, len(r), n - len(r))
    x += 2
  return r

def primesBetween(x, y):
  r = []
  s = x
  if x % 2 == 0:
    s += 1
  for i in range(s, y + 1, 2):
    if isPrime(i):
      r.append(i)
      print(i, y - i)
  return r

def isPalindrome(n):
  s = str(n)
  if s == s[ :: -1]:
    return True
  return False


def factorSum(n):
  if n == 1:
    return 1
  factors = n + 1
  for i in range(2, floor(sqrt(n)) + 1):
    if n % i == 0:
      factors += i
      if n / i != i:
        factors += int(n / i)
  return factors


def factorCount(n):
  if n == 1:
    return 1
  factors = 2
  for i in range(2, floor(sqrt(n)) + 1):
    if n % i == 0:
      factors += 1
      if n / i != i:
        factors += 1
  return factors


def lcm(n1, n2):
  if n1 > n2:
    n = n1
    while True:
      if n % n1 == n % n2 == 0:
        return n
      n += n1
  elif n2 > n1:
    n = n2
    while True:
      if n % n1 == n % n2 == 0:
        return n
      n += n2
  else:
    return n1

def reducedFrac(n, d):
  h = hcf(n, d)
  return [int(n / h), int(d / h)]


def addFrac(n1, d1, n2, d2):
  l = lcm(d1, d2)
  rn = (n1 * (l / d1)) + (n2 * (l / d2))
  rd = l
  return reducedFrac(int(rn), rd)

def multiplyFrac(n1, d1, n2, d2):
  return reducedFrac(n1 * n2, d1 * d2)

def phi(n):
  r = 0
  for i in range(1, n):
    if hcf(n, i) == 1:
      r += 1
  return r

def totients(upper, primes):
  t = list(range(upper))
  for prime in primes:
    multiply = (prime - 1) / prime
    index = prime
    while index < upper:
      t[index] = int(t[index] * multiply)
      index += prime
    print(prime)
  return t

def divisibleByNumbersTo(n):
  r = 1
  for i in sieve(n):
    r *= i ** (floor(log(n, i)))
  return r

def decToBase(n, b):
  chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  power = int(log(n, b))
  currPower = b ** power
  result = ""
  current = n
  for p in range(power, -1, -1):
    add = int(current / currPower)
    result += chars[add]
    current -= add * currPower
    currPower /= b
  return result

def nChooseK(n, k):
  return int(factorial(n) / factorial(k) / factorial(n - k))

def digitalRoot(n):
  s = sum(int(i) for i in str(n))
  if len(str(s)) == 1:
    return s
  else:
    return digitalRoot(s)

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b % a, a)

def modExp(b, e, m):
  r = 1
  while e > 0:
    if e % 2 == 1:
      r = (r * b) % m
    b = (b * b) % m
    e //= 2
  return r

def avg(arr):
  return sum(arr) / len(arr)

def sumOfSquares(n):
  return int((n * (n + 1) * ((2 * n) + 1)) / 6)
  
def padBin(n, d):
  b = bin(n)[2 : ]
  return ("0" * (d - len(b))) + b

def changeChar(s, i, c):
  return s[ : i] + c + s[i + 1 : ]