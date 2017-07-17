from functools import reduce

def aVeryBigSum(n, ar):
	return reduce(
		lambda x, y: x + y
		,ar[:n]
	)