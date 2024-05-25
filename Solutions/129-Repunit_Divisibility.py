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

# Same principle;
#   as we continue taking n_i+1 = (n_i + 10 ^ e mod p) mod p,
#   (i.e. adding the next power of 10 and modding),
#   we will eventually get zero (a divisibility match!)
#   The indices (k where R(k) mod p = 0) will cycle as well, and once
#    we find the interval, we can determine if it ever falls on k = 10 ^ 9
#   If it does, that means that p is a factor of the target repunit

# I will start guessing at new values, since it seems that 
# the n's with high k values have k a bit less than n
n = 999999 # one less than 10 ** 6; it worked!!
"""
tried:
11
999999: got n = 1000023, k = 1000020 in a few seconds
"""
target_k = 10 ** 6
curr_target = 2
while True:
  if n % 2 == 0 or n % 5 == 0:
    n += 1
    continue
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
      break
      
    # loop through the modexp cycle
    cycle_index = (cycle_index + 1) % len(cycle)

  if k > curr_target:
    print(n, k)
    curr_target = k
  if k > target_k:
    break
  n += 1

print(n, k)