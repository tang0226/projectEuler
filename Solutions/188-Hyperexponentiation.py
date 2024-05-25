from functions import sieve

def get_mod_exp_cycle(b, m):
  last_occurence = [0 for i in range(m + 1)]
  cycle = []
  n = 1
  p = 0
  while last_occurence[n] < 1:
    cycle.append(n)
    last_occurence[n] += 1
    n = (n * b) % m
    p += 1
  return cycle

base = 1777
hyperexp = 1855
digs = 8

# primes = sieve(10 ** 6)
print("getting digit cycle...")
digit_cycle = get_mod_exp_cycle(base, 10 ** digs)
print("getting inter cycle...")
inter_cycle = get_mod_exp_cycle(base, len(digit_cycle))

print("calculating...")
curr_val = base
print(len(inter_cycle))
for i in range(hyperexp - 2):
  curr_val = inter_cycle[curr_val % len(inter_cycle)]
print(digit_cycle[curr_val])
