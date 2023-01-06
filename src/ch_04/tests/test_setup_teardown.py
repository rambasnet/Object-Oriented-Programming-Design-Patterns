import unittest

class TestValues(unittest.TestCase):
	def setUp(self) -> None:
		print("setUp")
		return super().setUp()

	def tearDown(self) -> None:
		print("tearDown")
		return super().tearDown()

	def test_int_float(self) -> None:
		print("test_int_float")
		self.assertEqual(1, 1.0)

	def test_int_string(self) -> None:
		print("test_int_string")
		self.assertNotEqual(1, "1")

	def test_int_bool(self) -> None:
		print("test_int_bool")
		self.assertEqual(1, True)

if __name__ == "__main__":
	unittest.main(verbosity=2)
