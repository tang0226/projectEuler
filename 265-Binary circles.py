from functions import binToDec

def cleanBin(n, l):
	r = bin(n)[2 : ]
	while len(r) < l:
		r = "0" + r
	return r

"""
THE KEY:
N: how many bits will be in each unique sub-sequence

chains: the chains that we are expanding

total: the total of the decimal values of complete chains

c: the current chain we're modifying

target: the last N-1 (in this case 4) bits in c that will be used to look for available sequences in chains[0][1]

newBit: the Nth (5th here) bit in the found sequence chains[0][1] that will be added to the end of newChain (see below)

newChain: a reusable variable that will store the modified copy of c to be added to chains

i: the unique subsequence being checked

b: the complete newChain (stripped of the final bits, since those loop back and would have been double-counted)

d: the decimal representation b (to add to the total)
"""
N = 5
# chains = [[current chain, available 5-bit sequences; we add the last bit to expand the chain]]
chains = [["0" * N, list(cleanBin(i, N) for i in range(1, 2 ** N))]]
total = 0
# Repeat until chains is empty (all are done or unable to be completed)
while len(chains) > 0:
	c = chains[0]
	target = c[0][- N + 1 : ]
	newChain = []
	# loop through all available sequences
	for i in c[1]:
		# if the last bits of i match the target bits...
		if i[ : N - 1] == target:
			# this is the bit that is going to be added to c[0][0]
			newBit = i[N - 1]
			# copy the current chain to create the new chain
			newChain = [c[0], list(x for x in c[1])]
			# add the new bit to the new chain
			newChain[0] += newBit
			# remove the used sequence so it can't be used again
			newChain[1].remove(target + newBit)
			# if there are no more sequences to be added, the chain must be complete.
			if newChain[1] == []:
				# strip the binary of redundant bits that loop around to the beginning of the chain
				b = newChain[0][ : 2 ** N]
				# find the decimal value of the chain to add to the total
				d = binToDec(b)
				# add the decimal to the total
				total += d
				print(b, d, total)
				# continue so that it skips the following steps
				continue
			# add the new chain to the array at the beginning only if it isn't complete (the continue above)
			chains.insert(0, newChain)
	# remove the current chain only if it can't be completed or it is complete
	chains.remove(c)