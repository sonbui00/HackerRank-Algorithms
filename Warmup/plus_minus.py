from functools import reduce

def plusMinus(n, arr):
	return list(
		map(
			lambda x: "%.6f" % (x / n)
			,reduce(
				lambda x, y: [
					x[0] + 1 if y > 0 else x[0]
					,x[1] + 1 if y < 0 else x[1]
					,x[2] + 1 if y == 0 else x[2]
				]
				,arr[:n]
				,[0, 0, 0]
			)
		)
	)