import unittest
from a_very_big_sum import aVeryBigSum

class TestSimpleArrayFunction(unittest.TestCase):
	def test_compare_the_triplets(self):
		data = [
			[5, [1000000001, 1000000002, 1000000003, 1000000004, 1000000005], 5000000015]
			,[5, [1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1111111111, 2222222222], 5000000015]
		]
		for item in data:
			self.assertEqual(
				item[2]
				,aVeryBigSum(item[0], item[1])
				,"Test aVeryBigSum() with n = {0} and ar = {1}, expect return value is {2}"
						.format(item[0], item[1], item[2])
			)

if __name__ == '__main__' :
	unittest.main()