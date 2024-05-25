# Similar to 132 - Large Repunit Factors

# Get cycle of b^e mod m for all exponents
#   i.e. when constantly iterating n_i+1 = (n_i * b) mod m
#   cycles are guaranteed to appear
def get_mod_exp_cycle(b, m):
  #print("initializing search array...")
  last_occurence = [[0] for i in range(m + 1)]
  #print("init done")
  cycle = [b % m]
  n = (b % m)
  last_occurence[n][0] += 1
  #last_occurence[n][1] = 1
  n = (n * b) % m
  p = 2
  cycle.append(n)
  
  # keep iterating until we reach a mod value we've seen before
  while last_occurence[n][0] < 1:
    last_occurence[n][0] += 1
    #last_occurence[n][1] = p
    n = (n * b) % m
    cycle.append(n)
    p += 1
  return cycle

# Loop through cycle mod n to find first divisible repunit
def A(n):
  cycle = get_mod_exp_cycle(10, n)[ : -1]

  repunit_mod_n = 1
  k = 1
  cycle_index = 0
  while True:
    # Add the next power of 10 using the modexp cycle
    repunit_mod_n = (repunit_mod_n + cycle[cycle_index]) % n
    k += 1

    # i.e. if repunit is divisible by p
    if repunit_mod_n == 0:
      return k
      
    # loop through the modexp cycle
    cycle_index = (cycle_index + 1) % len(cycle)

from functions import sieve
primes = sieve(10 ** 5)

print()

curr_prime_i = 4
n = 10

total = 0
count = 0

while True:
  if n % 2 == 0 or n % 5 == 0:
    n += 1
    continue

  if n == primes[curr_prime_i]:
    n += 1
    curr_prime_i += 1
    continue

  if (n - 1) % A(n) == 0:
    print(n)
    total += n
    count += 1
    if count == 25:
      break

  n += 1

print()
print(total)
