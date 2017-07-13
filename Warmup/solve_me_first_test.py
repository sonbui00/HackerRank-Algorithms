import unittest
from solve_me_first import solveMeFirst

class TestSolveMeFirstFunction(unittest.TestCase):

	def test_solve_me_first(self):
		data = [
			[5, 2, 3],
			[0, 0, 0],
			[3, -2, 5],
			[-6, -2, -4]
		]
		for item in data:
			self.assertEqual(item[0], solveMeFirst(item[1], item[2]), "solveMeFirst with {0} and {1}, expect value {2}".format(item[1], item[2], item[0]))	

if __name__ == '__main__':
	unittest.main()		