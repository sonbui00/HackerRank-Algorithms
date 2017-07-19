import unittest
from plus_minus import plusMinus

class TestSimpleArrayFunction(unittest.TestCase):
	def test_plus_minus(self):
		data = [
			[6, [-4, 3, -9, 0, 4, 1], ['0.500000', '0.333333', '0.166667']]
		]
		for item in data:
			self.assertEqual(
				item[2]
				,plusMinus(item[0], item[1])
				,"Test plusMinus() with n = {0} and arr = {1}, expect return value is {2}"
						.format(item[0], item[1], item[2])
			)

if __name__ == '__main__' :
	unittest.main()