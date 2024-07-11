import unittest
import employee
# from employee import Employee

class testEmployee(unittest.TestCase):

	def test_email(self):
		user1 = employee.Employee("Carlos", "André", 00000)
		self.assertEqual(user1.email, "Carlos.André@email.com")

if __name__ == "__main__":
	unittest.main()