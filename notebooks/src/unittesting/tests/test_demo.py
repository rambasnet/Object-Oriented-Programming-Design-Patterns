import unittest

class TestValues(unittest.TestCase):
	def test_int_float(self):
		self.assertEqual(1, 1.0)

	def test_int_string(self):
		self.assertEqual(1, "1")

	def test_int_bool(self):
		self.assertEqual(1, True)

	def test_float_string(self):
		self.assertNotEqual(1.0, "1.0")

	def test_float_bool(self):
		self.assertEqual(1.0, True)

	def test_int_string2(self):
		self.assertNotEqual(1, "1")

	def test_float_float(self):
		self.assertEqual(1.0, 1.00001)

	def test_float_float1(self):
		self.assertAlmostEqual(2.0, 1.000001, 3)

if __name__ == "__main__":
	unittest.main(verbosity=2)
	