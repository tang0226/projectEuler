from functions import nextPrime
currPrime = 2
index = 1
while index < 10001:
	currPrime = nextPrime(currPrime)
	index += 1
	print(currPrime, index)
print(currPrime)