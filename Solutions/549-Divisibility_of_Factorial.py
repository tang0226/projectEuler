from Code.Solutions.functions import sieve
upper = 10 ** 8
primes = sieve(upper)
print(len(primes))

prime_factorizations = [[] for i in range(upper + 1)]
for i in range(len(primes)):
  p = primes[i]
  power = p
  while power < upper:
    for n in range(power, upper + 1, power):
      prime_factorizations[n].append(i)
    power *= p

factor_req_met = [[1] for i in range(len(primes))]
for n in range(1, len(prime_factorizations)):
  for p_i in prime_factorizations[n]:
    factor_req_met[p_i].append(n)


total = 0

for n in range(2, upper + 1):
  f = prime_factorizations[n]

  j = 1
  curr_p_i = f[0]
  curr_power = 1
  options = []
  while j < len(f):
    if f[j] != curr_p_i:
      options.append(factor_req_met[curr_p_i][curr_power])
      curr_p_i = f[j]
      curr_power = 1
    else:
      curr_power += 1
    j += 1
  options.append(factor_req_met[curr_p_i][curr_power])
  s = max(options)
  total += s
  if n % 100000 == 0: print(n, s, total)
print(total)

# first try: 5494373412573 (wrong)
# second try: 476001479068717 (correct)