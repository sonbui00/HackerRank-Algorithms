import unittest
from diagonal_difference import diagonalDifference

class TestSimpleArrayFunction(unittest.TestCase):
	def test_compare_the_triplets(self):
		data = [
			[3, [[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15]
			,[3, [[10, 2, 4], [4, 10, 6], [10, 8, -11]], 15]
			,[3, [[7, 2, 4], [4, 10, 6], [10, 8, 2]], 5]
		]
		for item in data:
			self.assertEqual(
				item[2]
				,diagonalDifference(item[0], item[1])
				,"Test diagonalDifference() with n = {0} and a = {1}, expect return value is {2}"
						.format(item[0], item[1], item[2])
			)

if __name__ == '__main__' :
	unittest.main()