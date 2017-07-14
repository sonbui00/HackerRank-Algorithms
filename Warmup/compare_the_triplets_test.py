import unittest
from compare_the_triplets import solve

class TestSimpleArrayFunction(unittest.TestCase):
	def test_compare_the_triplets(self):
		data = [
			[[5, 6, 7], [3, 6, 10], [1, 1]]
			,[[5, 2, 7], [3, 6, 10], [1, 2]]
			,[[5, 6, 7], [5, 6, 7], [0, 0]]
			,[[5, 2, 7], [7, 6, 10], [0, 3]]
		]
		for item in data:
			self.assertEqual(
				item[2]
				,solve(*(item[0] + item[1]))
				,"Test solve() with Alice rate = {0} and Bob rate = {1}, expect return value is {2}"
						.format(item[0], item[1], item[2])
			)

if __name__ == '__main__' :
	unittest.main()