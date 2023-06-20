import math
import time
start=time.time()
combos=8 # Combos that only use one coin
for c100 in range(2):
	sum=c100*100
	if sum==200:
		combos+=1
		continue
	for c50 in range(4):
		sum=c100*100+c50*50
		if sum==200:
			combos+=1
			continue
		for c20 in range(10):
			sum=c100*100+c50*50+c20*20
			if sum>200:
				break
			elif sum==200:
				combos+=1
				continue
			for c10 in range(20):
				sum=c100*100+c50*50+c20*20+c10*10
				if sum==200:
					combos+=1
					continue
				for c5 in range(40):
					sum=c100*100+c50*50+c20*20+c10*10+c5*5
					if sum==200:
						combos+=1
						continue
					for c2 in range(100):
						sum=c100*100+c50*50+c20*20+c10*10+c5*5+c2*2
						if sum>200:
							break
						elif sum==200:
							combos+=1
							continue
						for c1 in range(200):
							sum=c100*100+c50*50+c20*20+c10*10+c5*5+c2*2+c1
							if sum>200:
								break
							elif sum==200:
								combos+=1
								continue
end=time.time()-start
print (combos)
print (end)