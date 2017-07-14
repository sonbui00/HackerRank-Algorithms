import unittest
from simple_array_sum import simpleArraySum

class TestSimpleArrayFunction(unittest.TestCase):
	def test_simple_array_function(self):
		data = [
			[31, 6, [1, 2, 3, 4, 10, 11]]
			,[0, 4, [0, 0, 0, 0]]
			,[40, 6, [2, 6, 3, 4, 10, 15]]
			,[31, 6, [1, 2, 3, 4, 10, 11]]
			# Not normal case here. when n <> number array items
			,[21, 6, [1, 2, 3, 4, 11]]
			,[25, 5, [2, 6, 3, 4, 10, 15]]
		]
		for item in data:
			self.assertEqual(
				item[0]
				,simpleArraySum(item[1], item[2])
				,"Test simpleArraySum with n = {0} and ar = {1}, expect return value is {2}"
						.format(item[1], item[2], item[0])
			)

if __name__ == '__main__':
	unittest.main()