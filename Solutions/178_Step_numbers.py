w = [
	{'n': 0, '0': 1, '9': 0, 'b': 0},
	{'n': 1, '0': 0, '9': 0, 'b': 0}
] + list(
	{'n': 2, '0': 0, '9': 0, 'b': 0} for i in range(2, 8)
) + [
	{'n': 1, '0': 0, '9': 1, 'b': 0},
	{'n': 0, '0': 0, '9': 1, 'b': 0}
]
maxDigits = 40
total = 0
for i in range(maxDigits - 2):
	n = list({'n': 0, '0': 0, '9': 0, 'b': 0} for j in range(10))
	# 0
	n[0]['0'] += w[1]['n'] + w[1]['0']
	n[0]['b'] += w[1]['9'] + w[1]['b']

	# 1
	n[1]['n'] += w[2]['n']
	n[1]['0'] += w[0]['0'] + w[2]['0']
	n[1]['9'] += w[2]['9']
	n[1]['b'] += w[0]['b'] + w[2]['b']

	# 2-7
	for d in range(2, 8):
		for k in ['n', '0', '9', 'b']:
			n[d][k] += w[d - 1][k] + w[d + 1][k]
	
	# 8
	n[8]['n'] += w[7]['n']
	n[8]['0'] += w[7]['0']
	n[8]['9'] += w[7]['9'] + w[9]['9']
	n[8]['b'] += w[7]['b'] + w[9]['b']

	# 9
	n[9]['9'] += w[8]['n'] + w[8]['9']
	n[9]['b'] += w[8]['0'] + w[8]['b']

	w = n
	total += sum(j['b'] for j in w)
print(total)