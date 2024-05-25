from functions import sieve

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
#   If it does, we've found a prime factor of the target repunit

def get_repunit_pattern(p):

  # Get the cycle of powers of 10 (array of the cycle of 10 ^ e mod p)
  mep = get_mod_exp_cycle(10, p)
  cycle = mep[ : -1]
  
  last_occurence = [0 for i in range(p + 1)]

  repunit_mod_p = 1
  repunit_length = 1
  cycle_index = 0
  while True:
    # Add the next power of 10 using the modexp cycle
    repunit_mod_p = (repunit_mod_p + cycle[cycle_index]) % p
    repunit_length += 1

    # i.e. if repunit is divisible by p
    if repunit_mod_p == 0:
      # actually, i guess this is redundant, but if we've seen this mod before . . .
      # ok if this is the second time, then return the interval data
      if last_occurence[repunit_mod_p]:
        return (repunit_length, last_occurence[repunit_mod_p], repunit_length - last_occurence[repunit_mod_p])

      last_occurence[repunit_mod_p] = repunit_length
    cycle_index = (cycle_index + 1) % len(cycle)

primes = sieve(10 ** 6)

k = 10 ** 9
count = 0
total = 0

#       skip 2, 3, and 5 (2 and 5 for obvious reasons, but R(10^9) won't be divisible by 3 either)
for p in primes[3 : ]:
  # Get the interval of the repunit divisibility pattern for divisor p
  pattern = get_repunit_pattern(p)

  # if k falls on this interval, we've found one of R(k)'s prime factors
  if pattern[1] <= k and (k - pattern[1]) % pattern[2] == 0:
    count += 1
    total += p
    print(count, p, pattern)
    if count == 40:
      break
print(total)
  

# primes = sieve(10 ** 6)
# print(find_pattern(1777, 100000000)) done
# Here's what I found:
#  - cycle starts at 1777^0 (1)
#  - apparently 1777 ^ 1250000 ends in "00000001" (8 digs)
#  - cycle length: 1250000 - 1 = 1249999

"""
First try:
1 11 (4, 2, 2)
2 17 (32, 16, 16)
3 41 (10, 5, 5)
4 73 (16, 8, 8)
5 101 (8, 4, 4)
6 137 (16, 8, 8)
7 251 (100, 50, 50)
8 257 (512, 256, 256)
9 271 (10, 5, 5)
10 353 (64, 32, 32)
11 401 (400, 200, 200)
12 449 (64, 32, 32)
13 641 (64, 32, 32)
14 751 (250, 125, 125)
15 1201 (400, 200, 200)
16 1409 (64, 32, 32)
17 1601 (400, 200, 200)
18 3541 (40, 20, 20)
19 4001 (1000, 500, 500)
20 4801 (1600, 800, 800)
21 5051 (100, 50, 50)
22 9091 (20, 10, 10)
23 10753 (1024, 512, 512)
24 15361 (512, 256, 256)
25 16001 (4000, 2000, 2000)
26 19841 (128, 64, 64)
27 21001 (500, 250, 250)
28 21401 (50, 25, 25)
29 24001 (2000, 1000, 1000)
31 27961 (40, 20, 20)
32 37501 (25000, 12500, 12500)
33 40961 (5120, 2560, 2560)
34 43201 (1600, 800, 800)
35 60101 (200, 100, 100)
36 62501 (125000, 62500, 62500)
37 69857 (64, 32, 32)
38 76001 (1000, 500, 500)
39 76801 (6400, 3200, 3200)
683295 (wrong, didn't actually get 40!!)

Second try:
1 11 (4, 2, 2)
2 17 (32, 16, 16)
3 41 (10, 5, 5)
4 73 (16, 8, 8)
5 101 (8, 4, 4)
6 137 (16, 8, 8)
7 251 (100, 50, 50)
8 257 (512, 256, 256)
9 271 (10, 5, 5)
10 353 (64, 32, 32)
11 401 (400, 200, 200)
12 449 (64, 32, 32)
13 641 (64, 32, 32)
14 751 (250, 125, 125)
15 1201 (400, 200, 200)
16 1409 (64, 32, 32)
17 1601 (400, 200, 200)
18 3541 (40, 20, 20)
19 4001 (1000, 500, 500)
20 4801 (1600, 800, 800)
21 5051 (100, 50, 50)
22 9091 (20, 10, 10)
23 10753 (1024, 512, 512)
24 15361 (512, 256, 256)
25 16001 (4000, 2000, 2000)
26 19841 (128, 64, 64)
27 21001 (500, 250, 250)
28 21401 (50, 25, 25)
29 24001 (2000, 1000, 1000)
30 25601 (50, 25, 25)
31 27961 (40, 20, 20)
32 37501 (25000, 12500, 12500)
33 40961 (5120, 2560, 2560)
34 43201 (1600, 800, 800)
35 60101 (200, 100, 100)
36 62501 (125000, 62500, 62500)
37 69857 (64, 32, 32)
38 76001 (1000, 500, 500)
39 76801 (6400, 3200, 3200)
40 160001 (2500, 1250, 1250)
843296 (GOT IT!!!)
"""