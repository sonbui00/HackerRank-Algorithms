import sys
from functools import reduce

def solve(a0, a1, a2, b0, b1, b2):
	# FP style
	return reduce(
		lambda x, y: [
			x[0] + 1 if y[0] > y[1] else x[0]
			,x[1] + 1 if y[0] < y[1] else x[1]
		]
		,zip([a0, a1, a2], [b0, b1, b2])
		,[0, 0]
	)