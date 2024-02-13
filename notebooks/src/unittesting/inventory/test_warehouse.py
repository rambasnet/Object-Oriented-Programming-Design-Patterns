import unittest

from warehouse import Warehouse

class TestWarehouse(unittest.TestCase):
	def test_warehouse(self):
		# Create a warehouse with 10 shoes, 2 hats, and 0 umbrellas
		wh = Warehouse({'shoes': 10, 'hats': 2, 'umbrellas': 0})
		self.assertTrue(wh.in_stock('shoes'))
		self.assertFalse(wh.in_stock('umbrellas'))
		self.assertEqual(wh.stock_count('hats'), 2)

		wh.take_from_stock('shoes', 2)
		self.assertEqual(wh.stock_count('shoes'), 8)

		wh.take_from_stock('hats', 2)
		self.assertFalse(wh.in_stock('hats'))

		with self.assertRaises(Exception):
			wh.take_from_stock('umbrellas', 1)

if __name__ == '__main__':
	unittest.main(verbosity=2)