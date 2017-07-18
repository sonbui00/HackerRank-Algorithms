def diagonalDifference(n, a):
	return abs(
		sum([a[i][i] - a[i][n - i -1] for i in range(n)])
	)