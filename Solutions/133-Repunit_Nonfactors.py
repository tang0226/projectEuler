def get_condition(p):
  repunit_mod_p = 11 % p
  repunit_mod_p_cycle = [1]
  while repunit_mod_p != 1:
    repunit_mod_p_cycle.append(repunit_mod_p)
    repunit_mod_p = (repunit_mod_p * 10 + 1) % p
  period = len(repunit_mod_p_cycle)

  k = 10 % period
  k_cycle = [1]
  while k not in k_cycle:
    k_cycle.append(k)
    #power_repunit_mod_p_cycle.append(repunit_mod_p_cycle[k])
    k = (k * 10) % period
  print(k_cycle)
  return k_cycle[-1] == 0


from Code.Solutions.functions import sieve
primes = sieve(100)
print()
total = 0
for p in primes[3:]:
  if not get_condition(p):
    total += p
    print(p, total)
#453647695 wrong
# missed 2, 3 and 5: 453647705