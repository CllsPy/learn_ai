import unittest
import main

# Create a class
class testMain(unittest.TestCase):

	# It needs start with "test_" or it'll fail in test.
	def test_add(self):
		self.assertEqual(main.sum(10, 5), 15)
		self.assertEqual(main.sum(-1, 1), 0)
		self.assertEqual(main.sum(-1, -1), -2)

	# Raise ValueError
	def test_div(self):
		# self.assertRaises(ValueError, main.div, 10, 0)

		# Contest Approach
		with self.assertRaises(ValueError):
			main.div(10, 0)
		

if __name__ == '__main__':
	unittest.main()
	